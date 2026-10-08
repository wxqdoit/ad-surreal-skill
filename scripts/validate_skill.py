#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def validate():
    root = Path(__file__).resolve().parent.parent
    errors = []

    # 1. Check SKILL.md
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md does not exist.")
    else:
        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            errors.append("SKILL.md must start with YAML frontmatter ---")
        
        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not match:
            errors.append("SKILL.md frontmatter format is invalid.")
        else:
            fm = match.group(1)
            name_m = re.search(r"^name:\s*([^\s]+)", fm, re.MULTILINE)
            desc_m = re.search(r"^description:\s*(.+)", fm, re.MULTILINE)
            if not name_m:
                errors.append("Frontmatter missing 'name'")
            else:
                name = name_m.group(1).strip()
                if not re.match(r"^[a-z0-9-]+$", name):
                    errors.append(f"Invalid name format: {name}")
                if len(name) > 64:
                    errors.append(f"Name too long: {len(name)} chars")

            if not desc_m:
                errors.append("Frontmatter missing 'description'")
            else:
                desc = desc_m.group(1).strip()
                if "<" in desc or ">" in desc:
                    errors.append("Description contains angle brackets")
                if len(desc) > 1024:
                    errors.append(f"Description too long: {len(desc)} chars")

    # 2. Check agents/openai.yaml
    agent_yaml = root / "agents" / "openai.yaml"
    if not agent_yaml.exists():
        errors.append("agents/openai.yaml does not exist.")

    # 3. Check reference files mentioned in SKILL.md
    refs = [
        "references/metaphor-archetypes.md",
        "references/industry-blueprints.md",
        "references/prompt-grammar.md",
        "references/campaign-framework.md"
    ]
    for ref in refs:
        p = root / ref
        if not p.exists():
            errors.append(f"Referenced file missing: {ref}")
        else:
            if p.stat().st_size == 0:
                errors.append(f"Referenced file is empty: {ref}")

    if errors:
        print("Validation FAILED:")
        for e in errors:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("Validation PASSED: All files, frontmatter, and references are valid.")

if __name__ == "__main__":
    validate()
