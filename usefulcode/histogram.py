#!/usr/bin/python
from __future__ import division
"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

path1_results = np.tile(0, 0)
path2_results = np.tile(0, 0)
font = {'family': 'normal',
        'size': 11}

plt.rc('font', **font)

# file format should be a number in each line
path_1 = '/home/hacker/concurrent implementation/dmapwithdoublebuff/numbers'
path_2 = '/home/hacker/concurrent implementation/dmapwithdoublebuff/numbers1'


results_file_arm = open(path_1, 'r')
for line in results_file_arm:
    print(line)
    value = float(line)
    path1_results = np.append(path1_results, value)

print(path1_results)
N = 5
# path1_results = (551.3, 107.1, 143.6, 101.4, 471.8,535.5)
path1_std = (0, 0, 0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

path1_min = min(path1_results)
path1_max = max(path1_results)
# plt.rc('axes', labelsize=12)
# plt.rc('font', size=12)

results_file_arm.close()
results_file_intel = open(path_2, 'r')

for line in results_file_intel:
    print(line)
    value = (float(line))
    path2_results = np.append(path2_results, value)

fig, ax = plt.subplots()
rects1 = ax.bar(ind, path1_results, width, color='r', yerr=path1_std)
path2_std = (0, 0, 0, 0, 0)


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
print(path2_results)
# path2_results = (65.9, 7.4, 13.1, 7.4, 49.8, 65.9,45.3,87.6)
rects2 = ax.bar(ind + width, path2_results, width, color='yellowgreen', yerr=path2_std)
path2_min = min(path2_results)
path2_max = max(path2_results)

if path1_min < path2_min:
    minimum = path1_min
else:
    minimum = path2_min


if path1_max > path2_max:
    maximum = path1_max
else:
    maximum = path2_max

# add some text for labels, title and axes ticks
ax.set_ylabel('Y axis')

ax.set_title('Graph Name', loc="left")
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('load_a', 'run_a', 'run_b', 'run_c', 'run_d'))
ax.set_yticks([])  # removes numbers from  y axis
ax.legend((rects1[0], rects2[0]), ('RED', 'GREEN'))
ax.yaxis.grid(which='major', linestyle='-', linewidth='0.1', color='black')
ax.yaxis.grid(False)
maximum = int("{0:.0f}".format(maximum))
plt.xlabel("X Axis")
plt.ylim(0, maximum + 5)


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5 * height, '%d' % int(height), ha='center', va='bottom', rotation='vertical')


autolabel(rects1)
autolabel(rects2)

plt.savefig('figure_ops_sec.eps', format='eps', dpi=1000)
# plt.show()
