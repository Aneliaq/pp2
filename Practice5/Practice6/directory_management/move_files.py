import shutil
import os

os.makedirs("backup", exist_ok=True)

if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "backup/sample.txt")
    print("File moved to backup folder")
else:
    print("File not found")
