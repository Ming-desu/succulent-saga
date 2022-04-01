from glob import glob
from PIL import Image

images = glob('plants_dataset/**/*.jpg')

for image in images:
  img = Image.open(image)
  width, height = img.size

  if width > 224 and height > 224:
    img.thumbnail((width, height))

  if height < width:
    left = (width - height) / 2
    right = (width + height) / 2
    top = 0
    bottom = height
    img = img.crop((left, top, right, bottom))

  elif width < height:
    left = 0
    right = width
    top = 0
    bottom = width
    img = img.crop((left, top, right, bottom))

  if width > 224 and height > 224:
    img.thumbnail((224, 224))

  img.save(image)