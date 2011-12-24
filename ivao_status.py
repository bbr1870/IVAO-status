#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2011 by Antonio (emper0r) Peña Diaz <emperor.cu@gmail.com>
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
# IVAO-status :: License GPLv3+

import sys

try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtWebKit import *
    from PyQt4.Qt import *
except:
    print ('\nYou have not installed the packages Qt Modules for Python,\n')
    print ('please run command as root:  aptitude install python-qt4\n')
    print ('with all dependencies.\n\n')
    sys.exit(2)

import distance
import MainWindow_UI
import PilotInfo_UI
import ControllerInfo_UI
import SettingWindow_UI
import FollowMeCarService_UI
import urllib2

try:
    import sqlite3
except:
    print ('\nYou have not installed SQLite3 module for Python,\n')
    print ('please run command as root: aptitude install sqlite3 libsqlite3-0\n')
    sys.exit(2)

from BeautifulSoup import BeautifulSoup
import os
import datetime
import ConfigParser
import time

__version__ = '1.0.3'
url = 'http://de1.www.ivao.aero/'
scheduling_atc = 'http://www.ivao.aero/atcss/list.asp'
scheduling_flights = 'http://www.ivao.aero/flightss/list.asp'

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainWindow_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'ivao_status_splash.png')
        self.setWindowIcon(QIcon(image_icon))
        self.ui.PILOT_FullList.setColumnWidth(0, 90)
        self.ui.PILOT_FullList.setColumnWidth(1, 65)
        self.ui.PILOT_FullList.setColumnWidth(2, 60)
        self.ui.PILOT_FullList.setColumnWidth(3, 170)
        self.ui.PILOT_FullList.setColumnWidth(4, 160)
        self.ui.PILOT_FullList.setColumnWidth(5, 105)
        self.ui.PILOT_FullList.setColumnWidth(6, 70)
        self.ui.PILOT_FullList.setColumnWidth(7, 80)
        self.ui.PILOT_FullList.setColumnWidth(8, 92)
        self.ui.PilottableWidget.setColumnWidth(0, 90)
        self.ui.PilottableWidget.setColumnWidth(1, 65)
        self.ui.PilottableWidget.setColumnWidth(2, 60)
        self.ui.PilottableWidget.setColumnWidth(3, 180)
        self.ui.PilottableWidget.setColumnWidth(4, 160)
        self.ui.PilottableWidget.setColumnWidth(5, 105)
        self.ui.PilottableWidget.setColumnWidth(6, 70)
        self.ui.PilottableWidget.setColumnWidth(7, 80)
        self.ui.PilottableWidget.setColumnWidth(8, 65)
        self.ui.ATC_FullList.setColumnWidth(1, 70)
        self.ui.ATC_FullList.setColumnWidth(2, 37)
        self.ui.ATC_FullList.setColumnWidth(3, 180)
        self.ui.ATC_FullList.setColumnWidth(4, 70)
        self.ui.ATC_FullList.setColumnWidth(5, 128)
        self.ui.ATC_FullList.setColumnWidth(8, 40)
        self.ui.ATCtableWidget.setColumnWidth(1, 70)
        self.ui.ATCtableWidget.setColumnWidth(2, 60)
        self.ui.ATCtableWidget.setColumnWidth(3, 240)
        self.ui.ATCtableWidget.setColumnWidth(4, 110)
        self.ui.ATCtableWidget.setColumnWidth(5, 108)
        self.ui.ATCtableWidget.setColumnWidth(6, 110)
        self.ui.SearchtableWidget.setColumnWidth(0, 50)
        self.ui.SearchtableWidget.setColumnWidth(1, 100)
        self.ui.SearchtableWidget.setColumnWidth(2, 170)
        self.ui.FriendstableWidget.setColumnWidth(0, 50)
        self.ui.FriendstableWidget.setColumnWidth(1, 290)
        self.ui.FriendstableWidget.setColumnWidth(2, 105)
        self.ui.dbTableWidget_1.setColumnWidth(0, 30)
        self.ui.dbTableWidget_2.setColumnWidth(0, 45)
        self.ui.dbTableWidget_2.setColumnWidth(1, 80)
        self.ui.dbTableWidget_2.setColumnWidth(2, 80)
        self.ui.dbTableWidget_2.setColumnWidth(3, 140)
        self.ui.InboundTableWidget.setColumnWidth(0, 90)
        self.ui.InboundTableWidget.setColumnWidth(1, 34)
        self.ui.InboundTableWidget.setColumnWidth(2, 120)
        self.ui.InboundTableWidget.setColumnWidth(3, 30)
        self.ui.InboundTableWidget.setColumnWidth(4, 120)
        self.ui.OutboundTableWidget.setColumnWidth(0, 90)
        self.ui.OutboundTableWidget.setColumnWidth(1, 34)
        self.ui.OutboundTableWidget.setColumnWidth(2, 120)
        self.ui.OutboundTableWidget.setColumnWidth(3, 30)
        self.ui.OutboundTableWidget.setColumnWidth(4, 120)
        self.ui.Statistics.setColumnWidth(0, 30)
        self.ui.Statistics.setColumnWidth(1, 500)
        self.ui.Statistics.setColumnWidth(2, 100)
        self.ui.Statistics.setColumnWidth(3, 100)
        self.ui.SchedulingATC.setColumnWidth(0, 30)
        self.ui.SchedulingATC.setColumnWidth(1, 90)
        self.ui.SchedulingATC.setColumnWidth(2, 150)
        self.ui.SchedulingATC.setColumnWidth(3, 70)
        self.ui.SchedulingATC.setColumnWidth(4, 180)
        self.ui.SchedulingATC.setColumnWidth(5, 180)
        self.ui.SchedulingATC.setColumnWidth(6, 60)
        self.ui.SchedulingATC.setColumnWidth(7, 60)
        self.ui.SchedulingATC.setColumnWidth(8, 50)
        self.ui.SchedulingATC.setColumnWidth(9, 115)
        self.ui.SchedulingFlights.setColumnWidth(0, 90)
        self.ui.SchedulingFlights.setColumnWidth(1, 60)
        self.ui.SchedulingFlights.setColumnWidth(2, 175)
        self.ui.SchedulingFlights.setColumnWidth(3, 60)
        self.ui.SchedulingFlights.setColumnWidth(4, 30)
        self.ui.SchedulingFlights.setColumnWidth(5, 65)
        self.ui.SchedulingFlights.setColumnWidth(6, 180)
        self.ui.SchedulingFlights.setColumnWidth(7, 30)
        self.ui.SchedulingFlights.setColumnWidth(8, 70)
        self.ui.SchedulingFlights.setColumnWidth(9, 180)
        self.ui.SchedulingFlights.setColumnWidth(10, 55)
        self.ui.SchedulingFlights.setColumnWidth(11, 95)
        self.ui.SchedulingFlights.setColumnWidth(12, 150)
        self.ui.SchedulingFlights.setColumnWidth(13, 40)
        self.ui.SchedulingFlights.setColumnWidth(14, 50)
        self.ui.SchedulingFlights.setColumnWidth(15, 150)
        self.ui.network_table.setColumnWidth(0, 60)
        self.ui.network_table.setColumnWidth(1, 120)
        self.ui.network_table.setColumnWidth(2, 250)
        self.ui.network_table.setColumnWidth(3, 210)
        self.ui.network_table.setColumnWidth(4, 65)
        self.ui.network_table.setColumnWidth(5, 70)
        self.ui.network_table.setColumnWidth(6, 70)
        self.ui.network_table.setColumnWidth(7, 60)
        self.ui.PILOT_FullList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.ATC_FullList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.FriendstableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.PilottableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.ATCtableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.SearchtableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.METARtableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.OutboundTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.InboundTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.IVAOStatustableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.SearchtableWidget.selectionModel().selectedRows()
        self.ui.SearchtableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.ATC_FullList.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.PILOT_FullList.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.ATCtableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.PilottableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.FriendstableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.showInfo_Action = QAction("Show Info", self)
        self.showMap_Action = QAction("Show at Map", self)
        self.showDelete_Action = QAction("Delete Friend", self)
        self.ui.SearchtableWidget.addAction(self.showInfo_Action)
        self.ui.SearchtableWidget.addAction(self.showMap_Action)
        self.ui.ATC_FullList.addAction(self.showInfo_Action)
        self.ui.ATC_FullList.addAction(self.showMap_Action)
        self.ui.PILOT_FullList.addAction(self.showInfo_Action)
        self.ui.PILOT_FullList.addAction(self.showMap_Action)
        self.ui.ATCtableWidget.addAction(self.showInfo_Action)
        self.ui.ATCtableWidget.addAction(self.showMap_Action)
        self.ui.PilottableWidget.addAction(self.showInfo_Action)
        self.ui.PilottableWidget.addAction(self.showMap_Action)
        self.ui.FriendstableWidget.addAction(self.showInfo_Action)
        self.ui.FriendstableWidget.addAction(self.showMap_Action)
        self.ui.FriendstableWidget.addAction(self.showDelete_Action)
        self.showInfo_Action.triggered.connect(self.action_click)
        self.showMap_Action.triggered.connect(self.action_click)
        self.showDelete_Action.triggered.connect(self.action_click)
        image_departure = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'departures.png')
        Pixmap = QPixmap(image_departure)
        self.ui.departures_icon.setPixmap(Pixmap)
        self.ui.departures_icon.show()
        image_arrivals = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'arrivals.png')
        Pixmap = QPixmap(image_arrivals)
        self.ui.arrivals_icon.setPixmap(Pixmap)
        self.ui.arrivals_icon.show()
        QTimer.singleShot(1000, self.initial_load)
        self.progress = QProgressBar()
        self.statusBar().addPermanentWidget(self.progress)
        self.progress.hide()
        self.progress.setValue(0)
        self._maptab = None
        self.rating_pilot = {"0":"OBS - Observer", "2":"SFO - Second Flight Officer", "3":"FFO - First Flight Officer" \
                , "4":"C - Captain", "5":"FC - Flight Captain", "6":"SC - Senior Captain" \
                , "7":"SFC - Senior Flight Captain", "8":"CC - Commercial Captain" \
                , "9":"CFC - Commercial Flight Captain", "10":"CSC - Commercial Senior Captain" \
                , "11":"SUP - Supervisor", "12":"ADM - Administrator"}

        self.rating_atc = {"0":"OBS - Observer", "2":"S1 - Student 1", "3":"S2 - Student 2" \
                      , "4":"S3 - Student 3", "5":"C1 - Controller 1", "6":"C2 - Controller 2" \
                      , "7":"C3 - Controller 3", "8":"I1 - Instructor 1", "9":"I2 - Instructor 2" \
                      , "10":"I3 - Instructor 3", "11":"SUP - Supervisor", "12":"ADM - Administrator"}

        self.position_atc = {"0":"Observer", "1":"Flight Service Station", "2":"Clearance Delivery" \
                        , "3":"Ground", "4":"Tower", "5":"Approach", "6":"Center", "7":"Departure"}

        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        if os.path.exists(config_file):
            config.read(config_file)
            self.timer = QTimer(self)
            self.timer.setInterval(config.getint('Time_Update', 'time'))
            self.timer.timeout.connect(self.connect)
            self.timer.start()
        else:
            config.add_section('Settings')
            config.set('Settings', 'use_proxy', '0')
            config.set('Settings', 'host', '')
            config.set('Settings', 'port', '')
            config.set('Settings', 'auth', '0')
            config.set('Settings', 'user', '')
            config.set('Settings', 'pass', '')
            config.add_section('Info')
            config.set('Info', 'data_access', 'whazzup.txt')
            config.set('Info', 'url', url)
            config.set('Info', 'scheduling_atc', scheduling_atc)
            config.set('Info', 'scheduling_flights', scheduling_flights)
            config.add_section('Database')
            config.set('Database', 'db', 'ivao.db')
            config.add_section('Time_Update')
            config.set('Time_Update', 'time', '300000')
            config.add_section('Map')
            config.set('Map', 'auto_refresh', '0')
            config.set('Map', 'label_Pilots', '0')
            config.set('Map', 'label_ATCs', '0')
            with open(config_file, 'wb') as configfile:
                config.write(configfile)
        self.pilot_list = []
        self.atc_list = []
        self.vehicles = []
        self.SchedATC_URL = None
        self.SchedFlights_URL = None
        self.ui.tabWidget.currentChanged.connect(self.ivao_friend)

    @property
    def maptab(self):
        if self._maptab is None and self.ui.tabWidget.currentIndex() != 8:
            self._maptab = QWebView()
            self.ui.tabWidget.insertTab(8, self.maptab, 'Map')
        else:
            self.ui.tabWidget.setCurrentIndex(8)
        return self._maptab
    
    def sql_querys(self, args=None, var=None):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        if args == 'Get_All_Flags':
            Q_db = cursor.execute("SELECT DISTINCT(Country) FROM icao_codes ORDER BY Country ASC;")
        if args == 'Get_All_data_icao_codes':
            Q_db = cursor.execute("SELECT icao, Latitude, Longitude, City_Airport, Country FROM icao_codes DESC;")
        if args == 'Get_Country_from_ICAO':
            Q_db = cursor.execute('SELECT Country FROM icao_codes WHERE icao = ?;', (str(var[0]),))
        if args == 'Get_Country_from_FIR':
            Q_db = cursor.execute('SELECT Country FROM fir_data_list WHERE icao = ?;', (str(var[0]),))
        if args == 'Get_Country_from_Division':
            Q_db = cursor.execute('SELECT Country FROM division_ivao WHERE Division=?;', (str(var[0]),))
        if args == 'Get_Status':
            Q_db = cursor.execute("SELECT DISTINCT(callsign), planned_aircraft, planned_depairport, \
                                   planned_destairport, onground, time_connected, groundspeed, planned_altitude, \
                                   Latitude, Longitude FROM status_ivao WHERE callsign=?;", (str(var[0]),))
        if args == 'Get_City':
            Q_db = cursor.execute("SELECT City_Airport, Latitude, Longitude FROM icao_codes WHERE icao=?;", (str(var[0]),))
        if args == 'Get_Pilots':
            Q_db = cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='PILOT';")
        if args == 'Get_Pilot':
            Q_db = cursor.execute("SELECT callsign, planned_aircraft, rating, realname, planned_depairport, planned_destairport, \
                                   time_connected FROM status_ivao WHERE clienttype='PILOT' \
                                   AND realname LIKE ? ORDER BY vid DESC;", (('%'+str(var[0])),))
        if args == 'Get_Controllers':
            Q_db = cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='ATC';")
        if args == 'Get_FollowMeCarService':
            Q_db = cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='FOLME';")
        if args == 'Get_Observers':
            Q_db = cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='ATC' AND callsign like '%OBS%';")
        if args == 'Get_POB':
            Q_db = cursor.execute("SELECT SUM(planned_pob) FROM status_ivao;")
        if args == 'Get_Controller_List':
            Q_db = cursor.execute("SELECT callsign, frequency, realname, rating, facilitytype, time_connected FROM status_ivao \
                                   WHERE clienttype='ATC' ORDER BY vid DESC;")
        if args == 'Get_Controller':
            Q_db = cursor.execute("SELECT callsign, frequency, realname, rating, facilitytype, time_connected FROM status_ivao \
                                   WHERE clienttype='ATC' AND callsign LIKE ? ORDER BY vid DESC;", (('%'+var[0]+'%'),))
        if args == 'Get_Pilot_Lists':
            Q_db = cursor.execute("SELECT DISTINCT(callsign), planned_aircraft, rating, realname, planned_depairport, \
                                   planned_destairport, time_connected, clienttype FROM status_ivao \
                                   WHERE clienttype='PILOT' ORDER BY vid ASC;")
        if args == 'Get_FMC_List':
            Q_db = cursor.execute("SELECT DISTINCT(callsign), rating, realname, time_connected, clienttype \
                                   FROM status_ivao WHERE clienttype='FOLME';")
        if args == 'Get_Airline':
            Q_db = cursor.execute('SELECT Airline FROM airlines_codes WHERE Code = ?;', (str(var[0]),))
        if args == 'Get_ICAO_from_Country':
            Q_db = cursor.execute("SELECT icao FROM icao_codes WHERE country=?;", (str(var[0]),))
        if args == 'Get_Outbound_Traffic':
            Q_db= cursor.execute("SELECT callsign, planned_depairport, planned_destairport FROM status_ivao WHERE planned_depairport LIKE ?", \
                           (str(var[0]),))
        if args == 'Get_Inbound_Traffic':
            Q_db = cursor.execute("SELECT callsign, planned_depairport, planned_destairport FROM status_ivao WHERE planned_destairport LIKE ?", \
                           (str(var[0]),))
        return Q_db

    def initial_load(self):
        self.statusBar().showMessage('Populating Database', 2000)
        qApp.processEvents()
        Q_db = self.sql_querys('Get_All_Flags')
        db_t1 = Q_db.fetchall()
        Q_db = self.sql_querys('Get_All_data_icao_codes')
        db_t2 = Q_db.fetchall()
        startrow_dbt1 = startrow_dbt2 = 0

        for line in db_t1:
            if line[0] == None:
                self.ui.dbTableWidget_1.removeRow(self.ui.dbTableWidget_1.rowCount())
            else:
                pass
            country = "%s" % line[0]
            self.ui.country_list.addItem(country)
            self.ui.dbTableWidget_1.insertRow(self.ui.dbTableWidget_1.rowCount())
            image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
            flagCodePath = (image_flag + '/%s.png') % line
            if os.path.exists(flagCodePath) is True:
                Pixmap = QPixmap(flagCodePath)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.dbTableWidget_1.setCellWidget(startrow_dbt1, 0, flag_country)
            else:
                pass
            country = QTableWidgetItem(str(line[0]).encode('utf-8'), 0)
            self.ui.dbTableWidget_1.setItem(startrow_dbt1, 1, country)
            startrow_dbt1 += 1

        for line in db_t2:
            if line[0] == None:
                self.ui.dbTableWidget_2.removeRow(self.ui.dbTableWidget_2.rowCount())
            else:
                pass
            self.ui.dbTableWidget_2.insertRow(self.ui.dbTableWidget_2.rowCount())
            icao = QTableWidgetItem(str(line[0]), 0)
            self.ui.dbTableWidget_2.setItem(startrow_dbt2, 0, icao)
            latitude = QTableWidgetItem(str(line[1]), 0)
            self.ui.dbTableWidget_2.setItem(startrow_dbt2, 1, latitude)
            longitude = QTableWidgetItem(str(line[2]), 0)
            self.ui.dbTableWidget_2.setItem(startrow_dbt2, 2, longitude)
            AirportName = QTableWidgetItem(str(line[3].encode('utf-8')), 0)
            self.ui.dbTableWidget_2.setItem(startrow_dbt2, 3, AirportName)
            try:
                Country = QTableWidgetItem(str(line[4].encode('utf-8')), 0)
                self.ui.dbTableWidget_2.setItem(startrow_dbt2, 4, Country)
            except:
                pass
            startrow_dbt2 += 1

        qApp.processEvents()
        self.statusBar().showMessage('Showing friends list', 2000)
        self.ivao_friend()
        self.country_view()
        qApp.restoreOverrideCursor()

    def connect(self):
        self.statusBar().showMessage('Trying connecting to IVAO', 3000)
        qApp.processEvents()
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        try:
            use_proxy = config.getint('Settings', 'use_proxy')
            auth = config.getint('Settings', 'auth')
            host = config.get('Settings', 'host')
            port = config.get('Settings', 'port')
            user = config.get('Settings', 'user')
            pswd = config.get('Settings', 'pass')
            if use_proxy == 2 and auth == 2:
                passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
                passmgr.add_password(None, 'http://' + host + ':' + port, user, pswd)
                authinfo = urllib2.ProxyBasicAuthHandler(passmgr)
                proxy_support = urllib2.ProxyHandler({"http" : "http://" + host + ':' + port})
                opener = urllib2.build_opener(proxy_support, authinfo)
                urllib2.install_opener(opener)
                StatusURL = urllib2.urlopen(config.get('Info', 'url') + config.get('Info', 'data_access'))
                self.SchedATC_URL = urllib2.urlopen(config.get('Info', 'scheduling_atc'))
                self.SchedFlights_URL = urllib2.urlopen(config.get('Info', 'scheduling_fligths'))
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, str(host), int(port), str(user), str(pswd)))
                qApp.processEvents()
            if use_proxy == 2 and auth == 0:
                proxy_support = urllib2.ProxyHandler({"http" : "http://" + host + ':' + port})
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)
                StatusURL = urllib2.urlopen(config.get('Info', 'url') + config.get('Info', 'data_access'))
                self.SchedATC_URL = urllib2.urlopen(config.get('Info', 'scheduling_atc'))
                self.SchedFlights_URL = urllib2.urlopen(config.get('Info', 'scheduling_fligths'))
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, str(host), int(port)))
                qApp.processEvents()
            if use_proxy == 0 and auth == 0:
                StatusURL = urllib2.urlopen(config.get('Info', 'url') + config.get('Info', 'data_access'))
                self.SchedATC_URL = urllib2.urlopen(config.get('Info', 'scheduling_atc'))
                self.SchedFlights_URL = urllib2.urlopen(config.get('Info', 'scheduling_flights'))
                qApp.processEvents()

            self.statusBar().showMessage('Downloading info from IVAO', 2000)
            qApp.processEvents()
            self.pilot_list = []
            self.atc_list = []

            for logged_users in StatusURL.readlines():
                if "PILOT" in logged_users:
                    self.pilot_list.append(logged_users)
                if "ATC" in logged_users:
                    self.atc_list.append(logged_users)
                if "FOLME" in logged_users:
                    self.pilot_list.append(logged_users)
            self.update_db()

        except IOError:
            self.statusBar().showMessage('Error! when trying to download info from IVAO. Check your connection to Internet.')

    def update_db(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("BEGIN TRANSACTION;")
        cursor.execute("DELETE FROM status_ivao;")
        qApp.processEvents()

        for rows in self.pilot_list:
            fields = rows.split(":")
            callsign = fields[0]
            vid = fields[1]
            realname = rows.rsplit(":")[2].decode('latin-1')
            clienttype = fields[3]
            latitude = fields[5]
            longitude = fields[6]
            altitude = fields[7]
            groundspeed = fields[8]
            planned_aircraft = fields[9]
            planned_tascruise = fields[10]
            planned_depairport = fields[11]
            planned_altitude = fields[12]
            planned_destairport = fields[13]
            server = fields[14]
            protrevision = fields[15]
            rating = fields[16]
            transponder = fields[17]
            visualrange = fields[19]
            planned_revision = fields[20]
            planned_flighttype = fields[21]
            planned_deptime = fields[22]
            planned_actdeptime = fields[23]
            planned_hrsenroute = fields[24]
            planned_minenroute = fields[25]
            planned_hrsfuel = fields[26]
            planned_minfuel = fields[27]
            planned_altairport = fields[28]
            planned_remarks = fields[29]
            planned_route = fields[30]
            planned_depairport_lat = fields[31]
            planned_depairport_lon = fields[32]
            planned_destairport_lat = fields[33]
            planned_destairport_lon = fields[34]
            time_last_atis_received = fields[36]
            time_connected = fields[37]
            client_software_name = fields[38]
            client_software_version = fields[39]
            adminrating = fields[40]
            atc_or_pilotrating = fields[41]
            planned_altairport2 = fields[42]
            planned_typeofflight = fields[43]
            planned_pob = fields[44]
            true_heading = fields[45]
            onground = fields[46]
            cursor.execute("INSERT INTO status_ivao (callsign, vid, realname, clienttype \
            , latitude, longitude, altitude, groundspeed, planned_aircraft, planned_tascruise \
            , planned_depairport, planned_altitude, planned_destairport, server, protrevision \
            , rating, transponder, visualrange, planned_revision, planned_flighttype \
            , planned_deptime, planned_actdeptime, planned_hrsenroute, planned_minenroute, planned_hrsfuel \
            , planned_minfuel, planned_altairport, planned_remarks, planned_route, planned_depairport_lat \
            , planned_depairport_lon, planned_destairport_lat, planned_destairport_lon \
            , time_last_atis_received, time_connected, client_software_name, client_software_version \
            , adminrating, atc_or_pilotrating, planned_altairport2, planned_typeofflight, planned_pob, true_heading \
            , onground) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
            (callsign, vid, realname, clienttype, latitude, longitude, altitude, groundspeed, planned_aircraft \
             , planned_tascruise, planned_depairport, planned_altitude, planned_destairport, server, protrevision \
             , rating, transponder, visualrange, planned_revision, planned_flighttype \
             , planned_deptime, planned_actdeptime, planned_hrsenroute, planned_minenroute, planned_hrsfuel \
             , planned_minfuel, planned_altairport, planned_remarks, planned_route, planned_depairport_lat \
             , planned_depairport_lon, planned_destairport_lat, planned_destairport_lon \
             , time_last_atis_received, time_connected, client_software_name, client_software_version \
             , adminrating, atc_or_pilotrating, planned_altairport2, planned_typeofflight, planned_pob, true_heading \
             , onground))
        connection.commit()

        for rows in self.atc_list:
            fields = rows.split(":")
            callsign = fields[0]
            vid = fields[1]
            realname = rows.rsplit(":")[2].decode('latin-1')
            clienttype = fields[3]
            frequency = fields[4]
            latitude = fields[5]
            longitude = fields[6]
            altitude = fields[7]
            server = fields[14]
            protrevision = fields[15]
            rating = fields[16]
            facilitytype = fields[18]
            visualrange = fields[19]
            atis_message = fields[35].decode('latin-1')
            time_last_atis_received = fields[36]
            time_connected = fields[37]
            client_software_name = fields[38]
            client_software_version = fields[39]
            adminrating = fields[40]
            atc_or_atcrating = fields[41]

            cursor.execute("INSERT INTO status_ivao (callsign, vid, realname, clienttype, frequency \
            , latitude, longitude, altitude, server, protrevision, rating, facilitytype, visualrange \
            , time_last_atis_received, time_connected, client_software_name, client_software_version \
            , adminrating, atc_or_pilotrating, atis_message) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
            (callsign, vid, realname, clienttype, frequency, latitude, longitude, altitude, server \
             , protrevision, rating, facilitytype, visualrange, time_last_atis_received, time_connected \
             , client_software_name, client_software_version, adminrating, atc_or_pilotrating, atis_message))
        connection.commit()

        for row in self.vehicles:
            fields = rows.split(":")
            callsign = fields[0]
            vid = fields[1]
            realname = rows.rsplit(":")[2].decode('latin-1')
            clienttype = fields[3]
            server = fields[14]
            time_connected = fields[37]

        cursor.execute("INSERT INTO status_ivao (callsign, vid, realname, clienttype, server, time_connected) \
        VALUES (?,?,?,?,?,?)", (callsign, vid, realname, clienttype, server, time_connected))
        connection.commit()

        self.statusBar().showMessage('Events schedule for Controllers ...', 2000)
        qApp.processEvents()
        self.soup_atc = BeautifulSoup(self.SchedATC_URL)
        self.statusBar().showMessage('Events schedule for Flights ...', 2000)
        qApp.processEvents()
        self.soup_flights = BeautifulSoup(self.SchedFlights_URL)
        self.show_tables()
        self.ivao_friend()
        self.Scheduling()

    def Scheduling(self):
        if self.SchedATC_URL is None and self.SchedFlights_URL is None:
            self.statusBar().showMessage('You have to download data from IVAO, Select "Menu" and "Get data from IVAO"', 7000)
            qApp.processEvents()
            return

        table_atc = self.soup_atc.find("table")
        table_rows = table_atc.findAll('tr')
        while self.ui.SchedulingATC.rowCount () > 0:
            self.ui.SchedulingATC.removeRow(0)
        startrow = 0
        for line_atc_table in table_rows[1:]:
            columns = [col.find(text=True) for col in line_atc_table.findAll('td')]
            self.ui.SchedulingATC.insertRow(self.ui.SchedulingATC.rowCount())
            col_Name = QTableWidgetItem(str(columns[1]).decode('latin-1'), 0)
            self.ui.SchedulingATC.setItem(startrow, 2, col_Name)
            col_Position = QTableWidgetItem(str(columns[3]), 0)
            self.ui.SchedulingATC.setItem(startrow, 3, col_Position)
            col_StartTime = QTableWidgetItem(str(columns[4]), 0)
            self.ui.SchedulingATC.setItem(startrow, 4, col_StartTime)
            col_EndTime = QTableWidgetItem(str(columns[5]), 0)
            self.ui.SchedulingATC.setItem(startrow, 5, col_EndTime)
            col_Voice = QTableWidgetItem(str(columns[6]), 0)
            self.ui.SchedulingATC.setItem(startrow, 6, col_Voice)
            col_Training = QTableWidgetItem(str(columns[7]), 0)
            self.ui.SchedulingATC.setItem(startrow, 7, col_Training)
            col_Event = QTableWidgetItem(str(columns[8]), 0)
            self.ui.SchedulingATC.setItem(startrow, 8, col_Event)
            try:
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(columns[3][:4]),))
                country = Q_db.fetchone()
                if country is None:
                    Q_db = self.sql_querys('Get_Country_from_FIR', (str(columns[3][:4]),))
                    country = Q_db.fetchone()
                col_Country = QTableWidgetItem(str(country[0]), 0)
                self.ui.SchedulingATC.setItem(startrow, 1, col_Country)
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath = (image_flag + '/%s.png') % (str(country[0]))
                Pixmap = QPixmap(flagCodePath)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.SchedulingATC.setCellWidget(startrow, 0, flag_country)
            except:
                pass
            startrow += 1
            qApp.processEvents()

        table_flights = self.soup_flights.find("table")
        table_rows = table_flights.findAll('tr')
        while self.ui.SchedulingFlights.rowCount () > 0:
            self.ui.SchedulingFlights.removeRow(0)
        startrow = 0
        for line_flights_table in table_rows[2:]:
            columns = [col.find(text=True) for col in line_flights_table.findAll('td')]
            self.ui.SchedulingFlights.insertRow(self.ui.SchedulingFlights.rowCount())
            code_airline = columns[4][:3]
            image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
            airlineCodePath = (image_airlines + '/%s.gif') % code_airline
            try:
                if os.path.exists(airlineCodePath) is True:
                    Pixmap = QPixmap(airlineCodePath)
                    airline = QLabel(self)
                    airline.setPixmap(Pixmap)
                    self.ui.SchedulingFlights.setCellWidget(startrow, 0, airline)
                else:
                    code_airline = str(inbound[0])
                    col_airline = QTableWidgetItem(code_airline, 0)
                    self.ui.SchedulingFlights.setItem(startrow, 0, col_airline)
            except:
                pass
            col_Callsign = QTableWidgetItem(str(columns[4]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 1, col_Callsign)
            col_Name = QTableWidgetItem(str(columns[1]).decode('latin-1'), 0)
            self.ui.SchedulingFlights.setItem(startrow, 2, col_Name)
            col_StartTime = QTableWidgetItem(str(columns[5]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 3, col_StartTime)
            col_Departure = QTableWidgetItem(str(columns[6]), 0)
            try:
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(columns[6]),))
                country = Q_db.fetchone()
                if country is None:
                    Q_db = self.sql_querys('Get_Country_from_FIR',  (str(columns[6]),))
                    country = Q_db.fetchone()
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath = (image_flag + '/%s.png') % (str(country[0]))
                Pixmap = QPixmap(flagCodePath)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.SchedulingFlights.setCellWidget(startrow, 4, flag_country)
            except:
                pass
            self.ui.SchedulingFlights.setItem(startrow, 5, col_Departure)
            col_StartTime = QTableWidgetItem(str(columns[7]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 6, col_StartTime)
            col_Destination = QTableWidgetItem(str(columns[8]), 0)
            try:
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(columns[8]),))
                country = Q_db.fetchone()
                if country is None:
                    Q_db = self.sql_querys('Get_Country_from_FIR', (str(columns[8]),))
                    country = Q_db.fetchone()
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath = (image_flag + '/%s.png') % (str(country[0]))
            except:
                pass
            Pixmap = QPixmap(flagCodePath)
            flag_country = QLabel()
            flag_country.setPixmap(Pixmap)
            self.ui.SchedulingFlights.setCellWidget(startrow, 7, flag_country)
            self.ui.SchedulingFlights.setItem(startrow, 8, col_Destination)
            col_EndTime = QTableWidgetItem(str(columns[9]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 9, col_EndTime)
            col_Altitude = QTableWidgetItem(str(columns[10]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 10, col_Altitude)
            col_CruisingSpeed = QTableWidgetItem(str(columns[11]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 11, col_CruisingSpeed)
            col_Route = QTableWidgetItem(str(columns[12]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 12, col_Route)
            col_Voice = QTableWidgetItem(str(columns[13]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 13, col_Voice)
            col_Training = QTableWidgetItem(str(columns[14]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 14, col_Training)
            col_Event = QTableWidgetItem(str(columns[15]), 0)
            self.ui.SchedulingFlights.setItem(startrow, 15, col_Event)
            startrow += 1
            qApp.processEvents()
        self.statusBar().showMessage('Done!', 2000)

    def status_plane(self, callsign):
        Q_db = self.sql_querys('Get_Status', (str(callsign),))
        get_status = Q_db.fetchone()
        status = '-'
        for row_pilot in get_status:
            try:
                Q_db = self.sql_querys('Get_City', (str(get_status[2]),))
                city_orig = Q_db.fetchone()
                city_orig_point = float(city_orig[1]), float(city_orig[2])
                Q_db = self.sql_querys('Get_City', (str(get_status[3]),))
                city_dest = Q_db.fetchone()
                city_dest_point = float(city_dest[1]), float(city_dest[2])
                pilot_position = get_status[8], get_status[9]
                total_miles = distance.distance(city_orig_point, city_dest_point).miles
                dist_traveled = distance.distance(city_orig_point, pilot_position).miles
                percent = (float(dist_traveled) / float(total_miles)) * 100.0

                if percent > 105 :
                    status = 'Diverted'
                    return status
                else:
                    if int(str(get_status[4])) == 0:
                        if (percent >= 0.0) and (percent <= 2.0):
                            status = 'Takeoff'
                        if (percent >= 2.0) and (percent <= 7.0):
                            status = 'Initial Climbing'
                        if (percent >= 7.0) and (percent <= 10.0):
                            status = 'Climbing'
                        if (percent >= 10.0) and (percent <= 80.0):
                            status = 'On Route'
                        if (percent >= 80.0) and (percent <= 90.0):
                            status = 'Descending'
                        if (percent >= 90.0) and (percent <= 97.0):
                            status = 'Initial Approach'
                        if (((percent >= 97.0) and (percent <= 105.0)) and ((get_status[6] <= 200) and (get_status[6] >= 30))):
                            status = 'Final Approach'
                        return status
                    else:
                        if ((get_status[6] > 0) and (get_status[6] <= 30)) and (percent < 1.0):
                            status = 'Departing'
                        if (get_status[6] > 30) and (get_status[6] < 150) and (percent < 1.0):
                            status = 'Takeoff'
                        if (((percent >= 97.0) and (percent <= 105.0)) and ((get_status[6] <= 220) and (get_status[6] >= 30))):
                            status = 'Landed'
                        if (get_status[6] < 30) and (percent > 99.0):
                            status = 'Taxing to Gate'
                        if (get_status[6] == 0) and (percent > 99.0):
                            status = 'On Blocks'
                        if (get_status[6] == 0) and (percent <= 1.0):
                            status = 'Boarding'
                        if (get_status[6] == 0) and (percent >= 10.0 and percent <= 90.0):
                            status = 'Altern Airport'
                        return status
            except:
                status = 'Fill Flight Plan'
                return status

    def show_tables(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        self.statusBar().showMessage('Populating Controllers and Pilots', 10000)
        self.progress.show()
        pilots_ivao = atcs_ivao = obs_ivao = 0
        Q_db = self.sql_querys('Get_Pilots')
        pilots = Q_db.fetchone()
        Q_db = self.sql_querys('Get_Controllers')
        atc = Q_db.fetchone()
        Q_db = self.sql_querys('Get_FollowMeCarService')
        followme = Q_db.fetchone()
        Q_db = self.sql_querys('Get_Observers')
        obs = Q_db.fetchone()
        Q_db = self.sql_querys('Get_POB')
        pob = Q_db.fetchone()
        self.ui.IVAOStatustableWidget.setCurrentCell(-1, -1)
        pilots_ivao = QTableWidgetItem(str(pilots[0]))
        atcs_ivao = QTableWidgetItem(str((int(atc[0]) - int(obs[0]))))
        vehicles = QTableWidgetItem(str(int(followme[0])))
        obs_ivao = QTableWidgetItem(str(int(obs[0])))
        total_ivao = QTableWidgetItem(str(atc[0] + pilots[0] + followme[0]))
        if pob[0] is None:
            pob_ivao = QTableWidgetItem(str(0))
        else:
            pob_ivao = QTableWidgetItem(str(int(pob[0])))

        time_received = datetime.datetime.utcnow()
        time_board = QTableWidgetItem(str(time_received).split('.')[0] + ' - Zulu Time (UTC)')

        self.ui.IVAOStatustableWidget.setItem(0, 0, pilots_ivao)
        self.ui.IVAOStatustableWidget.setItem(1, 0, atcs_ivao)
        self.ui.IVAOStatustableWidget.setItem(2, 0, vehicles)
        self.ui.IVAOStatustableWidget.setItem(3, 0, obs_ivao)
        self.ui.IVAOStatustableWidget.setItem(4, 0, total_ivao)
        self.ui.IVAOStatustableWidget.setItem(6, 0, pob_ivao)
        self.ui.IVAOStatustableWidget.setItem(7, 0, time_board)
        qApp.processEvents()
        Q_db = self.sql_querys('Get_Controller_List')
        rows_atcs = Q_db.fetchall()
        startrow = 0

        while self.ui.ATC_FullList.rowCount () > 0:
            self.ui.ATC_FullList.removeRow(0)

        for row_atc in rows_atcs:
            if row_atc[3] is None:
                continue
            self.ui.ATC_FullList.insertRow(self.ui.ATC_FullList.rowCount())
            col_callsign = QTableWidgetItem(str(row_atc[0]), 0)
            if str(row_atc[0][:4]) == 'IVAO':
                self.ui.ATC_FullList.setColumnWidth(2, 60)
                col_callsign = QTableWidgetItem(str(row_atc[0]), 0)
                self.ui.ATC_FullList.setItem(startrow, 0, col_callsign)
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
                flagCodePath = (image_flag + '/ivao_member.png')
                Pixmap = QPixmap(flagCodePath)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.ATC_FullList.setCellWidget(startrow, 2, flag_country)
                col_country = QTableWidgetItem('IVAO Member', 0)
                self.ui.ATC_FullList.setItem(startrow, 3, col_country)

            elif str(row_atc[0][2:3]) == '-' or str(row_atc[0][2:3]) == '_':
                Q_db = self.sql_querys('Get_Country_from_Division', (str(row_atc[0][:2]),))
                div_ivao = Q_db.fetchone()
                if row_atc is None or div_ivao is None:
                    pass
                else:
                    image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                    flagCodePath = (image_flag + '/%s.png') % str(div_ivao[0])
                    col_callsign = QTableWidgetItem(str(row_atc[0]), 0)
                    self.ui.ATC_FullList.setItem(startrow, 0, col_callsign)
                    Pixmap = QPixmap(flagCodePath)
                    flag_country = QLabel()
                    flag_country.setPixmap(Pixmap)
                    self.ui.ATC_FullList.setCellWidget(startrow, 2, flag_country)
                    col_country = QTableWidgetItem(str(div_ivao[0]), 0)
                    self.ui.ATC_FullList.setItem(startrow, 3, col_country)
            else:
                code_icao = str(row_atc[0][:4])
                try:
                    Q_db = self.sql_querys('Get_Country_from_ICAO', (str(code_icao),))
                    flagCode = Q_db.fetchone()
                    if flagCode is None:
                        Q_db = self.sql_querys('Get_Country_from_FIR', (str(code_icao),))
                        division = Q_db.fetchone()
                        Q_db = self.sql_querys('Get_Country_from_Division', (str(division[0]),))
                        flagCode = Q_db.fetchone()
                    image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                    flagCodePath = (image_flag + '/%s.png') % flagCode
                    if os.path.exists(flagCodePath) is True:
                        Pixmap = QPixmap(flagCodePath)
                        flag_country = QLabel()
                        flag_country.setPixmap(Pixmap)
                        self.ui.ATC_FullList.setCellWidget(startrow, 2, flag_country)
                        col_country = QTableWidgetItem(str(flagCode[0]), 0)
                        self.ui.ATC_FullList.setItem(startrow, 3, col_country)
                        self.ui.ATC_FullList.setItem(startrow, 0, col_callsign)
                except:
                    col_country = QTableWidgetItem(str(flagCode).encode('latin-1'), 0)
                    self.ui.ATC_FullList.setItem(startrow, 0, col_callsign)
                    error_flag = QTableWidgetItem(str('None'), 0)
                    self.ui.ATC_FullList.setItem(startrow, 2, error_flag)
                    error_country = QTableWidgetItem(str('Error Callsign for IVAO'), 0)
                    error_country.setForeground(QBrush(QColor('red')))
                    self.ui.ATC_FullList.setItem(startrow, 3, error_country)
            col_frequency = QTableWidgetItem(str(row_atc[1]), 0)
            self.ui.ATC_FullList.setItem(startrow, 1, col_frequency)
            if row_atc[5] == '1.1.14':
                pass
            try:
                col_facility = QTableWidgetItem(str(self.position_atc[row_atc[4]]), 0)
                self.ui.ATC_FullList.setItem(startrow, 4, col_facility)
            except:
                pass
            col_realname = QTableWidgetItem(str(row_atc[2].encode('latin-1')), 0)
            self.ui.ATC_FullList.setItem(startrow, 5, col_realname)
            code_atc_rating = row_atc[3]
            ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
            ratingImagePath = ImagePath + '/atc_level%d.gif' % int(code_atc_rating)
            try:
                if os.path.exists(ratingImagePath) is True:
                    Pixmap = QPixmap(ratingImagePath)
                    ratingImage = QLabel(self)
                    ratingImage.setPixmap(Pixmap)
                    self.ui.ATC_FullList.setCellWidget(startrow, 7, ratingImage)
                    col_rating = QTableWidgetItem(str(self.rating_atc[row_atc[3]]), 0)
                    self.ui.ATC_FullList.setItem(startrow, 6, col_rating)
                else:
                    col_rating = QTableWidgetItem(str(self.rating_atc[row_atc[3]]), 0)
                    self.ui.ATC_FullList.setItem(startrow, 7, col_rating)
            except:
                pass
            try:
                start_connected = datetime.datetime(int(str(row_atc[5])[:4]), int(str(row_atc[5])[4:6]) \
                                                    , int(str(row_atc[5])[6:8]), int(str(row_atc[5])[8:10]) \
                                                    , int(str(row_atc[5])[10:12]), int(str(row_atc[5])[12:14]))
                diff = datetime.datetime.utcnow() - start_connected
                col_time = QTableWidgetItem(str(diff).split('.')[0], 0)
                self.ui.ATC_FullList.setItem(startrow, 8, col_time)
            except:
                pass
            self.progress.setValue(int(float(startrow) / float(len(rows_atcs)) * 100.0))
            startrow += 1
            qApp.processEvents()

        Q_db = self.sql_querys('Get_FMC_List')
        vehicles = Q_db.fetchall()

        startrow = 0
        while self.ui.PILOT_FullList.rowCount () > 0:
            self.ui.PILOT_FullList.removeRow(0)

        for followservice in vehicles:
            self.ui.PILOT_FullList.setCurrentCell(0, 0)
            self.ui.PILOT_FullList.insertRow(self.ui.PILOT_FullList.rowCount())
            image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
            followmeCodePath = (image_airlines + '/ZZZZ.png')
            Pixmap = QPixmap(followmeCodePath)
            FMC_img = QLabel(self)
            FMC_img.setPixmap(Pixmap)
            self.ui.PILOT_FullList.setCellWidget(startrow, 0, FMC_img)
            col_callsign = QTableWidgetItem(str(followservice[0]), 0)
            self.ui.PILOT_FullList.setItem(startrow, 1, col_callsign)
            col_aircraft = QTableWidgetItem(str('FOLME'), 0)
            self.ui.PILOT_FullList.setItem(startrow, 2, col_aircraft)
            col_realname = QTableWidgetItem(str(followservice[2][:-5].encode('latin-1')), 0)
            self.ui.PILOT_FullList.setItem(startrow, 3, col_realname)
            col_rating = QTableWidgetItem(str(self.rating_pilot[followservice[1]]), 0)
            self.ui.PILOT_FullList.setItem(startrow, 4, col_rating)
            code_pilot_rating = followservice[1]
            ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
            ratingImagePath = ImagePath + '/pilot_level%d.gif' % int(code_pilot_rating)
            try:
                if os.path.exists(ratingImagePath) is True:
                    Pixmap = QPixmap(ratingImagePath)
                    ratingImage = QLabel(self)
                    ratingImage.setPixmap(Pixmap)
                    self.ui.PILOT_FullList.setCellWidget(startrow, 5, ratingImage)
                else:
                    pass
            except:
                pass
            col_departure = QTableWidgetItem(str('-'), 0)
            self.ui.PILOT_FullList.setItem(startrow, 6, col_departure)
            col_destination = QTableWidgetItem(str('-'), 0)
            self.ui.PILOT_FullList.setItem(startrow, 7, col_destination)
            col_status = QTableWidgetItem(str("Follow Car Service"), 0)
            self.ui.PILOT_FullList.setItem(startrow, 8, col_status)
            start_connected = datetime.datetime(int(str(followservice[3])[:4]), int(str(followservice[3])[4:6]), int(str(followservice[3])[6:8]) \
                                , int(str(followservice[3])[8:10]), int(str(followservice[3])[10:12]), int(str(followservice[3])[12:14]))
            diff = datetime.datetime.utcnow() - start_connected
            col_time = QTableWidgetItem(str(diff).split('.')[0], 0)
            self.ui.PILOT_FullList.setItem(startrow, 9, col_time)
            self.progress.setValue(int(float(startrow) / float(len(vehicles)) * 100.0))
            startrow += 1
            qApp.processEvents()

        Q_db = self.sql_querys('Get_Pilot_Lists')
        rows_pilots = Q_db.fetchall()

        for row_pilot in rows_pilots:
            self.ui.PILOT_FullList.insertRow(self.ui.PILOT_FullList.rowCount())
            code_airline = row_pilot[0][:3]
            image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
            airlineCodePath = (image_airlines + '/%s.gif') % code_airline
            try:
                if os.path.exists(airlineCodePath) is True:
                    Pixmap = QPixmap(airlineCodePath)
                    airline = QLabel(self)
                    airline.setPixmap(Pixmap)
                    self.ui.PILOT_FullList.setCellWidget(startrow, 0, airline)
                else:
                    Q_db = self.sql_querys('Get_Airline', (str(row_pilot[0][:3]),))
                    airline_code = Q_db.fetchone()
                    if airline_code is None:
                        col_airline = QTableWidgetItem(str(row_pilot[0]))
                    else:
                        col_airline = QTableWidgetItem(str(airline_code[0]), 0)
                        self.ui.PILOT_FullList.setItem(startrow, 0, col_airline)
            except:
                pass
            col_callsign = QTableWidgetItem(str(row_pilot[0]), 0)
            self.ui.PILOT_FullList.setItem(startrow, 1, col_callsign)
            try:
                aircraft = row_pilot[1].split('/')[1]
                if aircraft != '-':
                    pass
            except:
                aircraft = '-'
            col_aircraft = QTableWidgetItem(aircraft, 0)
            self.ui.PILOT_FullList.setItem(startrow, 2, col_aircraft)
            col_realname = QTableWidgetItem(str(row_pilot[3][:-5].encode('latin-1')), 0)
            self.ui.PILOT_FullList.setItem(startrow, 3, col_realname)
            col_rating = QTableWidgetItem(str(self.rating_pilot[row_pilot[2]]), 0)
            self.ui.PILOT_FullList.setItem(startrow, 4, col_rating)
            code_pilot_rating = row_pilot[2]
            ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
            ratingImagePath = ImagePath + '/pilot_level%d.gif' % int(code_pilot_rating)
            try:
                if os.path.exists(ratingImagePath) is True:
                    Pixmap = QPixmap(ratingImagePath)
                    ratingImage = QLabel(self)
                    ratingImage.setPixmap(Pixmap)
                    self.ui.PILOT_FullList.setCellWidget(startrow, 5, ratingImage)
                else:
                    pass
            except:
                pass

            col_departure = QTableWidgetItem(str(row_pilot[4]), 0)
            self.ui.PILOT_FullList.setItem(startrow, 6, col_departure)
            col_destination = QTableWidgetItem(str(row_pilot[5]), 0)
            self.ui.PILOT_FullList.setItem(startrow, 7, col_destination)
            status_plane = self.status_plane(row_pilot[0])
            col_status = QTableWidgetItem(str(status_plane), 0)
            col_status.setForeground(QBrush(QColor(self.get_color(status_plane))))
            self.ui.PILOT_FullList.setItem(startrow, 8, col_status)
            start_connected = datetime.datetime(int(str(row_pilot[6])[:4]), int(str(row_pilot[6])[4:6]), int(str(row_pilot[6])[6:8]) \
                                , int(str(row_pilot[6])[8:10]), int(str(row_pilot[6])[10:12]), int(str(row_pilot[6])[12:14]))
            diff = datetime.datetime.utcnow() - start_connected
            col_time = QTableWidgetItem(str(diff).split('.')[0], 0)
            self.ui.PILOT_FullList.setItem(startrow, 9, col_time)
            self.progress.setValue(int(float(startrow) / float(len(rows_pilots)) * 100.0))
            startrow += 1
            qApp.processEvents()

        self.progress.hide()
        self.statusBar().showMessage('Done', 2000)
        qApp.processEvents()
        if config.getint('Map', 'auto_refresh') == 2:
            self.all2map()
        else:
            pass
        self.country_view()
        self.network()

    def country_view(self):
        country_selected = self.ui.country_list.currentText()
        Q_db = self.sql_querys('Get_Country_from_ICAO', (str(country_selected),))
        flagCode = Q_db.fetchone()

        image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
        flagCodePath = (image_flag + '/%s.png') % country_selected
        Pixmap = QPixmap(flagCodePath)
        self.ui.flagIcon.setPixmap(Pixmap)
        Q_db = self.sql_querys('Get_ICAO_from_Country', (str(country_selected),))
        icao_country = Q_db.fetchall()
        self.ui.Inbound_traffic.setText('Inbound Traffic in %s Airports' % (country_selected))
        self.ui.Outbound_traffic.setText('Outbound Traffic in %s Airports' % (country_selected))

        self.ui.PilottableWidget.insertRow(self.ui.PilottableWidget.rowCount())
        self.ui.ATCtableWidget.insertRow(self.ui.ATCtableWidget.rowCount())

        while self.ui.ATCtableWidget.rowCount() > 0:
            self.ui.ATCtableWidget.removeRow(0)

        while self.ui.PilottableWidget.rowCount() > 0:
            self.ui.PilottableWidget.removeRow(0)

        while self.ui.InboundTableWidget.rowCount() > 0:
            self.ui.InboundTableWidget.removeRow(0)

        while self.ui.OutboundTableWidget.rowCount() > 0:
            self.ui.OutboundTableWidget.removeRow(0)

        startrow_atc = 0
        startrow_pilot = 0
        startrow_in = 0
        startrow_out = 0

        for codes in icao_country:
            Q_db = self.sql_querys('Get_Controller', (('%'+str(codes[0])+'%'),))
            rows_atcs = Q_db.fetchall()

            Q_db = self.sql_querys('Get_Pilot', (('%'+str(codes[0])),))
            rows_pilots = Q_db.fetchall()

            Q_db = self.sql_querys('Get_Outbound_Traffic', ((str(codes[0])),))
            OutboundTrafficAirport = Q_db.fetchall()

            Q_db = self.sql_querys('Get_Inbound_Traffic', ((str(codes[0])),))
            InboundTrafficAirport = Q_db.fetchall()

            for row_atc in rows_atcs:
                self.ui.ATCtableWidget.insertRow(self.ui.ATCtableWidget.rowCount())
                col_callsign = QTableWidgetItem(str(row_atc[0]), 0)
                self.ui.ATCtableWidget.setItem(startrow_atc, 0, col_callsign)
                col_frequency = QTableWidgetItem(str(row_atc[1]), 0)
                self.ui.ATCtableWidget.setItem(startrow_atc, 1, col_frequency)
                col_facility = QTableWidgetItem(str(self.position_atc[row_atc[4]]), 0)
                self.ui.ATCtableWidget.setItem(startrow_atc, 2, col_facility)
                col_realname = QTableWidgetItem(str(row_atc[2].encode('latin-1')), 0)
                self.ui.ATCtableWidget.setItem(startrow_atc, 3, col_realname)
                code_atc_rating = row_atc[3]
                ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
                ratingImagePath = ImagePath + '/atc_level%d.gif' % int(code_atc_rating)
                try:
                    if os.path.exists(ratingImagePath) is True:
                        Pixmap = QPixmap(ratingImagePath)
                        ratingImage = QLabel(self)
                        ratingImage.setPixmap(Pixmap)
                        self.ui.ATCtableWidget.setCellWidget(startrow_atc, 5, ratingImage)
                        col_rating = QTableWidgetItem(str(self.rating_atc[row_atc[3]]), 0)
                        self.ui.ATCtableWidget.setItem(startrow_atc, 4, col_rating)
                    else:
                        col_rating = QTableWidgetItem(str(self.rating_atc[row_atc[3]]), 0)
                        self.ui.ATCtableWidget.setItem(startrow_atc, 4, col_rating)
                except:
                    pass
                try:
                    start_connected = datetime.datetime(int(str(row_atc[5])[:4]), int(str(row_atc[5])[4:6]) \
                                                        , int(str(row_atc[5])[6:8]), int(str(row_atc[5])[8:10]) \
                                                        , int(str(row_atc[5])[10:12]), int(str(row_atc[5])[12:14]))
                except:
                    pass
                diff = datetime.datetime.utcnow() - start_connected
                col_time = QTableWidgetItem(str(diff).split('.')[0], 0)
                self.ui.ATCtableWidget.setItem(startrow_atc, 6, col_time)
                qApp.processEvents()
                startrow_atc += 1

            for row_pilot in rows_pilots:
                self.ui.PilottableWidget.setCurrentCell(0, 0)
                self.ui.PilottableWidget.insertRow(self.ui.PilottableWidget.rowCount())

                code_airline = row_pilot[0][:3]
                image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
                airlineCodePath = (image_airlines + '/%s.gif') % code_airline
                try:
                    if os.path.exists(airlineCodePath) is True:
                        Pixmap = QPixmap(airlineCodePath)
                        airline = QLabel(self)
                        airline.setPixmap(Pixmap)
                        self.ui.PilottableWidget.setCellWidget(startrow_pilot, 0, airline)
                    else:
                        Q_db = self.sql_querys('Get_Airline', (str(row_pilot[0][:3]),))
                        airline_code = Q_db.fetchone()
                        if airline_code is None:
                            col_airline = QTableWidgetItem(str(row_pilot[0]))
                        else:
                            col_airline = QTableWidgetItem(str(airline_code[0]), 0)
                        self.ui.PilottableWidget.setItem(startrow_pilot, 0, col_airline)
                except:
                    pass

                col_callsign = QTableWidgetItem(str(row_pilot[0]), 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 1, col_callsign)

                try:
                    aircraft = row_pilot[1].split('/')[1]
                    if aircraft != '-':
                        pass
                except:
                    aircraft = '-'

                col_aircraft = QTableWidgetItem(aircraft, 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 2, col_aircraft)
                col_realname = QTableWidgetItem(str(row_pilot[3][:-5].encode('latin-1')), 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 3, col_realname)
                col_rating = QTableWidgetItem(str(self.rating_pilot[row_pilot[2]]), 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 4, col_rating)

                code_pilot_rating = row_pilot[2]
                ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
                ratingImagePath = ImagePath + '/pilot_level%d.gif' % int(code_pilot_rating)
                try:
                    if os.path.exists(ratingImagePath) is True:
                        Pixmap = QPixmap(ratingImagePath)
                        ratingImage = QLabel(self)
                        ratingImage.setPixmap(Pixmap)
                        self.ui.PilottableWidget.setCellWidget(startrow_pilot, 5, ratingImage)
                    else:
                        pass
                except:
                    pass

                col_departure = QTableWidgetItem(str(row_pilot[4]), 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 6, col_departure)
                col_destination = QTableWidgetItem(str(row_pilot[5]), 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 7, col_destination)
                status_plane = self.status_plane(row_pilot[0])
                col_status = QTableWidgetItem(str(status_plane), 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 8, col_status)
                col_status.setForeground(QBrush(QColor(self.get_color(status_plane))))
                start_connected = datetime.datetime(int(str(row_pilot[6])[:4]), int(str(row_pilot[6])[4:6]) \
                                                    , int(str(row_pilot[6])[6:8]), int(str(row_pilot[6])[8:10]) \
                                                    , int(str(row_pilot[6])[10:12]), int(str(row_pilot[6])[12:14]))
                diff = datetime.datetime.utcnow() - start_connected
                col_time = QTableWidgetItem(str(diff).split('.')[0], 0)
                self.ui.PilottableWidget.setItem(startrow_pilot, 9, col_time)
                startrow_pilot += 1
                qApp.processEvents()

            for inbound in InboundTrafficAirport:
                self.ui.InboundTableWidget.insertRow(self.ui.InboundTableWidget.rowCount())
                col_callsign = QTableWidgetItem(str(inbound[0]), 0)
                self.ui.InboundTableWidget.setItem(startrow_in, 0, col_callsign)
                code_airline = inbound[0][:3]
                image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
                airlineCodePath = (image_airlines + '/%s.gif') % code_airline
                try:
                    if os.path.exists(airlineCodePath) is True:
                        Pixmap = QPixmap(airlineCodePath)
                        airline = QLabel(self)
                        airline.setPixmap(Pixmap)
                        self.ui.InboundTableWidget.setCellWidget(startrow_in, 0, airline)
                    else:
                        code_airline = str(inbound[0])
                        col_airline = QTableWidgetItem(code_airline, 0)
                        self.ui.InboundTableWidget.setItem(startrow_in, 0, col_airline)
                except:
                    pass
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(inbound[1]),))
                flagCode = Q_db.fetchone()
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath_orig = (image_flag + '/%s.png') % flagCode
                Pixmap = QPixmap(flagCodePath_orig)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.InboundTableWidget.setCellWidget(startrow_in, 1, flag_country)
                Q_db = self.sql_querys('Get_City', (str(inbound[1]),))
                city = Q_db.fetchone()
                col_city = ''
                if city == None:
                    col_city = 'Pending...'
                else:
                    col_city = str(city[0].encode('latin-1'))
                col_country = QTableWidgetItem(col_city, 0)
                self.ui.InboundTableWidget.setItem(startrow_in, 2, col_country)
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(inbound[2]),))
                flagCode = Q_db.fetchone()
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath_dest = (image_flag + '/%s.png') % flagCode
                Pixmap = QPixmap(flagCodePath_dest)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.InboundTableWidget.setCellWidget(startrow_in, 3, flag_country)
                Q_db = self.sql_querys('Get_City', (str(inbound[2]),))
                city = Q_db.fetchone()
                col_city = ''
                if city == None:
                    col_city = 'Pending...'
                else:
                    col_city = str(city[0].encode('latin-1'))
                col_country = QTableWidgetItem(col_city, 0)
                self.ui.InboundTableWidget.setItem(startrow_in, 4, col_country)
                if  flagCodePath_orig == flagCodePath_dest:
                    status_flight = 'National'
                else:
                    status_flight = 'International'
                col_flight = QTableWidgetItem(status_flight, 0)
                self.ui.InboundTableWidget.setItem(startrow_in, 5, col_flight)
                startrow_in += 1

            for outbound in OutboundTrafficAirport:
                self.ui.OutboundTableWidget.insertRow(self.ui.OutboundTableWidget.rowCount())
                col_callsign = QTableWidgetItem(str(outbound[0]), 0)
                self.ui.OutboundTableWidget.setItem(startrow_out, 0, col_callsign)
                code_airline = outbound[0][:3]
                image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
                airlineCodePath = (image_airlines + '/%s.gif') % code_airline
                try:
                    if os.path.exists(airlineCodePath) is True:
                        Pixmap = QPixmap(airlineCodePath)
                        airline = QLabel(self)
                        airline.setPixmap(Pixmap)
                        self.ui.OutboundTableWidget.setCellWidget(startrow_out, 0, airline)
                    else:
                        code_airline = str(outbound[0])
                        col_airline = QTableWidgetItem(code_airline, 0)
                        self.ui.OutboundTableWidget.setItem(startrow_out, 0, col_airline)
                except:
                    pass
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(outbound[1]),))
                flagCode = Q_db.fetchone()
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath_orig = (image_flag + '/%s.png') % flagCode
                Pixmap = QPixmap(flagCodePath_orig)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.OutboundTableWidget.setCellWidget(startrow_out, 1, flag_country)
                Q_db = self.sql_querys('Get_City', (str(outbound[1]),))
                city = Q_db.fetchone()
                col_city = ''
                if city == None:
                    col_city = 'Pending...'
                else:
                    col_city = str(city[0].encode('latin-1'))
                col_country = QTableWidgetItem(col_city, 0)
                self.ui.OutboundTableWidget.setItem(startrow_out, 2, col_country)
                Q_db = self.sql_querys('Get_Country_from_ICAO', (str(outbound[2]),))
                flagCode = Q_db.fetchone()
                image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath_dest = (image_flag + '/%s.png') % flagCode
                Pixmap = QPixmap(flagCodePath_dest)
                flag_country = QLabel()
                flag_country.setPixmap(Pixmap)
                self.ui.OutboundTableWidget.setCellWidget(startrow_out, 3, flag_country)
                Q_db = self.sql_querys('Get_City', (str(outbound[2]),))
                city = Q_db.fetchone()
                col_city = ''
                if city == None:
                    col_city = 'Pending...'
                else:
                    col_city = str(city[0].encode('latin-1'))
                col_country = QTableWidgetItem(col_city, 0)
                self.ui.OutboundTableWidget.setItem(startrow_out, 4, col_country)
                if  flagCodePath_orig == flagCodePath_dest:
                    status_flight = 'National'
                else:
                    status_flight = 'International'
                col_flight = QTableWidgetItem(status_flight, 0)
                self.ui.OutboundTableWidget.setItem(startrow_out, 5, col_flight)
                startrow_out += 1
            qApp.processEvents()
        self.ui.PilottableWidget.setCurrentCell(-1, -1)
        self.ui.ATCtableWidget.setCurrentCell(-1, -1)

    def get_color(self, status_plane):
        color = 'black'
        if status_plane == 'Boarding':
            color = 'green'
        if status_plane == 'Departing':
            color = 'green'
        if status_plane == 'Takeoff':
            color = 'dark cyan'
        if status_plane == 'Initial Climbing':
            color = 'dark cyan'
        if status_plane == 'Climbing':
            color = 'blue'
        if status_plane == 'On Route':
            color = 'dark blue'
        if status_plane == 'Descending':
            color = 'blue'
        if status_plane == 'Initial Approach':
            color = 'orange'
        if status_plane == 'Final Approach':
            color = 'orange'
        if status_plane == 'Landed':
            color = 'red'
        if status_plane == 'Taxing to Gate':
            color = 'dark magenta'
        if status_plane == 'On Blocks':
            color = 'dark red'
        if status_plane == 'Fill Flight Plan':
            color = 'black'
        if status_plane == 'Diverted':
            color = 'dark gray'
        return color

    def search_button(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        arg = self.ui.SearchEdit.text()
        item = self.ui.SearchcomboBox.currentIndex()

        if item == 0:
            cursor.execute("SELECT vid, callsign, realname, rating, clienttype from status_ivao where vid like ?;" \
                           , ('%'+str(arg)+'%',))
        elif item == 1:
            cursor.execute("SELECT vid, callsign, realname, rating, clienttype from status_ivao where callsign like ?;" \
                           , ('%'+str(arg)+'%',))
        elif item == 2:
            cursor.execute("SELECT vid, callsign, realname, rating, clienttype from status_ivao where realname like ?;" \
                           , ('%'+str(arg)+'%',))
        connection.commit()
        search = cursor.fetchall()

        self.ui.SearchtableWidget.insertRow(self.ui.SearchtableWidget.rowCount())
        while self.ui.SearchtableWidget.rowCount () > 0:
            self.ui.SearchtableWidget.removeRow(0)

        startrow = 0
        for row in search:
            self.ui.SearchtableWidget.insertRow(self.ui.SearchtableWidget.rowCount())
            col_vid = QTableWidgetItem(str(row[0]), 0)
            self.ui.SearchtableWidget.setItem(startrow, 0, col_vid)
            col_callsign = QTableWidgetItem(str(row[1]), 0)
            self.ui.SearchtableWidget.setItem(startrow, 1, col_callsign)
            if row[4] == 'PILOT':
                col_realname = QTableWidgetItem(str(row[2][:-4].encode('latin-1')), 0)
                self.ui.SearchtableWidget.setItem(startrow, 2, col_realname)
                player = 'pilot_level'
            else:
                col_realname = QTableWidgetItem(str(row[2].encode('latin-1')), 0)
                self.ui.SearchtableWidget.setItem(startrow, 2, col_realname)
                player = 'atc_level'
            ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
            ratingImagePath = ImagePath + '/%s%d.gif' % (player, int(row[3]))
            try:
                if os.path.exists(ratingImagePath) is True:
                    Pixmap = QPixmap(ratingImagePath)
                    ratingImage = QLabel(self)
                    ratingImage.setPixmap(Pixmap)
                    self.ui.SearchtableWidget.setCellWidget(startrow, 3, ratingImage)
                else:
                    pass
            except:
                pass

            startrow += 1
            qApp.processEvents()
        connection.close()

    def action_click(self, event=None):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        sender = self.sender()
        if self.ui.SearchtableWidget.currentRow() >= 0:
            row = self.ui.SearchtableWidget.currentIndex().row()
            if row == -1:
                pass
            else:
                current_row = self.ui.SearchtableWidget.currentRow()
                current_callsign = self.ui.SearchtableWidget.item(current_row, 1)
                self.ui.SearchtableWidget.setCurrentCell(-1, -1)
                cursor.execute('SELECT clienttype FROM status_ivao WHERE callsign=?;', ((str(current_callsign.text())),))
                clienttype = cursor.fetchone()
                if sender == self.showInfo_Action:
                    if str(clienttype[0]) == 'PILOT':
                        self.show_pilot_info(current_callsign.text())
                    if str(clienttype[0]) == 'FOLME':
                        self.show_followme_info(current_callsign.text())
                    if str(clienttype[0]) == 'ATC':
                        self.show_controller_info(current_callsign.text())
                if sender == self.showMap_Action:
                    cursor.execute('SELECT planned_depairport, planned_destairport FROM status_ivao WHERE callsign=?;' \
                                   , ((str(current_callsign.text())),))
                    icao_depdest = cursor.fetchall()
                    self.view_map(current_callsign.text(), icao_depdest[0][0], icao_depdest[0][1])
        if self.ui.ATC_FullList.currentRow() >= 0:
            row = self.ui.ATC_FullList.currentIndex().row()
            if row == -1:
                pass
            else:
                current_row = self.ui.ATC_FullList.currentRow()
                current_callsign = self.ui.ATC_FullList.item(current_row, 0)
                self.ui.ATC_FullList.setCurrentCell(-1, -1)
                if sender == self.showInfo_Action:
                    if current_callsign is None:
                        pass
                    else:
                        self.show_controller_info(current_callsign.text())
                if sender == self.showMap_Action:
                    self.view_map(current_callsign.text(), None, None)
        if self.ui.ATCtableWidget.currentRow() >= 0:
            row = self.ui.ATCtableWidget.currentIndex().row()
            if row == -1:
                pass
            else:
                current_row = self.ui.ATCtableWidget.currentRow()
                current_callsign = self.ui.ATCtableWidget.item(current_row, 0)
                if sender == self.showInfo_Action:
                    self.show_controller_info(current_callsign.text())
                if sender == self.showMap_Action:
                    self.view_map(current_callsign.text(), None, None)
                self.ui.ATCtableWidget.setCurrentCell(-1, -1)
        if self.ui.PILOT_FullList.currentRow() >= 0:
            row = self.ui.PILOT_FullList.currentIndex().row()
            if row == -1:
                pass
            else:
                current_row = self.ui.PILOT_FullList.currentRow()
                current_callsign = self.ui.PILOT_FullList.item(current_row, 1)
                cursor.execute('SELECT clienttype FROM status_ivao WHERE callsign=?;', ((str(current_callsign.text())),))
                clienttype = cursor.fetchone()
                current_row = self.ui.PILOT_FullList.currentRow()
                current_callsign = self.ui.PILOT_FullList.item(current_row, 1)
                if sender == self.showInfo_Action:
                    if str(clienttype[0]) == 'FOLME':
                        self.show_followme_info(current_callsign.text())
                    if str(clienttype[0]) == 'PILOT':
                        self.show_pilot_info(current_callsign.text())
                if sender == self.showMap_Action:
                    if str(clienttype[0]) == 'PILOT':
                        icao_orig = self.ui.PILOT_FullList.item(current_row, 6)
                        icao_dest = self.ui.PILOT_FullList.item(current_row, 7)
                        self.view_map(current_callsign.text(), icao_orig.text(), icao_dest.text())
                    if str(clienttype[0]) == 'FOLME':
                        pass
                self.ui.PILOT_FullList.setCurrentCell(-1, -1)
        if self.ui.PilottableWidget.currentRow() >= 0:
            row = self.ui.PilottableWidget.currentIndex().row()
            if row == -1:
                pass
            else:
                current_row = self.ui.PilottableWidget.currentRow()
                current_callsign = self.ui.PilottableWidget.item(current_row, 1)
                icao_orig = self.ui.PilottableWidget.item(current_row, 6)
                icao_dest = self.ui.PilottableWidget.item(current_row, 7)
                if sender == self.showInfo_Action:
                    self.show_pilot_info(current_callsign.text())
                if sender == self.showMap_Action:
                    self.view_map(current_callsign.text(), icao_orig.text(), icao_dest.text())
                self.ui.PilottableWidget.setCurrentCell(-1, -1)
        if self.ui.FriendstableWidget.currentRow() >= 0:
            current_row = self.ui.FriendstableWidget.currentIndex().row()
            current_vid = self.ui.FriendstableWidget.item(current_row, 0)
            cursor.execute('SELECT clienttype, callsign FROM status_ivao WHERE vid=?;', ((int(current_vid.text())),))
            friend_data = cursor.fetchall()
            if current_row == -1:
                pass
            else:
                try:
                    if sender == self.showInfo_Action:
                        if str(friend_data[0][0]) == 'PILOT':
                            self.show_pilot_info(str(friend_data[0][1]))
                        if str(friend_data[0][0]) == 'FOLME':
                            self.show_followme_info(str(friend_data[0][1]))
                        if str(friend_data[0][0]) == 'ATC':
                            self.show_controller_info(str(friend_data[0][1]))
                    if sender == self.showMap_Action:
                        cursor.execute('SELECT planned_depairport, planned_destairport FROM status_ivao WHERE callsign=?;' \
                                       , ((str(friend_data[0][1])),))
                        icao_depdest = cursor.fetchall()
                        self.view_map(str(friend_data[0][1]), icao_depdest[0][0], icao_depdest[0][1])
                    if sender == self.showDelete_Action:
                        cursor.execute('DELETE FROM friends_ivao WHERE vid=?;', (int(current_vid.text()),))
                        self.statusBar().showMessage('Friend Deleted', 2000)
                        connection.commit()
                        connection.close()
                        self.ivao_friend()
                except:
                    if friend_data == []:
                        msg = "The user %d is off-line, can't see any info" % (int(current_vid.text()))
                        QMessageBox.information(None, 'Friends List', msg)

    def ivao_friend(self):
        self.ui.PILOT_FullList.setCurrentCell(-1, -1)
        self.ui.ATC_FullList.setCurrentCell(-1, -1)
        self.ui.PilottableWidget.setCurrentCell(-1, -1)
        self.ui.ATCtableWidget.setCurrentCell(-1, -1)
        self.ui.SearchtableWidget.setCurrentCell(-1, -1)
        self.ui.FriendstableWidget.setCurrentCell(-1, -1)
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute('SELECT vid, realname, rating, clienttype FROM friends_ivao;')
        roster = cursor.fetchall()
        self.ui.FriendstableWidget.insertRow(self.ui.FriendstableWidget.rowCount())
        while self.ui.FriendstableWidget.rowCount () > 0:
            self.ui.FriendstableWidget.removeRow(0)

        startrow = 0
        roster_row = 0
        for row in roster:
            self.ui.FriendstableWidget.insertRow(self.ui.FriendstableWidget.rowCount())
            col_vid = QTableWidgetItem(str(row[0]), 0)
            self.ui.FriendstableWidget.setItem(startrow, 0, col_vid)
            cursor.execute('SELECT vid FROM status_ivao where vid=?;', (int(row[0]),))
            check = cursor.fetchone()
            try:
                if check[0] == row[0]:
                    ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'airplane_online.png')
                    Pixmap = QPixmap(ImagePath)
                    online = QLabel(self)
                    online.setPixmap(Pixmap)
                    self.ui.FriendstableWidget.setCellWidget(startrow, 3, online)
                    roster_row += 1
            except:
                ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'airplane_offline.png')
                Pixmap = QPixmap(ImagePath)
                offline = QLabel(self)
                offline.setPixmap(Pixmap)
                self.ui.FriendstableWidget.setCellWidget(startrow, 3, offline)
                roster_row += 1
            col_realname = QTableWidgetItem(str(row[1].encode('latin-1')), 0)
            self.ui.FriendstableWidget.setItem(startrow, 1, col_realname)
            ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
            if str(row[2]) != '-':
                if str(row[3]) == 'ATC':
                    ratingImagePath = ImagePath + '/atc_level%d.gif' % int(row[2])
                else:
                    ratingImagePath = ImagePath + '/pilot_level%d.gif' % int(row[2])
                Pixmap = QPixmap(ratingImagePath)
                ratingImage = QLabel(self)
                ratingImage.setPixmap(Pixmap)
                col_rating = self.ui.FriendstableWidget.setCellWidget(startrow, 2, ratingImage)
            else:
                col_rating = QTableWidgetItem('-', 0)
                self.ui.FriendstableWidget.setItem(startrow, 2, col_rating)
            startrow += 1
        qApp.processEvents()
        connection.close()

    def metar(self):
        self.statusBar().showMessage('Downloading METAR', 2000)
        qApp.processEvents()
        icao_airport = self.ui.METAREdit.text()
        try:
            METAR = urllib2.urlopen('http://wx.ivao.aero/metar.php?id=%s' % icao_airport)

            if self.ui.METARtableWidget.rowCount() == 0:
                self.ui.METARtableWidget.insertRow(self.ui.METARtableWidget.rowCount())
                col_icao_airport = QTableWidgetItem(str(icao_airport), 0)
                self.ui.METARtableWidget.setItem(0, 0, col_icao_airport)
                col_metar = QTableWidgetItem(str(METAR.readlines()[0]), 0)
                self.ui.METARtableWidget.setItem(0, 1, col_metar)
                startrow = 1
            else:
                self.ui.METARtableWidget.rowCount() > 0
                startrow = self.ui.METARtableWidget.rowCount()
                self.ui.METARtableWidget.insertRow(self.ui.METARtableWidget.rowCount())
                col_icao_airport = QTableWidgetItem(str(icao_airport), 0)
                self.ui.METARtableWidget.setItem(startrow, 0, col_icao_airport)
                col_metar = QTableWidgetItem(str(METAR.readlines()[0]), 0)
                self.ui.METARtableWidget.setItem(startrow, 1, col_metar)
                startrow += 1
        except:
            self.statusBar().showMessage('Error! during try get Metar info, check your internet connection...', 4000)

    def view_map(self, vid, icao_orig=None, icao_dest=None):
        self.statusBar().showMessage('Showing player in Map', 4000)
        qApp.processEvents()
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT longitude, latitude FROM icao_codes WHERE ICAO=?;", (str(icao_orig),))
        icao_orig = cursor.fetchone()
        cursor.execute("SELECT longitude, latitude FROM icao_codes WHERE ICAO=?;", (str(icao_dest),))
        icao_dest = cursor.fetchone()
        cursor.execute("SELECT latitude, longitude, callsign, true_heading, clienttype FROM status_ivao WHERE callsign=?;" \
                       ,  (str(vid),))
        player = cursor.fetchall()
        latitude, longitude, heading = player[0][0], player[0][1], player[0][3]
        mapfileplayer_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        images = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
        player_location = open(mapfileplayer_path +'/player_location.html', 'w')
        player_location.write('<html><body>\n')
        player_location.write('  <div id="mapdiv"></div>\n')
        player_location.write('  <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAAjpkAC9ePGem0lIq5XcMiuhR_wWLPFku8Ix9i2SXYRVK3e45q1BQUd_beF8dtzKET_EteAjPdGDwqpQ"></script>\n')
        player_location.write('  <script src="%s/OpenLayers/OpenLayers.js"></script>\n' % (mapfileplayer_path))
        player_location.write('  <script>\n')
        player_location.write('\n')
        player_location.write('    map = new OpenLayers.Map("mapdiv",\n')
        player_location.write('             {   projection : new OpenLayers.Projection("EPSG:900913"),\n')
        player_location.write('                 maxResolution:156543.0339,\n')
        player_location.write('                 maxExtent:new OpenLayers.Bounds(-20037508, -20037508,20037508, 20037508.34)\n')
        player_location.write('             });\n')
        player_location.write('\n')
        player_location.write('    ghyb = new OpenLayers.Layer.Google(\n')
        player_location.write('         "Google Satellite",\n')
        player_location.write('         {type: G_HYBRID_MAP, sphericalMercator:true, numZoomLevels: 22}\n')
        player_location.write('         );\n')
        player_location.write('\n')
        player_location.write('    map.addLayers([ghyb]);\n')
        player_location.write('\n')
        player_location.write('    var position = new OpenLayers.LonLat( %f, %f )\n' % (longitude, latitude))
        player_location.write('         .transform(\n')
        player_location.write('            new OpenLayers.Projection("EPSG:4326"),\n')
        player_location.write('            map.getProjectionObject()\n')
        player_location.write('            );\n')
        if str(player[0][2][-4:]) == "_GND":
            player_location.write('    var zoom = 15;\n')
        if str(player[0][2][-4:]) == "_DEP":
            player_location.write('    var zoom = 15;\n')
        if str(player[0][2][-4:]) == "_TWR":
            player_location.write('    var zoom = 14;\n')
        if str(player[0][2][-4:]) == "_APP":
            player_location.write('    var zoom = 13;\n')
        if str(player[0][2][-4:]) == '_OBS':
            player_location.write('    var zoom = 12;\n')
        if str(player[0][2][-4:]) == '_CTR':
            player_location.write('    var zoom = 5;\n')
        if player[0][4] == 'PILOT':
            player_location.write('    var zoom = 5;\n')
        player_location.write('    var player=new OpenLayers.Layer.Vector("Player",\n')
        player_location.write('    {\n')
        player_location.write('    styleMap: new OpenLayers.StyleMap({\n')
        player_location.write('         "default": {\n')
        if player[0][4] == 'PILOT':
            player_location.write('         externalGraphic: "./images/airplane.gif",\n')
        else:
            player_location.write('         externalGraphic: "./images/tower.png",\n')
        player_location.write('         graphicWidth: 20,\n')
        player_location.write('         graphicHeight: 20,\n')
        player_location.write('         graphicYOffset: 0,\n')
        player_location.write('         rotation: "${angle}",\n')
        if player[0][4] == 'ATC':
            player_location.write('         fillColor: "white",\n')
            player_location.write('         strokeColor: "white",\n')
            player_location.write('         fillOpacity: "0.05",\n')
        else:
            player_location.write('         fillOpacity: "${opacity}",\n')
        player_location.write('         label: "%s",\n' % str(player[0][2]))
        player_location.write('         fontColor: "white",\n')
        player_location.write('         fontSize: "10px",\n')
        player_location.write('         fontFamily: "Courier New, monospace",\n')
        player_location.write('         labelAlign: "cm",\n')
        player_location.write('         labelXOffset: 30,\n')
        player_location.write('         labelYOffset: 5\n')
        if str(player[0][2][-4:]) == '_CTR':
            player_location.write('         }\n')
            player_location.write('      })\n')
            player_location.write('   });\n\n')
            player_location.write('   var vectorLayer = new OpenLayers.Layer.Vector("Vector Layer");\n')
            player_location.write('   var style_controller = {\n')
            player_location.write('       strokeColor: "white",\n')
            player_location.write('       strokeOpacity: 1.0,\n')
            player_location.write('       strokeWidth: 2,\n')
            player_location.write('       label: "%s",\n' % str(player[0][2]))
            player_location.write('       fontWeight: "bold",\n')
            player_location.write('       fontColor: "white",\n')
            player_location.write('       fontSize: "12px",\n')
            player_location.write('       fontFamily: "Courier New, monospace",\n')
            player_location.write('       labelAlign: "cm",\n')
            player_location.write('       labelXOffset: 30,\n')
            player_location.write('       labelYOffset: 5\n')
            player_location.write('   };\n\n')
            try:
                cursor.execute("SELECT ID_FIRCOASTLINE FROM fir_data_list WHERE ICAO = ?;", (str(player[0][2][:-4]),))
                id_ctr = cursor.fetchone()
                if id_ctr is None:
                    cursor.execute("SELECT ID_FIRCOASTLINE FROM fir_data_list WHERE ICAO = ?;", (str(player[0][2][:4]),))
                    id_ctr = cursor.fetchone()
            except:
                pass
            cursor.execute("SELECT Longitude, Latitude FROM fir_coastlines_list where ID_FIRCOASTLINE = ?;", (int(id_ctr[0]),))
            points_ctr = cursor.fetchall()
            player_location.write('    var points = [];\n')
            for position in range(0, len(points_ctr)):
                player_location.write('    var point_orig = new OpenLayers.Geometry.Point(%f, %f);\n'
                                     % (points_ctr[position][0], points_ctr[position][1]))
                if position == len(points_ctr) - 1:
                    continue
                else:
                    player_location.write('    var point_dest = new OpenLayers.Geometry.Point(%f, %f);\n'
                                         % (points_ctr[position+1][0], points_ctr[position+1][1]))
                    player_location.write('    points.push(point_orig);\n')
                    player_location.write('    points.push(point_dest);\n')
            player_location.write('\n')
            player_location.write('    var player_String = new OpenLayers.Geometry.LineString(points);\n')
            player_location.write('    player_String.transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());\n')
            player_location.write('    var DrawFeature = new OpenLayers.Feature.Vector(player_String, null, style_controller);\n')
            player_location.write('    vectorLayer.addFeatures([DrawFeature]);\n')
            player_location.write('    map.addLayer(vectorLayer);\n')
            player_location.write('    map.addLayer(player);\n')
        else:
            player_location.write('         }\n')
            player_location.write('      })\n')
            player_location.write('   });\n')
            if str(player[0][4]) == 'ATC':
                player_location.write('   var ratio = OpenLayers.Geometry.Polygon.createRegularPolygon(\n')
                player_location.write('     new OpenLayers.Geometry.Point(position.lon, position.lat),\n')
                if str(player[0][2][-4:]) == '_OBS' or str(player[0][2][-4:]) == '_DEP' or str(player[0][2][-4:]) == '_GND':
                    player_location.write('        20000,\n')
                elif str(player[0][2][-4:]) == '_TWR':
                    player_location.write('        40000,\n')
                elif str(player[0][2][-4:]) == '_APP':
                    player_location.write('        60000,\n')
                player_location.write('        360\n')
                player_location.write('     );\n')
                player_location.write('   var controller_ratio = new OpenLayers.Feature.Vector(ratio);\n')
                player_location.write('   player.addFeatures([controller_ratio]);\n')
            player_location.write('\n')
            if str(player[0][4]) == 'PILOT':
                player_location.write('    var vectorLayer = new OpenLayers.Layer.Vector("Vector Layer");\n')
                player_location.write('    var style_green = {\n')
                player_location.write('     strokeColor: "#00FF00",\n')
                player_location.write('     strokeOpacity: 0.7,\n')
                player_location.write('     strokeWidth: 2\n')
                player_location.write('    };\n')
                player_location.write('    var style_red = {\n')
                player_location.write('     strokeColor: "#FF0000",\n')
                player_location.write('     strokeOpacity: 0.7,\n')
                player_location.write('     strokeWidth: 2\n')
                player_location.write('    };\n')
                if icao_orig is None or icao_dest is None:
                    player_location.write('    var points = [];\n')
                    player_location.write('    var point_plane = new OpenLayers.Geometry.Point(%f, %f);\n' % (longitude, latitude))
                    player_location.write('    points.push(point_plane);\n')
                else:
                    player_location.write('    var points_green = [];\n')
                    player_location.write('    var point_orig = new OpenLayers.Geometry.Point(%f, %f);\n' % (icao_orig[0], icao_orig[1]))
                    player_location.write('    var point_orig_f = new OpenLayers.Geometry.Point(%f, %f);\n' % (longitude, latitude))
                    player_location.write('\n')
                    player_location.write('    var points_red = [];\n')
                    player_location.write('    var point_dest = new OpenLayers.Geometry.Point(%f, %f);\n' % (longitude, latitude))
                    player_location.write('    var point_dest_f = new OpenLayers.Geometry.Point(%f, %f);\n' % (icao_dest[0], icao_dest[1]))
                    player_location.write('\n')
                    player_location.write('    points_green.push(point_orig);\n')
                    player_location.write('    points_green.push(point_orig_f);\n')
                    player_location.write('\n')
                    player_location.write('    points_red.push(point_dest);\n')
                    player_location.write('    points_red.push(point_dest_f);\n')
                player_location.write('\n')
                if icao_orig is None or icao_dest is None:
                    player_location.write('    var lineString = new OpenLayers.Geometry.LineString(points);\n')
                    player_location.write('    lineString.transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject()); \n')
                else:
                    player_location.write('    var lineString_green = new OpenLayers.Geometry.LineString(points_green);\n')
                    player_location.write('    lineString_green.transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject()); \n')
                    player_location.write('    var lineString_red = new OpenLayers.Geometry.LineString(points_red);\n')
                    player_location.write('    lineString_red.transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject()); \n')
                player_location.write('\n')
                if icao_orig is None or icao_dest is None:
                    player_location.write('    var lineFeature = new OpenLayers.Feature.Vector(lineString, null, null);\n')
                    player_location.write('    vectorLayer.addFeatures([lineFeature]);\n')
                else:
                    player_location.write('    var lineFeature_green = new OpenLayers.Feature.Vector(lineString_green, null, style_green);\n')
                    player_location.write('    var lineFeature_red = new OpenLayers.Feature.Vector(lineString_red, null, style_red);\n')
                    player_location.write('    vectorLayer.addFeatures([lineFeature_green, lineFeature_red]);\n')
                player_location.write('\n')
                player_location.write('   map.addLayer(vectorLayer);\n')
                player_location.write('\n')
            player_location.write('   var feature=new OpenLayers.Feature.Vector(\n')
            if str(player[0][4]) == 'PILOT':
                player_location.write('     new OpenLayers.Geometry.Point(position.lon, position.lat), {"angle": %d, opacity: 100});\n'
                                      % (heading))
            else:
                player_location.write('     new OpenLayers.Geometry.Point(position.lon, position.lat), {"angle": 0, opacity: 100});\n')
            player_location.write('   player.addFeatures([feature]);\n')
            player_location.write('   map.addLayer(player);\n')
            player_location.write('\n')
        player_location.write('   map.setCenter (position, zoom);\n')
        player_location.write('  </script>\n')
        player_location.write('</body></html>\n')
        player_location.close()
        mapfileplayer_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.maptab.load(QUrl(mapfileplayer_path + '/player_location.html'))

    def metarHelp(self):
        msg = 'Must be entered 4-character alphanumeric code designated for each airport around the world'
        QMessageBox.information(None, 'METAR Help', msg)

    def about(self):
        QMessageBox.about(self, "About IVAO :: Status",
                          """<b>IVAO::Status</b>  version %s<p>License: GPL version 3+<p>
                          This Aplication can be used to see IVAO operational network.<p>
                          July 2011 Tony (emper0r) P. Diaz  --  emperor.cu@gmail.com<p>
                          IVAO User: 304605"""
                          % (__version__))

    def show_pilot_info(self, callsign):
        self.pilot_window = PilotInfo()
        self.pilot_window.status(callsign)
        self.pilot_window.closed.connect(self.show)
        self.pilot_window.show()

    def show_controller_info(self, callsign):
        self.controller_window = ControllerInfo()
        self.controller_window.status(callsign)
        self.controller_window.closed.connect(self.show)
        self.controller_window.show()

    def show_followme_info(self, callsign):
        self.followme_window = FollowMeService()
        self.followme_window.status(callsign)
        self.followme_window.closed.connect(self.show)
        self.followme_window.show()

    def show_settings(self):
        self.setting_window = Settings(self)
        self.setting_window.closed.connect(self.show)
        self.setting_window.show()

    def all2map(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        label_Pilots = config.getint('Map', 'label_Pilots')
        label_ATCs = config.getint('Map', 'label_ATCs')
        cursor = connection.cursor()
        cursor.execute("SELECT longitude, latitude, callsign, true_heading, clienttype FROM status_ivao;")
        players = cursor.fetchall()
        self.statusBar().showMessage('Populating all players in the Map', 10000)
        qApp.processEvents()
        mapfileall_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        images = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
        all_in_map = open(mapfileall_path + '/all_in_map.html', 'w')
        all_in_map.write('<html><body>\n')
        all_in_map.write('  <div id="mapdiv"></div>\n')
        all_in_map.write('  <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAAjpkAC9ePGem0lIq5XcMiuhR_wWLPFku8Ix9i2SXYRVK3e45q1BQUd_beF8dtzKET_EteAjPdGDwqpQ"></script>\n')
        all_in_map.write('  <script src="%s/OpenLayers/OpenLayers.js"></script>\n' % (mapfileall_path))
        all_in_map.write('  <script>\n')
        all_in_map.write('\n')
        all_in_map.write('    map = new OpenLayers.Map("mapdiv",\n')
        all_in_map.write('             {   projection : new OpenLayers.Projection("EPSG:900913"),\n')
        all_in_map.write('                 maxResolution:156543.0339,\n')
        all_in_map.write('                 maxExtent:new OpenLayers.Bounds(-20037508, -20037508, 20037508, 20037508.34)\n')
        all_in_map.write('             });\n')
        all_in_map.write('    ghyb = new OpenLayers.Layer.Google(\n')
        all_in_map.write('         "Google Satellite",\n')
        all_in_map.write('         {type: G_SATELLITE_MAP, sphericalMercator:true, numZoomLevels: 22}\n')
        all_in_map.write('         );\n')
        all_in_map.write('\n')
        all_in_map.write('    map.addLayers([ghyb]);\n')
        all_in_map.write('\n')
        for callsign in range(0, len(players)):
            if str(players[callsign][4]) == 'PILOT':
                if (str(players[callsign][0]) and str(players[callsign][1])) == '':
                    pass
                elif players[callsign][2] is None or players[callsign][3] is None:
                    pass
                else:
                    all_in_map.write('    var position = new OpenLayers.LonLat( %f, %f )\n' % \
                                     (float(players[callsign][0]), float(players[callsign][1])))
                    all_in_map.write('         .transform(\n')
                    all_in_map.write('            new OpenLayers.Projection("EPSG:4326"),\n')
                    all_in_map.write('            map.getProjectionObject()\n')
                    all_in_map.write('            );\n')
                    all_in_map.write('\n')
                    all_in_map.write('    var player_%s=new OpenLayers.Layer.Vector("Player",\n' % str(players[callsign][2]))
                    all_in_map.write('    {\n')
                    all_in_map.write('      styleMap: new OpenLayers.StyleMap({\n')
                    all_in_map.write('         "default": {\n')
                    all_in_map.write('          externalGraphic: "' + images + '/airplane.gif",\n')
                    all_in_map.write('          graphicWidth: 15,\n')
                    all_in_map.write('          graphicHeight: 15,\n')
                    all_in_map.write('          graphicYOffset: 0,\n')
                    all_in_map.write('          rotation: "${angle}",\n')
                    all_in_map.write('          fillOpacity: 100,\n')
                    if label_Pilots == 2:
                        all_in_map.write('          label: "%s",\n' % str(players[callsign][2]))
                        all_in_map.write('          fontColor: "yellow",\n')
                        all_in_map.write('          fontSize: "10px",\n')
                        all_in_map.write('          fontFamily: "Courier New, monospace",\n')
                        all_in_map.write('          labelAlign: "cm",\n')
                        all_in_map.write('          labelXOffset: 30,\n')
                        all_in_map.write('          labelYOffset: 5\n')
                    all_in_map.write('         }\n')
                    all_in_map.write('      })\n')
                    all_in_map.write('   });\n')
                    all_in_map.write('\n')
                    all_in_map.write('    var feature = new OpenLayers.Feature.Vector(\n')
                    all_in_map.write('      new OpenLayers.Geometry.Point( position.lon, position.lat), {"angle": %d});\n'
                                     % int(players[callsign][3]))
                    all_in_map.write('    player_%s.addFeatures([feature]);\n' % str(players[callsign][2]).replace('-',''))
                    all_in_map.write('    map.addLayer(player_%s);\n' % str(players[callsign][2]).replace('-',''))
                    all_in_map.write('\n')
            if str(players[callsign][4]) == 'ATC':
                if players[callsign][0] == '' or players[callsign][1] == '':
                    continue
            if str(players[callsign][2][-4:]) == '_OBS' \
               or str(players[callsign][4][-4:]) == '_DEP' or str(players[callsign][2][-4:]) == '_GND' \
               or str(players[callsign][2][-4:]) == '_TWR' or str(players[callsign][2][-4:]) == '_APP':
                if players[callsign][0] is None:
                    continue
                all_in_map.write('    var position = new OpenLayers.LonLat( %f, %f )\n' % \
                                 (float(players[callsign][0]), float(players[callsign][1])))
                all_in_map.write('         .transform(\n')
                all_in_map.write('            new OpenLayers.Projection("EPSG:4326"),\n')
                all_in_map.write('            map.getProjectionObject()\n')
                all_in_map.write('            );\n')
                all_in_map.write('\n')
                all_in_map.write('    var player_%s = new OpenLayers.Layer.Vector("Player",\n' % str(players[callsign][2]).replace('-',''))
                all_in_map.write('    {\n')
                all_in_map.write('    styleMap: new OpenLayers.StyleMap({\n')
                all_in_map.write('         "default": {\n')
                all_in_map.write('         externalGraphic: "' + images + '/tower.png",\n')
                all_in_map.write('         rotation: "${angle}",\n')
                all_in_map.write('         graphicWidth: 15,\n')
                all_in_map.write('         graphicHeight: 15,\n')
                all_in_map.write('         graphicYOffset: 0,\n')
                if str(players[callsign][2][-4:]) == '_OBS' or str(players[callsign][4][-4:]) == '_DEP' \
                   or str(players[callsign][2][-4:]) == '_GND':
                    all_in_map.write('         fillColor: "white",\n')
                    all_in_map.write('         strokeColor: "white",\n')
                elif str(players[callsign][2][-4:]) == '_TWR':
                    all_in_map.write('         fillColor: "white",\n')
                    all_in_map.write('         strokeColor: "white",\n')
                elif str(players[callsign][2][-4:]) == '_APP':
                    all_in_map.write('         fillColor: "white",\n')
                    all_in_map.write('         strokeColor: "white",\n')
                all_in_map.write('         fillOpacity: "0.2",\n')
                if label_ATCs == 2:
                    all_in_map.write('         label: "%s",\n' % str(players[callsign][2]))
                    all_in_map.write('         fontColor: "white",\n')
                    all_in_map.write('         fontSize: "10px",\n')
                    all_in_map.write('         fontFamily: "Courier New, monospace",\n')
                    all_in_map.write('         labelAlign: "cm",\n')
                    all_in_map.write('         labelXOffset: 30,\n')
                    all_in_map.write('         labelYOffset: 5\n')
                all_in_map.write('         }\n')
                all_in_map.write('       })\n')
                all_in_map.write('    });\n')
                all_in_map.write('\n')
                all_in_map.write('     var ratio = OpenLayers.Geometry.Polygon.createRegularPolygon(\n')
                all_in_map.write('        new OpenLayers.Geometry.Point(position.lon, position.lat),\n')
                if str(players[callsign][2][-4:]) == '_OBS' or str(players[callsign][4][-4:]) == '_DEP' \
                   or str(players[callsign][2][-4:]) == '_GND':
                    all_in_map.write('        20000,\n')
                elif str(players[callsign][2][-4:]) == '_TWR':
                    all_in_map.write('        40000,\n')
                elif str(players[callsign][2][-4:]) == '_APP':
                    all_in_map.write('        60000,\n')
                all_in_map.write('        360\n')
                all_in_map.write('    );\n')
                all_in_map.write('    var controller_ratio = new OpenLayers.Feature.Vector(ratio);\n')
                all_in_map.write('    player_%s.addFeatures([controller_ratio]);\n' % str(players[callsign][2]).replace('-',''))
                all_in_map.write('\n')
                all_in_map.write('    var feature = new OpenLayers.Feature.Vector(\n')
                all_in_map.write('        new OpenLayers.Geometry.Point( position.lon, position.lat), {"angle": 0, opacity: 100});\n')
                all_in_map.write('    player_%s.addFeatures([feature]);\n' % str(players[callsign][2]).replace('-',''))
                all_in_map.write('\n')
                all_in_map.write('    map.addLayer(player_%s);\n' % str(players[callsign][2]).replace('-',''))
                all_in_map.write('\n')
            if str(players[callsign][2][-4:]) == '_CTR':
                cursor.execute("SELECT Latitude, Longitude FROM fir_data_list WHERE ICAO = ?;", (str(players[callsign][2][:4]),))
                position = cursor.fetchall()
                all_in_map.write('    var position = new OpenLayers.LonLat( %f, %f )\n'
                                 % (float(position[0][0]), float(position[0][1])))
                all_in_map.write('    var player_%s = new OpenLayers.Layer.Vector("Player",\n' % str(players[callsign][2]).replace('-',''))
                all_in_map.write('    {\n')
                all_in_map.write('    styleMap: new OpenLayers.StyleMap({\n')
                all_in_map.write('         "default": {\n')
                all_in_map.write('         externalGraphic: "' + images + '/images/tower.png",\n')
                all_in_map.write('         rotation: "${angle}",\n')
                all_in_map.write('         fillOpacity: "1.00",\n')
                all_in_map.write('         }\n')
                all_in_map.write('       })\n')
                all_in_map.write('    });\n')
                all_in_map.write('\n')
                all_in_map.write('    var vectorLayer = new OpenLayers.Layer.Vector("Vector Layer");\n')
                all_in_map.write('    var style_controller = {\n')
                all_in_map.write('        strokeColor: "white",\n')
                all_in_map.write('        strokeOpacity: 1.0,\n')
                all_in_map.write('        strokeWidth: 2,\n')
                if label_ATCs == 2:
                    all_in_map.write('        label: "%s",\n' % str(players[callsign][2]))
                    all_in_map.write('        fontColor: "white",\n')
                    all_in_map.write('        fontSize: "12px",\n')
                    all_in_map.write('        fontWeight: "bold",\n')
                    all_in_map.write('        fontFamily: "Courier New, monospace",\n')
                    all_in_map.write('        labelAlign: "cm",\n')
                    all_in_map.write('        labelXOffset: 30,\n')
                    all_in_map.write('        labelYOffset: 5\n')
                all_in_map.write('    };\n\n')
                try:
                    cursor.execute("SELECT ID_FIRCOASTLINE FROM fir_data_list WHERE ICAO = ?;", (str(players[callsign][2][:-4]),))
                    id_ctr = cursor.fetchone()
                    if id_ctr is None:
                        cursor.execute("SELECT ID_FIRCOASTLINE FROM fir_data_list WHERE ICAO = ?;", (str(players[callsign][2][:4]),))
                        id_ctr = cursor.fetchone()
                except:
                    pass
                cursor.execute("SELECT Longitude, Latitude FROM fir_coastlines_list where ID_FIRCOASTLINE = ?;", (int(id_ctr[0]),))
                points_ctr = cursor.fetchall()
                all_in_map.write('    var points = [];\n')
                for position in range(0, len(points_ctr)):
                    all_in_map.write('    var point_orig = new OpenLayers.Geometry.Point(%f, %f);\n'
                                     % (points_ctr[position][0], points_ctr[position][1]))
                    if position == len(points_ctr) - 1:
                        continue
                    else:
                        all_in_map.write('    var point_dest = new OpenLayers.Geometry.Point(%f, %f);\n'
                                         % (points_ctr[position+1][0], points_ctr[position+1][1]))
                    all_in_map.write('    points.push(point_orig);\n')
                    all_in_map.write('    points.push(point_dest);\n')
                all_in_map.write('\n')
                all_in_map.write('    var %s_String = new OpenLayers.Geometry.LineString(points);\n'
                                 % str(players[callsign][2][:-4]))
                all_in_map.write('    %s_String.transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());\n'
                                 % str(players[callsign][2][:-4]))
                all_in_map.write('\n')
                all_in_map.write('    var DrawFeature = new OpenLayers.Feature.Vector(%s_String, null, style_controller);\n'
                                 % str(players[callsign][2][:-4]))
                all_in_map.write('    vectorLayer.addFeatures([DrawFeature]);\n')
                all_in_map.write('    map.addLayer(vectorLayer);\n')
                all_in_map.write('    map.addLayer(player_%s);\n' % str(players[callsign][2]).replace('-',''))
        all_in_map.write('   map.setCenter ((0, 0), 2);\n')
        all_in_map.write('  </script>\n')
        all_in_map.write('</body></html>\n')
        all_in_map.close()
        mapfileall_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.maptab.load(QUrl(mapfileall_path + '/all_in_map.html'))

    def statistics(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        item = self.ui.comboBoxStatistics.currentIndex()
        qApp.processEvents()

        if item == 0:
            self.statusBar().showMessage('Counting...', 2000)
            qApp.processEvents()
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0

            cursor.execute("SELECT callsign FROM status_ivao WHERE clienttype='ATC';" )
            controller_list = cursor.fetchall()

            list_all = []
            for callsign in range(0, len(controller_list)):
                if controller_list[callsign][0][2:3] == '-' or controller_list[callsign][0][2:3] == '_':
                    cursor.execute("SELECT Country FROM division_ivao WHERE division = ?;", (str(controller_list[callsign][0])[:2],))
                else:
                    cursor.execute("SELECT Country FROM icao_codes WHERE ICAO = ?;", (str(controller_list[callsign][0])[:4],))
                country_icao = cursor.fetchone()
                if country_icao is None:
                    continue
                else:
                    list_all.append(str(country_icao[0]))

            cursor.execute("SELECT realname FROM status_ivao WHERE clienttype='PILOT';" )
            pilot_list = cursor.fetchall()

            for callsign in range(0, len(pilot_list)):
                if pilot_list[callsign][0][-4:]:
                    cursor.execute("SELECT Country FROM icao_codes WHERE ICAO = ?;",
                                   (str(pilot_list[callsign][0].encode('latin-1'))[-4:],))
                country_icao = cursor.fetchone()
                if country_icao is None:
                    continue
                else:
                    list_all.append(str(country_icao[0]))

            all_countries = {}
            for item_list in set(list_all):
                all_countries[item_list] = list_all.count(item_list)

            for country in sorted(all_countries, key=all_countries.__getitem__, reverse=True):
                if country[0] == 0:
                    continue
                else:
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                    flagCodePath = (image_flag + '/%s.png') % country
                    if os.path.exists(flagCodePath) is True:
                        Pixmap = QPixmap(flagCodePath)
                        flag_country = QLabel()
                        flag_country.setPixmap(Pixmap)
                        self.ui.Statistics.setCellWidget(startrow, 0, flag_country)
                    else:
                        pass
                    col_item = QTableWidgetItem(str('%s' % (country)), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(all_countries[country])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(all_countries[country]) / float(len(list_all)) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 1:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0

            cursor.execute("SELECT callsign FROM status_ivao WHERE clienttype='ATC';" )
            controller_list = cursor.fetchall()

            list_icao = []
            for callsign in range(0, len(controller_list)):
                if controller_list[callsign][0][2:3] == '-' or controller_list[callsign][0][2:3] == '_':
                    cursor.execute("SELECT Country FROM division_ivao WHERE division = ?;", (str(controller_list[callsign][0])[:2],))
                else:
                    cursor.execute("SELECT Country FROM icao_codes WHERE ICAO = ?;", (str(controller_list[callsign][0])[:4],))
                country_icao = cursor.fetchone()
                if country_icao is None:
                    continue
                else:
                    list_icao.append(str(country_icao[0]))

            countries = {}
            for item_list in set(list_icao):
                countries[item_list] = list_icao.count(item_list)

            for country in sorted(countries, key=countries.__getitem__, reverse=True):
                if country[0] == 0:
                    continue
                else:
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                    flagCodePath = (image_flag + '/%s.png') % country
                    if os.path.exists(flagCodePath) is True:
                        Pixmap = QPixmap(flagCodePath)
                        flag_country = QLabel()
                        flag_country.setPixmap(Pixmap)
                        self.ui.Statistics.setCellWidget(startrow, 0, flag_country)
                    else:
                        pass
                    col_item = QTableWidgetItem(str('%s' % (country)), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(countries[country])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(countries[country]) / float(len(controller_list)) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 2:
            self.statusBar().showMessage('Counting...', 2000)
            qApp.processEvents()
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0

            cursor.execute("SELECT realname FROM status_ivao WHERE clienttype='PILOT';" )
            pilot_list = cursor.fetchall()

            list_icao = []
            for callsign in range(0, len(pilot_list)):
                if pilot_list[callsign][0][-4:]:
                    cursor.execute("SELECT Country FROM icao_codes WHERE ICAO = ?;",
                                   (str(pilot_list[callsign][0].encode('latin-1'))[-4:],))
                country_icao = cursor.fetchone()
                if country_icao is None:
                    continue
                else:
                    list_icao.append(str(country_icao[0]))

            countries = {}
            for item_list in set(list_icao):
                countries[item_list] = list_icao.count(item_list)

            for country in sorted(countries, key=countries.__getitem__, reverse=True):
                if country[0] == 0:
                    continue
                else:
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                    flagCodePath = (image_flag + '/%s.png') % country
                    if os.path.exists(flagCodePath) is True:
                        Pixmap = QPixmap(flagCodePath)
                        flag_country = QLabel()
                        flag_country.setPixmap(Pixmap)
                        self.ui.Statistics.setCellWidget(startrow, 0, flag_country)
                    else:
                        pass
                    col_item = QTableWidgetItem(str('%s' % (country)), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(countries[country])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(countries[country]) / float(len(pilot_list)) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 3:
            self.statusBar().showMessage('Counting...', 2000)
            qApp.processEvents()
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)

            cursor.execute("SELECT planned_depairport FROM status_ivao")
            allairports_dep = cursor.fetchall()
            cursor.execute("SELECT planned_destairport FROM status_ivao")
            allairports_dest = cursor.fetchall()

            list_traffic_airport = []
            for airport in range(0, len(allairports_dep)):
                cursor.execute("SELECT Country FROM icao_codes WHERE ICAO = ?;", (str(allairports_dep[airport][0]),))
                country = cursor.fetchone()
                if country is None:
                    continue
                else:
                    list_traffic_airport.append(str(country[0]))

            for airport in range(0, len(allairports_dest)):
                cursor.execute("SELECT Country FROM icao_codes WHERE ICAO = ?;", (str(allairports_dest[airport][0]),))
                country = cursor.fetchone()
                if country is None:
                    continue
                else:
                    list_traffic_airport.append(str(country[0]))

            country_dict = {}
            for item_list in set(list_traffic_airport):
                country_dict[item_list] = list_traffic_airport.count(item_list)

            startrow = 0
            for country in sorted(country_dict, key=country_dict.__getitem__, reverse=True):
                if country[0] == 0:
                    continue
                else:
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                    flagCodePath = (image_flag + '/%s.png') % country
                    if os.path.exists(flagCodePath) is True:
                        Pixmap = QPixmap(flagCodePath)
                        flag_country = QLabel()
                        flag_country.setPixmap(Pixmap)
                        self.ui.Statistics.setCellWidget(startrow, 0, flag_country)
                    else:
                        pass
                    col_item = QTableWidgetItem(str('%s' % (country)), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(country_dict[country])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(country_dict[country]) / float(len(list_traffic_airport)) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
            self.statusBar().showMessage('Done!', 2000)

        if item == 4:
            self.statusBar().showMessage('Counting...', 2000)
            qApp.processEvents()
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0
            cursor.execute("SELECT SUBSTR(callsign,1,3) AS prefix, COUNT(DISTINCT callsign) AS airlines FROM status_ivao WHERE clienttype='PILOT' GROUP BY prefix ORDER BY airlines DESC;")
            items = cursor.fetchall()

            for i in range(0, len(items)):
                self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                code_airline = items[i][0]
                image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
                airlineCodePath = (image_airlines + '/%s.gif') % code_airline
                try:
                    if os.path.exists(airlineCodePath) is True:
                        Pixmap = QPixmap(airlineCodePath)
                        airline = QLabel(self)
                        airline.setPixmap(Pixmap)
                        self.ui.Statistics.setCellWidget(startrow, 1, airline)
                    else:
                        cursor.execute('SELECT Airline FROM airlines_codes WHERE Code = ?', (str(items[i][0]),))
                        airline_code = cursor.fetchone()
                        if airline_code is None:
                            col_airline = QTableWidgetItem(str(items[i][0]), 0)
                        else:
                            col_airline = QTableWidgetItem(str(airline_code[0]), 0)
                        self.ui.Statistics.setItem(startrow, 1, col_airline)
                except:
                    col_item = QTableWidgetItem(str(items[i][0]), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                col_total = QTableWidgetItem(str(int(items[i][1])), 0)
                self.ui.Statistics.setItem(startrow, 2, col_total)
                percent = float(items[i][1]) / float(len(items)) * 100.0
                self.progressbar = QProgressBar()
                self.progressbar.setMinimum(1)
                self.progressbar.setMaximum(100)
                self.progressbar.setValue(float(percent))
                self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                startrow += 1
            self.statusBar().showMessage('Done!', 2000)

        if item == 5:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0
            cursor.execute("SELECT planned_aircraft FROM status_ivao WHERE clienttype='PILOT';" )
            airplane_type = cursor.fetchall()
            list_aircraft = []
            for item_list in range(0, len(airplane_type)):
                if str(airplane_type[item_list][0]) == '' or str(airplane_type[item_list][0]) == 'None':
                    continue
                else:
                    cursor.execute("SELECT Fabricant FROM icao_aircraft WHERE Model = ?;", (str(airplane_type[item_list][0]).split('/')[1],))
                    fabricant = cursor.fetchall()
                    if fabricant == []:
                        continue
                    else:
                        list_aircraft.append(str(fabricant[0][0]))

            fabricant_type = {}
            for item_list in set(list_aircraft):
                fabricant_type[item_list] = list_aircraft.count(item_list)

            for item in sorted(fabricant_type, key=fabricant_type.__getitem__, reverse=True):
                if fabricant_type == 0:
                    continue
                else:
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    col_item = QTableWidgetItem(str('%s' % (str(item))), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(fabricant_type[item])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(fabricant_type[item]) / float(len(list_aircraft)) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 6:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0
            cursor.execute("SELECT planned_aircraft FROM status_ivao WHERE clienttype='PILOT';" )
            airplane_type = cursor.fetchall()
            list_aircraft = []
            for item_list in range(0, len(airplane_type)):
                if str(airplane_type[item_list][0]) == '' or str(airplane_type[item_list][0]) == 'None':
                    continue
                else:
                    list_aircraft.append(str(airplane_type[item_list]).split('/')[1])

            list_type = {}
            for item_list in set(list_aircraft):
                list_type[item_list] = list_aircraft.count(item_list)

            for item in sorted(list_type, key=list_type.__getitem__, reverse=True):
                if list_type == 0:
                    continue
                else:
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    cursor.execute("SELECT Description FROM icao_aircraft WHERE Model = ?;", (item,))
                    aircraft_description = cursor.fetchone()
                    if aircraft_description is None:
                        continue
                    else:
                        col_item = QTableWidgetItem(str('%s - %s' % (str(item), str(aircraft_description[0]))), 0)
                        self.ui.Statistics.setItem(startrow, 1, col_item)
                        col_total = QTableWidgetItem(str(int(list_type[item])), 0)
                        self.ui.Statistics.setItem(startrow, 2, col_total)
                        percent = float(list_type[item]) / float(len(list_aircraft)) * 100.0
                        self.progressbar = QProgressBar()
                        self.progressbar.setMinimum(1)
                        self.progressbar.setMaximum(100)
                        self.progressbar.setValue(float(percent))
                        self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                        startrow += 1
                    qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 7:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0

            for min_pob, max_pob in [(1, 4), (5, 20), (21, 75), (76, 150), (151, 250), (250, 500)]:
                cursor.execute("SELECT COUNT(callsign) FROM status_ivao WHERE clienttype='PILOT';" )
                total_items = cursor.fetchone()
                if total_items[0] == 0:
                    continue
                else:
                    cursor.execute("SELECT COUNT(callsign) FROM status_ivao WHERE clienttype='PILOT' AND planned_pob >= ? AND planned_pob <= ?;", (min_pob, max_pob))
                    pob = cursor.fetchone()
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    col_item = QTableWidgetItem(str('Flights with Passengers on Boards: %d - %d' % (min_pob, max_pob)), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(pob[0])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(pob[0]) / float(total_items[0]) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 8:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0

            for type_flight in ('S', 'G', 'M', 'N', 'X'):
                cursor.execute("SELECT COUNT(planned_typeofflight) FROM status_ivao WHERE clienttype='PILOT';" )
                total_items = cursor.fetchone()
                if total_items[0] == 0:
                    continue
                else:
                    cursor.execute("SELECT COUNT(planned_typeofflight) FROM status_ivao WHERE clienttype='PILOT' and planned_typeofflight = ?;", (type_flight,))
                    item_typeofflight = cursor.fetchone()
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    if type_flight == 'S':
                        col_item = QTableWidgetItem(str('Flights: Scheduled Services'))
                    if type_flight == 'N':
                        col_item = QTableWidgetItem(str('Flights: Non-Scheduled Services'))
                    if type_flight == 'G':
                        col_item = QTableWidgetItem(str('Flights: General Aviation'))
                    if type_flight == 'M':
                        col_item = QTableWidgetItem(str('Flights: Military'))
                    if type_flight == 'X':
                        col_item = QTableWidgetItem(str('Flights: Others'))
                    col_1 = QTableWidgetItem(str(type_flight), 0)
                    self.ui.Statistics.setItem(startrow, 0, col_1)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(item_typeofflight[0]), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(item_typeofflight[0]) / float(total_items[0]) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()

            for type_flight in ('I', 'V', 'Y', 'Z'):
                cursor.execute("SELECT COUNT(planned_flighttype) FROM status_ivao WHERE clienttype='PILOT';" )
                total_items = cursor.fetchone()
                if total_items[0] == 0:
                    continue
                else:
                    cursor.execute("SELECT COUNT(planned_flighttype) FROM status_ivao WHERE clienttype='PILOT' and planned_flighttype = ?;", (type_flight,))
                    item_typeofflight = cursor.fetchone()
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    if type_flight == 'I':
                        col_item = QTableWidgetItem(str('Flights: Instrumental'))
                    if type_flight == 'V':
                        col_item = QTableWidgetItem(str('Flights: Visual'))
                    if type_flight == 'Y':
                        col_item = QTableWidgetItem(str('Flights: Instrumental changing to Visual'))
                    if type_flight == 'Z':
                        col_item = QTableWidgetItem(str('Flights: Visual changing to Instrumental'))
                    col_1 = QTableWidgetItem(str(type_flight), 0)
                    self.ui.Statistics.setItem(startrow, 0, col_1)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(item_typeofflight[0]), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(item_typeofflight[0]) / float(total_items[0]) * 100.0
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 9:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0

            for facility, description in (('DEP','Departure'), ('GND','Ground'), ('TWR', 'Tower'),
                                          ('APP','Approach'), ('CTR','Center'), ('OBS','Observer')):
                cursor.execute("SELECT COUNT(callsign) FROM status_ivao WHERE clienttype='ATC';" )
                total_items = cursor.fetchone()
                if total_items[0] == 0:
                    continue
                else:
                    cursor.execute("SELECT COUNT(callsign) FROM status_ivao WHERE clienttype='ATC' AND callsign LIKE ?;",
                                   ('%'+str(facility)+'%',))
                    position = cursor.fetchone()
                    self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                    col_item = QTableWidgetItem(str('Controllers in: %s - (%s)' % (facility, description)), 0)
                    self.ui.Statistics.setItem(startrow, 1, col_item)
                    col_total = QTableWidgetItem(str(int(position[0])), 0)
                    self.ui.Statistics.setItem(startrow, 2, col_total)
                    percent = float(position[0]) / float(total_items[0]) * 100.0
                    col_percent = QTableWidgetItem(str('%.1f' % (float(percent))), 0)
                    self.progressbar = QProgressBar()
                    self.progressbar.setMinimum(1)
                    self.progressbar.setMaximum(100)
                    self.progressbar.setValue(float(percent))
                    self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                    startrow += 1
                qApp.processEvents()
            self.statusBar().showMessage('Done!', 2000)

        if item == 10:
            self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
            while self.ui.Statistics.rowCount () > 0:
                self.ui.Statistics.removeRow(0)
            startrow = 0
            list_server = {}
            cursor.execute("SELECT COUNT(server) FROM status_ivao")
            total_server_used = cursor.fetchone()
            for server in ('AM1', 'AM2', 'AS1', 'EU1', 'EU2', 'EU3', 'EU4', 'EU5', 'EU6',
                           'EU7', 'EU8', 'EU9', 'EU11', 'EU12', 'EU13', 'EU14', 'EU15'):
                cursor.execute("SELECT COUNT(server) FROM status_ivao WHERE server=?;", (str(server),))
                total_items = cursor.fetchone()
                if total_items[0] == 0:
                    continue
                else:
                    list_server[server] = total_items[0]

            for item in list_server.keys():
                self.ui.Statistics.insertRow(self.ui.Statistics.rowCount())
                col_item = QTableWidgetItem(str('%s' % (str(item),)), 0)
                self.ui.Statistics.setItem(startrow, 1, col_item)
                col_total = QTableWidgetItem(str(list_server[item]), 0)
                self.ui.Statistics.setItem(startrow, 2, col_total)
                percent = float(list_server[item]) / float(total_server_used[0]) * 100.0
                self.progressbar = QProgressBar()
                self.progressbar.setMinimum(1)
                self.progressbar.setMaximum(100)
                self.progressbar.setValue(float(percent))
                self.ui.Statistics.setCellWidget(startrow, 3, self.progressbar)
                startrow += 1
                qApp.processEvents()
        self.statusBar().showMessage('Done!', 2000)

    def network(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        startrow = 0
        for item in ('AM1', 'AM2', 'AS1', 'EU1', 'EU2', 'EU3', 'EU4', 'EU5', 'EU6', 'EU7', 'EU8', 'EU9', 'EU11', 'EU12', 'EU13', 'EU14', 'EU15'):
            cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='PILOT' AND server=?;", (str(item),))
            server_pilot = cursor.fetchone()
            cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='ATC' AND NOT callsign LIKE '%OBS%' AND server=?;", (str(item),))
            server_controller = cursor.fetchone()
            cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE clienttype='ATC' AND callsign LIKE '%OBS%' AND server=?;", (str(item),))
            server_observer = cursor.fetchone()
            cursor.execute("SELECT COUNT(clienttype) FROM status_ivao WHERE server=?;", (str(item),))
            server_total = cursor.fetchone()
            col_pilot = QTableWidgetItem(str(server_pilot[0]), 0)
            self.ui.network_table.setItem(startrow, 4, col_pilot)
            col_controllers = QTableWidgetItem(str(server_controller[0]), 0)
            self.ui.network_table.setItem(startrow, 5, col_controllers)
            col_observers = QTableWidgetItem(str(server_observer[0]), 0)
            self.ui.network_table.setItem(startrow, 6, col_observers)
            col_total = QTableWidgetItem(str(server_total[0]), 0)
            self.ui.network_table.setItem(startrow, 7, col_total)
            startrow += 1
            qApp.processEvents()

class AddFriend(QMainWindow):
    def add_friend(self, vid2add):
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT vid FROM friends_ivao;")
        vid = cursor.fetchall()
        total_vid = len(vid)
        insert = True
        if total_vid >= 0:
            for i in range(0, total_vid):
                if int(vid2add) == vid[i][0]:
                    msg = 'The friend is already in the list'
                    QMessageBox.information(None, 'Friend of IVAO list', msg)
                    i += 1
                    insert = False
            try:
                if insert is True:
                    cursor.execute('INSERT INTO friends_ivao (vid, realname, rating, clienttype) \
                    SELECT vid, realname, rating, clienttype FROM status_ivao WHERE vid=?;', (vid2add,))
                    connection.commit()
            except:
                pass
        self.statusBar().showMessage('Done!', 2000)
        connection.close()

class PilotInfo(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = PilotInfo_UI.Ui_QPilotInfo()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'ivao_status_splash.png')
        self.setWindowIcon(QIcon(image_icon))
        self.callsign = ''
        QObject.connect(self.ui.AddFriend, SIGNAL('clicked()'), self.add_button)

    def status(self, callsign):
        self.callsign = callsign
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT vid, realname, altitude, groundspeed, planned_aircraft, planned_depairport, \
        planned_destairport, planned_altitude, planned_pob, planned_route, rating, transponder, onground,\
        latitude, longitude, planned_altairport, planned_altairport2, planned_tascruise, time_connected, clienttype \
        FROM status_ivao WHERE callsign=?;", (str(callsign),))
        info = cursor.fetchall()
        if info[0][19] == 'FOLME':
            pass
        else:
            try:
                cursor.execute("SELECT Country FROM icao_codes WHERE icao=?", (str(info[0][5]),))
                flagCodeOrig = cursor.fetchone()
                connection.commit()
                ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
                flagCodePath_orig = (ImagePath + '/%s.png') % flagCodeOrig
                Pixmap = QPixmap(flagCodePath_orig)
                self.ui.DepartureImage.setPixmap(Pixmap)
                cursor.execute("SELECT City_Airport, Latitude, Longitude FROM icao_codes WHERE icao=?", (str(info[0][5]),))
                city_orig = cursor.fetchone()
                self.ui.DepartureText.setText(str(city_orig[0].encode('latin-1')))
                city_orig_point = city_orig[1], city_orig[2]
            except:
                self.ui.DepartureText.setText('Pending...')
                city_orig_point = None

        try:
            cursor.execute("SELECT Country FROM icao_codes WHERE icao=?", (str(info[0][6]),))
            flagCodeDest = cursor.fetchone()
            connection.commit()
            ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
            flagCodePath_dest = (ImagePath + '/%s.png') % flagCodeDest
            Pixmap = QPixmap(flagCodePath_dest)
            self.ui.DestinationImage.setPixmap(Pixmap)
            cursor.execute("SELECT City_Airport, Latitude, Longitude FROM icao_codes WHERE icao=?", (str(info[0][6]),))
            city_dest = cursor.fetchone()
            self.ui.DestinationText.setText(str(city_dest[0].encode('latin-1')))
            city_dest_point = city_dest[1], city_dest[2]
        except:
            self.ui.DestinationText.setText('Pending...')
            city_dest_point = None

        self.ui.vidText.setText(str(info[0][0]))
        try:
            code_airline = callsign[:3]
            image_airlines = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airlines')
            airlineCodePath = (image_airlines + '/%s.gif') % code_airline
            if os.path.exists(airlineCodePath) is True:
                Pixmap = QPixmap(airlineCodePath)
                airline = QLabel(self)
                self.ui.airline_image.setPixmap(Pixmap)
            else:
                cursor.execute('SELECT Airline FROM airlines_codes WHERE Code = ?', str(callsign[:3]))
                airline_code = cursor.fetchone()
                self.ui.airline_image.setText(str(airline_code[0]))
        except:
            pass
        self.ui.callsign_text.setText(callsign)
        self.ui.PilotNameText.setText(str(info[0][1][:-4].encode('latin-1')))
        self.ui.RouteText.setText(str(info[0][9]))
        self.ui.GroundSpeedNumber.setText(str(info[0][3]))
        self.ui.AltitudeNumber.setText(str(info[0][2]))
        self.ui.PobText.setText(str(info[0][8]))
        self.ui.TransponderText.setText(str(info[0][11]))
        self.ui.GSFiledText.setText(str(info[0][17]))
        self.ui.FLText.setText(str(info[0][7]))
        altern_airport_1 = cursor.execute("SELECT City_Airport FROM icao_codes WHERE icao=?", (str(info[0][15]),))
        altern_city_1 = cursor.fetchone()
        altern_airport_2 = cursor.execute("SELECT City_Airport FROM icao_codes WHERE icao=?", (str(info[0][16]),))
        altern_city_2 = cursor.fetchone()
        if altern_city_1 is None:
            self.ui.Altern_Airport_Text.setText(str('-'))
        else:
            self.ui.Altern_Airport_Text.setText(str(altern_city_1[0]))
        if altern_city_2 is None:
            self.ui.Altern_Airport_Text_2.setText(str('-'))
        else:
            self.ui.Altern_Airport_Text_2.setText(str(altern_city_2[0]))
        try:
            if str(info[0][4]) != '':
                cursor.execute("SELECT Model, Fabricant, Description FROM icao_aircraft WHERE Model=?;", ((info[0][4].split('/')[1]),))
                data = cursor.fetchall()
                self.ui.AirplaneText.setText('Model: %s Fabricant: %s Description: %s' \
                                             % (str(data[0][0]), str(data[0][1]), str(data[0][2])))
        except:
            self.ui.AirplaneText.setText('Pending...')
        cursor.execute("SELECT Country FROM icao_codes WHERE icao=?", (str(info[0][1][-4:]),))
        flagCodeHome = cursor.fetchone()
        connection.commit()
        ImageFlag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
        flagCodePath = (ImageFlag + '/%s.png') % flagCodeHome
        Pixmap = QPixmap(flagCodePath)
        self.ui.HomeFlag.setPixmap(Pixmap)
        ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
        ratingImagePath = ImagePath + '/pilot_level%d.gif' % int(info[0][10])
        Pixmap = QPixmap(ratingImagePath)
        self.ui.rating_img.setPixmap(Pixmap)
        player_point = info[0][13], info[0][14]
        if city_orig_point is None or city_dest_point is None:
            self.ui.nauticalmiles.setText('Pending...')
            self.ui.progressBarTrack.setValue(0)
        if str(info[0][5]) == str(info[0][6]):
                self.ui.progressBarTrack.setValue(0)
                self.ui.nauticalmiles.setText('Local Flight')
        else:
            total_miles = distance.distance(city_orig_point, city_dest_point).miles
            dist_traveled = distance.distance(city_orig_point, player_point).miles
            percent = float((dist_traveled / total_miles) * 100.0)
            self.ui.nauticalmiles.setText('%.1f / %.1f miles - %.1f%%' % (float(dist_traveled), float(total_miles), float(percent)))
            self.ui.progressBarTrack.setValue(int(percent))
        status_plane = Main().status_plane(callsign)
        self.ui.FlightStatusDetail.setText(str(status_plane))
        try:
            start_connected = datetime.datetime(int(str(info[0][18])[:4]), int(str(info[0][18])[4:6]) \
                                                , int(str(info[0][18])[6:8]), int(str(info[0][18])[8:10]) \
                                                , int(str(info[0][18])[10:12]), int(str(info[0][18])[12:14]))
            diff = datetime.datetime.utcnow() - start_connected
            self.ui.time_online_text.setText(str(diff)[:-7])
        except:
            self.ui.time_online_text.setText('Pending...')


    def add_button(self):
        add2friend = AddFriend()
        add2friend.add_friend(str(self.ui.vidText.text()).encode('latin-1'))
        self.statusBar().showMessage('Friend Added', 3000)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

class ControllerInfo(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ControllerInfo_UI.Ui_QControllerInfo()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'ivao_status_splash.png')
        self.setWindowIcon(QIcon(image_icon))
        QObject.connect(self.ui.AddFriend, SIGNAL('clicked()'), self.add_button)

    def status(self, callsign):
        self.callsign = callsign
        self.position_atc = {"0":"Observer", "1":"Flight Service Station", "2":"Clearance Delivery" \
                             , "3":"Ground", "4":"Tower", "5":"Approach", "6":"Center", "7":"Departure"}
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT vid, realname, server, clienttype, frequency, rating, facilitytype, atis_message, \
        time_connected, client_software_name, client_software_version FROM status_ivao WHERE callsign=?;", (str(callsign),))
        info = cursor.fetchall()
        self.ui.VidText.setText(str(info[0][0]))
        self.ui.ControllerText.setText(str(info[0][1].encode('latin-1')))
        self.ui.SoftwareText.setText('%s %s' % (str(info[0][9]), str(info[0][10])))
        self.ui.ConnectedText.setText(str(info[0][2]))
        self.ui.ATISInfo.setText(str(info[0][7].encode('latin-1')).replace('^\xa7', '\n'))
        try:
            cursor.execute("SELECT Country FROM icao_codes WHERE icao=?", (str(callsign[:4]),))
            flagCodeOrig = cursor.fetchone()
            connection.commit()
            if flagCodeOrig is None:
                cursor.execute('SELECT Country FROM division_ivao WHERE Division=?;', (str(callsign[:2]),))
                flagCodeOrig = cursor.fetchone()
                connection.commit()
            image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
            flagCodePath_orig = (image_flag + '/%s.png') % flagCodeOrig
            Pixmap = QPixmap(flagCodePath_orig)
            self.ui.Flag.setPixmap(Pixmap)
            cursor.execute("SELECT City_Airport FROM icao_codes WHERE icao=?", (str(callsign[:4]),))
            city_orig = cursor.fetchone()
            if str(callsign[-4:]) == '_CTR':
                cursor.execute("SELECT FIR FROM fir_data_list WHERE icao=?", (str(callsign[:4]),))
                city_orig = cursor.fetchone()
            if str(callsign[2:3]) == '_' or str(callsign[2:3]) == '-':
                cursor.execute("SELECT Country FROM division_ivao WHERE Division=?", (str(callsign[:2]),))
                city_orig = cursor.fetchone()
            self.ui.ControllingText.setText(str(city_orig[0].encode('latin-1')))
        except:
            self.ui.ControllingText.setText('Pending...')
        ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ratings')
        ratingImagePath = ImagePath + '/atc_level%d.gif' % int(info[0][5])
        Pixmap = QPixmap(ratingImagePath)
        self.ui.rating_img.setPixmap(Pixmap)
        self.ui.facility_freq_Text.setText(str(self.position_atc[str(info[0][6])]) + ' ' + str(info[0][4]) + ' MHz')
        try:
            start_connected = datetime.datetime(int(str(info[0][8])[:4]), int(str(info[0][8])[4:6]) \
                                                , int(str(info[0][8])[6:8]), int(str(info[0][8])[8:10]) \
                                                , int(str(info[0][8])[10:12]), int(str(info[0][8])[12:14]))
            diff = datetime.datetime.utcnow() - start_connected
            self.ui.TimeOnLineText.setText('Time on line: ' + str(diff)[:-7])
        except:
            self.ui.TimeOnLineText.setText('Pending...')

    def add_button(self):
        add2friend = AddFriend()
        add2friend.add_friend(str(self.ui.VidText.text()).encode('latin-1'))
        self.statusBar().showMessage('Friend Added', 3000)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

class FollowMeService(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = FollowMeCarService_UI.Ui_QFMC()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'ivao_status_splash.png')
        self.setWindowIcon(QIcon(image_icon))
        QObject.connect(self.ui.AddFriend, SIGNAL('clicked()'), self.add_button)

    def status(self, callsign):
        self.callsign = callsign
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', config.get('Database', 'db'))
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT vid, realname, server, clienttype, rating, time_connected, client_software_name, \
        client_software_version FROM status_ivao WHERE callsign=?;", (str(callsign),))
        info = cursor.fetchall()
        self.ui.VidText.setText(str(info[0][0]))
        self.ui.FMCRealname.setText(str(info[0][1].encode('latin-1'))[:-4])
        self.ui.SoftwareText.setText('%s %s' % (str(info[0][6]), str(info[0][7])))
        self.ui.ConnectedText.setText(str(info[0][2]))
        try:
            cursor.execute("SELECT Country FROM icao_codes WHERE icao=?", (str(info[0][1][-4:]),))
            flagCodeOrig = cursor.fetchone()
            connection.commit()
            image_flag = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flags')
            flagCodePath_orig = (image_flag + '/%s.png') % flagCodeOrig
            Pixmap = QPixmap(flagCodePath_orig)
            self.ui.Flag.setPixmap(Pixmap)
            cursor.execute("SELECT City_Airport FROM icao_codes WHERE icao=?", (str(callsign[:4]),))
            city_orig = cursor.fetchone()
        except:
            self.ui.ControllingText.setText('Pending...')
        ImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
        ratingImagePath = (ImagePath + '/ZZZZ.png')
        Pixmap = QPixmap(ratingImagePath)
        self.ui.rating_img.setPixmap(Pixmap)
        try:
            start_connected = datetime.datetime(int(str(info[0][5])[:4]), int(str(info[0][5])[4:6]) \
                                                , int(str(info[0][5])[6:8]), int(str(info[0][5])[8:10]) \
                                                , int(str(info[0][5])[10:12]), int(str(info[0][5])[12:14]))
            diff = datetime.datetime.utcnow() - start_connected
            self.ui.TimeOnLineText.setText('Time on line: ' + str(diff)[:-7])
        except:
            self.ui.TimeOnLineText.setText('Pending...')

    def add_button(self):
        add2friend = AddFriend()
        add2friend.add_friend(str(self.ui.VidText.text()).encode('latin-1'))
        self.statusBar().showMessage('Friend Added', 3000)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

class Settings(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = SettingWindow_UI.Ui_SettingWindow()
        self.ui.setupUi(self)
        self.parent = parent
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'ivao_status_splash.png')
        self.setWindowIcon(QIcon(image_icon))
        self.connect(self.ui.SettingAccepButton, SIGNAL('clicked()'), self.options)
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.read(config_file)
        self.ui.spinBox.setValue(config.getint('Time_Update', 'time') / 60000)
        use_proxy = config.getint('Settings', 'use_proxy')
        if use_proxy == 2:
            self.ui.Setting_checkBox.setChecked(True)
        else:
            self.ui.Setting_checkBox.setChecked(False)
        host = config.get('Settings', 'host')
        self.ui.lineEdit_host.setText(host)
        port = config.get('Settings', 'port')
        self.ui.lineEdit_port.setText(port)
        auth = config.getint('Settings', 'auth')
        if auth == 2:
            self.ui.Setting_auth.setChecked(True)
        else:
            self.ui.Setting_auth.setChecked(False)
        user = config.get('Settings', 'user')
        self.ui.lineEdit_user.setText(user)
        pswd = config.get('Settings', 'pass')
        self.ui.lineEdit_pass.setText(pswd)
        map_refresh = config.getint('Map', 'auto_refresh')
        label_pilot = config.getint('Map', 'label_Pilots')
        label_atcs = config.getint('Map', 'label_ATCs')
        if map_refresh == 2:
            self.ui.AutoRefreshMap.setChecked(True)
        else:
            self.ui.AutoRefreshMap.setChecked(False)
        if label_pilot == 2:
            self.ui.ShowLabelPilots.setChecked(True)
        else:
            self.ui.ShowLabelPilots.setChecked(False)
        if label_atcs == 2:
            self.ui.ShowLabelControllers.setChecked(True)
        else:
            self.ui.ShowLabelControllers.setChecked(False)

    def options(self):
        minutes = self.ui.spinBox.value()
        time_update = minutes * 60000
        config = ConfigParser.RawConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Config.cfg')
        config.add_section('Settings')
        config.set('Settings', 'use_proxy', self.ui.Setting_checkBox.checkState())
        config.set('Settings', 'host', self.ui.lineEdit_host.text())
        config.set('Settings', 'port', self.ui.lineEdit_port.text())
        config.set('Settings', 'auth', self.ui.Setting_auth.checkState())
        config.set('Settings', 'user', self.ui.lineEdit_user.text())
        config.set('Settings', 'pass', self.ui.lineEdit_pass.text())
        config.add_section('Info')
        config.set('Info', 'data_access', 'whazzup.txt')
        config.set('Info', 'url', url)
        config.set('Info', 'scheduling_atc', scheduling_atc)
        config.set('Info', 'scheduling_flights', scheduling_flights)
        config.add_section('Database')
        config.set('Database', 'db', 'ivao.db')
        config.add_section('Time_Update')
        config.set('Time_Update', 'time', time_update)
        config.add_section('Map')
        if self.ui.AutoRefreshMap.checkState() == 2:
            config.set('Map', 'auto_refresh', '2')
        else:
            config.set('Map', 'auto_refresh', '0')
        if self.ui.ShowLabelPilots.checkState() == 2:
            config.set('Map', 'label_Pilots', '2')
        else:
            config.set('Map', 'label_Pilots', '0')
        if self.ui.ShowLabelControllers.checkState() == 2:
            config.set('Map', 'label_ATCs', '2')
        else:
            config.set('Map', 'label_ATCs', '0')
        with open (config_file, 'wb') as configfile:
            config.write(configfile)

        self.close()

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

def main():
    import sys, time, os
    QApplication.setStyle(QStyleFactory.create("Cleanlooks"))
    QApplication.setPalette(QApplication.style().standardPalette())
    app = QApplication(sys.argv)
    image_splash = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'ivao_status_splash.png')
    splash_pix = QPixmap(image_splash)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    qApp.processEvents()
    time.sleep(4)
    window = Main()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
