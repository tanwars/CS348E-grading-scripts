import numpy as np
import matplotlib.pyplot as plt
import os
import sys

assert len(sys.argv)==2, 'enter SUID'
foldername = sys.argv[1]

def findfile(name, path):
    files = []
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            files.append(os.path.join(dirpath, name))
    return files
filepaths = findfile('console_output.log', './'+foldername)

print(filepaths)

for filepath in filepaths:
    with open(filepath) as f:
        lines = f.readlines()

    update_idx = []
    mean_r = []
    med_r = []
    min_r = []
    max_r = []
    for line in lines:
        comps = line.split(' ')
        # print(comps)
        if 'Updates' in comps:
            update_idx.append(int(comps[9].strip(',')))
        if 'reward' in comps:
            mean_r.append(float((comps[7].split('/'))[0]))
            med_r.append(float(((comps[7].split('/'))[1]).strip(',')))
            min_r.append(float((comps[10].split('/'))[0]))
            max_r.append(float(((comps[10].split('/'))[1]).strip(',')))

    assert len(update_idx)==len(mean_r), 'something wrong with log file'

    cmap = plt.cm.get_cmap('hsv', 5)

    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(filepath) 


    ax.plot(update_idx,mean_r, color=cmap(0), label = f'mean', zorder = 0)
    ax.plot(update_idx,med_r, color=cmap(1), label = f'med', zorder = 0)
    # ax.plot(update_idx,min_r, color=cmap(2), label = f'min', zorder = 0)
    # ax.plot(update_idx,max_r, color=cmap(3), label = f'max', zorder = 0)

    ax.legend()
    ax.set_xlabel('update_idx')
    ax.set_ylabel('reward')
    ax.grid(True)

    # plt.savefig(f'log_rewards.png')

plt.show()