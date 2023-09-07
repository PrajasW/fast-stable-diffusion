import os

# get the images in cwd
DIR_NAME = "zoro-age"
DIR_PATH = f"C:\\Users\\praja\\Desktop\\ai-gen\\animation\\{DIR_NAME}"
if not os.path.exists(DIR_PATH):
    print("invalid path")
    exit()
    
images = os.listdir(DIR_PATH)
if DIR_PATH == '':
    images = os.listdir(os.getcwd())
# get images and name in reverse order
images = sorted(images, reverse=True)
# rename images and store in renamed dir

# create renamed dir if it doesn't exist
if not os.path.exists(os.path.join(DIR_PATH,'renamed')):
    os.mkdir(os.path.join(DIR_PATH,'renamed'))

# rename images and store in renamed dir
for image in images:
    # image ends with .png
    if image.endswith('.png'):
        os.rename(os.path.join(DIR_PATH,image) ,os.path.join(DIR_PATH,'renamed/{:02d}.png'.format(images.index(image))))


print("reversed images")
