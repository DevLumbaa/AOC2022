import os
from pathlib import Path

def get_inputs_directory(file, new_file):
    cur_dir, _ = os.path.split(os.path.abspath(file))
    filename =  str((Path(cur_dir).parents[0])) + new_file
    return filename