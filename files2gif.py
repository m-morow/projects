# Code from stack overflow
import imageio
import os

path = './'

image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.png', '.jpeg') ):
        filenames.append(filename)

filenames.sort() # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('synth_prop.gif'), images, duration = 0.3) # duration in seconds
