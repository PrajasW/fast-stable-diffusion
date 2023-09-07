from PIL import Image, ImageSequence
import os
# List of image file paths to include in the GIF
DIR_NAME = "hitori-gotou"
DIR_PATH = f"C:\\Users\\praja\\Desktop\\ai-gen\\animation\\{DIR_NAME}"
DURATION = 200 # Duration between frames in milliseconds
GIF_NAME = "age-progression"

if DIR_PATH == "":
    DIR_PATH = os.getcwd()

if not os.path.exists(DIR_PATH):
    print("invalid path")
    exit()

image_files = os.listdir(DIR_PATH)# Replace with your image file paths

# Create an empty list to store the image frames
print(image_files)
frames = []

# Load each image and append it to the frames list
for image_file in image_files:
    if image_file.endswith(".png"):
        img = Image.open(os.path.join(DIR_PATH,image_file))
        frames.append(img)

output_gif = os.path.join(DIR_PATH,f"{GIF_NAME}.gif")
# Specify the output GIF file name

# Save the frames as a GIF
frames[0].save(
    output_gif,
    save_all=True,
    append_images=frames[1:],
    duration=DURATION,  # Duration between frames in milliseconds
    loop=0,  # 0 means loop indefinitely; set to a positive integer for a finite loop
)

print(f"GIF saved as {output_gif}")
