#!/bin/bash

(setxkbmap -query | grep -q "layout:\s\+us") && setxkbmap gr || setxkbmap us
