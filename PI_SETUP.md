# Raspbian Lite Setup

Test de Kano puis PiBooth. Lignes de commandes utilisées sur la même carte SD.

---

# Common Raspberry Config

## Boot config

```bash
sudo nano /boot/cmdline.txt
```

Ajouter à la fin de la ligne:

- quiet (Réduire les logs au démarrage)
- splash (Ca ne fait rien...)
- loglevel=0 (Ca ne fait rien...)
- logo.nologo (Supprimer le logo Raspberry en haut de l'écran)

quiet splash loglevel=0 logo.nologo

## Splashscreen

https://wiredzero.com/kiosk

```bash
sudo apt-get install lightdm
sudo apt-get install plymouth plymouth-themes
sudo apt-get install pix-plym-splash

sudo mv splash.png /usr/share/plymouth/themes/pix

sudo nano /boot/config.txt # disable_splash=1
```

```bash
sudo nano /usr/share/plymouth/themes/pix/pix.script
```

Supprimer les lignes suivantes à la fin: 

```
message_sprite = Sprite();
message_sprite.SetPosition(screen_width * 0.1, screen_height * 0.9, 10000);
my_image = Image.Text(text, 1, 1, 1);
message_sprite.SetImage(my_image);
```

```
sudo nano /boot/cmdline.txt # Replacer “console=tty1” par “console=tty3”
```
et ajouter à la fin de la ligne `splash quiet plymouth.ignore-serial-consoles logo.nologo vt.global_cursor_default=0`

---

# Kano 

## Python

### Check Python 3
Python 3 installé par défaut sur Raspbian Stretch Lite.

```bash
dpkg --get-selections | grep python3
```

### Pip 3

```bash
sudo apt-get install python3-pip -y
pip3 list
```

### Virtual env

```bash
sudo apt-get install virtualenv -y
```

#### Créer un environnement virtuel

```bash
cd folder_name
python3 -m venv ./venv
```

#### Activer un environnement virtuel

```bash
source ./venv/bin/activate
```

## Dépendances

```bash
cd folder_name
source ./venv/bin/activate

pip3 install docopt
pip3 install pgi # not 'gi' ! => import pgi in py code

sudo apt-get install libglib2.0-dev
sudo apt install libgirepository1.0-dev
sudo apt install libcairo2-dev

pip3 install PyGObject
sudo apt-get update
sudo apt-get install gir1.2-gtk-3.0
```

## Xinit

```bash
sudo apt-get install xserver-xorg-video-all xserver-xorg-input-all \
     xserver-xorg-core xinit x11-xserver-utils
     
sudo apt-get install xinit xserver-xorg xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable xinput
sudo apt-get install matchbox-window-manager
```

###Test

```bash
xinit
matchbox-window-manager & python3 ./shutdown/main.py
```
ou
```bash
xinit
matchbox-window-manager & python3 ./init_flow/bin/desktop-flow
```

## Démarrage automatique

Editer fichier .bash_profile pour démarrer sur le virtual env.
Editer fichier .xinitrc pour lancer l'app via la commande `xinit` ou `startx`.

---

# PiBooth

## Installation

```bash
git clone https://github.com/pibooth/pibooth.git 
cd pibooth
git checkout tags/2.0.1

cd ..
mkdir temp
cd temp
sudo wget raw.github.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh
sudo chmod 755 gphoto2-updater.sh
sudo ./gphoto2-updater.sh

sudo apt-get install cups libcups2-dev
sudo apt-get install python3-opencv

cd ../pibooth
# Je ne sais pas si c'est nécessaire d'avoir un venv
python3 -m pibooth ./venv
source ./venv/bin/activate

sudo pip3 install -e .[dslr,printer]

# Si pygame 2.0.1 (setup.py pygame >=1.9.6)
sudo apt-get install libsdl2-dev
sudo apt-get install libsdl2-ttf-2.0-0
sudo apt-get install libsdl2-mixer-2.0-0

# Si pygame 1.9.6 (setup.py pygame ==1.9.6)
sudo apt-get install libsdl1.2-dev
sudo apt-get install libsdl-ttf2.0-dev
sudo apt-get install libsdl-mixer1.2
```

```bash
pibooth
```

## Problèmes avec camera

Activer piCamera et I2C via `sudo raspi-config`.

```bash
vcgencmd get_camera
```

```bash
sudo nano /boot/config.txt # set gpu_mem=256
```

## CUPS

```bash
sudo nano /etc/cups/cupsd.conf # Voir https://www.howtogeek.com/169679/how-to-add-a-printer-to-your-raspberry-pi-or-other-linux-computer/
sudo /etc/init.d/cups restart
```
localhost:631

## PiBooth Config

```bash
sudo nano ~/.config/pibooth/pibooth.cfg
```


