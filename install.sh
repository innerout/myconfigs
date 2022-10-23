echo "Sudo access needed for Package manager configs!!!"
#Package manager configuration
sudo cp arch/makepkg.conf /etc/makepkg.conf
sudo cp arch/pacman.conf /etc/pacman.conf

if [ ! -d ~/.config ]; then
	mkdir -p ~/.config/i3
	mkdir -p ~/.config/alacritty
	mkdir -p ~/.config/kitty
fi

./i3/install.sh
cp zsh/z4human/.p10k.zsh zsh/z4human/.zshenv zsh/z4human/.zshrc ~/
cp i3/config ~/.config/i3/config
cp terminal/alacritty/* ~/.config/alacritty/
cp terminal/kitty/* ~/.config/kitty/

echo "Dont forget to install better fonts from here https://gist.github.com/cryzed/e002e7057435f02cc7894b9e748c5671"
