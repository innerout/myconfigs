if [ ! -d ~/.config ]; then
	mkdir ~/.config
fi

if [ ! -d ~/.dir_colors ]; then
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
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git gterm-solarized
cd gterm-solarized
./install.sh
cd ..

