import os, sys, mmap


files_received = sys.argv[1:]

for file in files_received:
    if not os.path.isfile(file):
        raise Exception("Only files are accepted!")


for file in files_received:
    with open("reversed-" + file, "wb") as w:
        with open(file, "rb") as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            w.write(mm[::-1])
