from PIL import Image
import os

images = [image for image in os.listdir('images') if image.endswith('.jpg') or image.endswith('.png')]


class ImagesMaker:
    def __init__(self, images, scale):
        self.images = images
        self.scale = scale

    def check_size(self, image):
        width = int(image.size[0] * self.scale)
        height = int(image.size[1] * self.scale)
        return [width, height]

    def change_photo(self):
        for item in self.images:
            photo = Image.open(f'images/{item}')
            actual_sizes = self.check_size(photo)
            photo.resize((actual_sizes[0], actual_sizes[1])).save(f'./{item}', quality=50)
            # photo.save(f'good_images/{item}')


if __name__ == '__main__':
    ImagesMaker(images, 0.65).change_photo()
