
from PIL import Image
import os,collections
import bitplanelib

this_dir = os.path.abspath(os.path.dirname(__file__))
indir = os.path.join(this_dir,"..","tiles","aga")
outdir = os.path.join(this_dir,"..","..","src","amiga")

dump_pics = True

dumpdir = os.path.join(this_dir,"dumps")
if dump_pics and not os.path.exists(dumpdir):
    os.mkdir(dumpdir)



imgdict = dict()
for layer in ["back","fore"]:
    for level in [0,1]:
        img = Image.open(os.path.join(indir,f"sheet_{layer}_{level}.png"))
        imgdict[layer,level] = img

black_row = Image.new("RGB",(256,8))

tile_cache = collections.defaultdict(list)

with open(os.path.join(outdir,"palette_aga.68k"),"w") as fp:

    # generate tiles for each level, back/fore: 10 sheets
    for layer in ["back","fore"]:

        fp.write(f"{layer}_palettes:\n")
        for level in [0,1]:
            fp.write(f"\t.long\tpalette_{layer}_{level}\n")

    for layer in ["back","fore"]:

        for level in [0,1]:

            img_in = imgdict[layer,level]

            img_out = img_in


            palette = bitplanelib.palette_extract(img_out)
            if len(palette)>16:
                raise Exception(f"Palette layer={layer} level={level} more than 16 colors: {len(palette)}")
            palette += [(16,16,16)]*(16-len(palette))

            fp.write(f"palette_{layer}_{level}:\n")
            bitplanelib.palette_dump(palette,fp,pformat=bitplanelib.PALETTE_FORMAT_ASMGNU)
            # blacken strips if needed, makes lighter tiles



            index = 0
            for y in range(0,64,8):
                for x in range(0,256,8):
                    # create 8x8 tiles
                    tile = Image.new("RGB",(8,8))
                    for dx in range(8):
                        for dy in range(8):
                            p =img_out.getpixel((x+dx,y+dy))
                            tile.putpixel((dx,dy),p)
                    #tile.save(f"tile_{x}_{y}_{level}_{layer}.png")
                    raw = bitplanelib.palette_image2raw(tile,None,palette)
                    tile_cache[raw].append((index,layer,level))
                    index += 1


# drop the "defaultdict" property
tile_cache = dict(tile_cache)
# invert the dict per layer/level

tile_dict = collections.defaultdict(lambda : [0]*256)
for k,vl in tile_cache.items():
    for (index,layer,level) in vl:
        tile_dict[layer,level][index] = k

with open(os.path.join(outdir,"graphics_aga.68k"),"w") as fp:
    for layer in ["back","fore"]:
        fp.write(f"\t.global\t{layer}_tile_table\n")

    for layer in ["back","fore"]:
        fp.write(f"{layer}_tile_table:\n")

        for level in [0,1]:
            fp.write(f"\t.long\t{layer}_lvl_{level}_tile_table\n")

    fp.write("\n")

    for layer in ["back","fore"]:
        for level in [0,1]:
            fp.write(f"{layer}_lvl_{level}_tile_table:\n")
            for raw in tile_dict[layer,level]:
                # just use first occurrence for name


                tile_name = "tile_{}_{}_{}".format(*(tile_cache[raw][0]))
                fp.write(f"\t.long\t{tile_name}\n")
            fp.write("\n")

    already_seen = set()
    for layer in ["back","fore"]:
        for level in [0,1]:
            for raw in tile_dict[layer,level]:
                # just use first occurrence for name
                tile_name = "tile_{}_{}_{}".format(*(tile_cache[raw][0]))
                if tile_name in already_seen:
                    continue
                already_seen.add(tile_name)
                fp.write(f"{tile_name}:")
                bitplanelib.dump_asm_bytes(raw,fp,mit_format=True)
            fp.write("\n")

##    fp.write("\n")
##    for k,v in tile_cache.items():
##        fp.write(f"{v}:\n")
##

