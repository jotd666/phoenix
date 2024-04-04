# generate equivalent of Mark C format _gfx.* from MAME tilesaving edition gfxrips

from PIL import Image,ImageOps
import os,glob,collections,itertools

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

    out[0].save(f"sheet_{name}_0.png")
    out[1].save(f"sheet_{name}_1.png")
