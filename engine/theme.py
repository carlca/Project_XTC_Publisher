from pathlib import Path

import yaml


def load_theme(path: Path) -> dict:
   data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
   required = ("page", "fonts", "colours", "typography")
   missing = [k for k in required if k not in data]
   if missing:
      raise ValueError(f"Theme missing required sections: {', '.join(missing)}")
   return data
