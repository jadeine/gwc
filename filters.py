# Rename this file to be "filters.py"
# Add commands to import modules here
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(pic):
    im = Image.open(pic)
    return im


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(pic):
    pic.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(pic, sunset2):
    pic.save(sunset2)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(pic):
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    pixels = list(pic.getdata())
    list_len = len(pixels)
    for i in range(list_len):
        red_value = pixels[i][0]
        green_value = pixels[i][1]
        blue_value = pixels[i][2]
        sum = red_value + green_value + blue_value
        if sum < 182:
            pixels[i] = darkBlue
        elif sum >= 182 and sum < 364:
            pixels[i] = red
        elif sum >= 364 and sum < 546:
            pixels[i] = lightBlue
        else:
            pixels[i] = yellow

    obamasun = im.putdata(pixels)
    def save_img(im, obamasun):
        im.save(obamasun)
    save_img(im, "obamasun.jpg")
    newpic = load_img("obamasun.jpg")
    show_img(newpic)

def mono_blue(pic):
    lightestBlue = (229, 250, 250)
    lighterBlue = (187, 232, 233)
    lightBlue2 = (130, 213, 216)
    lghtBlue = (77, 184, 188)
    pixels = list(pic.getdata())
    list_len = len(pixels)
    for i in range(list_len):
        red_value = pixels[i][0]
        green_value = pixels[i][1]
        blue_value = pixels[i][2]
        sum = red_value + green_value + blue_value
        if sum < 182:
            pixels[i] = lghtBlue
        elif sum >= 182 and sum < 364:
            pixels[i] = lightBlue2
        elif sum >= 364 and sum < 546:
            pixels[i] = lighterBlue
        else:
            pixels[i] = lightestBlue

    bluesun = im.putdata(pixels)
    def save_img(im, bluesun):
        im.save(bluesun)
    save_img(im, "bluesun.jpg")
    newpic = load_img("bluesun.jpg")
    show_img(newpic)

def half_obama(pic):
    #width = pic.width()
    #half_width = width / 2
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    pixels = list(pic.getdata())
    list_len = len(pixels)#/ half_width
    for i in range(list_len // 2):
        red_value = pixels[i][0]
        green_value = pixels[i][1]
        blue_value = pixels[i][2]
        sum = red_value + green_value + blue_value
        if sum < 182:
            pixels[i] = darkBlue
        elif sum >= 182 and sum < 364:
            pixels[i] = red
        elif sum >= 364 and sum < 546:
            pixels[i] = lightBlue
        else:
            pixels[i] = yellow

    new_image2 = Image.new("RGB", pic.size)
    new_image2.putdata(pixels)
    return new_image2

im = load_img("carousel.jpg")
show_img(im)
#half_obama(im)
mono_blue(im)
#obamicon(im)
#save_img(im, "sunset2.jpg")
