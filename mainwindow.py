import sys
from os.path import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import main


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle('StatsViewer')
        self.setMinimumSize(350, 150)
        self.setCentralWidget(TabWidget(self))

        # self.show()


class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.characters = ["---Small---", "Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy",
                           "Toad", "Toadette", "Koopa Troopa", "Dry Bones", "Small Mii", "---Medium---",
                           "Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Birdo", "Diddy Kong", "Bowser Jr.",
                           "Medium Mii", "---Large---", "Wario", "Waluigi", "Donkey Kong", "Bowser", "King Boo",
                           "Rosalina", "Funky Kong", "Dry Bowser", "Large Mii"]

        self.character_icons = ['', 'icons/bmr.png', 'icons/blg.png', 'icons/bpc.png', 'icons/bds.png', 'icons/ko.png',
                                'icons/kk.png', 'icons/nk.png', 'icons/ka.png', 'icons/mii.png', '', 'icons/mr.png',
                                'icons/lg.png', 'icons/pc.png', 'icons/ds.png', 'icons/ys.png', 'icons/ca.png',
                                'icons/dd.png', 'icons/jr.png', 'icons/mii.png', '', 'icons/wr.png', 'icons/wl.png',
                                'icons/dk.png', 'icons/kp.png', 'icons/kt.png', 'icons/rs.png', 'icons/fk.png',
                                'icons/bk.png', 'icons/mii.png']

        self.vehicles = ["---Small---", "Standard Kart S", "Baby Booster", "Mini Beast", "Cheep Charger",
                         "Tiny Titan", "Blue Falcon", "Standard Bike S", "Bullet Bike", "Bit Bike", "Quacker",
                         "Magikruiser", "Jet Bubble", "---Medium---", "Standard Kart M", "Classic Dragster",
                         "Wild Wing", "Super Blooper", "Daytripper", "Sprinter", "Standard Bike M", "Mach Bike",
                         "Sugarscoot", "Zip Zip", "Sneakster", "Dolphin Dasher", "---Large---", "Standard Kart L",
                         "Offroader", "Flame Flyer", "Piranha Prowler", "Jetsetter", "Honeycoupe", "Standard Bike L",
                         "Flame Runner", "Wario Bike", "Shooting Star", "Spear", "Phantom"]

        self.vehicle_icons = ['', 'icons/sdf_kart.png', 'icons/sa_kart.png', 'icons/sb_kart.png', 'icons/sc_kart.png',
                              'icons/sd_kart.png', 'icons/se_kart.png', 'icons/sdf_bike.png', 'icons/sa_bike.png',
                              'icons/sb_bike.png', 'icons/sc_bike.png', 'icons/sd_bike.png', 'icons/se_bike.png', '',
                              'icons/mdf_kart.png', 'icons/ma_kart.png', 'icons/mb_kart.png', 'icons/mc_kart.png',
                              'icons/md_kart.png', 'icons/me_kart.png', 'icons/mdf_bike.png', 'icons/ma_bike.png',
                              'icons/mb_bike.png', 'icons/mc_bike.png', 'icons/md_bike.png', 'icons/me_bike.png', '',
                              'icons/ldf_kart.png', 'icons/la_kart.png', 'icons/lb_kart.png', 'icons/lc_kart.png',
                              'icons/ld_kart.png', 'icons/le_kart.png', 'icons/ldf_bike.png', 'icons/la_bike.png',
                              'icons/lb_bike.png', 'icons/lc_bike.png', 'icons/ld_bike.png', 'icons/le_bike.png']

        style = """QTabWidget::tab-bar{
                alignment: left;
                }"""
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.writetab = QWidget()
        self.comparetab = QWidget()
        self.previewtab = QWidget()
        self.acceltab = QWidget()
        self.itemtab = QWidget()
        self.tabs.resize(300, 200)
  
        # Add tabs
        self.tabs.addTab(self.writetab, "Write")
        self.tabs.addTab(self.comparetab, "Compare")
        self.tabs.addTab(self.itemtab, "Items")
        self.tabs.addTab(self.acceltab, "Graph")
        self.tabs.addTab(self.previewtab, "Preview")
  
        # Create write tab
        self.writetab.layout = QGridLayout(self)
        self.lw = QLabel()
        self.lw.setText("This is the edit tab")

        # Need these Defined now
        self.editScroll = QScrollArea(self)
        self.editWidget = QWidget(self)
        self.editWidget.layout = QGridLayout(self)
        self.driverselect = QComboBox(self)
        self.kartselect = QComboBox(self)

        for entry in range(0, len(self.characters)):
            if self.character_icons[entry] != '':
                if exists(self.character_icons[entry]):
                    icon = QIcon(self.character_icons[entry])
                    self.driverselect.addItem(icon, self.characters[entry])
                else:
                    self.driverselect.addItem(self.characters[entry])
            else:
                self.driverselect.addItem(self.characters[entry])

        self.driverselect.setCurrentIndex(1)

        for entry in range(0, len(self.vehicles)):
            if self.vehicle_icons[entry] != '':
                if exists(self.vehicle_icons[entry]):
                    icon = QIcon(self.vehicle_icons[entry])
                    self.kartselect.addItem(icon, self.vehicles[entry])
                else:
                    self.kartselect.addItem(self.vehicles[entry])
            else:
                self.kartselect.addItem(self.vehicles[entry])

        self.kartselect.setCurrentIndex(1)

        self.lastselecteddriver = self.driverselect.currentIndex()
        self.lastselectedkart = self.driverselect.currentIndex()

        font = QFont("Arial", 15, QFont.Bold)

        item = self.driverselect.model()
        item.item(0, 0).setFont(font)
        item.item(10, 0).setFont(font)
        item.item(20, 0).setFont(font)
        item = self.kartselect.model()
        item.item(0, 0).setFont(font)
        item.item(13, 0).setFont(font)
        item.item(26, 0).setFont(font)

        self.paramselect = QComboBox(self)
        self.paramselect.addItems(["Kart", "Driver"])
        self.paramselect.currentTextChanged.connect(lambda: self.setEditWindow())
        self.driverselect.currentTextChanged.connect(lambda: self.canBeSelected())
        self.kartselect.currentTextChanged.connect(lambda: self.canBeSelected())
        self.editScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.editScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.editScroll.setWidgetResizable(True)
        self.editScroll.setWidget(self.editWidget)
        self.editWidget.setLayout(self.editWidget.layout)
        self.editWidget.layout.addWidget(self.lw, 1, 1)

        #self.writetab.layout.addWidget(self.lw, 3, 2)
        self.writetab.layout.addWidget(self.paramselect, 1, 1)
        self.writetab.layout.addWidget(self.kartselect, 2, 1)
        self.writetab.layout.addWidget(self.driverselect, 2, 1)
        self.writetab.layout.addWidget(self.editScroll, 3, 1)
        self.editWidget.layout.addWidget(self.lw, 1, 1)
        self.writetab.setLayout(self.writetab.layout)
        self.driverselect.hide()

        # Create compare tab
        self.comparetab.layout = QVBoxLayout(self)
        self.lc = QLabel()
        self.lc.setText("This is the Compare tab")
        self.comparetab.layout.addWidget(self.lc)
        self.comparetab.setLayout(self.comparetab.layout)

        # Create preview tab
        self.previewtab.layout = QVBoxLayout(self)
        self.lp = QLabel()
        self.lp.setText("This is the Preview tab")
        self.previewtab.layout.addWidget(self.lp)
        self.previewtab.setLayout(self.previewtab.layout)

        # Create acceleration graph tab
        self.acceltab.layout = QVBoxLayout(self)
        self.la = QLabel()
        self.la.setText("This is the Graph tab")
        self.acceltab.layout.addWidget(self.la)
        self.acceltab.setLayout(self.acceltab.layout)

        # Create item tab (ItemSlot.bin support)
        self.itemtab.layout = QVBoxLayout(self)
        self.li = QLabel()
        self.li.setText("This is the Item tab")
        self.itemtab.layout.addWidget(self.li)
        self.itemtab.setLayout(self.itemtab.layout)
  
        self.setStyleSheet(style)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def setEditWindow(self):
        index = self.paramselect.currentIndex()
        if index == 0:
            self.driverselect.hide()
            self.kartselect.show()
        else:
            self.kartselect.hide()
            self.driverselect.show()

    def canBeSelected(self):
        self.unselectable = ["---Small---", "---Medium---", "---Large---"]
        if not(self.driverselect.currentText() in self.unselectable):
            self.lastselecteddriver = self.driverselect.currentIndex()
        else:
            self.driverselect.setCurrentIndex(self.lastselecteddriver)
        if not(self.kartselect.currentText() in self.unselectable):
            self.lastselectedkart = self.kartselect.currentIndex()
        else:
            self.kartselect.setCurrentIndex(self.lastselectedkart)

