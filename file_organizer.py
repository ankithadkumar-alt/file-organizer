import os
import shutil
import logging
from datetime import datetime

# ── 1. Setup logging ──────────────────────────────────────────────────────────
# Creates a logs/ folder and writes every action to a timestamped log file
# AND prints it to the terminal at the same time.

os.makedirs("logs", exist_ok=True)  # make logs/ folder if it doesn't exist

log_filename = "logs/organizer_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_filename),   # save to file
        logging.StreamHandler()              # print to terminal
    ]
)

# ── 2. File type categories ───────────────────────────────────────────────────
# A dictionary that maps folder names to file extensions.
# When we see a .jpg file, we move it into the "Images" folder, etc.

CATEGORIES = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos":    [".mp4", ".mkv", ".avi", ".mov"],
    "Audio":     [".mp3", ".wav", ".aac", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".md"],
    "Code":      [".py", ".js", ".html", ".css", ".json"],
    "Archives":  [".zip", ".tar", ".gz", ".rar"],
}

def get_folder_name(extension):
    """Look up which folder a file extension belongs to."""
    for folder, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return folder
    return "Others"  # anything not in the list goes to Others/


# ── 3. Sort files ─────────────────────────────────────────────────────────────

def sort_files(directory):
    """Move every file in `directory` into a matching sub-folder by type."""
    logging.info(f"Starting sort in: {directory}")

    files_moved = 0

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip sub-folders — only process actual files
        if not os.path.isfile(filepath):
            continue

        # Get the extension, e.g. ".jpg"
        _, extension = os.path.splitext(filename)
        folder_name = get_folder_name(extension)

        # Create the destination folder if it doesn't exist
        destination_folder = os.path.join(directory, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file
        destination = os.path.join(destination_folder, filename)
        try:
            shutil.move(filepath, destination)
            logging.info(f"  Moved: {filename}  -->  {folder_name}/")
            files_moved += 1
        except Exception as error:
            logging.error(f"  Could not move {filename}: {error}")

    logging.info(f"Done! {files_moved} file(s) moved.")


# ── 4. Main — ask user for input ─────────────────────────────────────────────

def main():
    print("\n===================================")
    print("   File Organizer — InternSpark")
    print("===================================\n")

    # Ask the user which folder to organise
    folder = input("Enter the folder path to organise (or press Enter for current folder): ").strip()

    # If user pressed Enter without typing, use the current working directory
    if folder == "":
        folder = os.getcwd()

    # Check the folder actually exists before doing anything
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid folder.")
        return

    print(f"\nFolder selected: {folder}")
    confirm = input("Proceed? (y/n): ").strip().lower()

    if confirm == "y":
        sort_files(folder)
        print(f"\nLog saved to: {log_filename}")
    else:
        print("Cancelled.")

if __name__ == "__main__":
    main()
