from pathlib import Path
import shutil  # useful and trustable module for files movement
import ctypes  # useful to get access of windows tools

def clean_desktop():
    # path.home help to get your home directory and / sign to get in desktop dir
    desktop_path = Path.home() / "Desktop"

    # Rules ko loop ke bahar sabse upar rakhein (Memory Optimization)
    rules = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Zips': ['.zip', '.rar']
    }

    # Initialize a dictionary to track how many files are moved into each folder
    moved_counts = {folder: 0 for folder in rules.keys()} 
    total_moved = 0

    for item in desktop_path.iterdir():
        if item.is_file():
            extension = item.suffix.lower()

            for folder_name, extensions_list in rules.items():
                if extension in extensions_list:
                    target_folder = desktop_path / folder_name

                    # if folder already exists, exist_ok=True prevents FileExistsError
                    target_folder.mkdir(exist_ok=True)
                    
                    destination_path = target_folder / item.name
                    if destination_path.exists():
                        print(f"  {item.name} already exists")
                    else:
                        # Move file from old path to new path
                        shutil.move(str(item), str(destination_path))
                        print(f"✅ Moved: {item.name} -> {folder_name}/")
                        
                        # Increment counters
                        moved_counts[folder_name] += 1
                        total_moved += 1

                    break # Match milne ke baad inner loop tod dein

    # =====================================================================
    #  WINDOWS POPUP LOGIC WITH SUMMARY REPORT
    # =====================================================
    print("Desktop Pop-up notification")

    message = f"Desktop cleaned successfully!\nTotal files moved: {total_moved}"
    
    # ctypes.windll.user32.MessageBoxW विंडोज का इन-बिल्ट पॉप-अप बॉक्स है
    ctypes.windll.user32.MessageBoxW(0, message, "🧹 Desktop Cleaner Report", 64)

    print("successfully desktop cleaned !")


if __name__ == "__main__":
    clean_desktop()