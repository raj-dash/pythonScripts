import os, time
from datetime import datetime

log_path = r"C:\Users\rajar\OneDrive\Coding\Python\Scripts\folderStuff\log.txt"
path = r"C:\Users\rajar\Downloads"
img_folder = "img"
doc_folder = "doc"
pdf_folder = "pdf"
txt_folder = "txt"
zip_folder = "zip"
ppt_folder = "ppt"
exe_folder = "exe"
other_folder = "other"
img_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"]
temp_download = [".tmp", ".opdownload", ".crdownload"]

# functions

def moveItems(item, path, folder):
    new_path = os.path.join(path, folder)
    new_path = os.path.join(new_path, item)
    count = 1
    temp = new_path
    while os.path.exists(temp):
        temp = f"{new_path}({count})"
        count += 1
    new_path = temp
    old_path = os.path.join(path, item)
    os.replace(old_path, new_path)
    print(new_path)
    try:
        with open(log_path, "a") as f:
            f.write(f"{item} -> {new_path}\n")
    except IOError:
        print("Log file could not be opened correctly")

def executeMove():
    for item in os.listdir(path):
        extension = os.path.splitext(item)[-1]
        if extension == ".docx":
            moveItems(item, path, doc_folder)
        elif extension == ".pdf":
            moveItems(item, path, pdf_folder)
        elif extension == ".txt":
            moveItems(item, path, txt_folder)
        elif extension == ".zip":
            moveItems(item, path, zip_folder)
        elif extension == ".pptx":
            moveItems(item, path, ppt_folder)
        elif extension == ".pdf":
            moveItems(item, path, pdf_folder)
        elif extension == ".exe":
            moveItems(item, path, exe_folder)
        elif extension in img_extensions:
            moveItems(item, path, img_folder)
        elif extension in temp_download:
            continue
        else:
            temp = os.path.join(path, item)
            if not os.path.isdir(temp):
                moveItems(item, path, other_folder)


# main code

if __name__ == "__main__":
    try:
        with open(log_path, "a") as f:
            f.write(str(datetime.now()) + "\n\n")
        executeMove()
        old = os.listdir(path)
        count = 0
        while True:
            new = os.listdir(path)
            if len(new) > len(old):
                new_file = list(set(new) - set(old))
                print(new_file)
                executeMove()
            else:
                count += 1
                print(count)
            time.sleep(5)
        # executeMove()
    except KeyboardInterrupt:
        print(f"Program ended")
        line = "-" * 50
        with open(log_path, "a") as f:
            f.write("\n" + line + "\n\n")
    except IOError:
        print("Could not open log file")

