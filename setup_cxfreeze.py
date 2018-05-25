import sys, os
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_msvcr":True,
                     "packages": ["argparse","openpyxl"],
                     "excludes": [],
                     "include_files":[PYTHON_INSTALL_DIR]
                     }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "file_convert",
        version = "0.1",
        description = "Converts CSV and TSV files to Excel",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, targetName="file_convert.exe")])

