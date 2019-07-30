from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("carousel.jpg")
    #pick one of the filters here
    newImg = breezy_emphasize_color(myImg)

    newImg.show()

main()
