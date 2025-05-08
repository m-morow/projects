# Code from stack overflow
import imageio
import os

path = '/Users/mata7085/Desktop/creep_files/'

image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.png', '.jpeg') ):
        filenames.append(filename)

filenames.sort() # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('synth_prop.gif'), images, fps = 0.5) # use fps call to adjust duration
