import upygame as pygame

def ConvStrTo4bitPixelArray(w, h, strArray, numArray):
    #print("strArray=", strArray)
    for y in range(h):
        for x in range(w//2):
            #print("y=",y," x=", x*2)
            pixStr = "0x" + strArray[y*w + (x*2)] + strArray[y*w + (x*2) + 1]
            pix = int(pixStr, 16)
            numArray.append(pix)

def ConvStrTo2bitPixelArray(w, h, strArray, numArray):
    #print("strArray=", strArray)
    for y in range(h):
        for x in range(w//4):
            # make a byte
            #print("y=",y," x=", x*4)
            c0 = int(strArray[y*w + (x*4)])
            c1 = int(strArray[y*w + (x*4) + 1])
            c2 = int(strArray[y*w + (x*4) + 2])
            c3 = int(strArray[y*w + (x*4) + 3])
            #print("c0=", bin(c0),"c1=", bin(c1),"c2=", bin(c2),"c3=", bin(c3))
            bytepixels = (c0 << 6) + (c1 << 4) + (c2 << 2) + c3
            #print("bytepixels=",bin(bytepixels))
            numArray.append(bytepixels)

# Rock head picture: 1
w = 16
h = 6
rockHead1Pixels = [
0x01,0x10,0x20,0x00,
0x05,0x54,0x24,0x00,
0x07,0x74,0x24,0x00,
0x05,0xA4,0x24,0x40,
0x31,0xA2,0xA5,0x40,
0x3D,0xAA,0xA5,0x40,
]
rockHead1Surf = pygame.surface.Surface(w, h, bytearray(rockHead1Pixels))
rockHead2Surf = rockHead1Surf
rockHead3Surf = rockHead1Surf
rockHead4Surf = rockHead1Surf
rockHead5Surf = rockHead1Surf
rockHead6Surf = rockHead1Surf
rockHead7Surf = rockHead1Surf

# Rock picture: 1
w = 16
h = 14
rock1Pixels = [
0xFF,0xFF,0xFF,0xA0,
0xFA,0xAA,0xAA,0x50,
0x55,0x55,0x55,0x50,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
0x3E,0xAA,0xA5,0x40,
]
rock1Surf = pygame.surface.Surface(w, h, bytearray(rock1Pixels))
rock2Surf =  rock1Surf
rock3Surf =  rock1Surf
rock4Surf =  rock1Surf
rock5Surf =  rock1Surf
rock6Surf =  rock1Surf
rock7Surf =  rock1Surf

w = 32
h = 16
shipF1Pixels = [
0xFC,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0xFF,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0xFF,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,
0x3F,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,
0x3F,0xFC,0x00,0x00,0x00,0x00,0x00,0x00,
0x3F,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,
0x0F,0xFF,0xC0,0x00,0x00,0x00,0x00,0x00,
0x0F,0xFF,0xF0,0x00,0x00,0x00,0x00,0x00,
0x03,0xFF,0xFF,0xFF,0xFF,0xFF,0xF0,0x00,
0x03,0xFF,0xFF,0xFF,0xFF,0xFF,0xFC,0x00,
0x0C,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xC0,
0x0F,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFC,
0x0F,0xFF,0xFF,0xD5,0x55,0x5F,0xFF,0xD7,
0x0F,0xFF,0xF5,0x55,0x55,0x57,0xFF,0xDF,
0x0C,0x3F,0xFF,0xFF,0xFF,0xFF,0xFF,0xFC,
0x00,0x00,0x3C,0x00,0x00,0x00,0x0F,0x00,
]
shipF1Surf = pygame.surface.Surface(w, h, bytearray(shipF1Pixels))

# Bomb
w = 8
h = 8
bombColorMap = [60683,32963,49572,65502]
bombPixels = [
0xF3,0xC0,
0xF3,0xC0,
0x0C,0x00,
0x3F,0x00,
0x3F,0x00,
0x3F,0x00,
0x3F,0x00,
0x0C,0x00,
]
bombSurf = pygame.surface.Surface(w, h, bytearray(bombPixels))

# Explosion 1
w = 16
h = 16
explosion1ColorMap = [65535,60288,63353,65351]

# Explosion 1, frame 1
explosion1f1Pixels = [
0x00,0x00,0x00,0x00,
0x00,0x00,0x30,0x00,
0x00,0xC0,0x20,0x00,
0x0C,0xF7,0x64,0xF0,
0x03,0xFF,0xE7,0x80,
0x00,0xFF,0xEE,0xC0,
0x01,0x7E,0xAA,0xFF,
0x03,0xEA,0xAA,0xB0,
0x3E,0xAA,0xAF,0x40,
0x00,0xFE,0xBB,0x40,
0x00,0x7A,0xAF,0xC0,
0x03,0xEF,0xE5,0x40,
0x0C,0xF1,0xE5,0x00,
0x03,0xC0,0x30,0x00,
0x0C,0x00,0x30,0x00,
0x00,0x00,0x00,0x00,
]
explosion1f1Surf = pygame.surface.Surface(w, h, bytearray(explosion1f1Pixels))

# Explosion 1, frame 2
explosion1f2Pixels = [
0x00,0x15,0x40,0x00,
0x01,0x6A,0x90,0x00,
0x01,0x6A,0xBA,0x50,
0x06,0x59,0xBA,0x54,
0x15,0x55,0x79,0x64,
0x5A,0x55,0xF7,0x64,
0x6A,0x9F,0xFD,0x55,
0x69,0x7F,0xFF,0xD9,
0x17,0xFF,0xF5,0xA9,
0x06,0x57,0xD5,0xA9,
0x1A,0x9F,0xD5,0x64,
0x19,0x75,0x7A,0x90,
0x16,0x5A,0x7A,0x90,
0x05,0x66,0xBA,0x90,
0x04,0x01,0x9A,0x50,
0x00,0x00,0x55,0x40,
]
explosion1f2Surf = pygame.surface.Surface(w, h, bytearray(explosion1f2Pixels))

# Explosion 1, frame 3
explosion1f3Pixels = [
0x01,0x00,0x69,0x00,
0x06,0x91,0xAA,0xA9,
0x06,0xA5,0xAA,0xA8,
0x1A,0xA8,0x6A,0xA9,
0x2A,0xA8,0x02,0xA9,
0x6A,0x56,0x85,0xA5,
0xAA,0x86,0xAA,0xA4,
0x2A,0x82,0xAA,0x40,
0x0A,0x82,0xAA,0x40,
0x1A,0x82,0xA9,0x94,
0x1A,0x42,0xA2,0xA9,
0x6A,0xA4,0x42,0xA9,
0x6A,0xA4,0x19,0xA8,
0x19,0xA0,0xAA,0xA8,
0x1A,0x91,0xAA,0x50,
0x05,0x40,0x15,0x00,
]
explosion1f3Surf = pygame.surface.Surface(w, h, bytearray(explosion1f3Pixels))

# Explosion 1, frame 4
explosion1f4Pixels = [
0x00,0x00,0x01,0xA4,
0x29,0x00,0x02,0xA9,
0x2A,0x40,0x00,0x2A,
0xA9,0x00,0x00,0x19,
0xA8,0x00,0x40,0x18,
0x10,0x01,0x90,0x00,
0x00,0x01,0x94,0x00,
0x05,0x80,0x29,0x00,
0x0A,0x80,0x69,0x00,
0x05,0x00,0xA4,0x00,
0x00,0x00,0x60,0x00,
0x00,0x00,0x00,0x25,
0x25,0x00,0x00,0x6A,
0x6A,0x80,0x01,0xA9,
0x29,0x00,0x0A,0xA8,
0x19,0x00,0x02,0x80,
]
explosion1f4Surf = pygame.surface.Surface(w, h, bytearray(explosion1f4Pixels))

