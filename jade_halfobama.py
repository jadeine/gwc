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

    newpic = im.putdata(pixels)
    def save_img(im, newpic):
        im.save(newpic)
    save_img(im, "halfobama.jpg")
    newerpic = load_img("halfobama.jpg")
    show_img(newerpic)
