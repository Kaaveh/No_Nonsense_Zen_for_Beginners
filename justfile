# Task runner.
#
#     just check              # everything that must pass before a commit
#     just fix                # the corrections that can be made automatically
#     just translate 1-04     # one file through the whole pipeline (000 §3)

py := if path_exists(".venv/bin/python") == "true" { ".venv/bin/python" } else { "python3" }
gt := env("GT", home_directory() / "Project/Backend/gTranslator")

_default:
    @just --list

# The checkers read pyproject.toml from the current directory, so run from here.
check: test
    {{py}} -m bargardan_tools.normalize --check
    {{py}} -m bargardan_tools.check_linebreaks --check
    {{py}} -m bargardan_tools.check_parity --check

test:
    {{py}} -m unittest discover -s tools/tests

# Bidi overrides are reported, never rewritten: `check` can still fail after this.
fix:
    {{py}} -m bargardan_tools.normalize --fix
    {{py}} -m bargardan_tools.check_linebreaks --fix

# Create missing fa/ stubs. Never overwrites existing work.
stubs:
    {{py}} -m bargardan_tools.make_stubs

# Rebuild source/ from the transcript. source/ is generated.
split:
    python3 tools/split_book.py

# strip -> gTranslator -> restore -> fix -> check, for one file. On a refusal,
# repair the sentinel in /tmp/FILE.fa.md and re-run only the restore line.
translate FILE:
    {{py}} tools/apparatus.py strip source/{{FILE}}.md -o /tmp/{{FILE}}.en.md
    "{{gt}}/.venv/bin/python" "{{gt}}/gtranslate.py" -f /tmp/{{FILE}}.en.md -t fa -w --raw -o /tmp/{{FILE}}.fa.md
    {{py}} tools/apparatus.py restore source/{{FILE}}.md /tmp/{{FILE}}.fa.md -o fa/{{FILE}}.md
    just fix
    just check

venv:
    python3 -m venv .venv
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r tools/requirements.txt
