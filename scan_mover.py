#! python3

import os, re, shutil
from pathlib import Path

os.chdir('d:\\_Docs\\Scan')
targetPath = Path(r'\\S\выписки\Выписки в бухгалтерию\выписки')
antarcticaRegex = re.compile(r'^\d\d\d\d \d\d \d\d.jpg$')
antarridRegex = re.compile(r'^a\d\d\d\d \d\d \d\d.jpg$')

for folderName, subfolders, filenames in os.walk(str(Path.cwd())):
    for filename in filenames:
        mo_antarctica_filename = antarcticaRegex.search(filename)
        mo_antarrid_filename = antarridRegex.search(filename)
        if mo_antarctica_filename is not None:
            antarctica_filepath = Path(folderName) / mo_antarctica_filename.group()
            antarctica_targetDir = targetPath / f'Антарктика20/{mo_antarctica_filename.group()[5:7]}'
            if not antarctica_targetDir.exists():
                antarctica_targetDir.mkdir()
            shutil.move(str(antarctica_filepath), str(antarctica_targetDir))
        if mo_antarrid_filename is not None:
            antarrid_filepath = Path(folderName) / mo_antarrid_filename.group()
            antarrid_targetDir = targetPath / f'Антаррид20/{mo_antarrid_filename.group()[6:8]}'
            if not antarrid_targetDir.exists():
                antarrid_targetDir.mkdir()
            shutil.move(str(antarrid_filepath), str(antarrid_targetDir))
    if not os.listdir(folderName):
        os.rmdir(folderName)
