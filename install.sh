echo "Sudo access needed for Package manager configs!!!"
#Package manager configuration
sudo cp zsh/makepkg.conf /etc/makepkg.conf
sudo cp zsh/pacman.conf /etc/pacman.conf

if [ ! -d ~/.config ]; then
	mkdir ~/.config
	mkdir ~/.config/i3
	mkdir ~/.config/alacritty
	mkdir ~/.config/kitty
fi

if [ ! -d ~/.dir_colors ]; then
	mkdir ~/.dir_colors
fi

./i3/install.sh
cp zsh/zshrc ~/.zshrc
cp zsh/dircolors ~/.dir_colors/
cp i3/config ~/.config/i3/config
cp terminal/alacritty/* ~/.config/alacritty/
cp terminal/kitty/* ~/.config/kitty/

echo "Dont forget to install better fonts from here https://gist.github.com/cryzed/e002e7057435f02cc7894b9e748c5671"
