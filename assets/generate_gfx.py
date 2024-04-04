# this program takes output of MAME gfx save edition (located in "gfx")
# to create tile sheets with proper palette for all layers & palettes
# stored in "tiles"
# once the tiles are generated, there's no need to generate them again
# I'm tracking them, no need to run this program again, but it's useful to keep it
# in case regenerating is necessary, or just to understand how it's done & reuse it
# for other projects
#
# for this game, I'm not going to use Mark C format used for most ports I made, for at least 2 reasons
#
# - Before he stopped answering my emails and disappeared into overworked outer space,
#   Mark explicitly stated that he wasn't interested in doing this game for NeoGeo
# - It started as pngs, and continues as pngs, very easy to understand & monitor

from PIL import Image
import os

this_dir = os.path.abspath(os.path.dirname(__file__))
indir = os.path.join(this_dir,"gfx")

config = {
0:
    {
    (0,31):(0x10,0X10),
    (32,63):(1,0x10),
    (64,95):(0x12,0x12),
    (96,127):(3,3),
    (128,159):(4,0x15),
    (160,255):(1,0x15)
},
1:
    {
    (0,31):(8,8),
    (32,95):(9,9),
    (96,191):(0xB,0x1B),
    (192,223):(0xE,0xB),
    (224,255):(0x1F,0x1F)
}}

for cs,name in enumerate(["back","fore"]):



    setdir = os.path.join(indir,f"set_{cs}")
    cc = config[cs]

    out = [Image.new("RGB",(256,64)) for _ in range(2)]
    for (start,end),pals in cc.items():
        for k,p in enumerate(pals):
            img = Image.open(os.path.join(setdir,f"{p:02X}.png"))
            for i in range(start,end+1):
                x = (i%32)*8
                y = (i//32)*8
                for dx in range(8):
                    for dy in range(8):
                        out[k].putpixel((x+dx,y+dy),img.getpixel((x+dx,y+dy)))

    for i in range(2):
        out[0].save(os.path.join(this_dir,f"tiles/sheet_{name}_{i}.png"))

