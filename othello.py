#####################################
# OTHELLO GAME V1.0 by Edan_Zoung
#####################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3
#import multitimer

import time
import datetime

class OTHELLO(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1000
      self.height=1000
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('OTHELLO GAME')
      self.setStyleSheet("""
                        QMainWindow{ background-color:#000;color:#fff;
                             background-image: url("images/back.jpg");
                             background-repeat: no-repeat;
                             background-position: center;}
                          QMessageBox{ background-color:#fff}
                         """)
      #self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)

      self.value1=0
      self.value2=0
      self.value3=0
      self.value4=0
      self.value5=0
      self.value6=0
      self.value7=0
      self.value8=0
      self.value9=0
      self.value10=0
      self.value11=0
      self.value12=0
      self.value13=0
      self.value14=0
      self.value15=0
      self.value16=0
      self.value17=0
      self.value18=0
      self.value19=0
      self.value20=0
      self.value21=0
      self.value22=0
      self.value23=0
      self.value24=0
      self.value25=0
      self.value26=0
      self.value27=0
      self.value28=0
      self.value29=0
      self.value30=0
      self.value31=0
      self.value32=0
      self.value33=0
      self.value34=0
      self.value35=0
      self.value36=0
      self.value37=0
      self.value38=0
      self.value39=0
      self.value40=0
      self.value41=0
      self.value42=0
      self.value43=0
      self.value44=0
      self.value45=0
      self.value46=0
      self.value47=0
      self.value48=0
      self.value49=0
      self.value50=0
      self.value51=0
      self.value52=0
      self.value53=0
      self.value54=0
      self.value55=0
      self.value56=0
      self.value57=0
      self.value58=0
      self.value59=0
      self.value60=0
      self.value61=0
      self.value62=0
      self.value63=0
      self.value64=0

      self.board=[]

      self.tour=1

      self.pion1='images/pion1.svg'
      self.pion2='images/pion2.svg'

      self.p1_color = 1
      self.p2_color = 2
      self.empty_color = 0
      self.board_size=8
      
      self.x=3
      self.y=3
      self.icon_size=100
      self.color1="#31947e"
      self.color2="#31947e"
      self.select_color="#555"
      self.focus_color="#31947e"
      self.hover_color="#610dba"
      self.border_color="#fff"
      self.icon_size=80
      self.app_name="OTHELLO GAME"
      

      self.button_case={}
      self.Zone_game()
      self.Design()
      self.showMaximized()
      self.database()
      self.refresh_data()
      
   def Zone_game(self):
      #================================================================================================#
      #================================================================================================#
      #========================================== ZONE GAME ===========================================#
      #================================================================================================#

      #_______TITLE GAME
      self.lab_title=QLabel(self)
      self.lab_title.setStyleSheet("""background-color:transparent;color:#fff;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_title.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_title.resize(500,100)
      self.pixmap = QPixmap('images/title2.svg').scaled(500,300)
      self.lab_title.setPixmap(self.pixmap)
      self.lab_title.move(250,5)

      #_______FRAME TOUR
      self.frame_tour=QLabel(self)
      self.frame_tour.setCursor(QCursor(Qt.PointingHandCursor))
      self.frame_tour.resize(280,250)
      

      #_________________________________________RESET GAME

      self.btn_reset=QPushButton('RESET GAME',self)
      self.btn_reset.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::hover{border-style:solid;border-width:1px;border-color:#6600ff;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_reset.clicked.connect(self.reset)
      self.btn_reset.move(1000,100)
      self.btn_reset.resize(200,50)


      #_______JOUEUR 1
      self.lab_pion1=QLabel(self)
      self.lab_pion1.setStyleSheet("""background-color:transparent;color:#fff;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_pion1.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_pion1.resize(100,100)
      self.pixmap1 = QPixmap('images/pion2.svg').scaled(100,70)
      self.lab_pion1.setPixmap(self.pixmap1)
      self.lab_pion1.move(950,200)

      #_______JOUEUR 1
      self.lab_joueur1=QLabel("JOUEUR 1",self)
      self.lab_joueur1.setStyleSheet("""background-color:transparent;color:#7700ff;font-style:italic; font-size:20pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_joueur1.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_joueur1.resize(500,100)
      self.lab_joueur1.move(1050,200)

      #_______JOUEUR 1
      self.lab_score1=QLabel("64",self)
      self.lab_score1.setStyleSheet("""background-color:transparent;color:#7700ff;font-style:italic; font-size:80pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_score1.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_score1.resize(500,100)
      self.lab_score1.move(1030,300)

      #_______JOUEUR 2
      self.lab_pion2=QLabel(self)
      self.lab_pion2.setStyleSheet("""background-color:transparent;color:#fff;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_pion2.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_pion2.resize(100,100)
      self.pixmap2 = QPixmap('images/pion1.svg').scaled(100,70)
      self.lab_pion2.setPixmap(self.pixmap2)
      self.lab_pion2.move(950,500)

      #_______JOUEUR 2
      self.lab_joueur2=QLabel("JOUEUR 2",self)
      self.lab_joueur2.setStyleSheet("""background-color:transparent;color:#ff0000;font-style:italic; font-size:20pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_joueur2.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_joueur2.resize(500,100)
      self.lab_joueur2.move(1050,500)

      #_______JOUEUR 2
      self.lab_score2=QLabel("64",self)
      self.lab_score2.setStyleSheet("""background-color:transparent;color:#ff0000;font-style:italic; font-size:80pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_score2.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_score2.resize(500,100)
      self.lab_score2.move(1030,600)

      #______FRAME ZONE
      self.zone_frame=QFrame(self)
      self.zone_frame.setStyleSheet(""" background-color:#000;font-family:Time; font-style:italic; font-size:8pt;
                                font-weight:bold; border-color:#fff; border-style:solid; border-width:3px;
                                border-top-left-radius:0px; border-radius:10px """)

      self.zone_frame.move(100,100)
      self.zone_frame.resize(806,806)

      
      for i in range(8):
         for j in range(8):
            self.button_case[(i,j)]=QToolButton(self.zone_frame)
            self.button_case[(i,j)].setStyleSheet("""
                                  QToolButton::pressed{background-color :#03fcb1;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::focus{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:"""+self.border_color+""";font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  
                                """)
            #self.button_case[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            self.button_case[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
            self.button_case[(i,j)].resize(100,100)
            #self.button_case[(i,j)].setFocus(False)

      self.button_case[(0,0)].move(self.x,self.y)
      self.button_case[(0,1)].move(self.x+100,self.y)
      self.button_case[(0,2)].move(self.x+200,self.y)
      self.button_case[(0,3)].move(self.x+300,self.y)
      self.button_case[(0,4)].move(self.x+400,self.y)
      self.button_case[(0,5)].move(self.x+500,self.y)
      self.button_case[(0,6)].move(self.x+600,self.y)
      self.button_case[(0,7)].move(self.x+700,self.y)

      
      self.button_case[(1,0)].move(self.x,self.y+100)
      self.button_case[(1,1)].move(self.x+100,self.y+100)
      self.button_case[(1,2)].move(self.x+200,self.y+100)
      self.button_case[(1,3)].move(self.x+300,self.y+100)
      self.button_case[(1,4)].move(self.x+400,self.y+100)
      self.button_case[(1,5)].move(self.x+500,self.y+100)
      self.button_case[(1,6)].move(self.x+600,self.y+100)
      self.button_case[(1,7)].move(self.x+700,self.y+100)

      
      self.button_case[(2,0)].move(self.x,self.y+200)
      self.button_case[(2,1)].move(self.x+100,self.y+200)
      self.button_case[(2,2)].move(self.x+200,self.y+200)
      self.button_case[(2,3)].move(self.x+300,self.y+200)
      self.button_case[(2,4)].move(self.x+400,self.y+200)
      self.button_case[(2,5)].move(self.x+500,self.y+200)
      self.button_case[(2,6)].move(self.x+600,self.y+200)
      self.button_case[(2,7)].move(self.x+700,self.y+200)

      
      self.button_case[(3,0)].move(self.x,self.y+300)
      self.button_case[(3,1)].move(self.x+100,self.y+300)
      self.button_case[(3,2)].move(self.x+200,self.y+300)
      self.button_case[(3,3)].move(self.x+300,self.y+300)
      self.button_case[(3,4)].move(self.x+400,self.y+300)
      self.button_case[(3,5)].move(self.x+500,self.y+300)
      self.button_case[(3,6)].move(self.x+600,self.y+300)
      self.button_case[(3,7)].move(self.x+700,self.y+300)

      self.button_case[(4,0)].move(self.x,self.y+400)
      self.button_case[(4,1)].move(self.x+100,self.y+400)
      self.button_case[(4,2)].move(self.x+200,self.y+400)
      self.button_case[(4,3)].move(self.x+300,self.y+400)
      self.button_case[(4,4)].move(self.x+400,self.y+400)
      self.button_case[(4,5)].move(self.x+500,self.y+400)
      self.button_case[(4,6)].move(self.x+600,self.y+400)
      self.button_case[(4,7)].move(self.x+700,self.y+400)

      
      self.button_case[(5,0)].move(self.x,self.y+500)
      self.button_case[(5,1)].move(self.x+100,self.y+500)
      self.button_case[(5,2)].move(self.x+200,self.y+500)
      self.button_case[(5,3)].move(self.x+300,self.y+500)
      self.button_case[(5,4)].move(self.x+400,self.y+500)
      self.button_case[(5,5)].move(self.x+500,self.y+500)
      self.button_case[(5,6)].move(self.x+600,self.y+500)
      self.button_case[(5,7)].move(self.x+700,self.y+500)

      
      self.button_case[(6,0)].move(self.x,self.y+600)
      self.button_case[(6,1)].move(self.x+100,self.y+600)
      self.button_case[(6,2)].move(self.x+200,self.y+600)
      self.button_case[(6,3)].move(self.x+300,self.y+600)
      self.button_case[(6,4)].move(self.x+400,self.y+600)
      self.button_case[(6,5)].move(self.x+500,self.y+600)
      self.button_case[(6,6)].move(self.x+600,self.y+600)
      self.button_case[(6,7)].move(self.x+700,self.y+600)

      
      self.button_case[(7,0)].move(self.x,self.y+700)
      self.button_case[(7,1)].move(self.x+100,self.y+700)
      self.button_case[(7,2)].move(self.x+200,self.y+700)
      self.button_case[(7,3)].move(self.x+300,self.y+700)
      self.button_case[(7,4)].move(self.x+400,self.y+700)
      self.button_case[(7,5)].move(self.x+500,self.y+700)
      self.button_case[(7,6)].move(self.x+600,self.y+700)
      self.button_case[(7,7)].move(self.x+700,self.y+700)
      #================================================================================================#
      #================================================================================================#
      #========================================== ZONE GAME ===========================================#
      #================================================================================================#

      self.button_case[(0,0)].clicked.connect(self.case1)
      self.button_case[(0,1)].clicked.connect(self.case2)
      self.button_case[(0,2)].clicked.connect(self.case3)
      self.button_case[(0,3)].clicked.connect(self.case4)
      self.button_case[(0,4)].clicked.connect(self.case5)
      self.button_case[(0,5)].clicked.connect(self.case6)
      self.button_case[(0,6)].clicked.connect(self.case7)
      self.button_case[(0,7)].clicked.connect(self.case8)
      
      self.button_case[(1,0)].clicked.connect(self.case9)
      self.button_case[(1,1)].clicked.connect(self.case10)
      self.button_case[(1,2)].clicked.connect(self.case11)
      self.button_case[(1,3)].clicked.connect(self.case12)
      self.button_case[(1,4)].clicked.connect(self.case13)
      self.button_case[(1,5)].clicked.connect(self.case14)
      self.button_case[(1,6)].clicked.connect(self.case15)
      self.button_case[(1,7)].clicked.connect(self.case16)

      self.button_case[(2,0)].clicked.connect(self.case17)
      self.button_case[(2,1)].clicked.connect(self.case18)
      self.button_case[(2,2)].clicked.connect(self.case19)
      self.button_case[(2,3)].clicked.connect(self.case20)
      self.button_case[(2,4)].clicked.connect(self.case21)
      self.button_case[(2,5)].clicked.connect(self.case22)
      self.button_case[(2,6)].clicked.connect(self.case23)
      self.button_case[(2,7)].clicked.connect(self.case24)
      
      self.button_case[(3,0)].clicked.connect(self.case25)
      self.button_case[(3,1)].clicked.connect(self.case26)
      self.button_case[(3,2)].clicked.connect(self.case27)
      self.button_case[(3,3)].clicked.connect(self.case28)
      self.button_case[(3,4)].clicked.connect(self.case29)
      self.button_case[(3,5)].clicked.connect(self.case30)
      self.button_case[(3,6)].clicked.connect(self.case31)
      self.button_case[(3,7)].clicked.connect(self.case32)

      self.button_case[(4,0)].clicked.connect(self.case33)
      self.button_case[(4,1)].clicked.connect(self.case34)
      self.button_case[(4,2)].clicked.connect(self.case35)
      self.button_case[(4,3)].clicked.connect(self.case36)
      self.button_case[(4,4)].clicked.connect(self.case37)
      self.button_case[(4,5)].clicked.connect(self.case38)
      self.button_case[(4,6)].clicked.connect(self.case39)
      self.button_case[(4,7)].clicked.connect(self.case40)
      
      self.button_case[(5,0)].clicked.connect(self.case41)
      self.button_case[(5,1)].clicked.connect(self.case42)
      self.button_case[(5,2)].clicked.connect(self.case43)
      self.button_case[(5,3)].clicked.connect(self.case44)
      self.button_case[(5,4)].clicked.connect(self.case45)
      self.button_case[(5,5)].clicked.connect(self.case46)
      self.button_case[(5,6)].clicked.connect(self.case47)
      self.button_case[(5,7)].clicked.connect(self.case48)

      self.button_case[(6,0)].clicked.connect(self.case49)
      self.button_case[(6,1)].clicked.connect(self.case50)
      self.button_case[(6,2)].clicked.connect(self.case51)
      self.button_case[(6,3)].clicked.connect(self.case52)
      self.button_case[(6,4)].clicked.connect(self.case53)
      self.button_case[(6,5)].clicked.connect(self.case54)
      self.button_case[(6,6)].clicked.connect(self.case55)
      self.button_case[(6,7)].clicked.connect(self.case56)
      
      self.button_case[(7,0)].clicked.connect(self.case57)
      self.button_case[(7,1)].clicked.connect(self.case58)
      self.button_case[(7,2)].clicked.connect(self.case59)
      self.button_case[(7,3)].clicked.connect(self.case60)
      self.button_case[(7,4)].clicked.connect(self.case61)
      self.button_case[(7,5)].clicked.connect(self.case62)
      self.button_case[(7,6)].clicked.connect(self.case63)
      self.button_case[(7,7)].clicked.connect(self.case64)

   def Design(self):
      self.button_case[(0,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      

      self.button_case[(1,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(2,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(3,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      

      self.button_case[(4,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(5,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      

      self.button_case[(6,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(7,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")


   def database(self):
      
      record_game=[ (1,0,""), (2,0,""), (3,0,""), (4,0,""), (5,0,""), (6,0,""), (7,0,""), (8,0,""),
                    (9,0,""), (10,0,""), (11,0,""), (12,0,""), (13,0,""), (14,0,""), (15,0,""), (16,0,""),
                    (17,0,""), (18,0,""), (19,0,""), (20,0,""), (21,0,""), (22,0,""), (23,0,""), (24,0,""),
                    (25,0,""), (26,0,""), (27,0,""), (28,1,'images/pion1.svg'), (29,2,'images/pion2.svg'), (30,0,""), (31,0,""), (32,0,""),
                    (33,0,""), (34,0,""), (35,0,""), (36,2,'images/pion2.svg'), (37,1,'images/pion1.svg'), (38,0,""), (39,0,""), (40,0,""),
                    (41,0,""), (42,0,""), (43,0,""), (44,0,""), (45,0,""), (46,0,""), (47,0,""), (48,0,""),
                    (49,0,""), (50,0,""), (51,0,""), (52,0,""), (53,0,""), (54,0,""), (55,0,""), (56,0,""),
                    (57,0,""), (58,0,""), (59,0,""), (60,0,""), (61,0,""), (62,0,""), (63,0,""), (64,0,"") ]
      
      if not os.path.exists('othello.bd') and not os.path.isfile('othello.bd'):
         self.question=QMessageBox.question(self,"OTHELLO GAME",'BASE DE DONNEE OTHELLO NON TROUVE\nVOULEZ-VOUS EN CREER ?',QMessageBox.Yes,QMessageBox.No)
         if self.question==QMessageBox.Yes:
            try:
               self.bdd=sqlite3.connect('othello.bd')
            except sqlite3.Error as e:
               QMessageBox.information(self,"OTHELLO GAME",e,QMessageBox.Ok)
            finally:
               if self.bdd:
                  
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS game (
                                      id integer primary key,
                                      value integer,
                                      image text)""")       

                  
                  self.cursor.executemany("""INSERT INTO game (id,value,image)
                                         VALUES (?,?,?)""",record_game)
                  
                  self.bdd.commit()
                  self.bdd.close()
                  QMessageBox.information(self,"OTHELLO GAME",'BASE DE DONNEE CREEE AVEC SUCCES',QMessageBox.Ok)

               else:
                  self.bdd.rollback()
                  QMessageBox.information(self,"OTHELLO GAME","BASE DE DONNEE NON CREEE \nUNE ERREUR S'EST PRODUITE ",QMessageBox.Ok)
         else:
            QMessageBox.information(self,"OTHELLO GAME","SANS BASE DE DONNEE LE PROGRAMME\nNE FONCTIONNERA PAS CORRECTEMENT ",QMessageBox.Ok)
      else:
         pass

   def case1(self):
      if self.button_case[(0,0)]:
         self.button_case[(0,0)].setFocus()
         self.id_case=1
         self.game_rule()
   def case2(self):
      if self.button_case[(0,1)]:
         self.button_case[(0,1)].setFocus()
         self.id_case=2
         self.game_rule()
   def case3(self):
      if self.button_case[(0,2)]:
         self.button_case[(0,2)].setFocus()
         self.id_case=3
         self.game_rule()
   def case4(self):
      if self.button_case[(0,3)]:
         self.button_case[(0,3)].setFocus()
         self.id_case=4
         self.game_rule()
   def case5(self):
      if self.button_case[(0,4)]:
         self.button_case[(0,4)].setFocus()
         self.id_case=5
         self.game_rule()
   def case6(self):
      if self.button_case[(0,5)]:
         self.button_case[(0,5)].setFocus()
         self.id_case=6
         self.game_rule()
   def case7(self):
      if self.button_case[(0,6)]:
         self.button_case[(0,6)].setFocus()
         self.id_case=7
         self.game_rule()
   def case8(self):
      if self.button_case[(0,7)]:
         self.button_case[(0,7)].setFocus()
         self.id_case=8
         self.game_rule()
   def case9(self):
      if self.button_case[(1,0)]:
         self.button_case[(1,0)].setFocus()
         self.id_case=9
         self.game_rule()
   def case10(self):
      if self.button_case[(1,1)]:
         self.button_case[(1,1)].setFocus()
         self.id_case=10
         self.game_rule()
   def case11(self):
      if self.button_case[(1,2)]:
         self.button_case[(1,2)].setFocus()
         self.id_case=11
         self.game_rule()
   def case12(self):
      if self.button_case[(1,3)]:
         self.button_case[(1,3)].setFocus()
         self.id_case=12
         self.game_rule()
   def case13(self):
      if self.button_case[(1,4)]:
         self.button_case[(1,4)].setFocus()
         self.id_case=13
         self.game_rule()
   def case14(self):
      if self.button_case[(1,5)]:
         self.button_case[(1,5)].setFocus()
         self.id_case=14
         self.game_rule()
   def case15(self):
      if self.button_case[(1,6)]:
         self.button_case[(1,6)].setFocus()
         self.id_case=15
         self.game_rule()
   def case16(self):
      if self.button_case[(1,7)]:
         self.button_case[(1,7)].setFocus()
         self.id_case=16
         self.game_rule()
   def case17(self):
      if self.button_case[(2,0)]:
         self.button_case[(2,0)].setFocus()
         self.id_case=17
         self.game_rule()
   def case18(self):
      if self.button_case[(2,1)]:
         self.button_case[(2,1)].setFocus()
         self.id_case=18
         self.game_rule()
   def case19(self):
      if self.button_case[(2,2)]:
         self.button_case[(2,2)].setFocus()
         self.id_case=19
         self.game_rule()
   def case20(self):
      if self.button_case[(2,3)]:
         self.button_case[(2,3)].setFocus()
         self.id_case=20
         self.game_rule()
   def case21(self):
      if self.button_case[(2,4)]:
         self.button_case[(2,4)].setFocus()
         self.id_case=21
         self.game_rule()
   def case22(self):
      if self.button_case[(2,5)]:
         self.button_case[(2,5)].setFocus()
         self.id_case=22
         self.game_rule()
   def case23(self):
      if self.button_case[(2,6)]:
         self.button_case[(2,6)].setFocus()
         self.id_case=23
         self.game_rule()
   def case24(self):
      if self.button_case[(2,7)]:
         self.button_case[(2,7)].setFocus()
         self.id_case=24
         self.game_rule()
   def case25(self):
      if self.button_case[(3,0)]:
         self.button_case[(3,0)].setFocus()
         self.id_case=25
         self.game_rule()
   def case26(self):
      if self.button_case[(3,1)]:
         self.button_case[(3,1)].setFocus()
         self.id_case=26
         self.game_rule()
   def case27(self):
      if self.button_case[(3,2)]:
         self.button_case[(3,2)].setFocus()
         self.id_case=27
         self.game_rule()
   def case28(self):
      if self.button_case[(3,3)]:
         self.button_case[(3,3)].setFocus()
         self.id_case=28
         self.game_rule()
   def case29(self):
      if self.button_case[(3,4)]:
         self.button_case[(3,4)].setFocus()
         self.id_case=29
         self.game_rule()
   def case30(self):
      if self.button_case[(3,5)]:
         self.button_case[(3,5)].setFocus()
         self.id_case=30
         self.game_rule()
   def case31(self):
      if self.button_case[(3,6)]:
         self.button_case[(3,6)].setFocus()
         self.id_case=31
         self.game_rule()
   def case32(self):
      if self.button_case[(3,7)]:
         self.button_case[(3,7)].setFocus()
         self.id_case=32
         self.game_rule()
   def case33(self):
      if self.button_case[(4,0)]:
         self.button_case[(4,0)].setFocus()
         self.id_case=33
         self.game_rule()
   def case34(self):
      if self.button_case[(4,1)]:
         self.button_case[(4,1)].setFocus()
         self.id_case=34
         self.game_rule()
   def case35(self):
      if self.button_case[(4,2)]:
         self.button_case[(4,2)].setFocus()
         self.id_case=35
         self.game_rule()
   def case36(self):
      if self.button_case[(4,3)]:
         self.button_case[(4,3)].setFocus()
         self.id_case=36
         self.game_rule()
   def case37(self):
      if self.button_case[(4,4)]:
         self.button_case[(4,4)].setFocus()
         self.id_case=37
         self.game_rule()
   def case38(self):
      if self.button_case[(4,5)]:
         self.button_case[(4,5)].setFocus()
         self.id_case=38
         self.game_rule()
   def case39(self):
      if self.button_case[(4,6)]:
         self.button_case[(4,6)].setFocus()
         self.id_case=39
         self.game_rule()
   def case40(self):
      if self.button_case[(4,7)]:
         self.button_case[(4,7)].setFocus()
         self.id_case=40
         self.game_rule()
   def case41(self):
      if self.button_case[(5,0)]:
         self.button_case[(5,0)].setFocus()
         self.id_case=41
         self.game_rule()
   def case42(self):
      if self.button_case[(5,1)]:
         self.button_case[(5,1)].setFocus()
         self.id_case=42
         self.game_rule()
   def case43(self):
      if self.button_case[(5,2)]:
         self.button_case[(5,2)].setFocus()
         self.id_case=43
         self.game_rule()
   def case44(self):
      if self.button_case[(5,3)]:
         self.button_case[(5,3)].setFocus()
         self.id_case=44
         self.game_rule()
   def case45(self):
      if self.button_case[(5,4)]:
         self.button_case[(5,4)].setFocus()
         self.id_case=45
         self.game_rule()
   def case46(self):
      if self.button_case[(5,5)]:
         self.button_case[(5,5)].setFocus()
         self.id_case=46
         self.game_rule()
   def case47(self):
      if self.button_case[(5,6)]:
         self.button_case[(5,6)].setFocus()
         self.id_case=47
         self.game_rule()
   def case48(self):
      if self.button_case[(5,7)]:
         self.button_case[(5,7)].setFocus()
         self.id_case=48
         self.game_rule()
   def case49(self):
      if self.button_case[(6,0)]:
         self.button_case[(6,0)].setFocus()
         self.id_case=49
         self.game_rule()
   def case50(self):
      if self.button_case[(6,1)]:
         self.button_case[(6,1)].setFocus()
         self.id_case=50
         self.game_rule()
   def case51(self):
      if self.button_case[(6,2)]:
         self.button_case[(6,2)].setFocus()
         self.id_case=51
         self.game_rule()
   def case52(self):
      if self.button_case[(6,3)]:
         self.button_case[(6,3)].setFocus()
         self.id_case=52
         self.game_rule()
   def case53(self):
      if self.button_case[(6,4)]:
         self.button_case[(6,4)].setFocus()
         self.id_case=53
         self.game_rule()
   def case54(self):
      if self.button_case[(6,5)]:
         self.button_case[(6,5)].setFocus()
         self.id_case=54
         self.game_rule()
   def case55(self):
      if self.button_case[(6,6)]:
         self.button_case[(6,6)].setFocus()
         self.id_case=55
         self.game_rule()
   def case56(self):
      if self.button_case[(6,7)]:
         self.button_case[(6,7)].setFocus()
         self.id_case=56
         self.game_rule()
   def case57(self):
      if self.button_case[(7,0)]:
         self.button_case[(7,0)].setFocus()
         self.id_case=57
         self.game_rule()
   def case58(self):
      if self.button_case[(7,1)]:
         self.button_case[(7,1)].setFocus()
         self.id_case=58
         self.game_rule()
   def case59(self):
      if self.button_case[(7,2)]:
         self.button_case[(7,2)].setFocus()
         self.id_case=59
         self.game_rule()
   def case60(self):
      if self.button_case[(7,3)]:
         self.button_case[(7,3)].setFocus()
         self.id_case=60
         self.game_rule()
   def case61(self):
      if self.button_case[(7,4)]:
         self.button_case[(7,4)].setFocus()
         self.id_case=61
         self.game_rule()
   def case62(self):
      if self.button_case[(7,5)]:
         self.button_case[(7,5)].setFocus()
         self.id_case=62
         self.game_rule()
   def case63(self):
      if self.button_case[(7,6)]:
         self.button_case[(7,6)].setFocus()
         self.id_case=63
         self.game_rule()
   def case64(self):
      if self.button_case[(7,7)]:
         self.button_case[(7,7)].setFocus()
         self.id_case=64
         self.game_rule()

   def game_rule(self):
      if os.path.exists('othello.bd') and os.path.isfile('othello.bd'):
         try:
            self.bdd=sqlite3.connect('othello.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,"OTHELLO GAME",e)
         finally:
            try:
               self.cursor=self.bdd.cursor()
               self.refresh_data()
               
               if self.tour==1:
                  self.select=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case))   
                  for row in self.select:
                     if  row[0]==0:
                        #=======================================#
                        #================== UN =================#
                        #=======================================#
                        self.west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.west:
                           if  row[0]==2 :
                              self.west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.west2:
                                 if  row[0]==1 :
                                    if (self.id_case==8 or
                                        self.id_case==16 or
                                        self.id_case==24 or
                                        self.id_case==32 or
                                        self.id_case==40 or
                                        self.id_case==48 or
                                        self.id_case==56 or
                                        self.id_case==64 or

                                        self.id_case==7 or
                                        self.id_case==15 or
                                        self.id_case==23 or
                                        self.id_case==31 or
                                        self.id_case==39 or
                                        self.id_case==47 or
                                        self.id_case==55 or
                                        self.id_case==63 or

                                        self.id_case==6 or
                                        self.id_case==14 or
                                        self.id_case==22 or
                                        self.id_case==30 or
                                        self.id_case==38 or
                                        self.id_case==46 or
                                        self.id_case==54 or
                                        self.id_case==62 or

                                        self.id_case==5 or
                                        self.id_case==13 or
                                        self.id_case==21 or
                                        self.id_case==29 or
                                        self.id_case==37 or
                                        self.id_case==45 or
                                        self.id_case==53 or
                                        self.id_case==61 or

                                        self.id_case==4 or
                                        self.id_case==12 or
                                        self.id_case==20 or
                                        self.id_case==28 or
                                        self.id_case==36 or
                                        self.id_case==44 or
                                        self.id_case==52 or
                                        self.id_case==60 or

                                        self.id_case==3 or
                                        self.id_case==11 or
                                        self.id_case==19 or
                                        self.id_case==27 or
                                        self.id_case==35 or
                                        self.id_case==43 or
                                        self.id_case==51 or
                                        self.id_case==59):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-1))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.east:
                           if  row[0]==2 :
                              self.east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.east2:
                                 if  row[0]==1 :
                                    if (self.id_case==1 or
                                        self.id_case==9 or
                                        self.id_case==17 or
                                        self.id_case==25 or
                                        self.id_case==33 or
                                        self.id_case==41 or
                                        self.id_case==49 or
                                        self.id_case==57 or

                                        self.id_case==2 or
                                        self.id_case==10 or
                                        self.id_case==18 or
                                        self.id_case==26 or
                                        self.id_case==34 or
                                        self.id_case==42 or
                                        self.id_case==50 or
                                        self.id_case==58 or

                                        self.id_case==3 or
                                        self.id_case==11 or
                                        self.id_case==19 or
                                        self.id_case==27 or
                                        self.id_case==35 or
                                        self.id_case==43 or
                                        self.id_case==51 or
                                        self.id_case==59 or

                                        self.id_case==4 or
                                        self.id_case==12 or
                                        self.id_case==20 or
                                        self.id_case==28 or
                                        self.id_case==36 or
                                        self.id_case==44 or
                                        self.id_case==52 or
                                        self.id_case==60 or

                                        self.id_case==5 or
                                        self.id_case==13 or
                                        self.id_case==21 or
                                        self.id_case==29 or
                                        self.id_case==37 or
                                        self.id_case==45 or
                                        self.id_case==53 or
                                        self.id_case==61 or

                                        self.id_case==6 or
                                        self.id_case==14 or
                                        self.id_case==22 or
                                        self.id_case==30 or
                                        self.id_case==38 or
                                        self.id_case==46 or
                                        self.id_case==54 or
                                        self.id_case==62):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+1))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.north:
                           if  row[0]==2 :
                              self.north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.north2:
                                 if  row[0]==1 :
                                    if (self.id_case==57 or
                                        self.id_case==58 or
                                        self.id_case==59 or
                                        self.id_case==60 or
                                        self.id_case==61 or
                                        self.id_case==62 or
                                        self.id_case==63 or
                                        self.id_case==64 or

                                        self.id_case==49 or
                                        self.id_case==50 or
                                        self.id_case==51 or
                                        self.id_case==52 or
                                        self.id_case==53 or
                                        self.id_case==54 or
                                        self.id_case==55 or
                                        self.id_case==56 or

                                        self.id_case==41 or
                                        self.id_case==42 or
                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or
                                        self.id_case==47 or
                                        self.id_case==48 or

                                        self.id_case==33 or
                                        self.id_case==34 or
                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or
                                        self.id_case==39 or
                                        self.id_case==40 or

                                        self.id_case==25 or
                                        self.id_case==26 or
                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or
                                        self.id_case==31 or
                                        self.id_case==32 or

                                        self.id_case==17 or
                                        self.id_case==18 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==23 or
                                        self.id_case==24):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-8))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.south:
                           if  row[0]==2 :
                              self.south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.south2:
                                 if  row[0]==1 :
                                    if (self.id_case==1 or
                                        self.id_case==2 or
                                        self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or
                                        self.id_case==7 or
                                        self.id_case==8 or

                                        self.id_case==9 or
                                        self.id_case==10 or
                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or
                                        self.id_case==15 or
                                        self.id_case==16 or

                                        self.id_case==17 or
                                        self.id_case==18 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==23 or
                                        self.id_case==24 or

                                        self.id_case==25 or
                                        self.id_case==26 or
                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or
                                        self.id_case==31 or
                                        self.id_case==32 or

                                        self.id_case==33 or
                                        self.id_case==34 or
                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or
                                        self.id_case==39 or
                                        self.id_case==40 or

                                        self.id_case==41 or
                                        self.id_case==42 or
                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or
                                        self.id_case==47 or
                                        self.id_case==48):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+8))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.north_west:
                           if  row[0]==2 :
                              self.north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.north_west:
                                 if  row[0]==1 :
                                    if (self.id_case==59 or
                                        self.id_case==60 or
                                        self.id_case==61 or
                                        self.id_case==62 or
                                        self.id_case==63 or
                                        self.id_case==64 or
                                        self.id_case==56 or
                                        self.id_case==48 or
                                        self.id_case==40 or
                                        self.id_case==32 or
                                        self.id_case==24 or

                                        self.id_case==51 or
                                        self.id_case==52 or
                                        self.id_case==53 or
                                        self.id_case==54 or
                                        self.id_case==55 or
                                        self.id_case==47 or
                                        self.id_case==39 or
                                        self.id_case==31 or
                                        self.id_case==23 or

                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or
                                        self.id_case==38 or
                                        self.id_case==30 or
                                        self.id_case==22 or

                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==29 or
                                        self.id_case==21 or

                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==20 or

                                        self.id_case==19):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-9))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.north_east:
                           if  row[0]==2 :
                              self.north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.north_east2:
                                 if  row[0]==1 :
                                    if (self.id_case==41 or
                                        self.id_case==33 or
                                        self.id_case==25 or
                                        self.id_case==17 or
                                        self.id_case==9 or
                                        self.id_case==1 or
                                        self.id_case==2 or
                                        self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or

                                        self.id_case==42 or
                                        self.id_case==34 or
                                        self.id_case==26 or
                                        self.id_case==18 or
                                        self.id_case==10 or
                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or

                                        self.id_case==43 or
                                        self.id_case==35 or
                                        self.id_case==27 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or

                                        self.id_case==44 or
                                        self.id_case==36 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or

                                        self.id_case==45 or
                                        self.id_case==37 or
                                        self.id_case==38 or

                                        self.id_case==46):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+9))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.south_west:
                           if  row[0]==2 :
                              self.south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.south_west2:
                                 if  row[0]==1 :
                                    if (self.id_case==17 or
                                        self.id_case==25 or
                                        self.id_case==33 or
                                        self.id_case==41 or
                                        self.id_case==49 or
                                        self.id_case==57 or
                                        self.id_case==58 or
                                        self.id_case==59 or
                                        self.id_case==60 or
                                        self.id_case==61 or
                                        self.id_case==62 or

                                        self.id_case==18 or
                                        self.id_case==26 or
                                        self.id_case==34 or
                                        self.id_case==42 or
                                        self.id_case==50 or
                                        self.id_case==51 or
                                        self.id_case==52 or
                                        self.id_case==53 or
                                        self.id_case==54 or

                                        self.id_case==19 or
                                        self.id_case==27 or
                                        self.id_case==35 or
                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or

                                        self.id_case==20 or
                                        self.id_case==28 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or

                                        self.id_case==21 or
                                        self.id_case==29 or
                                        self.id_case==30 or

                                        self.id_case==22):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-7))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()
                        self.south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.south_east:
                           if  row[0]==2 :
                              self.south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.south_east2:
                                 if  row[0]==1 :
                                    if (self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or
                                        self.id_case==7 or
                                        self.id_case==8 or
                                        self.id_case==16 or
                                        self.id_case==24 or
                                        self.id_case==32 or
                                        self.id_case==40 or
                                        self.id_case==48 or

                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or
                                        self.id_case==15 or
                                        self.id_case==23 or
                                        self.id_case==31 or
                                        self.id_case==39 or
                                        self.id_case==47 or

                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==30 or
                                        self.id_case==38 or
                                        self.id_case==46 or

                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==37 or
                                        self.id_case==45 or

                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==44 or

                                        self.id_case==43):
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+7))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=0
                                       self.refresh_data()

                        #=========================================#
                        #================== DEUX =================#
                        #=========================================#
                        self.west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.west:
                           if  row[0]==2 :
                              self.west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.west2:
                                 if  row[0]==2 :
                                    self.west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.west3:
                                       if  row[0]==1 :
                                          if (self.id_case==8 or
                                              self.id_case==16 or
                                              self.id_case==24 or
                                              self.id_case==32 or
                                              self.id_case==40 or
                                              self.id_case==48 or
                                              self.id_case==56 or
                                              self.id_case==64 or

                                              self.id_case==7 or
                                              self.id_case==15 or
                                              self.id_case==23 or
                                              self.id_case==31 or
                                              self.id_case==39 or
                                              self.id_case==47 or
                                              self.id_case==55 or
                                              self.id_case==63 or

                                              self.id_case==6 or
                                              self.id_case==14 or
                                              self.id_case==22 or
                                              self.id_case==30 or
                                              self.id_case==38 or
                                              self.id_case==46 or
                                              self.id_case==54 or
                                              self.id_case==62 or

                                              self.id_case==5 or
                                              self.id_case==13 or
                                              self.id_case==21 or
                                              self.id_case==29 or
                                              self.id_case==37 or
                                              self.id_case==45 or
                                              self.id_case==53 or
                                              self.id_case==61 or

                                              self.id_case==4 or
                                              self.id_case==12 or
                                              self.id_case==20 or
                                              self.id_case==28 or
                                              self.id_case==36 or
                                              self.id_case==44 or
                                              self.id_case==52 or
                                              self.id_case==60):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-1))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.east:
                           if  row[0]==2 :
                              self.east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.east2:
                                 if  row[0]==2 :
                                    self.east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.east3:
                                       if  row[0]==1 :
                                          if (self.id_case==1 or
                                              self.id_case==9 or
                                              self.id_case==17 or
                                              self.id_case==25 or
                                              self.id_case==33 or
                                              self.id_case==41 or
                                              self.id_case==49 or
                                              self.id_case==57 or

                                              self.id_case==2 or
                                              self.id_case==10 or
                                              self.id_case==18 or
                                              self.id_case==26 or
                                              self.id_case==34 or
                                              self.id_case==42 or
                                              self.id_case==50 or
                                              self.id_case==58 or

                                              self.id_case==3 or
                                              self.id_case==11 or
                                              self.id_case==19 or
                                              self.id_case==27 or
                                              self.id_case==35 or
                                              self.id_case==43 or
                                              self.id_case==51 or
                                              self.id_case==59 or

                                              self.id_case==4 or
                                              self.id_case==12 or
                                              self.id_case==20 or
                                              self.id_case==28 or
                                              self.id_case==36 or
                                              self.id_case==44 or
                                              self.id_case==52 or
                                              self.id_case==60 or

                                              self.id_case==5 or
                                              self.id_case==13 or
                                              self.id_case==21 or
                                              self.id_case==29 or
                                              self.id_case==37 or
                                              self.id_case==45 or
                                              self.id_case==53 or
                                              self.id_case==61):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+1))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.north:
                           if  row[0]==2 :
                              self.north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.north2:
                                 if  row[0]==2 :
                                    self.north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.north3:
                                       if  row[0]==1 :
                                          if (self.id_case==57 or
                                              self.id_case==58 or
                                              self.id_case==59 or
                                              self.id_case==60 or
                                              self.id_case==61 or
                                              self.id_case==62 or
                                              self.id_case==63 or
                                              self.id_case==64 or

                                              self.id_case==49 or
                                              self.id_case==50 or
                                              self.id_case==51 or
                                              self.id_case==52 or
                                              self.id_case==53 or
                                              self.id_case==54 or
                                              self.id_case==55 or
                                              self.id_case==56 or

                                              self.id_case==41 or
                                              self.id_case==42 or
                                              self.id_case==43 or
                                              self.id_case==44 or
                                              self.id_case==45 or
                                              self.id_case==46 or
                                              self.id_case==47 or
                                              self.id_case==48 or

                                              self.id_case==33 or
                                              self.id_case==34 or
                                              self.id_case==35 or
                                              self.id_case==36 or
                                              self.id_case==37 or
                                              self.id_case==38 or
                                              self.id_case==39 or
                                              self.id_case==40 or

                                              self.id_case==25 or
                                              self.id_case==26 or
                                              self.id_case==27 or
                                              self.id_case==28 or
                                              self.id_case==29 or
                                              self.id_case==30 or
                                              self.id_case==31 or
                                              self.id_case==32):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-8))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.south:
                           if  row[0]==2 :
                              self.south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.south2:
                                 if  row[0]==2 :
                                    self.south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.south3:
                                       if  row[0]==1 :
                                          if (self.id_case==1 or
                                        self.id_case==2 or
                                        self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or
                                        self.id_case==7 or
                                        self.id_case==8 or

                                        self.id_case==9 or
                                        self.id_case==10 or
                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or
                                        self.id_case==15 or
                                        self.id_case==16 or

                                        self.id_case==17 or
                                        self.id_case==18 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==23 or
                                        self.id_case==24 or

                                        self.id_case==25 or
                                        self.id_case==26 or
                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or
                                        self.id_case==31 or
                                        self.id_case==32 or

                                        self.id_case==33 or
                                        self.id_case==34 or
                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or
                                        self.id_case==39 or
                                        self.id_case==40):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+8))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.north_west:
                           if  row[0]==2 :
                              self.north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.north_west2:
                                 if  row[0]==2 :
                                    self.north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.north_west3:
                                       if  row[0]==1 :
                                          if (self.id_case==60 or
                                              self.id_case==61 or
                                              self.id_case==62 or
                                              self.id_case==63 or
                                              self.id_case==64 or
                                              self.id_case==56 or
                                              self.id_case==48 or
                                              self.id_case==40 or
                                              self.id_case==32 or

                                              self.id_case==52 or
                                              self.id_case==53 or
                                              self.id_case==54 or
                                              self.id_case==55 or
                                              self.id_case==47 or
                                              self.id_case==39 or
                                              self.id_case==31 or

                                              self.id_case==44 or
                                              self.id_case==45 or
                                              self.id_case==46 or
                                              self.id_case==38 or
                                              self.id_case==30 or

                                              self.id_case==36 or
                                              self.id_case==37 or
                                              self.id_case==29 or

                                              self.id_case==28):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-9))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.north_east:
                           if  row[0]==2 :
                              self.north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.north_east2:
                                 if  row[0]==2 :
                                    self.north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.north_east3:
                                       if  row[0]==1 :
                                          if (self.id_case==33 or
                                              self.id_case==25 or
                                              self.id_case==17 or
                                              self.id_case==9 or
                                              self.id_case==1 or
                                              self.id_case==2 or
                                              self.id_case==3 or
                                              self.id_case==4 or
                                              self.id_case==5 or

                                              self.id_case==34 or
                                              self.id_case==26 or
                                              self.id_case==18 or
                                              self.id_case==10 or
                                              self.id_case==11 or
                                              self.id_case==12 or
                                              self.id_case==13 or

                                              self.id_case==35 or
                                              self.id_case==27 or
                                              self.id_case==19 or
                                              self.id_case==20 or
                                              self.id_case==21 or

                                              self.id_case==36 or
                                              self.id_case==28 or
                                              self.id_case==29 or

                                              self.id_case==37):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+9))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.south_west:
                           if  row[0]==2 :
                              self.south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.south_west:
                                 if  row[0]==2 :
                                    self.south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.south_west3:
                                       if  row[0]==1 :
                                          if (self.id_case==25 or
                                              self.id_case==33 or
                                              self.id_case==41 or
                                              self.id_case==49 or
                                              self.id_case==57 or
                                              self.id_case==58 or
                                              self.id_case==59 or
                                              self.id_case==60 or
                                              self.id_case==61 or

                                              self.id_case==26 or
                                              self.id_case==34 or
                                              self.id_case==42 or
                                              self.id_case==50 or
                                              self.id_case==51 or
                                              self.id_case==52 or
                                              self.id_case==53 or

                                              self.id_case==27 or
                                              self.id_case==35 or
                                              self.id_case==43 or
                                              self.id_case==44 or
                                              self.id_case==45 or

                                              self.id_case==28 or
                                              self.id_case==36 or
                                              self.id_case==37 or

                                              self.id_case==29):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-7))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()
                        self.south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.south_east:
                           if  row[0]==2 :
                              self.south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.south_east2:
                                 if  row[0]==2 :
                                    self.south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.south_east3:
                                       if  row[0]==1 :
                                          if (self.id_case==4 or
                                              self.id_case==5 or
                                              self.id_case==6 or
                                              self.id_case==7 or
                                              self.id_case==8 or
                                              self.id_case==16 or
                                              self.id_case==24 or
                                              self.id_case==32 or
                                              self.id_case==40 or

                                              self.id_case==12 or
                                              self.id_case==13 or
                                              self.id_case==14 or
                                              self.id_case==15 or
                                              self.id_case==23 or
                                              self.id_case==31 or
                                              self.id_case==39 or

                                              self.id_case==20 or
                                              self.id_case==21 or
                                              self.id_case==22 or
                                              self.id_case==30 or
                                              self.id_case==38 or

                                              self.id_case==28 or
                                              self.id_case==29 or
                                              self.id_case==37 or

                                              self.id_case==36):
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+7))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=0
                                             self.refresh_data()


                        #=========================================#
                        #================== TROIS ================#
                        #=========================================#
                        self.west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.west:
                           if  row[0]==2 :
                              self.west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.west2:
                                 if  row[0]==2 :
                                    self.west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.west3:
                                       if  row[0]==2 :
                                          self.west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.west4:
                                             if  row[0]==1 :
                                                if (self.id_case==8 or
                                                    self.id_case==16 or
                                                    self.id_case==24 or
                                                    self.id_case==32 or
                                                    self.id_case==40 or
                                                    self.id_case==48 or
                                                    self.id_case==56 or
                                                    self.id_case==64 or

                                                    self.id_case==7 or
                                                    self.id_case==15 or
                                                    self.id_case==23 or
                                                    self.id_case==31 or
                                                    self.id_case==39 or
                                                    self.id_case==47 or
                                                    self.id_case==55 or
                                                    self.id_case==63 or

                                                    self.id_case==6 or
                                                    self.id_case==14 or
                                                    self.id_case==22 or
                                                    self.id_case==30 or
                                                    self.id_case==38 or
                                                    self.id_case==46 or
                                                    self.id_case==54 or
                                                    self.id_case==62 or

                                                    self.id_case==5 or
                                                    self.id_case==13 or
                                                    self.id_case==21 or
                                                    self.id_case==29 or
                                                    self.id_case==37 or
                                                    self.id_case==45 or
                                                    self.id_case==53 or
                                                    self.id_case==61):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-1))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.east:
                           if  row[0]==2 :
                              self.east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.east2:
                                 if  row[0]==2 :
                                    self.east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.east3:
                                       if  row[0]==2 :
                                          self.east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.east4:
                                             if  row[0]==1 :
                                                if (self.id_case==1 or
                                                    self.id_case==9 or
                                                    self.id_case==17 or
                                                    self.id_case==25 or
                                                    self.id_case==33 or
                                                    self.id_case==41 or
                                                    self.id_case==49 or
                                                    self.id_case==57 or

                                                    self.id_case==2 or
                                                    self.id_case==10 or
                                                    self.id_case==18 or
                                                    self.id_case==26 or
                                                    self.id_case==34 or
                                                    self.id_case==42 or
                                                    self.id_case==50 or
                                                    self.id_case==58 or

                                                    self.id_case==3 or
                                                    self.id_case==11 or
                                                    self.id_case==19 or
                                                    self.id_case==27 or
                                                    self.id_case==35 or
                                                    self.id_case==43 or
                                                    self.id_case==51 or
                                                    self.id_case==59 or

                                                    self.id_case==4 or
                                                    self.id_case==12 or
                                                    self.id_case==20 or
                                                    self.id_case==28 or
                                                    self.id_case==36 or
                                                    self.id_case==44 or
                                                    self.id_case==52 or
                                                    self.id_case==60):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+1))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.north:
                           if  row[0]==2 :
                              self.north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.north2:
                                 if  row[0]==2 :
                                    self.north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.north3:
                                       if  row[0]==2 :
                                          self.north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.north4:
                                             if  row[0]==1 :
                                                if (self.id_case==57 or
                                                    self.id_case==58 or
                                                    self.id_case==59 or
                                                    self.id_case==60 or
                                                    self.id_case==61 or
                                                    self.id_case==62 or
                                                    self.id_case==63 or
                                                    self.id_case==64 or

                                                    self.id_case==49 or
                                                    self.id_case==50 or
                                                    self.id_case==51 or
                                                    self.id_case==52 or
                                                    self.id_case==53 or
                                                    self.id_case==54 or
                                                    self.id_case==55 or
                                                    self.id_case==56 or

                                                    self.id_case==41 or
                                                    self.id_case==42 or
                                                    self.id_case==43 or
                                                    self.id_case==44 or
                                                    self.id_case==45 or
                                                    self.id_case==46 or
                                                    self.id_case==47 or
                                                    self.id_case==48 or

                                                    self.id_case==33 or
                                                    self.id_case==34 or
                                                    self.id_case==35 or
                                                    self.id_case==36 or
                                                    self.id_case==37 or
                                                    self.id_case==38 or
                                                    self.id_case==39 or
                                                    self.id_case==40):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-8))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.south:
                           if  row[0]==2 :
                              self.south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.south2:
                                 if  row[0]==2 :
                                    self.south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.south3:
                                       if  row[0]==2 :
                                          self.south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.south4:
                                             if  row[0]==1 :
                                                if (self.id_case==1 or
                                                    self.id_case==2 or
                                                    self.id_case==3 or
                                                    self.id_case==4 or
                                                    self.id_case==5 or
                                                    self.id_case==6 or
                                                    self.id_case==7 or
                                                    self.id_case==8 or

                                                    self.id_case==9 or
                                                    self.id_case==10 or
                                                    self.id_case==11 or
                                                    self.id_case==12 or
                                                    self.id_case==13 or
                                                    self.id_case==14 or
                                                    self.id_case==15 or
                                                    self.id_case==16 or

                                                    self.id_case==17 or
                                                    self.id_case==18 or
                                                    self.id_case==19 or
                                                    self.id_case==20 or
                                                    self.id_case==21 or
                                                    self.id_case==22 or
                                                    self.id_case==23 or
                                                    self.id_case==24 or

                                                    self.id_case==25 or
                                                    self.id_case==26 or
                                                    self.id_case==27 or
                                                    self.id_case==28 or
                                                    self.id_case==29 or
                                                    self.id_case==30 or
                                                    self.id_case==31 or
                                                    self.id_case==32):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+8))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.north_west:
                           if  row[0]==2 :
                              self.north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.north_west2:
                                 if  row[0]==2 :
                                    self.north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.north_west3:
                                       if  row[0]==2 :
                                          self.north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.north_west4:
                                             if  row[0]==1 :
                                                if (self.id_case==61 or
                                                    self.id_case==62 or
                                                    self.id_case==63 or
                                                    self.id_case==64 or
                                                    self.id_case==56 or
                                                    self.id_case==48 or
                                                    self.id_case==40 or

                                                    self.id_case==53 or
                                                    self.id_case==54 or
                                                    self.id_case==55 or
                                                    self.id_case==47 or
                                                    self.id_case==39 or

                                                    self.id_case==45 or
                                                    self.id_case==46 or
                                                    self.id_case==38 or

                                                    self.id_case==37):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-9))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.north_east:
                           if  row[0]==2 :
                              self.north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.north_east2:
                                 if  row[0]==2 :
                                    self.north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.north_east3:
                                       if  row[0]==2 :
                                          self.north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.north_east4:
                                             if  row[0]==1 :
                                                if (self.id_case==25 or
                                                    self.id_case==17 or
                                                    self.id_case==9 or
                                                    self.id_case==1 or
                                                    self.id_case==2 or
                                                    self.id_case==3 or
                                                    self.id_case==4 or

                                                    self.id_case==26 or
                                                    self.id_case==18 or
                                                    self.id_case==10 or
                                                    self.id_case==11 or
                                                    self.id_case==12 or

                                                    self.id_case==27 or
                                                    self.id_case==19 or
                                                    self.id_case==20 or

                                                    self.id_case==28):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+9))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.south_west:
                           if  row[0]==2 :
                              self.south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.south_west:
                                 if  row[0]==2 :
                                    self.south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.south_west3:
                                       if  row[0]==2 :
                                          self.south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.south_west4:
                                             if  row[0]==1 :
                                                if (self.id_case==33 or
                                                    self.id_case==41 or
                                                    self.id_case==49 or
                                                    self.id_case==57 or
                                                    self.id_case==58 or
                                                    self.id_case==59 or
                                                    self.id_case==60 or

                                                    self.id_case==34 or
                                                    self.id_case==42 or
                                                    self.id_case==50 or
                                                    self.id_case==51 or
                                                    self.id_case==52 or

                                                    self.id_case==35 or
                                                    self.id_case==43 or
                                                    self.id_case==44 or

                                                    self.id_case==36):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-7))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()
                        self.south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.south_east:
                           if  row[0]==2 :
                              self.south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.south_east2:
                                 if  row[0]==2 :
                                    self.south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.south_east3:
                                       if  row[0]==2 :
                                          self.south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.south_east4:
                                             if  row[0]==1 :
                                                if (self.id_case==5 or
                                                    self.id_case==6 or
                                                    self.id_case==7 or
                                                    self.id_case==8 or
                                                    self.id_case==16 or
                                                    self.id_case==24 or
                                                    self.id_case==32 or

                                                    self.id_case==13 or
                                                    self.id_case==14 or
                                                    self.id_case==15 or
                                                    self.id_case==23 or
                                                    self.id_case==31 or

                                                    self.id_case==21 or
                                                    self.id_case==22 or
                                                    self.id_case==30 or

                                                    self.id_case==29 ):
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+7))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=0
                                                   self.refresh_data()

                        #=========================================#
                        #================== QUATRE ===============#
                        #=========================================#
                        self.west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.west:
                           if  row[0]==2 :
                              self.west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.west2:
                                 if  row[0]==2 :
                                    self.west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.west3:
                                       if  row[0]==2 :
                                          self.west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.west4:
                                             if  row[0]==2 :
                                                self.west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*5)))
                                                for row in self.west5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==8 or
                                                          self.id_case==16 or
                                                          self.id_case==24 or
                                                          self.id_case==32 or
                                                          self.id_case==40 or
                                                          self.id_case==48 or
                                                          self.id_case==56 or
                                                          self.id_case==64 or

                                                          self.id_case==7 or
                                                          self.id_case==15 or
                                                          self.id_case==23 or
                                                          self.id_case==31 or
                                                          self.id_case==39 or
                                                          self.id_case==47 or
                                                          self.id_case==55 or
                                                          self.id_case==63 or

                                                          self.id_case==6 or
                                                          self.id_case==14 or
                                                          self.id_case==22 or
                                                          self.id_case==30 or
                                                          self.id_case==38 or
                                                          self.id_case==46 or
                                                          self.id_case==54 or
                                                          self.id_case==62):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-1))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.east:
                           if  row[0]==2 :
                              self.east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.east2:
                                 if  row[0]==2 :
                                    self.east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.east3:
                                       if  row[0]==2 :
                                          self.east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.east4:
                                             if  row[0]==2 :
                                                self.east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*5)))
                                                for row in self.east5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==1 or
                                                          self.id_case==9 or
                                                          self.id_case==17 or
                                                          self.id_case==25 or
                                                          self.id_case==33 or
                                                          self.id_case==41 or
                                                          self.id_case==49 or
                                                          self.id_case==57 or

                                                          self.id_case==2 or
                                                          self.id_case==10 or
                                                          self.id_case==18 or
                                                          self.id_case==26 or
                                                          self.id_case==34 or
                                                          self.id_case==42 or
                                                          self.id_case==50 or
                                                          self.id_case==58 or

                                                          self.id_case==3 or
                                                          self.id_case==11 or
                                                          self.id_case==19 or
                                                          self.id_case==27 or
                                                          self.id_case==35 or
                                                          self.id_case==43 or
                                                          self.id_case==51 or
                                                          self.id_case==59):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+1))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.north:
                           if  row[0]==2 :
                              self.north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.north2:
                                 if  row[0]==2 :
                                    self.north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.north3:
                                       if  row[0]==2 :
                                          self.north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.north4:
                                             if  row[0]==2 :
                                                self.north5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*5)))
                                                for row in self.north5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==57 or
                                                          self.id_case==58 or
                                                          self.id_case==59 or
                                                          self.id_case==60 or
                                                          self.id_case==61 or
                                                          self.id_case==62 or
                                                          self.id_case==63 or
                                                          self.id_case==64 or

                                                          self.id_case==49 or
                                                          self.id_case==50 or
                                                          self.id_case==51 or
                                                          self.id_case==52 or
                                                          self.id_case==53 or
                                                          self.id_case==54 or
                                                          self.id_case==55 or
                                                          self.id_case==56 or

                                                          self.id_case==41 or
                                                          self.id_case==42 or
                                                          self.id_case==43 or
                                                          self.id_case==44 or
                                                          self.id_case==45 or
                                                          self.id_case==46 or
                                                          self.id_case==47 or
                                                          self.id_case==48):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-8))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.south:
                           if  row[0]==2 :
                              self.south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.south2:
                                 if  row[0]==2 :
                                    self.south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.south3:
                                       if  row[0]==2 :
                                          self.south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.south4:
                                             if  row[0]==2 :
                                                self.south5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*5)))
                                                for row in self.south5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==1 or
                                                          self.id_case==2 or
                                                          self.id_case==3 or
                                                          self.id_case==4 or
                                                          self.id_case==5 or
                                                          self.id_case==6 or
                                                          self.id_case==7 or
                                                          self.id_case==8 or

                                                          self.id_case==9 or
                                                          self.id_case==10 or
                                                          self.id_case==11 or
                                                          self.id_case==12 or
                                                          self.id_case==13 or
                                                          self.id_case==14 or
                                                          self.id_case==15 or
                                                          self.id_case==16 or

                                                          self.id_case==17 or
                                                          self.id_case==18 or
                                                          self.id_case==19 or
                                                          self.id_case==20 or
                                                          self.id_case==21 or
                                                          self.id_case==22 or
                                                          self.id_case==23 or
                                                          self.id_case==24):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+8))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.north_west:
                           if  row[0]==2 :
                              self.north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.north_west2:
                                 if  row[0]==2 :
                                    self.north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.north_west3:
                                       if  row[0]==2 :
                                          self.north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.north_west4:
                                             if  row[0]==2 :
                                                self.north_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*5)))
                                                for row in self.north_west5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==62 or
                                                          self.id_case==63 or
                                                          self.id_case==64 or
                                                          self.id_case==56 or
                                                          self.id_case==48 or

                                                          self.id_case==54 or
                                                          self.id_case==55 or
                                                          self.id_case==47 or

                                                          self.id_case==46):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-9))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.north_east:
                           if  row[0]==2 :
                              self.north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.north_east2:
                                 if  row[0]==2 :
                                    self.north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.north_east3:
                                       if  row[0]==2 :
                                          self.north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.north_east4:
                                             if  row[0]==2 :
                                                self.north_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*5)))
                                                for row in self.north_east5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==17 or
                                                          self.id_case==9 or
                                                          self.id_case==1 or
                                                          self.id_case==2 or
                                                          self.id_case==3 or

                                                          self.id_case==18 or
                                                          self.id_case==10 or
                                                          self.id_case==11 or

                                                          self.id_case==19):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+9))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.south_west:
                           if  row[0]==2 :
                              self.south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.south_west:
                                 if  row[0]==2 :
                                    self.south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.south_west3:
                                       if  row[0]==2 :
                                          self.south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.south_west4:
                                             if  row[0]==2 :
                                                self.south_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*5)))
                                                for row in self.south_west5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==41 or
                                                          self.id_case==49 or
                                                          self.id_case==57 or
                                                          self.id_case==58 or
                                                          self.id_case==59 or

                                                          self.id_case==42 or
                                                          self.id_case==50 or
                                                          self.id_case==51 or

                                                          self.id_case==43):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-7))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()
                        self.south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.south_east:
                           if  row[0]==2 :
                              self.south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.south_east2:
                                 if  row[0]==2 :
                                    self.south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.south_east3:
                                       if  row[0]==2 :
                                          self.south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.south_east4:
                                             if  row[0]==2 :
                                                self.south_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*5)))
                                                for row in self.south_east5:
                                                   if  row[0]==1 :
                                                      if (self.id_case==6 or
                                                          self.id_case==7 or
                                                          self.id_case==8 or
                                                          self.id_case==16 or
                                                          self.id_case==24 or

                                                          self.id_case==14 or
                                                          self.id_case==15 or
                                                          self.id_case==23 or

                                                          self.id_case==22):
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+7))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=0
                                                         self.refresh_data()

                        #=========================================#
                        #================== CINQ =================#
                        #=========================================#
                        self.west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.west:
                           if  row[0]==2 :
                              self.west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.west2:
                                 if  row[0]==2 :
                                    self.west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.west3:
                                       if  row[0]==2 :
                                          self.west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.west4:
                                             if  row[0]==2 :
                                                self.west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*5)))
                                                for row in self.west5:
                                                   if  row[0]==2 :
                                                      self.west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*6)))
                                                      for row in self.west6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==8 or
                                                                self.id_case==16 or
                                                                self.id_case==24 or
                                                                self.id_case==32 or
                                                                self.id_case==40 or
                                                                self.id_case==48 or
                                                                self.id_case==56 or
                                                                self.id_case==64 or

                                                                self.id_case==7 or
                                                                self.id_case==15 or
                                                                self.id_case==23 or
                                                                self.id_case==31 or
                                                                self.id_case==39 or
                                                                self.id_case==47 or
                                                                self.id_case==55 or
                                                                self.id_case==63):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-1))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.east:
                           if  row[0]==2 :
                              self.east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.east2:
                                 if  row[0]==2 :
                                    self.east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.east3:
                                       if  row[0]==2 :
                                          self.east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.east4:
                                             if  row[0]==2 :
                                                self.east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*5)))
                                                for row in self.east5:
                                                   if  row[0]==2 :
                                                      self.east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*6)))
                                                      for row in self.east6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==1 or
                                                                self.id_case==9 or
                                                                self.id_case==17 or
                                                                self.id_case==25 or
                                                                self.id_case==33 or
                                                                self.id_case==41 or
                                                                self.id_case==49 or
                                                                self.id_case==57 or

                                                                self.id_case==2 or
                                                                self.id_case==10 or
                                                                self.id_case==18 or
                                                                self.id_case==26 or
                                                                self.id_case==34 or
                                                                self.id_case==42 or
                                                                self.id_case==50 or
                                                                self.id_case==58):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+1))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.north:
                           if  row[0]==2 :
                              self.north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.north2:
                                 if  row[0]==2 :
                                    self.north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.north3:
                                       if  row[0]==2 :
                                          self.north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.north4:
                                             if  row[0]==2 :
                                                self.north5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*5)))
                                                for row in self.north5:
                                                   if  row[0]==2 :
                                                      self.north6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*6)))
                                                      for row in self.north6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==57 or
                                                                self.id_case==58 or
                                                                self.id_case==59 or
                                                                self.id_case==60 or
                                                                self.id_case==61 or
                                                                self.id_case==62 or
                                                                self.id_case==63 or
                                                                self.id_case==64 or

                                                                self.id_case==49 or
                                                                self.id_case==50 or
                                                                self.id_case==51 or
                                                                self.id_case==52 or
                                                                self.id_case==53 or
                                                                self.id_case==54 or
                                                                self.id_case==55 or
                                                                self.id_case==56):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-8))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.south:
                           if  row[0]==2 :
                              self.south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.south2:
                                 if  row[0]==2 :
                                    self.south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.south3:
                                       if  row[0]==2 :
                                          self.south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.south4:
                                             if  row[0]==2 :
                                                self.south5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*5)))
                                                for row in self.south5:
                                                   if  row[0]==2 :
                                                      self.south6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*6)))
                                                      for row in self.south6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==1 or
                                                                self.id_case==2 or
                                                                self.id_case==3 or
                                                                self.id_case==4 or
                                                                self.id_case==5 or
                                                                self.id_case==6 or
                                                                self.id_case==7 or
                                                                self.id_case==8 or

                                                                self.id_case==9 or
                                                                self.id_case==10 or
                                                                self.id_case==11 or
                                                                self.id_case==12 or
                                                                self.id_case==13 or
                                                                self.id_case==14 or
                                                                self.id_case==15 or
                                                                self.id_case==16):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+8))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.north_west:
                           if  row[0]==2 :
                              self.north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.north_west2:
                                 if  row[0]==2 :
                                    self.north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.north_west3:
                                       if  row[0]==2 :
                                          self.north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.north_west4:
                                             if  row[0]==2 :
                                                self.north_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*5)))
                                                for row in self.north_west5:
                                                   if  row[0]==2 :
                                                      self.north_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*6)))
                                                      for row in self.north_west6:
                                                         if  row[0]==1 :
                                                            if (sself.id_case==63 or
                                                                self.id_case==64 or
                                                                self.id_case==56 or

                                                                self.id_case==55):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-9))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.north_east:
                           if  row[0]==2 :
                              self.north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.north_east2:
                                 if  row[0]==2 :
                                    self.north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.north_east3:
                                       if  row[0]==2 :
                                          self.north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.north_east4:
                                             if  row[0]==2 :
                                                self.north_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*5)))
                                                for row in self.north_east5:
                                                   if  row[0]==2 :
                                                      self.north_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*6)))
                                                      for row in self.north_east6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==9 or
                                                                self.id_case==1 or
                                                                self.id_case==2 or

                                                                self.id_case==10):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+9))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.south_west:
                           if  row[0]==2 :
                              self.south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.south_west:
                                 if  row[0]==2 :
                                    self.south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.south_west3:
                                       if  row[0]==2 :
                                          self.south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.south_west4:
                                             if  row[0]==2 :
                                                self.south_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*5)))
                                                for row in self.south_west5:
                                                   if  row[0]==2 :
                                                      self.south_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*6)))
                                                      for row in self.south_west6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==49 or
                                                                self.id_case==57 or
                                                                self.id_case==58 or

                                                                self.id_case==50):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-7))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()
                        self.south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.south_east:
                           if  row[0]==2 :
                              self.south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.south_east2:
                                 if  row[0]==2 :
                                    self.south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.south_east3:
                                       if  row[0]==2 :
                                          self.south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.south_east4:
                                             if  row[0]==2 :
                                                self.south_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*5)))
                                                for row in self.south_east5:
                                                   if  row[0]==2 :
                                                      self.south_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*6)))
                                                      for row in self.south_east6:
                                                         if  row[0]==1 :
                                                            if (self.id_case==7 or
                                                                self.id_case==8 or
                                                                self.id_case==16 or

                                                                self.id_case==15):
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+7))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=0
                                                               self.refresh_data()

                        #=========================================#
                        #================== SIX ==================#
                        #=========================================#
                        self.west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.west:
                           if  row[0]==2 :
                              self.west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.west2:
                                 if  row[0]==2 :
                                    self.west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.west3:
                                       if  row[0]==2 :
                                          self.west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.west4:
                                             if  row[0]==2 :
                                                self.west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*5)))
                                                for row in self.west5:
                                                   if  row[0]==2 :
                                                      self.west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*6)))
                                                      for row in self.west6:
                                                         if  row[0]==2 :
                                                            self.west7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*7)))
                                                            for row in self.west7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==8 or
                                                                      self.id_case==16 or
                                                                      self.id_case==24 or
                                                                      self.id_case==32 or
                                                                      self.id_case==40 or
                                                                      self.id_case==48 or
                                                                      self.id_case==56 or
                                                                      self.id_case==64):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-1))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.east:
                           if  row[0]==2 :
                              self.east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.east2:
                                 if  row[0]==2 :
                                    self.east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.east3:
                                       if  row[0]==2 :
                                          self.east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.east4:
                                             if  row[0]==2 :
                                                self.east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*5)))
                                                for row in self.east5:
                                                   if  row[0]==2 :
                                                      self.east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*6)))
                                                      for row in self.east6:
                                                         if  row[0]==2 :
                                                            self.east7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*7)))
                                                            for row in self.east7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==1 or
                                                                      self.id_case==9 or
                                                                      self.id_case==17 or
                                                                      self.id_case==25 or
                                                                      self.id_case==33 or
                                                                      self.id_case==41 or
                                                                      self.id_case==49 or
                                                                      self.id_case==57):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+1))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.north:
                           if  row[0]==2 :
                              self.north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.north2:
                                 if  row[0]==2 :
                                    self.north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.north3:
                                       if  row[0]==2 :
                                          self.north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.north4:
                                             if  row[0]==2 :
                                                self.north5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*5)))
                                                for row in self.north5:
                                                   if  row[0]==2 :
                                                      self.north6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*6)))
                                                      for row in self.north6:
                                                         if  row[0]==2 :
                                                            self.north7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*7)))
                                                            for row in self.north7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==57 or
                                                                      self.id_case==58 or
                                                                      self.id_case==59 or
                                                                      self.id_case==60 or
                                                                      self.id_case==61 or
                                                                      self.id_case==62 or
                                                                      self.id_case==63 or
                                                                      self.id_case==64):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-8))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.south:
                           if  row[0]==2 :
                              self.south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.south2:
                                 if  row[0]==2 :
                                    self.south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.south3:
                                       if  row[0]==2 :
                                          self.south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.south4:
                                             if  row[0]==2 :
                                                self.south5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*5)))
                                                for row in self.south5:
                                                   if  row[0]==2 :
                                                      self.south6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*6)))
                                                      for row in self.south6:
                                                         if  row[0]==2 :
                                                            self.south7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*7)))
                                                            for row in self.south7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==1 or
                                                                      self.id_case==2 or
                                                                      self.id_case==3 or
                                                                      self.id_case==4 or
                                                                      self.id_case==5 or
                                                                      self.id_case==6 or
                                                                      self.id_case==7 or
                                                                      self.id_case==8):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+8))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.north_west:
                           if  row[0]==2 :
                              self.north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.north_west2:
                                 if  row[0]==2 :
                                    self.north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.north_west3:
                                       if  row[0]==2 :
                                          self.north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.north_west4:
                                             if  row[0]==2 :
                                                self.north_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*5)))
                                                for row in self.north_west5:
                                                   if  row[0]==2 :
                                                      self.north_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*6)))
                                                      for row in self.north_west6:
                                                         if  row[0]==2 :
                                                            self.north_west7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*7)))
                                                            for row in self.north_west7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==64):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-9))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.north_east:
                           if  row[0]==2 :
                              self.north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.north_east2:
                                 if  row[0]==2 :
                                    self.north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.north_east3:
                                       if  row[0]==2 :
                                          self.north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.north_east4:
                                             if  row[0]==2 :
                                                self.north_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*5)))
                                                for row in self.north_east5:
                                                   if  row[0]==2 :
                                                      self.north_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*6)))
                                                      for row in self.north_east6:
                                                         if  row[0]==2 :
                                                            self.north_east7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*7)))
                                                            for row in self.north_east7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==1):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+9))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.south_west:
                           if  row[0]==2 :
                              self.south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.south_west:
                                 if  row[0]==2 :
                                    self.south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.south_west3:
                                       if  row[0]==2 :
                                          self.south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.south_west4:
                                             if  row[0]==2 :
                                                self.south_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*5)))
                                                for row in self.south_west5:
                                                   if  row[0]==2 :
                                                      self.south_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*6)))
                                                      for row in self.south_west6:
                                                         if  row[0]==2 :
                                                            self.south_west7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*7)))
                                                            for row in self.south_west7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==57):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case-7))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()
                        self.south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.south_east:
                           if  row[0]==2 :
                              self.south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.south_east2:
                                 if  row[0]==2 :
                                    self.south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.south_east3:
                                       if  row[0]==2 :
                                          self.south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.south_east4:
                                             if  row[0]==2 :
                                                self.south_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*5)))
                                                for row in self.south_east5:
                                                   if  row[0]==2 :
                                                      self.south_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*6)))
                                                      for row in self.south_east6:
                                                         if  row[0]==2 :
                                                            self.south_east7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*7)))
                                                            for row in self.south_east7:
                                                               if  row[0]==1 :
                                                                  if (self.id_case==8):
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case+7))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=1,image='images/pion1.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=0
                                                                     self.refresh_data()

                  
                                          
               elif self.tour==0:
                  self.ai_select=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case))   
                  for row in self.ai_select:
                     if  row[0]==0:
                        #=======================================#
                        #================== UN =================#
                        #=======================================#
                        self.ai_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.ai_west:
                           if  row[0]==1 :
                              self.ai_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.ai_west2:
                                 if  row[0]==2 :
                                    if (self.id_case==8 or
                                        self.id_case==16 or
                                        self.id_case==24 or
                                        self.id_case==32 or
                                        self.id_case==40 or
                                        self.id_case==48 or
                                        self.id_case==56 or
                                        self.id_case==64 or

                                        self.id_case==7 or
                                        self.id_case==15 or
                                        self.id_case==23 or
                                        self.id_case==31 or
                                        self.id_case==39 or
                                        self.id_case==47 or
                                        self.id_case==55 or
                                        self.id_case==63 or

                                        self.id_case==6 or
                                        self.id_case==14 or
                                        self.id_case==22 or
                                        self.id_case==30 or
                                        self.id_case==38 or
                                        self.id_case==46 or
                                        self.id_case==54 or
                                        self.id_case==62 or

                                        self.id_case==5 or
                                        self.id_case==13 or
                                        self.id_case==21 or
                                        self.id_case==29 or
                                        self.id_case==37 or
                                        self.id_case==45 or
                                        self.id_case==53 or
                                        self.id_case==61 or

                                        self.id_case==4 or
                                        self.id_case==12 or
                                        self.id_case==20 or
                                        self.id_case==28 or
                                        self.id_case==36 or
                                        self.id_case==44 or
                                        self.id_case==52 or
                                        self.id_case==60 or

                                        self.id_case==3 or
                                        self.id_case==11 or
                                        self.id_case==19 or
                                        self.id_case==27 or
                                        self.id_case==35 or
                                        self.id_case==43 or
                                        self.id_case==51 or
                                        self.id_case==59):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-1))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.ai_east:
                           if  row[0]==1 :
                              self.ai_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.ai_east2:
                                 if  row[0]==2 :
                                    if (self.id_case==1 or
                                        self.id_case==9 or
                                        self.id_case==17 or
                                        self.id_case==25 or
                                        self.id_case==33 or
                                        self.id_case==41 or
                                        self.id_case==49 or
                                        self.id_case==57 or

                                        self.id_case==2 or
                                        self.id_case==10 or
                                        self.id_case==18 or
                                        self.id_case==26 or
                                        self.id_case==34 or
                                        self.id_case==42 or
                                        self.id_case==50 or
                                        self.id_case==58 or

                                        self.id_case==3 or
                                        self.id_case==11 or
                                        self.id_case==19 or
                                        self.id_case==27 or
                                        self.id_case==35 or
                                        self.id_case==43 or
                                        self.id_case==51 or
                                        self.id_case==59 or

                                        self.id_case==4 or
                                        self.id_case==12 or
                                        self.id_case==20 or
                                        self.id_case==28 or
                                        self.id_case==36 or
                                        self.id_case==44 or
                                        self.id_case==52 or
                                        self.id_case==60 or

                                        self.id_case==5 or
                                        self.id_case==13 or
                                        self.id_case==21 or
                                        self.id_case==29 or
                                        self.id_case==37 or
                                        self.id_case==45 or
                                        self.id_case==53 or
                                        self.id_case==61 or

                                        self.id_case==6 or
                                        self.id_case==14 or
                                        self.id_case==22 or
                                        self.id_case==30 or
                                        self.id_case==38 or
                                        self.id_case==46 or
                                        self.id_case==54 or
                                        self.id_case==62):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+1))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.ai_north:
                           if  row[0]==1 :
                              self.ai_north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.ai_north2:
                                 if  row[0]==2 :
                                    if (self.id_case==57 or
                                        self.id_case==58 or
                                        self.id_case==59 or
                                        self.id_case==60 or
                                        self.id_case==61 or
                                        self.id_case==62 or
                                        self.id_case==63 or
                                        self.id_case==64 or

                                        self.id_case==49 or
                                        self.id_case==50 or
                                        self.id_case==51 or
                                        self.id_case==52 or
                                        self.id_case==53 or
                                        self.id_case==54 or
                                        self.id_case==55 or
                                        self.id_case==56 or

                                        self.id_case==41 or
                                        self.id_case==42 or
                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or
                                        self.id_case==47 or
                                        self.id_case==48 or

                                        self.id_case==33 or
                                        self.id_case==34 or
                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or
                                        self.id_case==39 or
                                        self.id_case==40 or

                                        self.id_case==25 or
                                        self.id_case==26 or
                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or
                                        self.id_case==31 or
                                        self.id_case==32 or

                                        self.id_case==17 or
                                        self.id_case==18 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==23 or
                                        self.id_case==24):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-8))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.ai_south:
                           if  row[0]==1 :
                              self.ai_south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.ai_south2:
                                 if  row[0]==2 :
                                    if (self.id_case==1 or
                                        self.id_case==2 or
                                        self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or
                                        self.id_case==7 or
                                        self.id_case==8 or

                                        self.id_case==9 or
                                        self.id_case==10 or
                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or
                                        self.id_case==15 or
                                        self.id_case==16 or

                                        self.id_case==17 or
                                        self.id_case==18 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==23 or
                                        self.id_case==24 or

                                        self.id_case==25 or
                                        self.id_case==26 or
                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or
                                        self.id_case==31 or
                                        self.id_case==32 or

                                        self.id_case==33 or
                                        self.id_case==34 or
                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or
                                        self.id_case==39 or
                                        self.id_case==40 or

                                        self.id_case==41 or
                                        self.id_case==42 or
                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or
                                        self.id_case==47 or
                                        self.id_case==48):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+8))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.ai_north_west:
                           if  row[0]==1 :
                              self.ai_north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.ai_north_west:
                                 if  row[0]==2 :
                                    if (self.id_case==59 or
                                        self.id_case==60 or
                                        self.id_case==61 or
                                        self.id_case==62 or
                                        self.id_case==63 or
                                        self.id_case==64 or
                                        self.id_case==56 or
                                        self.id_case==48 or
                                        self.id_case==40 or
                                        self.id_case==32 or
                                        self.id_case==24 or

                                        self.id_case==51 or
                                        self.id_case==52 or
                                        self.id_case==53 or
                                        self.id_case==54 or
                                        self.id_case==55 or
                                        self.id_case==47 or
                                        self.id_case==39 or
                                        self.id_case==31 or
                                        self.id_case==23 or

                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or
                                        self.id_case==38 or
                                        self.id_case==30 or
                                        self.id_case==22 or

                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==29 or
                                        self.id_case==21 or

                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==20 or

                                        self.id_case==19):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-9))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.ai_north_east:
                           if  row[0]==1 :
                              self.ai_north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.ai_north_east2:
                                 if  row[0]==2 :
                                    if (self.id_case==41 or
                                        self.id_case==33 or
                                        self.id_case==25 or
                                        self.id_case==17 or
                                        self.id_case==9 or
                                        self.id_case==1 or
                                        self.id_case==2 or
                                        self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or

                                        self.id_case==42 or
                                        self.id_case==34 or
                                        self.id_case==26 or
                                        self.id_case==18 or
                                        self.id_case==10 or
                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or

                                        self.id_case==43 or
                                        self.id_case==35 or
                                        self.id_case==27 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or

                                        self.id_case==44 or
                                        self.id_case==36 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or

                                        self.id_case==45 or
                                        self.id_case==37 or
                                        self.id_case==38 or

                                        self.id_case==46):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+9))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.ai_south_west:
                           if  row[0]==1 :
                              self.ai_south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.ai_south_west2:
                                 if  row[0]==2 :
                                    if (self.id_case==17 or
                                        self.id_case==25 or
                                        self.id_case==33 or
                                        self.id_case==41 or
                                        self.id_case==49 or
                                        self.id_case==57 or
                                        self.id_case==58 or
                                        self.id_case==59 or
                                        self.id_case==60 or
                                        self.id_case==61 or
                                        self.id_case==62 or

                                        self.id_case==18 or
                                        self.id_case==26 or
                                        self.id_case==34 or
                                        self.id_case==42 or
                                        self.id_case==50 or
                                        self.id_case==51 or
                                        self.id_case==52 or
                                        self.id_case==53 or
                                        self.id_case==54 or

                                        self.id_case==19 or
                                        self.id_case==27 or
                                        self.id_case==35 or
                                        self.id_case==43 or
                                        self.id_case==44 or
                                        self.id_case==45 or
                                        self.id_case==46 or

                                        self.id_case==20 or
                                        self.id_case==28 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or

                                        self.id_case==21 or
                                        self.id_case==29 or
                                        self.id_case==30 or

                                        self.id_case==22):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-7))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()
                        self.ai_south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.ai_south_east:
                           if  row[0]==1 :
                              self.ai_south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.ai_south_east2:
                                 if  row[0]==2 :
                                    if (self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or
                                        self.id_case==7 or
                                        self.id_case==8 or
                                        self.id_case==16 or
                                        self.id_case==24 or
                                        self.id_case==32 or
                                        self.id_case==40 or
                                        self.id_case==48 or

                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or
                                        self.id_case==15 or
                                        self.id_case==23 or
                                        self.id_case==31 or
                                        self.id_case==39 or
                                        self.id_case==47 or

                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==30 or
                                        self.id_case==38 or
                                        self.id_case==46 or

                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==37 or
                                        self.id_case==45 or

                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==44 or

                                        self.id_case==43):
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+7))
                                       self.bdd.commit()
                                       self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                       self.bdd.commit()
                                       self.tour=1
                                       self.refresh_data()

                        #=========================================#
                        #================== DEUX =================#
                        #=========================================#
                        self.ai_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.ai_west:
                           if  row[0]==1 :
                              self.ai_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.ai_west2:
                                 if  row[0]==1 :
                                    self.ai_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.ai_west3:
                                       if  row[0]==2 :
                                          if (self.id_case==8 or
                                              self.id_case==16 or
                                              self.id_case==24 or
                                              self.id_case==32 or
                                              self.id_case==40 or
                                              self.id_case==48 or
                                              self.id_case==56 or
                                              self.id_case==64 or

                                              self.id_case==7 or
                                              self.id_case==15 or
                                              self.id_case==23 or
                                              self.id_case==31 or
                                              self.id_case==39 or
                                              self.id_case==47 or
                                              self.id_case==55 or
                                              self.id_case==63 or

                                              self.id_case==6 or
                                              self.id_case==14 or
                                              self.id_case==22 or
                                              self.id_case==30 or
                                              self.id_case==38 or
                                              self.id_case==46 or
                                              self.id_case==54 or
                                              self.id_case==62 or

                                              self.id_case==5 or
                                              self.id_case==13 or
                                              self.id_case==21 or
                                              self.id_case==29 or
                                              self.id_case==37 or
                                              self.id_case==45 or
                                              self.id_case==53 or
                                              self.id_case==61 or

                                              self.id_case==4 or
                                              self.id_case==12 or
                                              self.id_case==20 or
                                              self.id_case==28 or
                                              self.id_case==36 or
                                              self.id_case==44 or
                                              self.id_case==52 or
                                              self.id_case==60):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-1))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.ai_east:
                           if  row[0]==1 :
                              self.ai_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.ai_east2:
                                 if  row[0]==1 :
                                    self.ai_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.ai_east3:
                                       if  row[0]==2 :
                                          if (self.id_case==1 or
                                              self.id_case==9 or
                                              self.id_case==17 or
                                              self.id_case==25 or
                                              self.id_case==33 or
                                              self.id_case==41 or
                                              self.id_case==49 or
                                              self.id_case==57 or

                                              self.id_case==2 or
                                              self.id_case==10 or
                                              self.id_case==18 or
                                              self.id_case==26 or
                                              self.id_case==34 or
                                              self.id_case==42 or
                                              self.id_case==50 or
                                              self.id_case==58 or

                                              self.id_case==3 or
                                              self.id_case==11 or
                                              self.id_case==19 or
                                              self.id_case==27 or
                                              self.id_case==35 or
                                              self.id_case==43 or
                                              self.id_case==51 or
                                              self.id_case==59 or

                                              self.id_case==4 or
                                              self.id_case==12 or
                                              self.id_case==20 or
                                              self.id_case==28 or
                                              self.id_case==36 or
                                              self.id_case==44 or
                                              self.id_case==52 or
                                              self.id_case==60 or

                                              self.id_case==5 or
                                              self.id_case==13 or
                                              self.id_case==21 or
                                              self.id_case==29 or
                                              self.id_case==37 or
                                              self.id_case==45 or
                                              self.id_case==53 or
                                              self.id_case==61):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+1))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.ai_north:
                           if  row[0]==1 :
                              self.ai_north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.ai_north2:
                                 if  row[0]==1 :
                                    self.ai_north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.ai_north3:
                                       if  row[0]==2 :
                                          if (self.id_case==57 or
                                              self.id_case==58 or
                                              self.id_case==59 or
                                              self.id_case==60 or
                                              self.id_case==61 or
                                              self.id_case==62 or
                                              self.id_case==63 or
                                              self.id_case==64 or

                                              self.id_case==49 or
                                              self.id_case==50 or
                                              self.id_case==51 or
                                              self.id_case==52 or
                                              self.id_case==53 or
                                              self.id_case==54 or
                                              self.id_case==55 or
                                              self.id_case==56 or

                                              self.id_case==41 or
                                              self.id_case==42 or
                                              self.id_case==43 or
                                              self.id_case==44 or
                                              self.id_case==45 or
                                              self.id_case==46 or
                                              self.id_case==47 or
                                              self.id_case==48 or

                                              self.id_case==33 or
                                              self.id_case==34 or
                                              self.id_case==35 or
                                              self.id_case==36 or
                                              self.id_case==37 or
                                              self.id_case==38 or
                                              self.id_case==39 or
                                              self.id_case==40 or

                                              self.id_case==25 or
                                              self.id_case==26 or
                                              self.id_case==27 or
                                              self.id_case==28 or
                                              self.id_case==29 or
                                              self.id_case==30 or
                                              self.id_case==31 or
                                              self.id_case==32):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-8))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.ai_south:
                           if  row[0]==1 :
                              self.ai_south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.ai_south2:
                                 if  row[0]==1 :
                                    self.ai_south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.ai_south3:
                                       if  row[0]==2 :
                                          if (self.id_case==1 or
                                        self.id_case==2 or
                                        self.id_case==3 or
                                        self.id_case==4 or
                                        self.id_case==5 or
                                        self.id_case==6 or
                                        self.id_case==7 or
                                        self.id_case==8 or

                                        self.id_case==9 or
                                        self.id_case==10 or
                                        self.id_case==11 or
                                        self.id_case==12 or
                                        self.id_case==13 or
                                        self.id_case==14 or
                                        self.id_case==15 or
                                        self.id_case==16 or

                                        self.id_case==17 or
                                        self.id_case==18 or
                                        self.id_case==19 or
                                        self.id_case==20 or
                                        self.id_case==21 or
                                        self.id_case==22 or
                                        self.id_case==23 or
                                        self.id_case==24 or

                                        self.id_case==25 or
                                        self.id_case==26 or
                                        self.id_case==27 or
                                        self.id_case==28 or
                                        self.id_case==29 or
                                        self.id_case==30 or
                                        self.id_case==31 or
                                        self.id_case==32 or

                                        self.id_case==33 or
                                        self.id_case==34 or
                                        self.id_case==35 or
                                        self.id_case==36 or
                                        self.id_case==37 or
                                        self.id_case==38 or
                                        self.id_case==39 or
                                        self.id_case==40):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+8))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.ai_north_west:
                           if  row[0]==1 :
                              self.ai_north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.ai_north_west2:
                                 if  row[0]==1 :
                                    self.ai_north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.ai_north_west3:
                                       if  row[0]==2 :
                                          if (self.id_case==60 or
                                              self.id_case==61 or
                                              self.id_case==62 or
                                              self.id_case==63 or
                                              self.id_case==64 or
                                              self.id_case==56 or
                                              self.id_case==48 or
                                              self.id_case==40 or
                                              self.id_case==32 or

                                              self.id_case==52 or
                                              self.id_case==53 or
                                              self.id_case==54 or
                                              self.id_case==55 or
                                              self.id_case==47 or
                                              self.id_case==39 or
                                              self.id_case==31 or

                                              self.id_case==44 or
                                              self.id_case==45 or
                                              self.id_case==46 or
                                              self.id_case==38 or
                                              self.id_case==30 or

                                              self.id_case==36 or
                                              self.id_case==37 or
                                              self.id_case==29 or

                                              self.id_case==28):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-9))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.ai_north_east:
                           if  row[0]==1 :
                              self.ai_north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.ai_north_east2:
                                 if  row[0]==1 :
                                    self.ai_north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.ai_north_east3:
                                       if  row[0]==2 :
                                          if (self.id_case==33 or
                                              self.id_case==25 or
                                              self.id_case==17 or
                                              self.id_case==9 or
                                              self.id_case==1 or
                                              self.id_case==2 or
                                              self.id_case==3 or
                                              self.id_case==4 or
                                              self.id_case==5 or

                                              self.id_case==34 or
                                              self.id_case==26 or
                                              self.id_case==18 or
                                              self.id_case==10 or
                                              self.id_case==11 or
                                              self.id_case==12 or
                                              self.id_case==13 or

                                              self.id_case==35 or
                                              self.id_case==27 or
                                              self.id_case==19 or
                                              self.id_case==20 or
                                              self.id_case==21 or

                                              self.id_case==36 or
                                              self.id_case==28 or
                                              self.id_case==29 or

                                              self.id_case==37):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+9))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.ai_south_west:
                           if  row[0]==1 :
                              self.ai_south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.ai_south_west:
                                 if  row[0]==1 :
                                    self.ai_south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.ai_south_west3:
                                       if  row[0]==2 :
                                          if (self.id_case==25 or
                                              self.id_case==33 or
                                              self.id_case==41 or
                                              self.id_case==49 or
                                              self.id_case==57 or
                                              self.id_case==58 or
                                              self.id_case==59 or
                                              self.id_case==60 or
                                              self.id_case==61 or

                                              self.id_case==26 or
                                              self.id_case==34 or
                                              self.id_case==42 or
                                              self.id_case==50 or
                                              self.id_case==51 or
                                              self.id_case==52 or
                                              self.id_case==53 or

                                              self.id_case==27 or
                                              self.id_case==35 or
                                              self.id_case==43 or
                                              self.id_case==44 or
                                              self.id_case==45 or

                                              self.id_case==28 or
                                              self.id_case==36 or
                                              self.id_case==37 or

                                              self.id_case==29):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-7))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()
                        self.ai_south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.ai_south_east:
                           if  row[0]==1 :
                              self.ai_south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.ai_south_east2:
                                 if  row[0]==1 :
                                    self.ai_south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.ai_south_east3:
                                       if  row[0]==2 :
                                          if (self.id_case==4 or
                                              self.id_case==5 or
                                              self.id_case==6 or
                                              self.id_case==7 or
                                              self.id_case==8 or
                                              self.id_case==16 or
                                              self.id_case==24 or
                                              self.id_case==32 or
                                              self.id_case==40 or

                                              self.id_case==12 or
                                              self.id_case==13 or
                                              self.id_case==14 or
                                              self.id_case==15 or
                                              self.id_case==23 or
                                              self.id_case==31 or
                                              self.id_case==39 or

                                              self.id_case==20 or
                                              self.id_case==21 or
                                              self.id_case==22 or
                                              self.id_case==30 or
                                              self.id_case==38 or

                                              self.id_case==28 or
                                              self.id_case==29 or
                                              self.id_case==37 or

                                              self.id_case==36):
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+7))
                                             self.bdd.commit()
                                             self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                             self.bdd.commit()
                                             self.tour=1
                                             self.refresh_data()


                        #=========================================#
                        #================== TROIS ================#
                        #=========================================#
                        self.ai_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.ai_west:
                           if  row[0]==1 :
                              self.ai_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.ai_west2:
                                 if  row[0]==1 :
                                    self.ai_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.ai_west3:
                                       if  row[0]==1 :
                                          self.ai_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.ai_west4:
                                             if  row[0]==2 :
                                                if (self.id_case==8 or
                                                    self.id_case==16 or
                                                    self.id_case==24 or
                                                    self.id_case==32 or
                                                    self.id_case==40 or
                                                    self.id_case==48 or
                                                    self.id_case==56 or
                                                    self.id_case==64 or

                                                    self.id_case==7 or
                                                    self.id_case==15 or
                                                    self.id_case==23 or
                                                    self.id_case==31 or
                                                    self.id_case==39 or
                                                    self.id_case==47 or
                                                    self.id_case==55 or
                                                    self.id_case==63 or

                                                    self.id_case==6 or
                                                    self.id_case==14 or
                                                    self.id_case==22 or
                                                    self.id_case==30 or
                                                    self.id_case==38 or
                                                    self.id_case==46 or
                                                    self.id_case==54 or
                                                    self.id_case==62 or

                                                    self.id_case==5 or
                                                    self.id_case==13 or
                                                    self.id_case==21 or
                                                    self.id_case==29 or
                                                    self.id_case==37 or
                                                    self.id_case==45 or
                                                    self.id_case==53 or
                                                    self.id_case==61):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-1))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.ai_east:
                           if  row[0]==1 :
                              self.ai_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.ai_east2:
                                 if  row[0]==1 :
                                    self.ai_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.ai_east3:
                                       if  row[0]==1 :
                                          self.ai_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.ai_east4:
                                             if  row[0]==2 :
                                                if (self.id_case==1 or
                                                    self.id_case==9 or
                                                    self.id_case==17 or
                                                    self.id_case==25 or
                                                    self.id_case==33 or
                                                    self.id_case==41 or
                                                    self.id_case==49 or
                                                    self.id_case==57 or

                                                    self.id_case==2 or
                                                    self.id_case==10 or
                                                    self.id_case==18 or
                                                    self.id_case==26 or
                                                    self.id_case==34 or
                                                    self.id_case==42 or
                                                    self.id_case==50 or
                                                    self.id_case==58 or

                                                    self.id_case==3 or
                                                    self.id_case==11 or
                                                    self.id_case==19 or
                                                    self.id_case==27 or
                                                    self.id_case==35 or
                                                    self.id_case==43 or
                                                    self.id_case==51 or
                                                    self.id_case==59 or

                                                    self.id_case==4 or
                                                    self.id_case==12 or
                                                    self.id_case==20 or
                                                    self.id_case==28 or
                                                    self.id_case==36 or
                                                    self.id_case==44 or
                                                    self.id_case==52 or
                                                    self.id_case==60):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+1))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.ai_north:
                           if  row[0]==1 :
                              self.ai_north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.ai_north2:
                                 if  row[0]==1 :
                                    self.ai_north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.ai_north3:
                                       if  row[0]==1 :
                                          self.ai_north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.ai_north4:
                                             if  row[0]==2 :
                                                if (self.id_case==57 or
                                                    self.id_case==58 or
                                                    self.id_case==59 or
                                                    self.id_case==60 or
                                                    self.id_case==61 or
                                                    self.id_case==62 or
                                                    self.id_case==63 or
                                                    self.id_case==64 or

                                                    self.id_case==49 or
                                                    self.id_case==50 or
                                                    self.id_case==51 or
                                                    self.id_case==52 or
                                                    self.id_case==53 or
                                                    self.id_case==54 or
                                                    self.id_case==55 or
                                                    self.id_case==56 or

                                                    self.id_case==41 or
                                                    self.id_case==42 or
                                                    self.id_case==43 or
                                                    self.id_case==44 or
                                                    self.id_case==45 or
                                                    self.id_case==46 or
                                                    self.id_case==47 or
                                                    self.id_case==48 or

                                                    self.id_case==33 or
                                                    self.id_case==34 or
                                                    self.id_case==35 or
                                                    self.id_case==36 or
                                                    self.id_case==37 or
                                                    self.id_case==38 or
                                                    self.id_case==39 or
                                                    self.id_case==40):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-8))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.ai_south:
                           if  row[0]==1 :
                              self.ai_south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.ai_south2:
                                 if  row[0]==1 :
                                    self.ai_south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.ai_south3:
                                       if  row[0]==1 :
                                          self.ai_south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.ai_south4:
                                             if  row[0]==2 :
                                                if (self.id_case==1 or
                                                    self.id_case==2 or
                                                    self.id_case==3 or
                                                    self.id_case==4 or
                                                    self.id_case==5 or
                                                    self.id_case==6 or
                                                    self.id_case==7 or
                                                    self.id_case==8 or

                                                    self.id_case==9 or
                                                    self.id_case==10 or
                                                    self.id_case==11 or
                                                    self.id_case==12 or
                                                    self.id_case==13 or
                                                    self.id_case==14 or
                                                    self.id_case==15 or
                                                    self.id_case==16 or

                                                    self.id_case==17 or
                                                    self.id_case==18 or
                                                    self.id_case==19 or
                                                    self.id_case==20 or
                                                    self.id_case==21 or
                                                    self.id_case==22 or
                                                    self.id_case==23 or
                                                    self.id_case==24 or

                                                    self.id_case==25 or
                                                    self.id_case==26 or
                                                    self.id_case==27 or
                                                    self.id_case==28 or
                                                    self.id_case==29 or
                                                    self.id_case==30 or
                                                    self.id_case==31 or
                                                    self.id_case==32):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+8))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.ai_north_west:
                           if  row[0]==1 :
                              self.ai_north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.ai_north_west2:
                                 if  row[0]==1 :
                                    self.ai_north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.ai_north_west3:
                                       if  row[0]==1 :
                                          self.ai_north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.ai_north_west4:
                                             if  row[0]==2 :
                                                if (self.id_case==61 or
                                                    self.id_case==62 or
                                                    self.id_case==63 or
                                                    self.id_case==64 or
                                                    self.id_case==56 or
                                                    self.id_case==48 or
                                                    self.id_case==40 or

                                                    self.id_case==53 or
                                                    self.id_case==54 or
                                                    self.id_case==55 or
                                                    self.id_case==47 or
                                                    self.id_case==39 or

                                                    self.id_case==45 or
                                                    self.id_case==46 or
                                                    self.id_case==38 or

                                                    self.id_case==37):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-9))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.ai_north_east:
                           if  row[0]==1 :
                              self.ai_north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.ai_north_east2:
                                 if  row[0]==1 :
                                    self.ai_north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.ai_north_east3:
                                       if  row[0]==1 :
                                          self.ai_north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.ai_north_east4:
                                             if  row[0]==2 :
                                                if (self.id_case==25 or
                                                    self.id_case==17 or
                                                    self.id_case==9 or
                                                    self.id_case==1 or
                                                    self.id_case==2 or
                                                    self.id_case==3 or
                                                    self.id_case==4 or

                                                    self.id_case==26 or
                                                    self.id_case==18 or
                                                    self.id_case==10 or
                                                    self.id_case==11 or
                                                    self.id_case==12 or

                                                    self.id_case==27 or
                                                    self.id_case==19 or
                                                    self.id_case==20 or

                                                    self.id_case==28):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+9))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.ai_south_west:
                           if  row[0]==1 :
                              self.ai_south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.ai_south_west:
                                 if  row[0]==1 :
                                    self.ai_south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.ai_south_west3:
                                       if  row[0]==1 :
                                          self.ai_south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.ai_south_west4:
                                             if  row[0]==2 :
                                                if (self.id_case==33 or
                                                    self.id_case==41 or
                                                    self.id_case==49 or
                                                    self.id_case==57 or
                                                    self.id_case==58 or
                                                    self.id_case==59 or
                                                    self.id_case==60 or

                                                    self.id_case==34 or
                                                    self.id_case==42 or
                                                    self.id_case==50 or
                                                    self.id_case==51 or
                                                    self.id_case==52 or

                                                    self.id_case==35 or
                                                    self.id_case==43 or
                                                    self.id_case==44 or

                                                    self.id_case==36):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-7))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()
                        self.ai_south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.ai_south_east:
                           if  row[0]==1 :
                              self.ai_south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.ai_south_east2:
                                 if  row[0]==1 :
                                    self.ai_south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.ai_south_east3:
                                       if  row[0]==1 :
                                          self.ai_south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.ai_south_east4:
                                             if  row[0]==2 :
                                                if (self.id_case==5 or
                                                    self.id_case==6 or
                                                    self.id_case==7 or
                                                    self.id_case==8 or
                                                    self.id_case==16 or
                                                    self.id_case==24 or
                                                    self.id_case==32 or

                                                    self.id_case==13 or
                                                    self.id_case==14 or
                                                    self.id_case==15 or
                                                    self.id_case==23 or
                                                    self.id_case==31 or

                                                    self.id_case==21 or
                                                    self.id_case==22 or
                                                    self.id_case==30 or

                                                    self.id_case==29 ):
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+7))
                                                   self.bdd.commit()
                                                   self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                   self.bdd.commit()
                                                   self.tour=1
                                                   self.refresh_data()

                        #=========================================#
                        #================== QUATRE ===============#
                        #=========================================#
                        self.ai_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.ai_west:
                           if  row[0]==1 :
                              self.ai_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.ai_west2:
                                 if  row[0]==1 :
                                    self.ai_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.ai_west3:
                                       if  row[0]==1 :
                                          self.ai_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.ai_west4:
                                             if  row[0]==1 :
                                                self.ai_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*5)))
                                                for row in self.ai_west5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==8 or
                                                          self.id_case==16 or
                                                          self.id_case==24 or
                                                          self.id_case==32 or
                                                          self.id_case==40 or
                                                          self.id_case==48 or
                                                          self.id_case==56 or
                                                          self.id_case==64 or

                                                          self.id_case==7 or
                                                          self.id_case==15 or
                                                          self.id_case==23 or
                                                          self.id_case==31 or
                                                          self.id_case==39 or
                                                          self.id_case==47 or
                                                          self.id_case==55 or
                                                          self.id_case==63 or

                                                          self.id_case==6 or
                                                          self.id_case==14 or
                                                          self.id_case==22 or
                                                          self.id_case==30 or
                                                          self.id_case==38 or
                                                          self.id_case==46 or
                                                          self.id_case==54 or
                                                          self.id_case==62):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-1))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.ai_east:
                           if  row[0]==1 :
                              self.ai_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.ai_east2:
                                 if  row[0]==1 :
                                    self.ai_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.ai_east3:
                                       if  row[0]==1 :
                                          self.ai_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.ai_east4:
                                             if  row[0]==1 :
                                                self.ai_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*5)))
                                                for row in self.ai_east5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==1 or
                                                          self.id_case==9 or
                                                          self.id_case==17 or
                                                          self.id_case==25 or
                                                          self.id_case==33 or
                                                          self.id_case==41 or
                                                          self.id_case==49 or
                                                          self.id_case==57 or

                                                          self.id_case==2 or
                                                          self.id_case==10 or
                                                          self.id_case==18 or
                                                          self.id_case==26 or
                                                          self.id_case==34 or
                                                          self.id_case==42 or
                                                          self.id_case==50 or
                                                          self.id_case==58 or

                                                          self.id_case==3 or
                                                          self.id_case==11 or
                                                          self.id_case==19 or
                                                          self.id_case==27 or
                                                          self.id_case==35 or
                                                          self.id_case==43 or
                                                          self.id_case==51 or
                                                          self.id_case==59):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+1))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.ai_north:
                           if  row[0]==1 :
                              self.ai_north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.ai_north2:
                                 if  row[0]==1 :
                                    self.ai_north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.ai_north3:
                                       if  row[0]==1 :
                                          self.ai_north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.ai_north4:
                                             if  row[0]==1 :
                                                self.ai_north5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*5)))
                                                for row in self.ai_north5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==57 or
                                                          self.id_case==58 or
                                                          self.id_case==59 or
                                                          self.id_case==60 or
                                                          self.id_case==61 or
                                                          self.id_case==62 or
                                                          self.id_case==63 or
                                                          self.id_case==64 or

                                                          self.id_case==49 or
                                                          self.id_case==50 or
                                                          self.id_case==51 or
                                                          self.id_case==52 or
                                                          self.id_case==53 or
                                                          self.id_case==54 or
                                                          self.id_case==55 or
                                                          self.id_case==56 or

                                                          self.id_case==41 or
                                                          self.id_case==42 or
                                                          self.id_case==43 or
                                                          self.id_case==44 or
                                                          self.id_case==45 or
                                                          self.id_case==46 or
                                                          self.id_case==47 or
                                                          self.id_case==48):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-8))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.ai_south:
                           if  row[0]==1 :
                              self.ai_south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.ai_south2:
                                 if  row[0]==1 :
                                    self.ai_south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.ai_south3:
                                       if  row[0]==1 :
                                          self.ai_south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.ai_south4:
                                             if  row[0]==1 :
                                                self.ai_south5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*5)))
                                                for row in self.ai_south5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==1 or
                                                          self.id_case==2 or
                                                          self.id_case==3 or
                                                          self.id_case==4 or
                                                          self.id_case==5 or
                                                          self.id_case==6 or
                                                          self.id_case==7 or
                                                          self.id_case==8 or

                                                          self.id_case==9 or
                                                          self.id_case==10 or
                                                          self.id_case==11 or
                                                          self.id_case==12 or
                                                          self.id_case==13 or
                                                          self.id_case==14 or
                                                          self.id_case==15 or
                                                          self.id_case==16 or

                                                          self.id_case==17 or
                                                          self.id_case==18 or
                                                          self.id_case==19 or
                                                          self.id_case==20 or
                                                          self.id_case==21 or
                                                          self.id_case==22 or
                                                          self.id_case==23 or
                                                          self.id_case==24):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+8))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.ai_north_west:
                           if  row[0]==1 :
                              self.ai_north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.ai_north_west2:
                                 if  row[0]==1 :
                                    self.ai_north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.ai_north_west3:
                                       if  row[0]==1 :
                                          self.ai_north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.ai_north_west4:
                                             if  row[0]==1 :
                                                self.ai_north_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*5)))
                                                for row in self.ai_north_west5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==62 or
                                                          self.id_case==63 or
                                                          self.id_case==64 or
                                                          self.id_case==56 or
                                                          self.id_case==48 or

                                                          self.id_case==54 or
                                                          self.id_case==55 or
                                                          self.id_case==47 or

                                                          self.id_case==46):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-9))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.ai_north_east:
                           if  row[0]==1 :
                              self.ai_north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.ai_north_east2:
                                 if  row[0]==1 :
                                    self.ai_north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.ai_north_east3:
                                       if  row[0]==1 :
                                          self.ai_north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.ai_north_east4:
                                             if  row[0]==1 :
                                                self.ai_north_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*5)))
                                                for row in self.ai_north_east5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==17 or
                                                          self.id_case==9 or
                                                          self.id_case==1 or
                                                          self.id_case==2 or
                                                          self.id_case==3 or

                                                          self.id_case==18 or
                                                          self.id_case==10 or
                                                          self.id_case==11 or

                                                          self.id_case==19):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+9))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.ai_south_west:
                           if  row[0]==1 :
                              self.ai_south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.ai_south_west:
                                 if  row[0]==1 :
                                    self.ai_south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.ai_south_west3:
                                       if  row[0]==1 :
                                          self.ai_south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.ai_south_west4:
                                             if  row[0]==1 :
                                                self.ai_south_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*5)))
                                                for row in self.ai_south_west5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==41 or
                                                          self.id_case==49 or
                                                          self.id_case==57 or
                                                          self.id_case==58 or
                                                          self.id_case==59 or

                                                          self.id_case==42 or
                                                          self.id_case==50 or
                                                          self.id_case==51 or

                                                          self.id_case==43):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-7))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()
                        self.ai_south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.ai_south_east:
                           if  row[0]==1 :
                              self.ai_south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.ai_south_east2:
                                 if  row[0]==1 :
                                    self.ai_south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.ai_south_east3:
                                       if  row[0]==1 :
                                          self.ai_south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.ai_south_east4:
                                             if  row[0]==1 :
                                                self.ai_south_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*5)))
                                                for row in self.ai_south_east5:
                                                   if  row[0]==2 :
                                                      if (self.id_case==6 or
                                                          self.id_case==7 or
                                                          self.id_case==8 or
                                                          self.id_case==16 or
                                                          self.id_case==24 or

                                                          self.id_case==14 or
                                                          self.id_case==15 or
                                                          self.id_case==23 or

                                                          self.id_case==22):
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*4)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+7))
                                                         self.bdd.commit()
                                                         self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                         self.bdd.commit()
                                                         self.tour=1
                                                         self.refresh_data()

                        #=========================================#
                        #================== CINQ =================#
                        #=========================================#
                        self.ai_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.ai_west:
                           if  row[0]==1 :
                              self.ai_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.ai_west2:
                                 if  row[0]==1 :
                                    self.ai_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.ai_west3:
                                       if  row[0]==1 :
                                          self.ai_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.ai_west4:
                                             if  row[0]==1 :
                                                self.ai_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*5)))
                                                for row in self.ai_west5:
                                                   if  row[0]==1 :
                                                      self.ai_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*6)))
                                                      for row in self.ai_west6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==8 or
                                                                self.id_case==16 or
                                                                self.id_case==24 or
                                                                self.id_case==32 or
                                                                self.id_case==40 or
                                                                self.id_case==48 or
                                                                self.id_case==56 or
                                                                self.id_case==64 or

                                                                self.id_case==7 or
                                                                self.id_case==15 or
                                                                self.id_case==23 or
                                                                self.id_case==31 or
                                                                self.id_case==39 or
                                                                self.id_case==47 or
                                                                self.id_case==55 or
                                                                self.id_case==63):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-1))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.ai_east:
                           if  row[0]==1 :
                              self.ai_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.ai_east2:
                                 if  row[0]==1 :
                                    self.ai_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.ai_east3:
                                       if  row[0]==1 :
                                          self.ai_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.ai_east4:
                                             if  row[0]==1 :
                                                self.ai_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*5)))
                                                for row in self.ai_east5:
                                                   if  row[0]==1 :
                                                      self.ai_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*6)))
                                                      for row in self.ai_east6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==1 or
                                                                self.id_case==9 or
                                                                self.id_case==17 or
                                                                self.id_case==25 or
                                                                self.id_case==33 or
                                                                self.id_case==41 or
                                                                self.id_case==49 or
                                                                self.id_case==57 or

                                                                self.id_case==2 or
                                                                self.id_case==10 or
                                                                self.id_case==18 or
                                                                self.id_case==26 or
                                                                self.id_case==34 or
                                                                self.id_case==42 or
                                                                self.id_case==50 or
                                                                self.id_case==58):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+1))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.ai_north:
                           if  row[0]==1 :
                              self.ai_north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.ai_north2:
                                 if  row[0]==1 :
                                    self.ai_north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.ai_north3:
                                       if  row[0]==1 :
                                          self.ai_north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.ai_north4:
                                             if  row[0]==1 :
                                                self.ai_north5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*5)))
                                                for row in self.ai_north5:
                                                   if  row[0]==1 :
                                                      self.ai_north6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*6)))
                                                      for row in self.ai_north6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==57 or
                                                                self.id_case==58 or
                                                                self.id_case==59 or
                                                                self.id_case==60 or
                                                                self.id_case==61 or
                                                                self.id_case==62 or
                                                                self.id_case==63 or
                                                                self.id_case==64 or

                                                                self.id_case==49 or
                                                                self.id_case==50 or
                                                                self.id_case==51 or
                                                                self.id_case==52 or
                                                                self.id_case==53 or
                                                                self.id_case==54 or
                                                                self.id_case==55 or
                                                                self.id_case==56):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-8))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.ai_south:
                           if  row[0]==1 :
                              self.ai_south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.ai_south2:
                                 if  row[0]==1 :
                                    self.ai_south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.ai_south3:
                                       if  row[0]==1 :
                                          self.ai_south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.ai_south4:
                                             if  row[0]==1 :
                                                self.ai_south5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*5)))
                                                for row in self.ai_south5:
                                                   if  row[0]==1 :
                                                      self.ai_south6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*6)))
                                                      for row in self.ai_south6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==1 or
                                                                self.id_case==2 or
                                                                self.id_case==3 or
                                                                self.id_case==4 or
                                                                self.id_case==5 or
                                                                self.id_case==6 or
                                                                self.id_case==7 or
                                                                self.id_case==8 or

                                                                self.id_case==9 or
                                                                self.id_case==10 or
                                                                self.id_case==11 or
                                                                self.id_case==12 or
                                                                self.id_case==13 or
                                                                self.id_case==14 or
                                                                self.id_case==15 or
                                                                self.id_case==16):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+8))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.ai_north_west:
                           if  row[0]==1 :
                              self.ai_north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.ai_north_west2:
                                 if  row[0]==1 :
                                    self.ai_north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.ai_north_west3:
                                       if  row[0]==1 :
                                          self.ai_north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.ai_north_west4:
                                             if  row[0]==1 :
                                                self.ai_north_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*5)))
                                                for row in self.ai_north_west5:
                                                   if  row[0]==1 :
                                                      self.ai_north_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*6)))
                                                      for row in self.ai_north_west6:
                                                         if  row[0]==2 :
                                                            if (sself.id_case==63 or
                                                                self.id_case==64 or
                                                                self.id_case==56 or

                                                                self.id_case==55):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-9))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.ai_north_east:
                           if  row[0]==1 :
                              self.ai_north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.ai_north_east2:
                                 if  row[0]==1 :
                                    self.ai_north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.ai_north_east3:
                                       if  row[0]==1 :
                                          self.ai_north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.ai_north_east4:
                                             if  row[0]==1 :
                                                self.ai_north_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*5)))
                                                for row in self.ai_north_east5:
                                                   if  row[0]==1 :
                                                      self.ai_north_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*6)))
                                                      for row in self.ai_north_east6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==9 or
                                                                self.id_case==1 or
                                                                self.id_case==2 or

                                                                self.id_case==10):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+9))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.ai_south_west:
                           if  row[0]==1 :
                              self.ai_south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.ai_south_west:
                                 if  row[0]==1 :
                                    self.ai_south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.ai_south_west3:
                                       if  row[0]==1 :
                                          self.ai_south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.ai_south_west4:
                                             if  row[0]==1 :
                                                self.ai_south_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*5)))
                                                for row in self.ai_south_west5:
                                                   if  row[0]==1 :
                                                      self.ai_south_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*6)))
                                                      for row in self.ai_south_west6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==49 or
                                                                self.id_case==57 or
                                                                self.id_case==58 or

                                                                self.id_case==50):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-7))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()
                        self.ai_south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.ai_south_east:
                           if  row[0]==1 :
                              self.ai_south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.ai_south_east2:
                                 if  row[0]==1 :
                                    self.ai_south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.ai_south_east3:
                                       if  row[0]==1 :
                                          self.ai_south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.ai_south_east4:
                                             if  row[0]==1 :
                                                self.ai_south_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*5)))
                                                for row in self.ai_south_east5:
                                                   if  row[0]==1 :
                                                      self.ai_south_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*6)))
                                                      for row in self.ai_south_east6:
                                                         if  row[0]==2 :
                                                            if (self.id_case==7 or
                                                                self.id_case==8 or
                                                                self.id_case==16 or

                                                                self.id_case==15):
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*5)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*4)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+7))
                                                               self.bdd.commit()
                                                               self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                               self.bdd.commit()
                                                               self.tour=1
                                                               self.refresh_data()

                        #=========================================#
                        #================== SIX ==================#
                        #=========================================#
                        self.ai_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-1))
                        for row in self.ai_west:
                           if  row[0]==1 :
                              self.ai_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*2)))
                              for row in self.ai_west2:
                                 if  row[0]==1 :
                                    self.ai_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*3)))
                                    for row in self.ai_west3:
                                       if  row[0]==1 :
                                          self.ai_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*4)))
                                          for row in self.ai_west4:
                                             if  row[0]==1 :
                                                self.ai_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*5)))
                                                for row in self.ai_west5:
                                                   if  row[0]==1 :
                                                      self.ai_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*6)))
                                                      for row in self.ai_west6:
                                                         if  row[0]==1 :
                                                            self.ai_west7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(1*7)))
                                                            for row in self.ai_west7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==8 or
                                                                      self.id_case==16 or
                                                                      self.id_case==24 or
                                                                      self.id_case==32 or
                                                                      self.id_case==40 or
                                                                      self.id_case==48 or
                                                                      self.id_case==56 or
                                                                      self.id_case==64):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(1*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-1))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+1))
                        for row in self.ai_east:
                           if  row[0]==1 :
                              self.ai_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*2)))
                              for row in self.ai_east2:
                                 if  row[0]==1 :
                                    self.ai_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*3)))
                                    for row in self.ai_east3:
                                       if  row[0]==1 :
                                          self.ai_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*4)))
                                          for row in self.ai_east4:
                                             if  row[0]==1 :
                                                self.ai_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*5)))
                                                for row in self.ai_east5:
                                                   if  row[0]==1 :
                                                      self.ai_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*6)))
                                                      for row in self.ai_east6:
                                                         if  row[0]==1 :
                                                            self.ai_east7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(1*7)))
                                                            for row in self.ai_east7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==1 or
                                                                      self.id_case==9 or
                                                                      self.id_case==17 or
                                                                      self.id_case==25 or
                                                                      self.id_case==33 or
                                                                      self.id_case==41 or
                                                                      self.id_case==49 or
                                                                      self.id_case==57):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(1*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+1))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_north=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-8))
                        for row in self.ai_north:
                           if  row[0]==1 :
                              self.ai_north2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*2)))
                              for row in self.ai_north2:
                                 if  row[0]==1 :
                                    self.ai_north3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*3)))
                                    for row in self.ai_north3:
                                       if  row[0]==1 :
                                          self.ai_north4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*4)))
                                          for row in self.ai_north4:
                                             if  row[0]==1 :
                                                self.ai_north5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*5)))
                                                for row in self.ai_north5:
                                                   if  row[0]==1 :
                                                      self.ai_north6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*6)))
                                                      for row in self.ai_north6:
                                                         if  row[0]==1 :
                                                            self.ai_north7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(8*7)))
                                                            for row in self.ai_north7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==57 or
                                                                      self.id_case==58 or
                                                                      self.id_case==59 or
                                                                      self.id_case==60 or
                                                                      self.id_case==61 or
                                                                      self.id_case==62 or
                                                                      self.id_case==63 or
                                                                      self.id_case==64):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(8*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-8))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_south=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+8))
                        for row in self.ai_south:
                           if  row[0]==1 :
                              self.ai_south2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*2)))
                              for row in self.ai_south2:
                                 if  row[0]==1 :
                                    self.ai_south3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*3)))
                                    for row in self.ai_south3:
                                       if  row[0]==1 :
                                          self.ai_south4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*4)))
                                          for row in self.ai_south4:
                                             if  row[0]==1 :
                                                self.ai_south5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*5)))
                                                for row in self.ai_south5:
                                                   if  row[0]==1 :
                                                      self.ai_south6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*6)))
                                                      for row in self.ai_south6:
                                                         if  row[0]==1 :
                                                            self.ai_south7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(8*7)))
                                                            for row in self.ai_south7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==1 or
                                                                      self.id_case==2 or
                                                                      self.id_case==3 or
                                                                      self.id_case==4 or
                                                                      self.id_case==5 or
                                                                      self.id_case==6 or
                                                                      self.id_case==7 or
                                                                      self.id_case==8):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(8*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+8))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_north_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-9))
                        for row in self.ai_north_west:
                           if  row[0]==1 :
                              self.ai_north_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*2)))
                              for row in self.ai_north_west2:
                                 if  row[0]==1 :
                                    self.ai_north_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*3)))
                                    for row in self.ai_north_west3:
                                       if  row[0]==1 :
                                          self.ai_north_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*4)))
                                          for row in self.ai_north_west4:
                                             if  row[0]==1 :
                                                self.ai_north_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*5)))
                                                for row in self.ai_north_west5:
                                                   if  row[0]==1 :
                                                      self.ai_north_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*6)))
                                                      for row in self.ai_north_west6:
                                                         if  row[0]==1 :
                                                            self.ai_north_west7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(9*7)))
                                                            for row in self.ai_north_west7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==64):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(9*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-9))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_north_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+9))
                        for row in self.ai_north_east:
                           if  row[0]==1 :
                              self.ai_north_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*2)))
                              for row in self.ai_north_east2:
                                 if  row[0]==1 :
                                    self.ai_north_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*3)))
                                    for row in self.ai_north_east3:
                                       if  row[0]==1 :
                                          self.ai_north_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*4)))
                                          for row in self.ai_north_east4:
                                             if  row[0]==1 :
                                                self.ai_north_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*5)))
                                                for row in self.ai_north_east5:
                                                   if  row[0]==1 :
                                                      self.ai_north_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*6)))
                                                      for row in self.ai_north_east6:
                                                         if  row[0]==1 :
                                                            self.ai_north_east7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(9*7)))
                                                            for row in self.ai_north_east7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==1):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(9*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+9))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_south_west=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-7))
                        for row in self.ai_south_west:
                           if  row[0]==1 :
                              self.ai_south_west2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*2)))
                              for row in self.ai_south_west:
                                 if  row[0]==1 :
                                    self.ai_south_west3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*3)))
                                    for row in self.ai_south_west3:
                                       if  row[0]==1 :
                                          self.ai_south_west4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*4)))
                                          for row in self.ai_south_west4:
                                             if  row[0]==1 :
                                                self.ai_south_west5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*5)))
                                                for row in self.ai_south_west5:
                                                   if  row[0]==1 :
                                                      self.ai_south_west6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*6)))
                                                      for row in self.ai_south_west6:
                                                         if  row[0]==1 :
                                                            self.ai_south_west7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case-(7*7)))
                                                            for row in self.ai_south_west7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==57):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-(7*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case-7))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
                        self.ai_south_east=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+7))
                        for row in self.ai_south_east:
                           if  row[0]==1 :
                              self.ai_south_east2=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*2)))
                              for row in self.ai_south_east2:
                                 if  row[0]==1 :
                                    self.ai_south_east3=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*3)))
                                    for row in self.ai_south_east3:
                                       if  row[0]==1 :
                                          self.ai_south_east4=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*4)))
                                          for row in self.ai_south_east4:
                                             if  row[0]==1 :
                                                self.ai_south_east5=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*5)))
                                                for row in self.ai_south_east5:
                                                   if  row[0]==1 :
                                                      self.ai_south_east6=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*6)))
                                                      for row in self.ai_south_east6:
                                                         if  row[0]==1 :
                                                            self.ai_south_east7=self.cursor.execute("""SELECT value,image FROM game WHERE rowid="""+str(self.id_case+(7*7)))
                                                            for row in self.ai_south_east7:
                                                               if  row[0]==2 :
                                                                  if (self.id_case==8):
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*6)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*5)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*4)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*3)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+(7*2)))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case+7))
                                                                     self.bdd.commit()
                                                                     self.cursor.execute(""" UPDATE game SET value=2,image='images/pion2.svg' WHERE rowid="""+str(self.id_case))
                                                                     self.bdd.commit()
                                                                     self.tour=1
                                                                     self.refresh_data()
            except:
               self.bdd.rollback()
               QMessageBox.information(self,"OTHELLO GAME","UNE ERREUR S'EST PRODUITE") 

   def refresh_data(self):
      if os.path.exists('othello.bd') and os.path.isfile('othello.bd'):
         try:
            self.bdd=sqlite3.connect('othello.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,"OTHELLO GAME",e)
         finally:
            self.cursor=self.bdd.cursor()
            #________LINE 1
            self.b1=self.cursor.execute("SELECT value,image FROM game WHERE rowid=1")          
            for row in self.b1:
               self.value1=row[0]
               if self.value1==1:
                  self.button_case[(0,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value1==2:
                  self.button_case[(0,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,0)].setIcon(QIcon(''))
                  self.button_case[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b2=self.cursor.execute("SELECT value,image FROM game WHERE rowid=2")        
            for row in self.b2:
               self.value2=row[0]
               if self.value2==1:
                  self.button_case[(0,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value2==2:
                  self.button_case[(0,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,1)].setIcon(QIcon(''))
                  self.button_case[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b3=self.cursor.execute("SELECT value,image FROM game WHERE rowid=3")               
            for row in self.b3:
               self.value3=row[0]
               if self.value3==1:
                  self.button_case[(0,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value3==2:
                  self.button_case[(0,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,2)].setIcon(QIcon(''))
                  self.button_case[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b4=self.cursor.execute("SELECT value,image FROM game WHERE rowid=4")               
            for row in self.b4:
               self.value4=row[0]
               if self.value4==1:
                  self.button_case[(0,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value4==2:
                  self.button_case[(0,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,3)].setIcon(QIcon(''))
                  self.button_case[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b5=self.cursor.execute("SELECT value,image FROM game WHERE rowid=5")               
            for row in self.b5:
               self.value5=row[0]
               if self.value5==1:
                  self.button_case[(0,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value5==2:
                  self.button_case[(0,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,4)].setIcon(QIcon(''))
                  self.button_case[(0,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b6=self.cursor.execute("SELECT value,image FROM game WHERE rowid=6")               
            for row in self.b6:
               self.value6=row[0]
               if self.value6==1:
                  self.button_case[(0,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value6==2:
                  self.button_case[(0,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,5)].setIcon(QIcon(''))
                  self.button_case[(0,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b7=self.cursor.execute("SELECT value,image FROM game WHERE rowid=7")               
            for row in self.b7:
               self.value7=row[0]
               if self.value7==1:
                  self.button_case[(0,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value7==2:
                  self.button_case[(0,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,6)].setIcon(QIcon(''))
                  self.button_case[(0,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b8=self.cursor.execute("SELECT value,image FROM game WHERE rowid=8")               
            for row in self.b8:
               self.value8=row[0]
               if self.value8==1:
                  self.button_case[(0,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(0,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value8==2:
                  self.button_case[(0,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(0,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(0,7)].setIcon(QIcon(''))
                  self.button_case[(0,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________LINE 2
            self.b9=self.cursor.execute("SELECT value,image FROM game WHERE rowid=9")               
            for row in self.b9:
               self.value9=row[0]
               if self.value9==1:
                  self.button_case[(1,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value9==2:
                  self.button_case[(1,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,0)].setIcon(QIcon(''))
                  self.button_case[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b10=self.cursor.execute("SELECT value,image FROM game WHERE rowid=10")               
            for row in self.b10:
               self.value10=row[0]
               if self.value10==1:
                  self.button_case[(1,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value10==2:
                  self.button_case[(1,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,1)].setIcon(QIcon(''))
                  self.button_case[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b11=self.cursor.execute("SELECT value,image FROM game WHERE rowid=11")               
            for row in self.b11:
               self.value11=row[0]
               if self.value11==1:
                  self.button_case[(1,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value11==2:
                  self.button_case[(1,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,2)].setIcon(QIcon(''))
                  self.button_case[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b12=self.cursor.execute("SELECT value,image FROM game WHERE rowid=12")               
            for row in self.b12:
               self.value12=row[0]
               if self.value12==1:
                  self.button_case[(1,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value12==2:
                  self.button_case[(1,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,3)].setIcon(QIcon(''))
                  self.button_case[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b13=self.cursor.execute("SELECT value,image FROM game WHERE rowid=13")               
            for row in self.b13:
               self.value13=row[0]
               if self.value13==1:
                  self.button_case[(1,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value13==2:
                  self.button_case[(1,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,4)].setIcon(QIcon(''))
                  self.button_case[(1,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b14=self.cursor.execute("SELECT value,image FROM game WHERE rowid=14")               
            for row in self.b14:
               self.value14=row[0]
               if self.value14==1:
                  self.button_case[(1,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value14==2:
                  self.button_case[(1,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,5)].setIcon(QIcon(''))
                  self.button_case[(1,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b15=self.cursor.execute("SELECT value,image FROM game WHERE rowid=15")               
            for row in self.b15:
               self.value15=row[0]
               if self.value15==1:
                  self.button_case[(1,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value15==2:
                  self.button_case[(1,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,6)].setIcon(QIcon(''))
                  self.button_case[(1,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b16=self.cursor.execute("SELECT value,image FROM game WHERE rowid=16")               
            for row in self.b16:
               self.value16=row[0]
               if self.value16==1:
                  self.button_case[(1,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(1,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value16==2:
                  self.button_case[(1,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(1,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(1,7)].setIcon(QIcon(''))
                  self.button_case[(1,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________PAGE 3
            self.b17=self.cursor.execute("SELECT value,image FROM game WHERE rowid=17")               
            for row in self.b17:
               self.value17=row[0]
               if self.value17==1:
                  self.button_case[(2,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value17==2:
                  self.button_case[(2,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,0)].setIcon(QIcon(''))
                  self.button_case[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b18=self.cursor.execute("SELECT value,image FROM game WHERE rowid=18")               
            for row in self.b18:
               self.value18=row[0]
               if self.value18==1:
                  self.button_case[(2,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value18==2:
                  self.button_case[(2,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,1)].setIcon(QIcon(''))
                  self.button_case[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b19=self.cursor.execute("SELECT value,image FROM game WHERE rowid=19")               
            for row in self.b19:
               self.value19=row[0]
               if self.value19==1:
                  self.button_case[(2,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value19==2:
                  self.button_case[(2,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,2)].setIcon(QIcon(''))
                  self.button_case[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b20=self.cursor.execute("SELECT value,image FROM game WHERE rowid=20")               
            for row in self.b20:
               self.value20=row[0]
               if self.value20==1:
                  self.button_case[(2,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value20==2:
                  self.button_case[(2,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,3)].setIcon(QIcon(''))
                  self.button_case[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b21=self.cursor.execute("SELECT value,image FROM game WHERE rowid=21")               
            for row in self.b21:
               self.value21=row[0]
               if self.value21==1:
                  self.button_case[(2,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value21==2:
                  self.button_case[(2,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,4)].setIcon(QIcon(''))
                  self.button_case[(2,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b22=self.cursor.execute("SELECT value,image FROM game WHERE rowid=22")               
            for row in self.b22:
               self.value22=row[0]
               if self.value22==1:
                  self.button_case[(2,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value22==2:
                  self.button_case[(2,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,5)].setIcon(QIcon(''))
                  self.button_case[(2,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b23=self.cursor.execute("SELECT value,image FROM game WHERE rowid=23")               
            for row in self.b23:
               self.value23=row[0]
               if self.value23==1:
                  self.button_case[(2,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value23==2:
                  self.button_case[(2,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,6)].setIcon(QIcon(''))
                  self.button_case[(2,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b24=self.cursor.execute("SELECT value,image FROM game WHERE rowid=24")               
            for row in self.b24:
               self.value24=row[0]
               if self.value24==1:
                  self.button_case[(2,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(2,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value24==2:
                  self.button_case[(2,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(2,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(2,7)].setIcon(QIcon(''))
                  self.button_case[(2,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________LINE 4
            self.b25=self.cursor.execute("SELECT value,image FROM game WHERE rowid=25")               
            for row in self.b25:
               self.value25=row[0]
               if self.value25==1:
                  self.button_case[(3,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value25==2:
                  self.button_case[(3,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,0)].setIcon(QIcon(''))
                  self.button_case[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b26=self.cursor.execute("SELECT value,image FROM game WHERE rowid=26")               
            for row in self.b26:
               self.value26=row[0]
               if self.value26==1:
                  self.button_case[(3,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value26==2:
                  self.button_case[(3,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,1)].setIcon(QIcon(''))
                  self.button_case[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b27=self.cursor.execute("SELECT value,image FROM game WHERE rowid=27")               
            for row in self.b27:
               self.value27=row[0]
               if self.value27==1:
                  self.button_case[(3,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value27==2:
                  self.button_case[(3,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,2)].setIcon(QIcon(''))
                  self.button_case[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b28=self.cursor.execute("SELECT value,image FROM game WHERE rowid=28")               
            for row in self.b28:
               self.value28=row[0]
               if self.value28==1:
                  self.button_case[(3,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value28==2:
                  self.button_case[(3,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,3)].setIcon(QIcon(''))
                  self.button_case[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b29=self.cursor.execute("SELECT value,image FROM game WHERE rowid=29")               
            for row in self.b29:
               self.value29=row[0]
               if self.value29==1:
                  self.button_case[(3,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value29==2:
                  self.button_case[(3,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,4)].setIcon(QIcon(''))
                  self.button_case[(3,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b30=self.cursor.execute("SELECT value,image FROM game WHERE rowid=30")               
            for row in self.b30:
               self.value30=row[0]
               if self.value30==1:
                  self.button_case[(3,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value30==2:
                  self.button_case[(3,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,5)].setIcon(QIcon(''))
                  self.button_case[(3,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b31=self.cursor.execute("SELECT value,image FROM game WHERE rowid=31")               
            for row in self.b31:
               self.value31=row[0]
               if self.value31==1:
                  self.button_case[(3,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value31==2:
                  self.button_case[(3,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,6)].setIcon(QIcon(''))
                  self.button_case[(3,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b32=self.cursor.execute("SELECT value,image FROM game WHERE rowid=32")               
            for row in self.b32:
               self.value32=row[0]
               if self.value32==1:
                  self.button_case[(3,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(3,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value32==2:
                  self.button_case[(3,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(3,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(3,7)].setIcon(QIcon(''))
                  self.button_case[(3,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________PAGE 5
            self.b33=self.cursor.execute("SELECT value,image FROM game WHERE rowid=33")               
            for row in self.b33:
               self.value33=row[0]
               if self.value33==1:
                  self.button_case[(4,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value33==2:
                  self.button_case[(4,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,0)].setIcon(QIcon(''))
                  self.button_case[(4,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b34=self.cursor.execute("SELECT value,image FROM game WHERE rowid=34")               
            for row in self.b34:
               self.value34=row[0]
               if self.value34==1:
                  self.button_case[(4,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value34==2:
                  self.button_case[(4,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,1)].setIcon(QIcon(''))
                  self.button_case[(4,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b35=self.cursor.execute("SELECT value,image FROM game WHERE rowid=35")               
            for row in self.b35:
               self.value35=row[0]
               if self.value35==1:
                  self.button_case[(4,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value35==2:
                  self.button_case[(4,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,2)].setIcon(QIcon(''))
                  self.button_case[(4,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b36=self.cursor.execute("SELECT value,image FROM game WHERE rowid=36")               
            for row in self.b36:
               self.value36=row[0]
               if self.value36==1:
                  self.button_case[(4,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value36==2:
                  self.button_case[(4,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,3)].setIcon(QIcon(''))
                  self.button_case[(4,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b37=self.cursor.execute("SELECT value,image FROM game WHERE rowid=37")               
            for row in self.b37:
               self.value37=row[0]
               if self.value37==1:
                  self.button_case[(4,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value37==2:
                  self.button_case[(4,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,4)].setIcon(QIcon(''))
                  self.button_case[(4,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b38=self.cursor.execute("SELECT value,image FROM game WHERE rowid=38")               
            for row in self.b38:
               self.value38=row[0]
               if self.value38==1:
                  self.button_case[(4,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value38==2:
                  self.button_case[(4,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,5)].setIcon(QIcon(''))
                  self.button_case[(4,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b39=self.cursor.execute("SELECT value,image FROM game WHERE rowid=39")               
            for row in self.b39:
               self.value39=row[0]
               if self.value39==1:
                  self.button_case[(4,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value39==2:
                  self.button_case[(4,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,6)].setIcon(QIcon(''))
                  self.button_case[(4,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b40=self.cursor.execute("SELECT value,image FROM game WHERE rowid=40")               
            for row in self.b40:
               self.value40=row[0]
               if self.value40==1:
                  self.button_case[(4,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(4,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value40==2:
                  self.button_case[(4,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(4,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(4,7)].setIcon(QIcon(''))
                  self.button_case[(4,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________LINE 6
            self.b41=self.cursor.execute("SELECT value,image FROM game WHERE rowid=41")               
            for row in self.b41:
               self.value41=row[0]
               if self.value41==1:
                  self.button_case[(5,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value41==2:
                  self.button_case[(5,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,0)].setIcon(QIcon(''))
                  self.button_case[(5,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b42=self.cursor.execute("SELECT value,image FROM game WHERE rowid=42")               
            for row in self.b42:
               self.value42=row[0]
               if self.value42==1:
                  self.button_case[(5,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value42==2:
                  self.button_case[(5,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,1)].setIcon(QIcon(''))
                  self.button_case[(5,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b43=self.cursor.execute("SELECT value,image FROM game WHERE rowid=43")               
            for row in self.b43:
               self.value43=row[0]
               if self.value43==1:
                  self.button_case[(5,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value43==2:
                  self.button_case[(5,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,2)].setIcon(QIcon(''))
                  self.button_case[(5,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b44=self.cursor.execute("SELECT value,image FROM game WHERE rowid=44")               
            for row in self.b44:
               self.value44=row[0]
               if self.value44==1:
                  self.button_case[(5,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value44==2:
                  self.button_case[(5,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,3)].setIcon(QIcon(''))
                  self.button_case[(5,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b45=self.cursor.execute("SELECT value,image FROM game WHERE rowid=45")               
            for row in self.b45:
               self.value45=row[0]
               if self.value45==1:
                  self.button_case[(5,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value45==2:
                  self.button_case[(5,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,4)].setIcon(QIcon(''))
                  self.button_case[(5,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b46=self.cursor.execute("SELECT value,image FROM game WHERE rowid=46")               
            for row in self.b46:
               self.value46=row[0]
               if self.value46==1:
                  self.button_case[(5,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value46==2:
                  self.button_case[(5,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,5)].setIcon(QIcon(''))
                  self.button_case[(5,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b47=self.cursor.execute("SELECT value,image FROM game WHERE rowid=47")               
            for row in self.b47:
               self.value47=row[0]
               if self.value47==1:
                  self.button_case[(5,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value47==2:
                  self.button_case[(5,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,6)].setIcon(QIcon(''))
                  self.button_case[(5,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b48=self.cursor.execute("SELECT value,image FROM game WHERE rowid=48")               
            for row in self.b48:
               self.value48=row[0]
               if self.value48==1:
                  self.button_case[(5,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(5,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value48==2:
                  self.button_case[(5,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(5,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(5,7)].setIcon(QIcon(''))
                  self.button_case[(5,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________PAGE 7
            self.b49=self.cursor.execute("SELECT value,image FROM game WHERE rowid=49")               
            for row in self.b49:
               self.value49=row[0]
               if self.value49==1:
                  self.button_case[(6,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value49==2:
                  self.button_case[(6,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,0)].setIcon(QIcon(''))
                  self.button_case[(6,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b50=self.cursor.execute("SELECT value,image FROM game WHERE rowid=50")           
            for row in self.b50:
               self.value50=row[0]
               if self.value50==1:
                  self.button_case[(6,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value50==2:
                  self.button_case[(6,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,1)].setIcon(QIcon(''))
                  self.button_case[(6,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b51=self.cursor.execute("SELECT value,image FROM game WHERE rowid=51")               
            for row in self.b51:
               self.value51=row[0]
               if self.value51==1:
                  self.button_case[(6,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value51==2:
                  self.button_case[(6,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,2)].setIcon(QIcon(''))
                  self.button_case[(6,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b52=self.cursor.execute("SELECT value,image FROM game WHERE rowid=52")               
            for row in self.b52:
               self.value52=row[0]
               if self.value52==1:
                  self.button_case[(6,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value52==2:
                  self.button_case[(6,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,3)].setIcon(QIcon(''))
                  self.button_case[(6,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b53=self.cursor.execute("SELECT value,image FROM game WHERE rowid=53")               
            for row in self.b53:
               self.value53=row[0]
               if self.value53==1:
                  self.button_case[(6,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value53==2:
                  self.button_case[(6,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,4)].setIcon(QIcon(''))
                  self.button_case[(6,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b54=self.cursor.execute("SELECT value,image FROM game WHERE rowid=54")               
            for row in self.b54:
               self.value54=row[0]
               if self.value54==1:
                  self.button_case[(6,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value54==2:
                  self.button_case[(6,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,5)].setIcon(QIcon(''))
                  self.button_case[(6,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b55=self.cursor.execute("SELECT value,image FROM game WHERE rowid=55")               
            for row in self.b55:
               self.value55=row[0]
               if self.value55==1:
                  self.button_case[(6,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value55==2:
                  self.button_case[(6,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,6)].setIcon(QIcon(''))
                  self.button_case[(6,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b56=self.cursor.execute("SELECT value,image FROM game WHERE rowid=56")               
            for row in self.b56:
               self.value56=row[0]
               if self.value56==1:
                  self.button_case[(6,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(6,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value56==2:
                  self.button_case[(6,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(6,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(6,7)].setIcon(QIcon(''))
                  self.button_case[(6,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            #________LINE 8
            self.b57=self.cursor.execute("SELECT value,image FROM game WHERE rowid=57")               
            for row in self.b57:
               self.value57=row[0]
               if self.value57==1:
                  self.button_case[(7,0)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value57==2:
                  self.button_case[(7,0)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,0)].setIcon(QIcon(''))
                  self.button_case[(7,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b58=self.cursor.execute("SELECT value,image FROM game WHERE rowid=58")               
            for row in self.b58:
               self.value58=row[0]
               if self.value58==1:
                  self.button_case[(7,1)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value58==2:
                  self.button_case[(7,1)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,1)].setIcon(QIcon(''))
                  self.button_case[(7,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b59=self.cursor.execute("SELECT value,image FROM game WHERE rowid=59")               
            for row in self.b59:
               self.value59=row[0]
               if self.value59==1:
                  self.button_case[(7,2)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value59==2:
                  self.button_case[(7,2)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,2)].setIcon(QIcon(''))
                  self.button_case[(7,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b60=self.cursor.execute("SELECT value,image FROM game WHERE rowid=60")               
            for row in self.b60:
               self.value60=row[0]
               if self.value60==1:
                  self.button_case[(7,3)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value60==2:
                  self.button_case[(7,3)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,3)].setIcon(QIcon(''))
                  self.button_case[(7,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b61=self.cursor.execute("SELECT value,image FROM game WHERE rowid=61")               
            for row in self.b61:
               self.value61=row[0]
               if self.value61==1:
                  self.button_case[(7,4)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value61==2:
                  self.button_case[(7,4)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,4)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,4)].setIcon(QIcon(''))
                  self.button_case[(7,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b62=self.cursor.execute("SELECT value,image FROM game WHERE rowid=62")               
            for row in self.b62:
               self.value62=row[0]
               if self.value62==1:
                  self.button_case[(7,5)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value62==2:
                  self.button_case[(7,5)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,5)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,5)].setIcon(QIcon(''))
                  self.button_case[(7,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b63=self.cursor.execute("SELECT value,image FROM game WHERE rowid=63")               
            for row in self.b63:
               self.value63=row[0]
               if self.value63==1:
                  self.button_case[(7,6)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value63==2:
                  self.button_case[(7,6)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,6)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,6)].setIcon(QIcon(''))
                  self.button_case[(7,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            self.b64=self.cursor.execute("SELECT value,image FROM game WHERE rowid=64")               
            for row in self.b64:
               self.value64=row[0]
               if self.value64==1:
                  self.button_case[(7,7)].setIcon(QIcon(self.pion1))
                  self.button_case[(7,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               elif self.value64==2:
                  self.button_case[(7,7)].setIcon(QIcon(self.pion2))
                  self.button_case[(7,7)].setIconSize(QSize(self.icon_size,self.icon_size))
               else:
                  self.button_case[(7,7)].setIcon(QIcon(''))
                  self.button_case[(7,7)].setIconSize(QSize(self.icon_size,self.icon_size))

            self.board=[[self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,self.value7,self.value8],
                          [self.value9,self.value10,self.value11,self.value12,self.value13,self.value14,self.value15,self.value16],
                          [self.value17,self.value18,self.value19,self.value20,self.value21,self.value22,self.value23,self.value24],
                          [self.value25,self.value26,self.value27,self.value28,self.value29,self.value30,self.value31,self.value32],
                          [self.value33,self.value34,self.value35,self.value36,self.value37,self.value38,self.value39,self.value40],
                          [self.value41,self.value42,self.value43,self.value44,self.value45,self.value46,self.value47,self.value48],
                          [self.value49,self.value50,self.value51,self.value52,self.value53,self.value54,self.value55,self.value56],
                          [self.value57,self.value58,self.value59,self.value60,self.value61,self.value62,self.value63,self.value64]]

            
            self.score1=self.cursor.execute("SELECT COUNT(*) FROM game WHERE value=2")               
            for row in self.score1:
               self.lab_score1.setText(str(row[0]))

            self.score2=self.cursor.execute("SELECT COUNT(*) FROM game WHERE value=1")               
            for row in self.score2:
               self.lab_score2.setText(str(row[0]))

            self.congrat=self.cursor.execute("SELECT COUNT(*) FROM game WHERE value=0")               
            for row in self.congrat:
               if row[0]==0:
                  if int(self.lab_score2.text())>int(self.lab_score1.text()):
                     QMessageBox.information(self,"OTHELLO GAME","JOUEUR 2 A GAGNE")
                     self.question=QMessageBox.question(self,"OTHELLO GAME",'VOULEZ VOUS RECOMMENCER ?',QMessageBox.Yes,QMessageBox.No)
                     if self.question==QMessageBox.Yes:
                        self.reset()
                  elif int(self.lab_score1.text())>int(self.lab_score2.text()):
                     QMessageBox.information(self,"OTHELLO GAME","JOUEUR 1 A GAGNE")
                     self.question=QMessageBox.question(self,"OTHELLO GAME",'VOULEZ VOUS RECOMMENCER ?',QMessageBox.Yes,QMessageBox.No)
                     if self.question==QMessageBox.Yes:
                        self.reset()
                     

            if self.tour==0:
               self.frame_tour.move(950,180)
               self.frame_tour.setStyleSheet("""background-color:transparent;border-style:solid;
                                  border-width:5px;border-color:#7700ff;border-radius:15px """)
               self.hover_color='#fff'

            elif self.tour==1:
               self.frame_tour.move(950,480)
               self.frame_tour.setStyleSheet("""background-color:transparent;border-style:solid;
                                  border-width:5px;border-color:#ff0000;border-radius:15px """)
               self.hover_color='#111'  
            self.Design()

   def reset(self):
      if os.path.exists('othello.bd') and os.path.isfile('othello.bd'):
         try:
            self.bdd=sqlite3.connect('othello.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,"OTHELLO GAME",e)
         finally:
            self.question=QMessageBox.question(self,"OTHELLO GAME",'CONTINUER ?',QMessageBox.Yes,QMessageBox.No)
            if self.question==QMessageBox.Yes:
               self.cursor=self.bdd.cursor()
               
               record_game=[ (1,0,""), (2,0,""), (3,0,""), (4,0,""), (5,0,""), (6,0,""), (7,0,""), (8,0,""),
                    (9,0,""), (10,0,""), (11,0,""), (12,0,""), (13,0,""), (14,0,""), (15,0,""), (16,0,""),
                    (17,0,""), (18,0,""), (19,0,""), (20,0,""), (21,0,""), (22,0,""), (23,0,""), (24,0,""),
                    (25,0,""), (26,0,""), (27,0,""), (28,1,'images/pion1.svg'), (29,2,'images/pion2.svg'), (30,0,""), (31,0,""), (32,0,""),
                    (33,0,""), (34,0,""), (35,0,""), (36,2,'images/pion2.svg'), (37,1,'images/pion1.svg'), (38,0,""), (39,0,""), (40,0,""),
                    (41,0,""), (42,0,""), (43,0,""), (44,0,""), (45,0,""), (46,0,""), (47,0,""), (48,0,""),
                    (49,0,""), (50,0,""), (51,0,""), (52,0,""), (53,0,""), (54,0,""), (55,0,""), (56,0,""),
                    (57,0,""), (58,0,""), (59,0,""), (60,0,""), (61,0,""), (62,0,""), (63,0,""), (64,0,"") ]

               self.cursor.execute("""DELETE FROM game""")
               self.cursor.executemany("""INSERT INTO game (id,value,image) VALUES (?,?,?)""",record_game)
               self.bdd.commit()
               self.refresh_data()
               self.tour=0
               QMessageBox.information(self,"OTHELLO GAME","JEUX REINITIALISE")
               self.question=QMessageBox.question(self,"OTHELLO GAME",'VOULEZ VOUS COMMENCER LE PREMIER ?',QMessageBox.Yes,QMessageBox.No)
               if self.question==QMessageBox.Yes:
                  self.tour=0
                  self.refresh_data()
               else:
                  self.tour=1
                  self.refresh_data()
               

      
if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('plastique')
   screen=OTHELLO() 
   screen.show()
   sys.exit(app.exec_())
