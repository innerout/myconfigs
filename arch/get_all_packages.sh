#!/bin/bash

pacman -Qqe > packages.txt && pacman -Qqm >> packages.txt
