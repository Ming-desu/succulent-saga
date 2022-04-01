from glob import glob

import os

images = glob('plants_dataset/**/*.jpg')

last_class_name = None
current_index = 1

for image in images:
  class_name = image.split('\\')[1]

  if last_class_name == None or class_name != last_class_name:
    current_index = 1

  last_class_name = class_name

  new_file_name = "{}_{}.jpg".format(last_class_name, current_index)

  current_index += 1

  # print(new_file_name)

  destination = '\\'.join([str(x) for x in image.split('\\')[:2]]) + '\\' + new_file_name

  os.rename(image, destination)
