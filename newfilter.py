import filters

def invert_colors(pic):
    pixels = list(pic.getdata())
    list_len = len(pixels)
    for i in range(list_len):
        red_value = pixels[i][0]
        green_value = pixels[i][1]
        blue_value = pixels[i][2]
        red_value - 255
        green_value - 255
        blue_value - 255

    invertsun = im.putdata(pixels)
    def save_img(im, invertsun):
        im.save(invertsun)
    save_img(im, "invertsun.jpg")
    newpic = load_img("invertsun.jpg")
    show_img(newpic)

    im = load_img("sunset.jpg")
    show_img(im)
    invert_colors(im)
