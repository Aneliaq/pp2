# read file examples

with open("sample.txt", "r") as f:
    print("Full content:")
    print(f.read())

with open("sample.txt", "r") as f:
    print("\nLine by line:")
    print(f.readline())

with open("sample.txt", "r") as f:
    print("\nAll lines list:")
    print(f.readlines())
