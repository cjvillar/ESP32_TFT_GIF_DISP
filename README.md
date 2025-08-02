# Animated GIF Display 
## With ESP32-S3/ST7735 TFT 

---

## Usage

* Will need the following arduino Libs in Arduino IDE:
Adafruit_GFX.h
Adafruit_ST7735.h
SPI.h


### 1. Resize Your GIF

For use with a 1.8" TFT display, make sure your GIF is exactly:

* **Width**: 160 pixels
* **Height**: 128 pixels

You can resize the GIF using any image editor or online tool before conversion.
TODO: add gif rezising to gif_2_c.py

---

### 2. Convert the GIF to a C Header

Use `gif_2_c.py` to convert your GIF into a `.h` file formatted in RGB565:

```bash
python gif_2_c.py YourGif.gif -o YourGif.h -n <frame_sequence_number>
```

* `YourGif.gif` — the input animated GIF
* `YourGif.h` — the output C header file
* `-n` — (optional) sequence number or index if needed for ordering frames

---

### 3. Include the Header in Your Arduino Sketch

In your `loadGif.ino` file, include the generated header:

```c
#include "YourGif.h"
```
---


├── bitsExample.c       # Example C file, to demo bit shifting
├── code4.gif           # Sample GIF used in the display
├── code4.h             # Header file with converted GIF data
├── gif_2_c.py          # Python script to convert GIFs into C headers (RGB565)
├── loadGif.ino         # Arduino sketch to display the animation
└── README.md           # This README


## TFT -- ESP32-S3
    RST    D3
    CS     D4
    D/C    D5
    DIN(MOSI)    D9
    CLK   D7
    VCC    vvsb
    BL     3v3
    GND    GND


# resources
https://barth-dev.de/online/rgb565-color-picker/


