
from PIL import Image
import os
import bitplanelib

this_dir = os.path.abspath(os.path.dirname(__file__))
indir = os.path.join(this_dir,"..","tiles")
outdir = os.path.join(this_dir,"..","..","src","amiga")

dumpdir = os.path.join(this_dir,"dumps")

def hex2rgb(c):
    return tuple(int(c[i:i+2],16) for i in range(0,6,2))

config = {"fore":
{
1:{
"F4CDCF":"FFFFFF",
"A518A5":"D31FD2"
},

3:{
"F6F644":None
}
},
"back":{
1:{
"A71BCE":None,
"D11EAA":None,
"CDF040":None
},
2:{
"A71BCE":None,
"CDF040":None
},
3:{
"A71BCE":None,
"0A07BD":None,  # dark blue
"CDF040":None
},
5:{
"C0C136":"EDC63A", # star yellow => boss yellow
"2DB8E0":None  # light blue
}

}
}



level_info = {
1:{"palette":0,"back_end_y":5},
2:{"palette":1,"back_end_y":5},
3:{"palette":0,"back_start_y":4},
4:{"palette":1,"back_start_y":4},
5:{"palette":1,"back_end_y":5},
}


# all foreground tiles need cyan merging (the "*" character is slightly different color wise)
# but barely noticeable so it's an easy slot to gain
for fc in config["fore"].values():
    fc["36E8E9"] = "35E7BF"

# stages 2,4,5 need the same replacements as stage 1 exactly
for i in [2,4,5]:
    config["fore"][i] = config["fore"][1].copy()

config["back"][4] = config["back"][3].copy()


def replace_color(img,color,replacement_color):
    rval = Image.new("RGB",img.size)
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            c = (x,y)
            rgb = img.getpixel(c)
            if rgb == color:
                rgb = replacement_color or (0,0,0)
            rval.putpixel(c,rgb)
    return rval


imgdict = dict()
for layer in ["back","fore"]:
    for p in [0,1]:
        img = Image.open(os.path.join(indir,f"sheet_{layer}_{p}.png"))
        imgdict[layer,p] = img

black_row = Image.new("RGB",(256,8))

with open(os.path.join(outdir,"palette.68k"),"w") as f:

    # generate tiles for each level, back/fore: 10 sheets
    for layer in ["back","fore"]:
        cd = config[layer]
        for level,data in sorted(cd.items()):
            linf = level_info[level]
            p = linf["palette"]
            yend = linf.get(f"{layer}_end_y",8)
            ystart = linf.get(f"{layer}_start_y",0)

            img_in = imgdict[layer,p]

            img_out = img_in

            for c1,c2 in data.items():
                img_out = replace_color(img_out,hex2rgb(c1),hex2rgb(c2) if c2 else None)

            palette = bitplanelib.palette_extract(img_out,0xF0)
            palette += [(16,16,16)]*(8-len(palette))

            f.write(f"palette_{layer}_{level}:\n")
            bitplanelib.palette_dump(palette,f)
            # blacken strips if needed
            for y in range(0,ystart):
                img_out.paste(black_row,(0,y*8))

            for y in range(yend,8):
                img_out.paste(black_row,(0,y*8))


            #img_out.save(f"sheet_{layer}_{level}_{p}.png")