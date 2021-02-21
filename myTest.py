
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V2 Demo")

    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    logging.info("init and Clear")
    #epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    font24 = ImageFont.truetype('Piboto-Regular.ttf', 24)
    ip_img = Image.new('1', (epd.height, epd.width), 255)
    ip_draw = ImageDraw.Draw(ip_img)
    
    epd.init (epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(ip_img))

    epd.init(epd.PART_UPDATE)
    #addrs = netifaces.ifaddresses('wlan0')
    ip_draw.text((0,0), ni.ifaddresses('wlan0')[AF_INET][0]['addr'], font = font24, fill = 0)
    #ip_draw.text((0,0), "192.168.86.117", font  = font15, fill = 0)
    epd.displayPartial(epd.getbuffer(ip_img)) 
    #    draw.text((0,0), 'Hi!', font = font15, fill = 0)
    #    epd.display(epd.getbuffer(image))
    #    time.sleep(2)
    # epd.Clear(0xFF)
    epd.sleep()
    time.sleep(10)
    epd.Dev_exit()
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
