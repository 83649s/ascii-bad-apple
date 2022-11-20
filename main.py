from PIL import Image
import time
import curses

def main():
    gradient = [' ', '.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@']
    image_count = 2191
    images = []
    print('Initalizing Images...')
    for i in range(1, image_count):
        counter = str(i)
        im = Image.open(f'input/frame{counter}.jpg')
        im = im.resize((100, 40))
        images.append(im)

    stdscr = curses.initscr()

    for i in range(image_count - 1):
        stdscr.refresh()
        for j in range(im.size[1]):
            line_buffer = ''
            for k in range(im.size[0]):
                line_buffer += gradient[int(images[i].getpixel((k, j))[0] / 21.25)]
            stdscr.addstr(j, 0, line_buffer)
        time.sleep(0.09)



if __name__ == '__main__':
    main()


