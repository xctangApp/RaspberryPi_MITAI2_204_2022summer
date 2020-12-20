import os
from brachiograph import BrachioGraph
from linedraw import *

inner_arm = 8
outer_arm = 8

bg = BrachioGraph(inner_arm, outer_arm)

if __name__ == "__main__":

    photo_path = "~/BrachioGraph/images/"
    photo_filename = "cam"
    photo_jpg = photo_path + photo_filename + ".jpg"
    photo_json = photo_path + photo_filename + ".json"

    # take photo and save it
    os.system('raspistill -o ' + photo_jpg)
    # vectorise an image to json file
    image_to_json(photo_filename, draw_contours=2, draw_hatch=16)
    # draw with the plotter
    bg.plot_file(photo_json)
