import os

# Define the base directory where you want to create the folders
base_dir = "/path/to/your/base/directory/"

# Loop through each day and create a folder
for day in range(1, 101):
    # Format the day number to have leading zeros if necessary
    day_folder_name = f"{day:02d}-Day{day}-"
    # Create the folder
    folder_path = os.path.join(base_dir, day_folder_name)
    os.makedirs(folder_path)
    print(f"Folder created: {folder_path}")
