echo "Sudo access needed for Package manager configs!!!"
#Package manager configuration
sudo cp zsh/makepkg.conf /etc/makepkg.conf
sudo cp zsh/pacman.conf /etc/pacman.conf

if [ ! -d ~/.config ]; then
	mkdir ~/.config
fi

if [ ! -d ~/.dir_colors ]; then
	mkdir ~/.dir_colors
fi

./i3/install.sh
cp zsh/zshrc ~/.zshrc
cp zsh/dircolors ~/.dir_colors/
cp i3/config ~/.config/i3/config

# Gnome terminal solarized
git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git gterm-solarized
cd gterm-solarized
./install.sh
cd ..

echo "Dont forget to install better fonts from here https://gist.github.com/cryzed/e002e7057435f02cc7894b9e748c5671"
