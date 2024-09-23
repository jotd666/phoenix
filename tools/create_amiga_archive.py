import subprocess,os,glob,shutil
gamename = "phoenix"

progdir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
for t in ["ocs","aga"]:
    packed_exe = os.path.join(progdir,f"{gamename}_{t}.rnc")
    if os.path.exists(packed_exe):
        os.remove(packed_exe)


# JOTD path for cranker, adapt to wh :)
os.environ["PATH"] += os.pathsep+r"K:\progs\cli"

cmd_prefix = ["make","-f",os.path.join(progdir,"makefile.am")]

subprocess.check_call(cmd_prefix+["clean"],cwd=os.path.join(progdir,"src"))

for s in ["convert_sounds.py","convert_graphics_aga.py","convert_graphics_ocs.py"]:
    subprocess.check_call(["cmd","/c",s],cwd=os.path.join(progdir,"assets","amiga"))

subprocess.check_call(cmd_prefix+["RELEASE_BUILD=1"],cwd=os.path.join(progdir,"src"))
# create archive

outdir = os.path.join(progdir,f"{gamename}_HD")
if os.path.exists(outdir):
    for x in glob.glob(os.path.join(outdir,"*")):
        os.remove(x)
else:
    os.mkdir(outdir)
for file in ["readme.md",f"{gamename}_ocs",f"{gamename}_aga",f"{gamename}.slave",f"{gamename}_AGA.slave"]:
    shutil.copy(os.path.join(progdir,file),outdir)

for icon in glob.glob(os.path.join(progdir,"assets","amiga","*.info")):
    shutil.copy(icon,outdir)
shutil.copy(os.path.join(progdir,"assets","amiga","Phoenix.png"),outdir)

# pack the file for floppy
for t in ["ocs","aga"]:
    exe = os.path.join(progdir,f"{gamename}_{t}")
    packed_exe = exe +".rnc"
    subprocess.check_output(["cranker_windows.exe","-f",os.path.join(progdir,exe),
"-o",packed_exe])
