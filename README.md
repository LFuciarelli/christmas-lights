[![](https://img.shields.io/github/license/LFuciarelli/christmas-lights)](https://github.com/LFuciarelli/christmas-lights/blob/master/LICENSE.md)
# Christmas lights
Christmas lights for Raspberry Pi :christmas_tree:.
## Table of contents
* [Technologies](#technologies)
* [Component list](#component-list)
* [Wiring diagram](#wiring-diagram)
* [Installing](#installing)
* [Support material](#support-material)
* [License](#license)
## Technologies
- Python3
- RPi.GPIO library
## Component list
- Raspberry Pi x1
- Breadboard x1
- GPIO extension board x1
- Jumper wire male to male x18
- LED x8 (red x2, blue x2, yellow x2 and green x2)
- 220Ω (ohms) resistor x8
- Push button x1 (small)
## Wiring diagram
![](christmaslights_bb.png)
## Installing
### Cloning the repository
You need to have git installed on your Raspberry Pi in order to clone this repository. If you are not sure whether you have git installed or not, open the command line and type `git --version`. 
If you already have git installed but a newer version is available, use the command `git clone https://github.com/git/git`' to update it.
But if you do not have git installed on your computer, type `sudo apt-get install git`.
To install the game, use the command `cd` and write the directory in which you want to save the repository. If you do not know where you want to save the repository, type `pwd` and check if the output is `/home/pi`. If it is, you do not need to change the directory; you can save the repository right there. To find the file later, you will only need to open the file manager.
To conclude, clone the repository using `git clone https://github.com/LFuciarelli/christmas-lights.git` and open the game using the commands `cd christmas-lights` and `python christmas_lights.py`.
### Downloading a ZIP file
If you do not know how to use the command line, you can download the project in ZIP format by clicking on the green button `Clone or download` on the top of the main page. After extracting the files, open christmas_lights.py in a text editor or in a Python IDE and run the code.
## Support material
[GPIO pinout guide for the Raspberry Pi](https://pinout.xyz/) (You can also open the terminal and run the command "pinout")

[RPi.GPIO library wiki](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
## License
This project is licensed under the MIT License - open the [LICENSE.md](https://github.com/LFuciarelli/christmas-lights/blob/master/LICENSE.md) file for more details
