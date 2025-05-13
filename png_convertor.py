from PIL import Image
import os

input_folder = "images2"  # your input folder
output_folder = "images"  # resized images2 will be saved here
os.makedirs(output_folder, exist_ok=True)

target_size = (216, 216)  # width x height

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    try:
        with Image.open(file_path) as img:
            resized_img = img.resize(target_size)
            new_name = os.path.splitext(filename)[0] + ".png"
            resized_img.save(os.path.join(output_folder, new_name), "PNG")
            print(f"[✓] Resized {filename} → {new_name}")
    except Exception as e:
        print(f"[✗] Skipped {filename}: {e}")
