#!/usr/bin/env python3

from PIL import Image
import os
import subprocess
import sys

"""
This function converts all images located at source from .tiff format to .jpeg,
changes resolution to 128 by 130 pixels and rotates them 90 degrees clockwise.
After the convertion, images are stored in the new folder created by adding '_fomratted' suffix to the source folder.
"""

def convert_image(source):
	destination = source[:len(source) - 1] + '_formatted/'
	if not os.path.exists(destination):
		subprocess.run(['mkdir', destination])

	for image in os.listdir(source):
		if not image.startswith('.'):
			image_path = os.path.join(source + image)
			with Image.open(image_path) as im:
				formatted_image = im.convert('RGB').resize((128,130)).rotate(90).save(destination + image, format='JPEG')

	print("Images convertion successfully completed!")

def main():
	source = sys.argv[1]
	convert_image(source)

if __name__ == "__main__":
	main()

