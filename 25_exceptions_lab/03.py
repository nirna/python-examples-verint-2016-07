"""
Write code to make the following unit test pass
"""
import re
import unittest

class InvalidImageExt(Exception):
    def __init__(self):
        self.message = "Not an image extension"

class ImageFile(object):
    def __init__(self,file_name):
        file_name = file_name.strip()
        ext = re.search(r'\.(\w+)$', file_name)
        if ext.group(1) in {'jpg','bmp','png','gif'}:
            open(file_name,'w').close
        else:
            raise InvalidImageExt

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()