# File Organizer — Python Automation Script

A simple Python script that automatically sorts files in any folder into sub-folders by file type. Built for the InternSpark Python Automation task.

---

## What it does

- Asks you for a folder path
- Reads every file's extension (e.g. `.jpg`, `.pdf`, `.py`)
- Moves each file into a matching sub-folder: `Images/`, `Documents/`, `Code/`, etc.
- Logs every action with a timestamp to both the terminal and a `.log` file

---

## Requirements

- Python 3.8 or higher
- No extra packages needed (uses only the standard library)

---

## How to run

```
python file_organizer.py
```

The script will ask you two questions:
1. Which folder do you want to organise? (press Enter to use the current folder)
2. Confirm with `y`

---

## Sample input / output

**Before** — messy folder:
```
test_folder/
  photo.jpg
  notes.txt
  report.pdf
  app.py
  song.mp3
  backup.zip
  clip.mp4
```

**Run the script:**
```
===================================
   File Organizer — InternSpark
===================================

Enter the folder path to organise (or press Enter for current folder): /tmp/test_folder
Folder selected: /tmp/test_folder
Proceed? (y/n): y
```

**Terminal output:**
```
2026-06-07 11:26:37  [INFO]  Starting sort in: /tmp/test_folder
2026-06-07 11:26:37  [INFO]    Moved: song.mp3  -->  Audio/
2026-06-07 11:26:37  [INFO]    Moved: report.pdf  -->  Documents/
2026-06-07 11:26:37  [INFO]    Moved: photo.jpg  -->  Images/
2026-06-07 11:26:37  [INFO]    Moved: clip.mp4  -->  Videos/
2026-06-07 11:26:37  [INFO]    Moved: notes.txt  -->  Documents/
2026-06-07 11:26:37  [INFO]    Moved: app.py  -->  Code/
2026-06-07 11:26:37  [INFO]    Moved: backup.zip  -->  Archives/
2026-06-07 11:26:37  [INFO]  Done! 7 file(s) moved.

Log saved to: logs/organizer_20260607_112637.log
```

**After** — organised folder:
```
test_folder/
  Audio/      song.mp3
  Documents/  notes.txt  report.pdf
  Images/     photo.jpg
  Videos/     clip.mp4
  Code/       app.py
  Archives/   backup.zip
```

---

## File categories

| Folder     | Extensions                              |
|------------|-----------------------------------------|
| Images     | .jpg .jpeg .png .gif .bmp .svg .webp   |
| Videos     | .mp4 .mkv .avi .mov                    |
| Audio      | .mp3 .wav .aac .flac                   |
| Documents  | .pdf .doc .docx .txt .md               |
| Code       | .py .js .html .css .json               |
| Archives   | .zip .tar .gz .rar                     |
| Others     | anything not in the list above         |

---

## Concepts used

- `os` module — check if paths exist, list files, create folders
- `shutil` module — move files
- `logging` module — record actions to terminal and a `.log` file
- `try / except` — handle errors without crashing
- `input()` — get folder path and confirmation from the user
