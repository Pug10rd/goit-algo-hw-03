import sys
from pathlib import Path
import shutil

src_dir = Path(sys.argv[1])
dest_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

def copy_files(src: Path, dest: Path):
    try:
        if src.is_dir():
            for item in src.iterdir():
                if item.is_dir():
                    copy_files(item, dest) 
                else:
                    ext = item.suffix.lstrip('.').lower() or 'no_extension'
                    ext_dir = dest / ext
                    ext_dir.mkdir(parents=True, exist_ok=True) 
                    shutil.copy2(item, ext_dir / item.name)
                    
                    print(f'Copied {item.name} to {ext_dir}')
        else:
            raise ValueError(f'{src} is not a directory.')
    except Exception as e:
        print(f'Error: {e}')

dest_dir.mkdir(parents=True, exist_ok=True)

copy_files(src_dir, dest_dir)


# PASTE IN TERMINAL TO TEST: /usr/local/bin/python3 /Users/centr/Desktop/algo-hw/goit-algo-hw-03/goit-algo-hw-03/task_1/dir_sort.py test