#!/usr/bin/python
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


def find_max(arg1, arg2, arg3, arg4):
    max_num = -1000
    if arg1 > max_num:
        max_num = arg1
    if arg2 > max_num:
        max_num = arg2
    if arg3 > max_num:
        max_num = arg3
    if arg4 > max_num:
        max_num = arg4

    return max_num


def find_min(arg1, arg2, arg3, arg4):
    min_num = 100000000000000000000000000000000000
    if arg1 < min_num:
        min_num = arg1
    if arg2 < min_num:
        min_num = arg2
    if arg3 < min_num:
        min_num = arg3
    if arg4 < min_num:
        min_num = arg4

    return min_num


N = 4
first_bar = np.tile(0, 0)
second_bar = np.tile(0, 0)
third_bar = np.tile(0, 0)
fourth_bar = np.tile(0, 0)

font = {"family": "normal", "size": 11}

plt.rc("font", **font)

path_1 = "numbers"
path_2 = "numbers2"
path_3 = "numbers3"
path_4 = "numbers4"

results_path1 = open(path_1, "r")
for line in results_path1:
    print(line)
    value = float(line)
    first_bar = np.append(first_bar, value)

print(first_bar)

first_std = (0, 0, 0, 0)

ind = np.arange(N)
width = 0.20

minimum_path1 = min(first_bar)
maximum_path1 = max(first_bar)

results_path1.close()

results_path2 = open(path_2, "r")
for line in results_path2:
    print(line)
    value = float(line)
    second_bar = np.append(second_bar, value)

print(second_bar)
minimum_path2 = min(second_bar)
maximum_path2 = max(second_bar)

path2_std = (0, 0, 0, 0)
results_path2.close()

results_path3 = open(path_3, "r")
for line in results_path3:
    print(line)
    value = float(line)
    third_bar = np.append(third_bar, value)

print(third_bar)
minimum_path3 = min(third_bar)
maximum_path3 = max(third_bar)

path3_std = (0, 0, 0, 0)
results_path3.close()

results_path4 = open(path_4, "r")
for line in results_path4:
    print(line)
    value = float(line)
    fourth_bar = np.append(fourth_bar, value)

print(fourth_bar)
minimum_path4 = min(fourth_bar)
maximum_path4 = max(fourth_bar)

path4_std = (0, 0, 0, 0)
results_path4.close()

minimum = find_min(
    minimum_path1,
    minimum_path2,
    minimum_path3,
    minimum_path4,
)

maximum = find_max(
    maximum_path1,
    maximum_path2,
    maximum_path3,
    maximum_path4,
)


fig, ax = plt.subplots()
path1_rects = ax.bar(ind, first_bar, width, color="r", yerr=first_std)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

path2_rects = ax.bar(
    ind + width, second_bar, width, color="yellowgreen", yerr=path2_std
)

path3_rects = ax.bar(
    ind + (width * 2), third_bar, width, color="royalblue", yerr=path3_std
)

path4_rects = ax.bar(
    ind + (width * 3), fourth_bar, width, color="olive", yerr=path4_std
)

ax.set_ylabel("Ops/s")

ax.set_title("Append Only ", loc="left")
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(("1", "8", "16", "32"))
ax.set_yticks([])  # removes numbers from  y axis
ax.legend(
    (path1_rects[0], path2_rects[0], path3_rects[0], path4_rects[0]),
    ("fake_blk", "Mmap", "Dmap", "Direct I/O"),
)

ax.yaxis.grid(which="major", linestyle="-", linewidth="0.1", color="black")
ax.yaxis.grid(False)
maximum = int("{0:.0f}".format(maximum))
plt.xlabel("Threads")
plt.ylim(0, maximum + 5)


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.,
            0.5 * height,
            "%d" % int(height),
            ha="center",
            va="bottom",
            rotation="vertical",
        )


autolabel(path1_rects)
autolabel(path2_rects)
autolabel(path3_rects)
autolabel(path4_rects)

plt.savefig("figure_ops_sec.eps", format="eps", dpi=1000)
# plt.show()
