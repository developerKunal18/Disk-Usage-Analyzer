import os

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Invalid folder path")
else:
    file_sizes = []

    total_size = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            size = os.path.getsize(path)
            total_size += size
            file_sizes.append((file, size))

    print("\nTotal Size:", round(total_size / (1024 * 1024), 2), "MB")

    print("\nLargest Files:\n")

    file_sizes.sort(key=lambda x: x[1], reverse=True)

    for file, size in file_sizes[:5]:
        print(f"{file} - {round(size / 1024, 2)} KB")
