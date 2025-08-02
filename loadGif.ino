#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SPI.h>

// image header files  
// defines image_data#, IMG#_WIDTH, IMG#_HEIGHT, IMG#_NUM_FRAMES
#include "code4.h"  

// defines TFT pins on esp32
#define TFT_CS     4
#define TFT_RST    3
#define TFT_DC     5
#define TFT_SCLK   7
#define TFT_MOSI   9

// init TFT obj
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

// animation struct 
struct Animation {
  const uint16_t* data;
  int width;
  int height;
  int numFrames;
};

// animation array
Animation animations[] = {
  { image_data1, IMG1_WIDTH, IMG1_HEIGHT, NUM1_FRAMES },
  { image_data2, IMG2_WIDTH, IMG2_HEIGHT, NUM2_FRAMES },
  { image_data3, IMG3_WIDTH, IMG3_HEIGHT, NUM3_FRAMES }
};

#define NUM_ANIMATIONS (sizeof(animations) / sizeof(animations[0]))

void setup() {
  Serial.begin(115200);
  SPI.begin(TFT_SCLK, -1, TFT_MOSI, TFT_CS);
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(3);  
  tft.fillScreen(ST77XX_BLACK);
}

// draws single frame
void drawFrame(const uint16_t* frame, int width, int height) {
  tft.setAddrWindow(0, 0, width, height);
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      uint16_t color = frame[y * width + x];
      tft.drawPixel(x, y, color);
    }
  }
}

// animates full sequence.
void drawAnimation(const Animation& anim) {
  for (int f = 0; f < anim.numFrames; f++) {
    const uint16_t* framePtr = anim.data + (f * anim.width * anim.height);
    drawFrame(framePtr, anim.width, anim.height);
    delay(500);  // frame speed
  }
}

// loop through animations
void loop() {
  for (int i = 0; i < NUM_ANIMATIONS; i++) {
    drawAnimation(animations[i]);
    delay(300);  // dleay between each animation 
  }
}