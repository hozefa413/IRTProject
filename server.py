# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:28:53 2021

@author: Icon
"""
import pandas as pd 
import qrcode 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import logging
import sys 
import os 
import time 
import datetime
from pathlib import Path
import pyodbc
import math 
import qrcode
import numpy as np
from PIL import Image, ImageDraw, ImageFont,ImageOps
import textwrap
from datetime import datetime




        
qrFolder = 'Images/'
boxPixels = 20
imageExt = '.png'
linecount = 0
MyfontName = ImageFont.truetype(r'fonts\KhmerOScontent.ttf', 12)
MyfontCode = ImageFont.truetype(r'fonts\CALIBRIB.ttf', 14)
MyfontAddress = ImageFont.truetype(r'fonts\KhmerOScontent.ttf', 12)
w, h = 310, 420
shape = [(30, 70), (w - 30, h - 40)]
pos = (65,140)

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome'

@app.route('/Home',methods=['GET', 'POST'])
def Form():
    
    if request.method == "POST":
               # getting input with name = fname in HTML form

    
        outlet = request.form.get("uid")
        name = request.form.get("uname")
        contact =request.form.get("contact")
        address =request.form.get("address")
        agentcode = request.form.get("aid")
        wrap_address = str(textwrap.fill(address,45))
        wrap_name = str(textwrap.fill(name,35))
        data = outlet

        qrFilename = qrFolder + agentcode + "_" + outlet

        try:
            def CreateQR(qrFilename):
                
        
                
            #Check if already exist
                if os.path.exists(str(qrFilename) + imageExt):
                    print('QR code ' + qrFilename + ' already exist, renaming to ' + qrFilename + ' - copy')
                    print(' ')
                    logging.warning('QR Code already exists, making a copy')
                    qrFilename =qrFilename + '-copy'

            # creating new Image object 
                img = Image.new("RGB", (w, h), (93,255,166,2)) 


# create rectangle image 
                img1 = ImageDraw.Draw(img)   
                img1.rectangle(shape, fill ="#ffffff", outline ="white") 
                           
#QR Code
                qr = qrcode.QRCode(box_size=6)
                qr.add_data(outlet)
                qr.make()
                img_qr = qr.make_image()


#Add Outlet Information in QR Code
                img.paste(img_qr, pos)
                draw = ImageDraw.Draw(img)
                draw.text((85,80),wrap_name,font = MyfontName,fill=(0,0,0),align="center")
                draw.text((115,130),outlet,font = MyfontCode,fill=(0,0,0),align="center")
                draw.multiline_text((40,310),wrap_address,font = MyfontAddress,fill=(0,0,0),align="center")
                draw.text((120,390),agentcode,font = MyfontCode,fill=(0,0,0),align="center")
                img = ImageOps.expand(img,border=4,fill=(5,46,62))


#Add Logo
                logo = Image.open('Content\JTI Logo - Copy.png')
                logo = logo.resize((70, 50))
                logo_w, logo_h = logo.size
                img.paste(logo, (125, 5))
                print("Image Created Successfully")
                print("Printing Image")
                img.save(qrFilename + imageExt)
                print("Image saved Successfully")

        
        
            CreateQR(qrFilename)
    

        except:
            logging.exception("Error in code")


        return "Your Outlet QR Image Create Successfulle File Name: " + qrFilename+imageExt
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
