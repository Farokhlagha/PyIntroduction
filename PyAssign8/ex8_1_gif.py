import os
import imageio

file_list = sorted(os.listdir('PyAssignment8/images'))

IMAGES = []
for file_name in file_list:
    file_path = 'PyAssignment8/images/' + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave('PyAssignment8/my_output.gif', IMAGES)