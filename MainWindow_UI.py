# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/MainWindow_UI.ui'
#
# Created: Thu Aug  4 00:20:21 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1024, 686)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 686))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 686))
        MainWindow.setCursor(QtCore.Qt.PointingHandCursor)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(4, 30, 1015, 631))
        self.tabWidget.setCursor(QtCore.Qt.PointingHandCursor)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.main = QtGui.QWidget()
        self.main.setObjectName(_fromUtf8("main"))
        self.IVAOStatustableWidget = QtGui.QTableWidget(self.main)
        self.IVAOStatustableWidget.setGeometry(QtCore.QRect(9, 22, 441, 211))
        self.IVAOStatustableWidget.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.IVAOStatustableWidget.setAutoFillBackground(True)
        self.IVAOStatustableWidget.setTabKeyNavigation(False)
        self.IVAOStatustableWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.IVAOStatustableWidget.setDragDropOverwriteMode(False)
        self.IVAOStatustableWidget.setAlternatingRowColors(True)
        self.IVAOStatustableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.IVAOStatustableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.IVAOStatustableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.IVAOStatustableWidget.setWordWrap(False)
        self.IVAOStatustableWidget.setObjectName(_fromUtf8("IVAOStatustableWidget"))
        self.IVAOStatustableWidget.setColumnCount(1)
        self.IVAOStatustableWidget.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.IVAOStatustableWidget.setHorizontalHeaderItem(0, item)
        self.IVAOStatustableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.IVAOStatustableWidget.horizontalHeader().setHighlightSections(False)
        self.IVAOStatustableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.IVAOStatustableWidget.horizontalHeader().setStretchLastSection(True)
        self.IVAOStatustableWidget.verticalHeader().setDefaultSectionSize(20)
        self.IVAOStatustableWidget.verticalHeader().setMinimumSectionSize(20)
        self.IVAOStatustableWidget.verticalHeader().setSortIndicatorShown(True)
        self.IVAOStatustableWidget.verticalHeader().setStretchLastSection(False)
        self.IVAOStatusLabel = QtGui.QLabel(self.main)
        self.IVAOStatusLabel.setGeometry(QtCore.QRect(11, 5, 91, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.IVAOStatusLabel.setFont(font)
        self.IVAOStatusLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.IVAOStatusLabel.setObjectName(_fromUtf8("IVAOStatusLabel"))
        self.FriendstableWidget = QtGui.QTableWidget(self.main)
        self.FriendstableWidget.setGeometry(QtCore.QRect(470, 23, 531, 211))
        self.FriendstableWidget.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.FriendstableWidget.setAutoFillBackground(True)
        self.FriendstableWidget.setTabKeyNavigation(False)
        self.FriendstableWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.FriendstableWidget.setAlternatingRowColors(True)
        self.FriendstableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.FriendstableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.FriendstableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.FriendstableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.FriendstableWidget.setWordWrap(False)
        self.FriendstableWidget.setObjectName(_fromUtf8("FriendstableWidget"))
        self.FriendstableWidget.setColumnCount(5)
        self.FriendstableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.FriendstableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.FriendstableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.FriendstableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.FriendstableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.FriendstableWidget.setHorizontalHeaderItem(4, item)
        self.FriendstableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.FriendstableWidget.horizontalHeader().setHighlightSections(True)
        self.FriendstableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.FriendstableWidget.horizontalHeader().setStretchLastSection(True)
        self.FriendstableWidget.verticalHeader().setDefaultSectionSize(15)
        self.FriendstableWidget.verticalHeader().setMinimumSectionSize(15)
        self.FriendsLabel = QtGui.QLabel(self.main)
        self.FriendsLabel.setGeometry(QtCore.QRect(470, 6, 61, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.FriendsLabel.setFont(font)
        self.FriendsLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.FriendsLabel.setObjectName(_fromUtf8("FriendsLabel"))
        self.SearchClientsLabel = QtGui.QLabel(self.main)
        self.SearchClientsLabel.setGeometry(QtCore.QRect(13, 251, 111, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.SearchClientsLabel.setFont(font)
        self.SearchClientsLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.SearchClientsLabel.setObjectName(_fromUtf8("SearchClientsLabel"))
        self.SearchtableWidget = QtGui.QTableWidget(self.main)
        self.SearchtableWidget.setGeometry(QtCore.QRect(10, 289, 441, 311))
        self.SearchtableWidget.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.SearchtableWidget.setAutoFillBackground(True)
        self.SearchtableWidget.setAlternatingRowColors(True)
        self.SearchtableWidget.setObjectName(_fromUtf8("SearchtableWidget"))
        self.SearchtableWidget.setColumnCount(0)
        self.SearchtableWidget.setRowCount(0)
        self.SearchForLabel = QtGui.QLabel(self.main)
        self.SearchForLabel.setGeometry(QtCore.QRect(13, 268, 81, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.SearchForLabel.setFont(font)
        self.SearchForLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.SearchForLabel.setObjectName(_fromUtf8("SearchForLabel"))
        self.METARtableWidget = QtGui.QTableWidget(self.main)
        self.METARtableWidget.setGeometry(QtCore.QRect(470, 289, 531, 311))
        self.METARtableWidget.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.METARtableWidget.setAutoFillBackground(True)
        self.METARtableWidget.setTabKeyNavigation(False)
        self.METARtableWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.METARtableWidget.setDragDropOverwriteMode(False)
        self.METARtableWidget.setAlternatingRowColors(True)
        self.METARtableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.METARtableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.METARtableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.METARtableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.METARtableWidget.setWordWrap(False)
        self.METARtableWidget.setColumnCount(2)
        self.METARtableWidget.setObjectName(_fromUtf8("METARtableWidget"))
        self.METARtableWidget.setColumnCount(2)
        self.METARtableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.METARtableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.METARtableWidget.setHorizontalHeaderItem(1, item)
        self.METARtableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.METARtableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.METARtableWidget.horizontalHeader().setHighlightSections(True)
        self.METARtableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.METARtableWidget.horizontalHeader().setStretchLastSection(True)
        self.METARtableWidget.verticalHeader().setDefaultSectionSize(15)
        self.METARtableWidget.verticalHeader().setMinimumSectionSize(15)
        self.MetarLabel = QtGui.QLabel(self.main)
        self.MetarLabel.setGeometry(QtCore.QRect(473, 269, 51, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.MetarLabel.setFont(font)
        self.MetarLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.MetarLabel.setObjectName(_fromUtf8("MetarLabel"))
        self.SearchcomboBox = QtGui.QComboBox(self.main)
        self.SearchcomboBox.setGeometry(QtCore.QRect(95, 267, 80, 20))
        self.SearchcomboBox.setCursor(QtCore.Qt.PointingHandCursor)
        self.SearchcomboBox.setObjectName(_fromUtf8("SearchcomboBox"))
        self.SearchcomboBox.addItem(_fromUtf8(""))
        self.SearchcomboBox.addItem(_fromUtf8(""))
        self.SearchcomboBox.addItem(_fromUtf8(""))
        self.SearchEdit = QtGui.QLineEdit(self.main)
        self.SearchEdit.setGeometry(QtCore.QRect(175, 267, 113, 20))
        self.SearchEdit.setCursor(QtCore.Qt.PointingHandCursor)
        self.SearchEdit.setObjectName(_fromUtf8("SearchEdit"))
        self.METAREdit = QtGui.QLineEdit(self.main)
        self.METAREdit.setGeometry(QtCore.QRect(524, 267, 61, 20))
        self.METAREdit.setCursor(QtCore.Qt.PointingHandCursor)
        self.METAREdit.setObjectName(_fromUtf8("METAREdit"))
        self.tabWidget.addTab(self.main, _fromUtf8(""))
        self.countries = QtGui.QWidget()
        self.countries.setObjectName(_fromUtf8("countries"))
        self.country_list = QtGui.QComboBox(self.countries)
        self.country_list.setGeometry(QtCore.QRect(9, 6, 215, 20))
        self.country_list.setCursor(QtCore.Qt.PointingHandCursor)
        self.country_list.setObjectName(_fromUtf8("country_list"))
        self.ATCtableWidget = QtGui.QTableWidget(self.countries)
        self.ATCtableWidget.setGeometry(QtCore.QRect(8, 30, 991, 161))
        self.ATCtableWidget.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.ATCtableWidget.setAutoFillBackground(True)
        self.ATCtableWidget.setAutoScrollMargin(16)
        self.ATCtableWidget.setTabKeyNavigation(False)
        self.ATCtableWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.ATCtableWidget.setDragDropOverwriteMode(False)
        self.ATCtableWidget.setAlternatingRowColors(True)
        self.ATCtableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ATCtableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ATCtableWidget.setShowGrid(True)
        self.ATCtableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.ATCtableWidget.setWordWrap(False)
        self.ATCtableWidget.setRowCount(0)
        self.ATCtableWidget.setColumnCount(6)
        self.ATCtableWidget.setObjectName(_fromUtf8("ATCtableWidget"))
        self.ATCtableWidget.setColumnCount(6)
        self.ATCtableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.ATCtableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ATCtableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ATCtableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.ATCtableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.ATCtableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.ATCtableWidget.setHorizontalHeaderItem(5, item)
        self.ATCtableWidget.horizontalHeader().setVisible(False)
        self.ATCtableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.ATCtableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.ATCtableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.ATCtableWidget.horizontalHeader().setStretchLastSection(True)
        self.ATCtableWidget.verticalHeader().setDefaultSectionSize(20)
        self.ATCtableWidget.verticalHeader().setMinimumSectionSize(20)
        self.ATCtableWidget.verticalHeader().setSortIndicatorShown(True)
        self.atc_label = QtGui.QLabel(self.countries)
        self.atc_label.setGeometry(QtCore.QRect(464, 13, 61, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.atc_label.setFont(font)
        self.atc_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.atc_label.setObjectName(_fromUtf8("atc_label"))
        self.pilot_list = QtGui.QLabel(self.countries)
        self.pilot_list.setGeometry(QtCore.QRect(455, 193, 81, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pilot_list.setFont(font)
        self.pilot_list.setCursor(QtCore.Qt.PointingHandCursor)
        self.pilot_list.setObjectName(_fromUtf8("pilot_list"))
        self.PilottableWidget = QtGui.QTableWidget(self.countries)
        self.PilottableWidget.setGeometry(QtCore.QRect(8, 210, 991, 401))
        self.PilottableWidget.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.PilottableWidget.setAutoFillBackground(True)
        self.PilottableWidget.setAutoScrollMargin(16)
        self.PilottableWidget.setTabKeyNavigation(False)
        self.PilottableWidget.setProperty(_fromUtf8("showDropIndicator"), False)
        self.PilottableWidget.setDragDropOverwriteMode(False)
        self.PilottableWidget.setAlternatingRowColors(True)
        self.PilottableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.PilottableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.PilottableWidget.setShowGrid(True)
        self.PilottableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.PilottableWidget.setWordWrap(False)
        self.PilottableWidget.setRowCount(0)
        self.PilottableWidget.setColumnCount(9)
        self.PilottableWidget.setObjectName(_fromUtf8("PilottableWidget"))
        self.PilottableWidget.setColumnCount(9)
        self.PilottableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.PilottableWidget.setHorizontalHeaderItem(8, item)
        self.PilottableWidget.horizontalHeader().setVisible(False)
        self.PilottableWidget.horizontalHeader().setDefaultSectionSize(109)
        self.PilottableWidget.horizontalHeader().setMinimumSectionSize(109)
        self.PilottableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.PilottableWidget.horizontalHeader().setStretchLastSection(True)
        self.PilottableWidget.verticalHeader().setDefaultSectionSize(20)
        self.PilottableWidget.verticalHeader().setMinimumSectionSize(20)
        self.PilottableWidget.verticalHeader().setSortIndicatorShown(True)
        self.flagIcon = QtGui.QLabel(self.countries)
        self.flagIcon.setGeometry(QtCore.QRect(230, 5, 71, 21))
        self.flagIcon.setCursor(QtCore.Qt.PointingHandCursor)
        self.flagIcon.setText(_fromUtf8(""))
        self.flagIcon.setObjectName(_fromUtf8("flagIcon"))
        self.tabWidget.addTab(self.countries, _fromUtf8(""))
        self.controllers = QtGui.QWidget()
        self.controllers.setObjectName(_fromUtf8("controllers"))
        self.ATC_FullList = QtGui.QTableWidget(self.controllers)
        self.ATC_FullList.setGeometry(QtCore.QRect(5, 8, 1001, 591))
        self.ATC_FullList.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.ATC_FullList.setAutoFillBackground(True)
        self.ATC_FullList.setTabKeyNavigation(False)
        self.ATC_FullList.setProperty(_fromUtf8("showDropIndicator"), False)
        self.ATC_FullList.setDragDropOverwriteMode(False)
        self.ATC_FullList.setAlternatingRowColors(True)
        self.ATC_FullList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ATC_FullList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ATC_FullList.setGridStyle(QtCore.Qt.DotLine)
        self.ATC_FullList.setWordWrap(False)
        self.ATC_FullList.setObjectName(_fromUtf8("ATC_FullList"))
        self.ATC_FullList.setColumnCount(9)
        self.ATC_FullList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.ATC_FullList.setHorizontalHeaderItem(8, item)
        self.ATC_FullList.horizontalHeader().setDefaultSectionSize(110)
        self.ATC_FullList.horizontalHeader().setMinimumSectionSize(110)
        self.ATC_FullList.horizontalHeader().setStretchLastSection(False)
        self.ATC_FullList.verticalHeader().setDefaultSectionSize(20)
        self.ATC_FullList.verticalHeader().setMinimumSectionSize(20)
        self.tabWidget.addTab(self.controllers, _fromUtf8(""))
        self.pilots = QtGui.QWidget()
        self.pilots.setObjectName(_fromUtf8("pilots"))
        self.PILOT_FullList = QtGui.QTableWidget(self.pilots)
        self.PILOT_FullList.setGeometry(QtCore.QRect(5, 8, 1001, 591))
        self.PILOT_FullList.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.PILOT_FullList.setAutoFillBackground(True)
        self.PILOT_FullList.setTabKeyNavigation(False)
        self.PILOT_FullList.setProperty(_fromUtf8("showDropIndicator"), False)
        self.PILOT_FullList.setDragDropOverwriteMode(False)
        self.PILOT_FullList.setAlternatingRowColors(True)
        self.PILOT_FullList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.PILOT_FullList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.PILOT_FullList.setGridStyle(QtCore.Qt.DotLine)
        self.PILOT_FullList.setWordWrap(False)
        self.PILOT_FullList.setObjectName(_fromUtf8("PILOT_FullList"))
        self.PILOT_FullList.setColumnCount(9)
        self.PILOT_FullList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.PILOT_FullList.setHorizontalHeaderItem(8, item)
        self.PILOT_FullList.horizontalHeader().setDefaultSectionSize(110)
        self.PILOT_FullList.horizontalHeader().setMinimumSectionSize(110)
        self.PILOT_FullList.horizontalHeader().setStretchLastSection(True)
        self.PILOT_FullList.verticalHeader().setDefaultSectionSize(20)
        self.PILOT_FullList.verticalHeader().setMinimumSectionSize(20)
        self.tabWidget.addTab(self.pilots, _fromUtf8(""))
        self.observers = QtGui.QWidget()
        self.observers.setObjectName(_fromUtf8("observers"))
        self.ObservertableView = QtGui.QTableView(self.observers)
        self.ObservertableView.setGeometry(QtCore.QRect(5, 8, 1001, 591))
        self.ObservertableView.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.ObservertableView.setTabKeyNavigation(False)
        self.ObservertableView.setProperty(_fromUtf8("showDropIndicator"), False)
        self.ObservertableView.setDragDropOverwriteMode(False)
        self.ObservertableView.setAlternatingRowColors(True)
        self.ObservertableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ObservertableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ObservertableView.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.ObservertableView.setGridStyle(QtCore.Qt.DotLine)
        self.ObservertableView.setWordWrap(False)
        self.ObservertableView.setObjectName(_fromUtf8("ObservertableView"))
        self.ObservertableView.verticalHeader().setDefaultSectionSize(20)
        self.ObservertableView.verticalHeader().setMinimumSectionSize(20)
        self.tabWidget.addTab(self.observers, _fromUtf8(""))
        self.database = QtGui.QWidget()
        self.database.setObjectName(_fromUtf8("database"))
        self.tableView = QtGui.QTableView(self.database)
        self.tableView.setGeometry(QtCore.QRect(6, 10, 485, 591))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView_2 = QtGui.QTableView(self.database)
        self.tableView_2.setGeometry(QtCore.QRect(500, 10, 501, 591))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.tabWidget.addTab(self.database, _fromUtf8(""))
        self.actual_user = QtGui.QWidget()
        self.actual_user.setObjectName(_fromUtf8("actual_user"))
        self.InboundTableView = QtGui.QTableView(self.actual_user)
        self.InboundTableView.setGeometry(QtCore.QRect(5, 20, 1001, 193))
        self.InboundTableView.setObjectName(_fromUtf8("InboundTableView"))
        self.Inbound_traffic = QtGui.QLabel(self.actual_user)
        self.Inbound_traffic.setGeometry(QtCore.QRect(435, 4, 111, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.Inbound_traffic.setFont(font)
        self.Inbound_traffic.setObjectName(_fromUtf8("Inbound_traffic"))
        self.OutboundTableView = QtGui.QTableView(self.actual_user)
        self.OutboundTableView.setGeometry(QtCore.QRect(5, 227, 1001, 192))
        self.OutboundTableView.setObjectName(_fromUtf8("OutboundTableView"))
        self.outbound_traffic = QtGui.QLabel(self.actual_user)
        self.outbound_traffic.setGeometry(QtCore.QRect(431, 211, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.outbound_traffic.setFont(font)
        self.outbound_traffic.setObjectName(_fromUtf8("outbound_traffic"))
        self.NearbyATCViewTable = QtGui.QTableView(self.actual_user)
        self.NearbyATCViewTable.setGeometry(QtCore.QRect(5, 440, 1001, 161))
        self.NearbyATCViewTable.setObjectName(_fromUtf8("NearbyATCViewTable"))
        self.nearby_controllers = QtGui.QLabel(self.actual_user)
        self.nearby_controllers.setGeometry(QtCore.QRect(434, 419, 111, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.nearby_controllers.setFont(font)
        self.nearby_controllers.setObjectName(_fromUtf8("nearby_controllers"))
        self.tabWidget.addTab(self.actual_user, _fromUtf8(""))
        self.UpdateBtn = QtGui.QPushButton(self.centralwidget)
        self.UpdateBtn.setGeometry(QtCore.QRect(7, 3, 92, 24))
        self.UpdateBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.UpdateBtn.setObjectName(_fromUtf8("UpdateBtn"))
        self.ExitBtn = QtGui.QPushButton(self.centralwidget)
        self.ExitBtn.setGeometry(QtCore.QRect(107, 3, 92, 24))
        self.ExitBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.ExitBtn.setObjectName(_fromUtf8("ExitBtn"))
        self.action_update = QtGui.QLabel(self.centralwidget)
        self.action_update.setGeometry(QtCore.QRect(6, 667, 241, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.action_update.setFont(font)
        self.action_update.setCursor(QtCore.Qt.PointingHandCursor)
        self.action_update.setObjectName(_fromUtf8("action_update"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.country_list.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "IVAO :: Status of IVAN", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatustableWidget.setSortingEnabled(True)
        self.IVAOStatustableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Pilots", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatustableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Controllers", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatustableWidget.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Observers", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatustableWidget.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Total Players", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatustableWidget.verticalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Total POB", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatustableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Information Board Data", None, QtGui.QApplication.UnicodeUTF8))
        self.IVAOStatusLabel.setText(QtGui.QApplication.translate("MainWindow", "IVAO Status", None, QtGui.QApplication.UnicodeUTF8))
        self.FriendstableWidget.setSortingEnabled(True)
        self.FriendstableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Callsing", None, QtGui.QApplication.UnicodeUTF8))
        self.FriendstableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "VID", None, QtGui.QApplication.UnicodeUTF8))
        self.FriendstableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.FriendstableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.FriendstableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.FriendsLabel.setText(QtGui.QApplication.translate("MainWindow", "Friends", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchClientsLabel.setText(QtGui.QApplication.translate("MainWindow", "Search Clients", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchForLabel.setText(QtGui.QApplication.translate("MainWindow", "Search For:", None, QtGui.QApplication.UnicodeUTF8))
        self.METARtableWidget.setSortingEnabled(True)
        self.METARtableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.METARtableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.MetarLabel.setText(QtGui.QApplication.translate("MainWindow", "METAR", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchcomboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "CallSign", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchcomboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "VID", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchcomboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QtGui.QApplication.translate("MainWindow", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.ATCtableWidget.setSortingEnabled(True)
        self.ATCtableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "VID", None, QtGui.QApplication.UnicodeUTF8))
        self.ATCtableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.ATCtableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Facility", None, QtGui.QApplication.UnicodeUTF8))
        self.ATCtableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.ATCtableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.ATCtableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.atc_label.setText(QtGui.QApplication.translate("MainWindow", "ATC List", None, QtGui.QApplication.UnicodeUTF8))
        self.pilot_list.setText(QtGui.QApplication.translate("MainWindow", "PILOT List", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "VID", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Captain", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Aircraft", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Departure", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.PilottableWidget.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.countries), QtGui.QApplication.translate("MainWindow", "Countries", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.setSortingEnabled(True)
        self.ATC_FullList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "CallSign", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Position", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "IVAN", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "IVAT", None, QtGui.QApplication.UnicodeUTF8))
        self.ATC_FullList.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.controllers), QtGui.QApplication.translate("MainWindow", "Controllers", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.setSortingEnabled(True)
        self.PILOT_FullList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "CallSign", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Aircraft", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Captain", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Departure", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "IVAN", None, QtGui.QApplication.UnicodeUTF8))
        self.PILOT_FullList.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pilots), QtGui.QApplication.translate("MainWindow", "Pilots", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.observers), QtGui.QApplication.translate("MainWindow", "Observers", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.database), QtGui.QApplication.translate("MainWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.Inbound_traffic.setText(QtGui.QApplication.translate("MainWindow", "Inbound Traffic", None, QtGui.QApplication.UnicodeUTF8))
        self.outbound_traffic.setText(QtGui.QApplication.translate("MainWindow", "Outbound Traffic", None, QtGui.QApplication.UnicodeUTF8))
        self.nearby_controllers.setText(QtGui.QApplication.translate("MainWindow", "Nearby Controllers", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actual_user), QtGui.QApplication.translate("MainWindow", "Actual User", None, QtGui.QApplication.UnicodeUTF8))
        self.UpdateBtn.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.ExitBtn.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_update.setText(QtGui.QApplication.translate("MainWindow", "Ready", None, QtGui.QApplication.UnicodeUTF8))

