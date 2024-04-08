#!/usr/bin/env python3

import unittest
import os
from PIL import Image
from app import convert_image

class TestConvertImage(unittest.TestCase):

	def setUp(self):
		self.source_dir = 'test_images/'
		self.dest_dir = 'test_images_formatted/'
		os.makedirs(self.source_dir, exist_ok=True)
		os.makedirs(self.dest_dir, exist_ok=True)

	def tearDown(self):
		for file in os.listdir(self.source_dir):
			os.remove(os.path.join(self.source_dir, file))
		for file in os.listdir(self.dest_dir):
			os.remove(os.path.join(self.dest_dir, file))
		os.rmdir(self.source_dir)
		os.rmdir(self.dest_dir)

	def test_convert_image(self):

		# Create a test image

		test_image = Image.new('RGB', (100,100))
		test_image.save(os.path.join(self.source_dir, 'test_image'), format='TIFF')

		#  Call the function

		convert_image(self.source_dir)

		# Check if an image is saved in a desitnation directory

		self.assertTrue(os.path.exists(os.path.join(self.dest_dir, 'test_image')))

		# Check if the new image is of JPEG format

		img = Image.open(os.path.join(self.dest_dir, 'test_image'))
		self.assertEqual(img.format, 'JPEG')

		# Check if the new image is resized

		self.assertEqual(img.size, (128,130))

		# Check if the image was rotated

		self.assertEqual(img.width, 128)
		self.assertEqual(img.height, 130)


if __name__ == '__main__':
	unittest.main()





