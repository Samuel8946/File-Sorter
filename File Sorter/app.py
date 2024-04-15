import os
import shutil

# Extensions
video_extensions = [".mp4",".webm", ".mkv", ".flv", ".vob", ".ogg", ".ogv", ".wmv", ".avi"]
img_extensions = [".gif", ".jpg", "jpeg", ".png", ".svg", ".webp"]
doc_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".txt", ".odt"]

# Directory path

print("Leave blank if you don't want a folder")

folder_name = input("Please enter folder name: ")

directory = os.path.join(os.path.expanduser("~"), "Downloads/")

videos_directory = os.path.join(os.path.expanduser("~"), f"Videos/{folder_name}")
pictures_directory = os.path.join(os.path.expanduser("~"), f"Pictures/{folder_name}")
music_directory = os.path.join(os.path.expanduser("~"), f"Music/{folder_name}")
documents_directory = os.path.join(os.path.expanduser("~"), f"Documents/{folder_name}")

# List all files in the directory
files = os.listdir(directory)

# Print the list of files
print("Files in the directory:")
for file in files:
    # If it's a video file
    for x in video_extensions:
        if file.endswith(x):
            if not os.path.exists(videos_directory):
                os.makedirs(videos_directory)

            source_path = os.path.join(directory, file)
            destination_path = os.path.join(videos_directory, file)

            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {videos_directory}")
        continue

    # If it's a img file
    for y in img_extensions:
        if file.endswith(y):
            if not os.path.exists(pictures_directory):
                os.makedirs(pictures_directory)

            source_path = os.path.join(directory, file)
            destination_path = os.path.join(pictures_directory, file)

            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {pictures_directory}")
    # If it's a music file
    if file.endswith(".mp3"):
        if not os.path.exists(music_directory):
            os.makedirs(music_directory)

        source_path = os.path.join(directory, file)
        destination_path = os.path.join(music_directory, file)

        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {music_directory}")

    # If it's a document
    for a in doc_extensions:
        if file.endswith(a):
            if not os.path.exists(documents_directory):
                os.makedirs(documents_directory)

            source_path = os.path.join(directory, file)
            destination_path = os.path.join(documents_directory, file)

            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {documents_directory}")
        
print("")
os.system("pause")
