# License
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# Pi0W_Display
Display system info like ip address, cpu usage, memory, and battery level on 2.13V2 e-paper display

## Setup
Install Piboto fonts
```markdown
$ apt-get update
$ sudo apt-get install fonts-piboto
```

Install the waveshare RaspberryPi python library

```markdown
$ git clone https://github.com/waveshare/e-Paper.git
$ cd ~/e-Paper/RaspberryPi_JetsonNano/python
$ python3 setup.py install_lib
```
