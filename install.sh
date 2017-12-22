if [ ! -d ~/.config ] then
	mkdir ~/.config
	mkdir ~/.dir_colors
fi
./i3/install.sh
./urxvt/install.sh
cp zsh/zshrc ~/.zshrc
cp -r i3 ~/.config
cp -r ranger ~/.config
cp urxvt/dircolors ~/.dir_colors/dircolors
cp urxvt/Xresources ~/.Xresources
xrdb merge ~/.Xresources
