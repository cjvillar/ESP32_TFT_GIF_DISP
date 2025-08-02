/*
bit shifting example

technique used in gif_2_c.py:

 frame_data = []
        for y in range(height):
            for x in range(width):
                r, g, b = frame.getpixel((x, y))
                rgb = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                frame_data.append(rgb)

        all_frames.extend(frame_data)
*/

#include<stdio.h>
#include <stdint.h>

int main(){
    uint16_t rgb = 0xff;
    printf("%x\n",rgb);
    printf("%x\n",rgb << 8);
}
