import sys
# import os
from pathlib import Path, PurePath
from PIL import Image

folder_path = str(sys.argv[1])
new_folder = str(sys.argv[2])

if not Path(f'{new_folder}').exists():
    Path(f'{new_folder}').mkdir()

for filename in Path(f'{folder_path}').iterdir():
    img = Image.open(f'{filename}')
    name = PurePath(f'{filename}').stem
    img.save(f"{new_folder}{name}.png",'png')
    print ('all done')
    
