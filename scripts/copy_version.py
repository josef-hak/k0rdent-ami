import os
import shutil
from pathlib import Path

VERSION = os.getenv('VERSION', 'v1.2.0')
print('>>>', VERSION)

src_dir = Path(f"docs/versions/{VERSION}")
dst_dir = Path("docs")

if not src_dir.exists():
    raise FileNotFoundError(f"Source directory does not exist: {src_dir}")

for item in src_dir.iterdir():
    target_path = dst_dir / item.name
    print(target_path)
    if item.is_dir():
        shutil.copytree(item, target_path, dirs_exist_ok=True)
    else:
        shutil.copy2(item, target_path)

print("Content copied successfully.")
