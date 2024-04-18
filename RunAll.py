import subprocess
import os
import time
from PIL import Image
def run_python_files(files_to_run):
    total_start_time = time.time()
    for file_name, _ in files_to_run:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, file_name)
        print("-" * 100)
        print(f"Running {file_name}...")
        subprocess.run(["python", file_path])
        print(f"{file_name} is done.")
    total_end_time = time.time()
    total_time_taken = total_end_time - total_start_time
    print(f"Total time taken for all scripts: {total_time_taken:.2f} seconds")

def convert_images_to_jpg(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file_path)[1].lower() != '.png':
                continue
            im = Image.open(file_path)
            output_path = os.path.splitext(file_path)[0] + '.jpg'
            im.convert('RGB').save(output_path, 'JPEG')
            os.remove(file_path)

if __name__ == "__main__":
    files_to_run = [
        ("preprocess.py", 1),
        ("cloth_mask.py", 2),
        ("openpose.py", 3),
        ("image-parse-v3.py", 4),
        ("agnostic-v3.2.py", 5),
        ("agnostic_mask.py", 6),
        ("densepose.py", 7),
        ("gt_cloth_warped_mask.py", 8),
        ("image-parse-agnostic-v3.2.py", 9)
        # Add other script paths here
    ]
    run_python_files(files_to_run)

    # Convert images to JPEG format
    output_folder = "./Output"
    sub_folders = os.listdir(output_folder)
    for sub_folder in sub_folders:
        if sub_folder != "agnostic-mask":
            folder_path = os.path.join(output_folder, sub_folder)
            convert_images_to_jpg(folder_path)
