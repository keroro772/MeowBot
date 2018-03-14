from __future__ import unicode_literals

from django.db import models

class RandomDrops(models.Model):
    Painted = 'P'
    Normal = 'N'
    Certified = 'C'
    PaintedCert = 'B'
    special = (
        (Painted, 'Painted'),
        (Normal, 'Normal'),
        (Certified, 'Certified'),
        (PaintedCert, 'Painted/Certified')
        )
    
    Body = 'BD'
    Wheel = 'WH'
    Boost = 'BO'
    Antenna = 'AN'
    Decal = 'DE'
    Topper = 'TO'
    type = (
        (Body, 'Body'),
        (Wheel, 'Wheel'),
        (Boost, 'Boost' ),
        (Antenna, 'Antenna'),
        (Decal, 'Decal'),
        (Topper, 'Topper')
        )
    
    Standard = 'ST'
    Black = 'BL'
    BurntSienna = 'BS'
    Cobalt = 'CO'
    Crimson = 'CR'
    ForestGreen = 'FG'
    Grey = 'GR'
    Lime = 'LI'
    Orange = 'OR'
    Pink = 'PI'
    Purple = 'PU'
    Saffron = 'SA'
    SkyBlue = 'SB'
    TitaniumWhite = 'TW'
    ItemColour = (
        (Standard, 'Standard'),
        (Black, 'Black'),
        (BurntSienna, 'Burnt Sienna'),
        (Cobalt, 'Cobalt'),
        (Crimson, 'Crimson'),
        (ForestGreen, 'Forest Green'),
        (Grey, 'Grey'),
        (Lime, 'Lime'),
        (Orange, 'Orange'),
        (Pink, 'Pink'),
        (Purple, 'Purple'),
        (Saffron, 'Saffron'),
        (SkyBlue, 'SkyBlue'),
        (TitaniumWhite, 'Titanium White')
        )
    
    Notcert = 'NO'
    Acrobat = 'AC'
    Aviator = 'Av'
    Goalkeeper = 'GK' 
    Guardian = 'GU'
    Juggler = 'JU'
    Paragon = 'PA'
    Playmaker = 'PL'
    Scorer = 'SC'
    ShowOff = 'SO' 
    Sniper = 'SN'
    Striker = 'ST'
    Sweeper =  'SW'
    Tactician = 'TA' 
    Turtle = 'TU'
    Victor = 'VI'
    ItemCert = (
        (Notcert, 'Notcert'),
        (Acrobat,'Acrobat' ),
        (Aviator, 'Aviator'),
        (Goalkeeper, 'Goalkeeper'),
        (Guardian, 'Guardian'),
        (Juggler, 'Juggler'),
        (Playmaker, 'Playmaker'),
        (Scorer, 'Scorer'),
        (ShowOff, 'ShowOff'),
        (Sniper, 'Sniper'),
        (Striker, 'Striker'),
        (Sweeper, 'Sweeper'),
        (Tactician, 'Tactician'),
        (Turtle, 'Turtle'),
        (Victor, 'Victor'),
        )
    Picture = models.CharField(max_length=1000)
    Name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=type, default=Body)
    type_special = models.CharField(max_length=1, choices=special, default=Normal)
    colour = models.CharField(max_length=2, choices=ItemColour, default=Standard)
    CertType = models.CharField(max_length=2, choices=ItemCert, default=Notcert)
    price = models.IntegerField()