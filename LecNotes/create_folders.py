import os

# List of folders to create
folders = ["split_files", "text_files", "Final_Notes"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Folder '{folder}' has been created!")
    else:
        print(f"Folder '{folder}' already exists!")

print("All folders have been created!")
