-- Every image in fa/ came from the EPUB and is the publisher's artwork: cover,
-- title page, author photo, bonsai and Buddha ornaments, thin rules. None is
-- licensed for this edition, so none is committed (spec 008 §3). fa/ keeps the
-- references so block parity with source/ holds; they are dropped here.
--
-- The one ornament that carried structure is kept as a rule: W3 opens each
-- EVERYDAY ZEN sidebar and W5 closes it, so a reader still sees where the
-- story starts and ends.
local RULE = { ["image_rsrcW3.jpg"] = true, ["image_rsrcW5.jpg"] = true }

function Para(el)
  if #el.content ~= 1 or el.content[1].t ~= "Image" then return nil end
  local src = el.content[1].src
  -- Unanchored: for PDF, Quarto has already rewritten it to fa/media/images/.
  if not src:match("media/images/") then return nil end
  if RULE[src:match("[^/]+$")] then return pandoc.HorizontalRule() end
  return {}
end
