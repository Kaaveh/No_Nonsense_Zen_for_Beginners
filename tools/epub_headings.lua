-- Kindle EPUB styles headings via CSS classes; turn them into real headers.
local level = {
  class_s2F = 1, class_sPW = 1, class_sRN = 1, class_s3X = 1, -- chapter / part titles
  class_s41 = 2, class_s5W = 2,                               -- questions
  class_s5G = 3, class_sP4 = 3,                               -- sidebar titles, subheads
}
local part_label

function Div(el)
  local c = el.classes[1]
  if c == "class_s3V" then                 -- "Part One" label, merged into the next title
    part_label = pandoc.utils.stringify(el); return {}
  end
  if level[c] then
    local text = pandoc.utils.stringify(el)
    if c == "class_s3X" and part_label then text = part_label .. ": " .. text; part_label = nil end
    return pandoc.Header(level[c], text)
  end
  if c == "class_s5E" then                 -- "EVERYDAY ZEN" sidebar label
    return pandoc.Para({pandoc.Strong(pandoc.utils.stringify(el))})
  end
end

function Pandoc(doc)                       -- drop the Kindle table of contents
  local out, skip = {}, false
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 then skip = pandoc.utils.stringify(b) == "CONTENTS" end
    if not skip then out[#out + 1] = b end
  end
  return pandoc.Pandoc(out, doc.meta)
end

function RawBlock() return {} end        -- cover <svg> wrapper duplicates the cover image
