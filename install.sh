echo "Sudo access needed for Package manager configs!!!"
#Package manager configuration
sudo cp zsh/makepkg.conf /etc/makepkg.conf
sudo cp zsh/pacman.conf /etc/pacman.conf

if [ ! -d ~/.config ]; then
	mkdir ~/.config
	mkdir ~/.config/i3
fi

if [ ! -d ~/.dir_colors ]; then
	mkdir ~/.dir_colors
fi

./i3/install.sh
cp zsh/zshrc ~/.zshrc
cp zsh/dircolors ~/.dir_colors/
cp i3/config ~/.config/i3/config

echo "Dont forget to install better fonts from here https://gist.github.com/cryzed/e002e7057435f02cc7894b9e748c5671"
