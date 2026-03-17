import os

os.makedirs("test_dir/sub_dir", exist_ok=True)

print("Directories created")

print("Current directory:", os.getcwd())

print("Directory content:")
print(os.listdir())
