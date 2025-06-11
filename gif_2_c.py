'''
Gif to C array for use with esp32-s3 
usage: python gif_2_c.py Some.gif -o SomeGif.h -n <show sequence order int>
ouput: C header file 

FOR USE WITH TFT 1.8 INCH you must edit the gif size:
WIDTH 160
HEIGHT 128
'''

from PIL import Image, ImageSequence
import argparse


def gif_to_rgb565_array(gif_path):
    '''Convert Gif to RGB565: 16bit colors, 5 red bits, 6 green bits, 5 blue bits 
    This is the format used by the ST7735 (or so im told)'''
    img = Image.open(gif_path)
    width, height = img.size

    all_frames = []

    for frame in ImageSequence.Iterator(img):
        frame = frame.convert("RGB")
        frame.load()
        #flip frame vertically if needed
        #frame = frame.transpose(Image.FLIP_TOP_BOTTOM)

        frame_data = []
        for y in range(height):
            for x in range(width):
                r, g, b = frame.getpixel((x, y))
                rgb = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                frame_data.append(rgb)

        all_frames.extend(frame_data)

    return all_frames, width, height, img.n_frames


def write_c_array(array, width, height, frame_count, output_file, frameNum):
    '''Write each array into a header file '''
    with open(output_file, "w") as f:
        f.write(f"#ifndef IMAGE_DATA{frameNum}_H\n")
        f.write(f"#define IMAGE_DATA{frameNum}_H\n\n")
        f.write("#include <stdint.h>\n\n")
        f.write(f"#define IMG_WIDTH {width}\n")
        f.write(f"#define IMG_HEIGHT {height}\n")
        f.write(f"#define NUM_FRAMES {frame_count}\n\n")
        f.write(f"const uint16_t image_data{frameNum}[{len(array)}] = {{\n")

        for i in range(len(array)):
            if i % width == 0:
                f.write("  ")
            f.write(f"0x{array[i]:04X}, ")
            if (i + 1) % width == 0:
                f.write("\n")

        f.write("};\n\n")
        f.write(f"#endif  // IMAGE_DATA{frameNum}_H\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert multi-frame GIF to C array for Arduino TFT."
    )
    parser.add_argument("gif", type=str, help="Input GIF file.")
    parser.add_argument(
        "-o", "--output", type=str, default="image_data.h", help="Output header file."
    )

    parser.add_argument(
        "-n",
        "--frameNum", #consider changing to image sequence number
        type=int,
        default=1,
        help="sequence order if in an array gifs",
    )
    args = parser.parse_args()

    frameNum = args.frameNum
    rgb565_data, width, height, frame_count = gif_to_rgb565_array(args.gif)
    write_c_array(rgb565_data, width, height, frame_count, args.output, frameNum)
