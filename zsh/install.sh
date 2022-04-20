#!/bin/bash
yay -S autojump lsd fkill fd ripgrep the_silver_searcher
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
