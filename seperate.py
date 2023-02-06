import shutil
import math
import os
import numpy as np

root_dir = "./rps/"
base_outdir = './rps-test-set/'

classes = ["paper", "rock", "scissor"]

for clss in classes:
    print('------------' + clss + '-------------')
    dirtry = root_dir + clss
    files = os.listdir(dirtry)
    np.random.shuffle(files)
    print(len(files))

    target_dir = base_outdir + clss
    images_to_pass = files[math.floor(0.8*len(files)): math.floor(0.9*len(files))]
    for img in images_to_pass:
        img = dirtry + '/' + img
        shutil.move(img, target_dir)
    
    files = os.listdir(target_dir)
    print(len(files))

print("END")