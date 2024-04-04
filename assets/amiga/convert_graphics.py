
from PIL import Image
import os

this_dir = os.path.abspath(os.path.dirname(__file__))
indir = os.path.join(this_dir,"..","tiles")
outdir = os.path.join(this_dir,"..","src","amiga")

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
3:{
"A71BCE":None,
"0A07BD":None,  # dark blue
"CDF040":None
},
5:{
"D5FBF9":None, # white
"2DB8E0":None  # light blue
}

}
}



# all foreground tiles need cyan merging (the "*" character is slightly different color wise)
# but barely noticeable so it's an easy slot to gain
for fc in config["fore"].values():
    fc["36E8E9"] = "35E7BF"

# stages 2,4,5 need the same replacements as stage 1 exactly
for i in [2,4,5]:
    config["fore"][i] = config["fore"][1].copy()

config["back"][2] = config["back"][1].copy()
config["back"][4] = config["back"][3].copy()

