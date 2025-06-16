import shutil

def move_json(server8Path, filename):
    filePath = f'{filename}.json'
    fileDest = f'{server8Path}/Uploads/{filename}.json'

    shutil.copyfile(filePath, fileDest)
