import os
import imageio
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
file_list = sorted(os.listdir('PyAssign8/images'))

IMAGES = []
for file_name in file_list:
    file_path = 'PyAssign8/images/' + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave('PyAssign8/my_output.gif', IMAGES)