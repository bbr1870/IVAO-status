# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/PilotInfo_UI.ui'
#
# Created: Tue Sep 13 11:07:18 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QPilotInfo(object):
    def setupUi(self, QPilotInfo):
        QPilotInfo.setObjectName(_fromUtf8("QPilotInfo"))
        QPilotInfo.setWindowModality(QtCore.Qt.WindowModal)
        QPilotInfo.resize(491, 540)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QPilotInfo.sizePolicy().hasHeightForWidth())
        QPilotInfo.setSizePolicy(sizePolicy)
        QPilotInfo.setMinimumSize(QtCore.QSize(491, 540))
        QPilotInfo.setMaximumSize(QtCore.QSize(491, 540))
        QPilotInfo.setCursor(QtCore.Qt.PointingHandCursor)
        QPilotInfo.setFocusPolicy(QtCore.Qt.StrongFocus)
        QPilotInfo.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(QPilotInfo)
        self.centralwidget.setCursor(QtCore.Qt.PointingHandCursor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.callsign_label = QtGui.QLabel(self.centralwidget)
        self.callsign_label.setGeometry(QtCore.QRect(10, 47, 57, 14))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.callsign_label.setFont(font)
        self.callsign_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.callsign_label.setObjectName(_fromUtf8("callsign_label"))
        self.callsign_text = QtGui.QLabel(self.centralwidget)
        self.callsign_text.setGeometry(QtCore.QRect(70, 41, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.callsign_text.setFont(font)
        self.callsign_text.setCursor(QtCore.Qt.PointingHandCursor)
        self.callsign_text.setText(_fromUtf8(""))
        self.callsign_text.setObjectName(_fromUtf8("callsign_text"))
        self.rating_img = QtGui.QLabel(self.centralwidget)
        self.rating_img.setGeometry(QtCore.QRect(310, 42, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rating_img.setFont(font)
        self.rating_img.setCursor(QtCore.Qt.PointingHandCursor)
        self.rating_img.setText(_fromUtf8(""))
        self.rating_img.setObjectName(_fromUtf8("rating_img"))
        self.rating_label = QtGui.QLabel(self.centralwidget)
        self.rating_label.setGeometry(QtCore.QRect(265, 47, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.rating_label.setFont(font)
        self.rating_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.rating_label.setObjectName(_fromUtf8("rating_label"))
        self.progressBarTrack = QtGui.QProgressBar(self.centralwidget)
        self.progressBarTrack.setGeometry(QtCore.QRect(56, 188, 381, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBarTrack.setFont(font)
        self.progressBarTrack.setCursor(QtCore.Qt.PointingHandCursor)
        self.progressBarTrack.setProperty(_fromUtf8("value"), 0)
        self.progressBarTrack.setFormat(_fromUtf8(""))
        self.progressBarTrack.setObjectName(_fromUtf8("progressBarTrack"))
        self.DepartureImage = QtGui.QLabel(self.centralwidget)
        self.DepartureImage.setGeometry(QtCore.QRect(30, 180, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DepartureImage.setFont(font)
        self.DepartureImage.setCursor(QtCore.Qt.PointingHandCursor)
        self.DepartureImage.setText(_fromUtf8(""))
        self.DepartureImage.setObjectName(_fromUtf8("DepartureImage"))
        self.DestinationImage = QtGui.QLabel(self.centralwidget)
        self.DestinationImage.setGeometry(QtCore.QRect(441, 180, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DestinationImage.setFont(font)
        self.DestinationImage.setCursor(QtCore.Qt.PointingHandCursor)
        self.DestinationImage.setText(_fromUtf8(""))
        self.DestinationImage.setObjectName(_fromUtf8("DestinationImage"))
        self.Departure_Info = QtGui.QLabel(self.centralwidget)
        self.Departure_Info.setGeometry(QtCore.QRect(10, 110, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.Departure_Info.setFont(font)
        self.Departure_Info.setCursor(QtCore.Qt.PointingHandCursor)
        self.Departure_Info.setObjectName(_fromUtf8("Departure_Info"))
        self.Destination_Info = QtGui.QLabel(self.centralwidget)
        self.Destination_Info.setGeometry(QtCore.QRect(253, 110, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.Destination_Info.setFont(font)
        self.Destination_Info.setCursor(QtCore.Qt.PointingHandCursor)
        self.Destination_Info.setObjectName(_fromUtf8("Destination_Info"))
        self.DepartureText = QtGui.QLabel(self.centralwidget)
        self.DepartureText.setGeometry(QtCore.QRect(10, 130, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DepartureText.setFont(font)
        self.DepartureText.setCursor(QtCore.Qt.PointingHandCursor)
        self.DepartureText.setText(_fromUtf8(""))
        self.DepartureText.setObjectName(_fromUtf8("DepartureText"))
        self.DestinationText = QtGui.QLabel(self.centralwidget)
        self.DestinationText.setGeometry(QtCore.QRect(253, 130, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DestinationText.setFont(font)
        self.DestinationText.setCursor(QtCore.Qt.PointingHandCursor)
        self.DestinationText.setText(_fromUtf8(""))
        self.DestinationText.setObjectName(_fromUtf8("DestinationText"))
        self.RouteText = QtGui.QTextEdit(self.centralwidget)
        self.RouteText.setGeometry(QtCore.QRect(8, 352, 476, 111))
        self.RouteText.setReadOnly(True)
        self.RouteText.setObjectName(_fromUtf8("RouteText"))
        self.Route_label = QtGui.QLabel(self.centralwidget)
        self.Route_label.setGeometry(QtCore.QRect(15, 332, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.Route_label.setFont(font)
        self.Route_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.Route_label.setObjectName(_fromUtf8("Route_label"))
        self.AddFriend = QtGui.QPushButton(self.centralwidget)
        self.AddFriend.setGeometry(QtCore.QRect(145, 497, 99, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddFriend.setFont(font)
        self.AddFriend.setCursor(QtCore.Qt.PointingHandCursor)
        self.AddFriend.setObjectName(_fromUtf8("AddFriend"))
        self.Close = QtGui.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(250, 497, 99, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Close.setFont(font)
        self.Close.setCursor(QtCore.Qt.PointingHandCursor)
        self.Close.setObjectName(_fromUtf8("Close"))
        self.GroundSpeed_label = QtGui.QLabel(self.centralwidget)
        self.GroundSpeed_label.setGeometry(QtCore.QRect(195, 210, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.GroundSpeed_label.setFont(font)
        self.GroundSpeed_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.GroundSpeed_label.setObjectName(_fromUtf8("GroundSpeed_label"))
        self.GroundSpeedNumber = QtGui.QLabel(self.centralwidget)
        self.GroundSpeedNumber.setGeometry(QtCore.QRect(290, 208, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GroundSpeedNumber.setFont(font)
        self.GroundSpeedNumber.setCursor(QtCore.Qt.PointingHandCursor)
        self.GroundSpeedNumber.setText(_fromUtf8(""))
        self.GroundSpeedNumber.setObjectName(_fromUtf8("GroundSpeedNumber"))
        self.AltitudeNumber = QtGui.QLabel(self.centralwidget)
        self.AltitudeNumber.setGeometry(QtCore.QRect(435, 208, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AltitudeNumber.setFont(font)
        self.AltitudeNumber.setCursor(QtCore.Qt.PointingHandCursor)
        self.AltitudeNumber.setText(_fromUtf8(""))
        self.AltitudeNumber.setObjectName(_fromUtf8("AltitudeNumber"))
        self.Altitude_label = QtGui.QLabel(self.centralwidget)
        self.Altitude_label.setGeometry(QtCore.QRect(380, 210, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.Altitude_label.setFont(font)
        self.Altitude_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.Altitude_label.setObjectName(_fromUtf8("Altitude_label"))
        self.FlightStatusNumber = QtGui.QLabel(self.centralwidget)
        self.FlightStatusNumber.setGeometry(QtCore.QRect(105, 208, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.FlightStatusNumber.setFont(font)
        self.FlightStatusNumber.setCursor(QtCore.Qt.PointingHandCursor)
        self.FlightStatusNumber.setText(_fromUtf8(""))
        self.FlightStatusNumber.setObjectName(_fromUtf8("FlightStatusNumber"))
        self.FlightStatus_label = QtGui.QLabel(self.centralwidget)
        self.FlightStatus_label.setGeometry(QtCore.QRect(16, 210, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.FlightStatus_label.setFont(font)
        self.FlightStatus_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.FlightStatus_label.setObjectName(_fromUtf8("FlightStatus_label"))
        self.line1 = QtGui.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(15, 75, 461, 16))
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.line2 = QtGui.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(10, 467, 461, 16))
        self.line2.setFrameShape(QtGui.QFrame.HLine)
        self.line2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2.setObjectName(_fromUtf8("line2"))
        self.PilotInfo = QtGui.QLabel(self.centralwidget)
        self.PilotInfo.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.PilotInfo.setFont(font)
        self.PilotInfo.setCursor(QtCore.Qt.PointingHandCursor)
        self.PilotInfo.setObjectName(_fromUtf8("PilotInfo"))
        self.FlightDetails = QtGui.QLabel(self.centralwidget)
        self.FlightDetails.setGeometry(QtCore.QRect(10, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.FlightDetails.setFont(font)
        self.FlightDetails.setCursor(QtCore.Qt.PointingHandCursor)
        self.FlightDetails.setObjectName(_fromUtf8("FlightDetails"))
        self.PilotNameText = QtGui.QLabel(self.centralwidget)
        self.PilotNameText.setGeometry(QtCore.QRect(129, 5, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PilotNameText.setFont(font)
        self.PilotNameText.setCursor(QtCore.Qt.PointingHandCursor)
        self.PilotNameText.setText(_fromUtf8(""))
        self.PilotNameText.setObjectName(_fromUtf8("PilotNameText"))
        self.Home = QtGui.QLabel(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(357, 10, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.Home.setFont(font)
        self.Home.setCursor(QtCore.Qt.PointingHandCursor)
        self.Home.setObjectName(_fromUtf8("Home"))
        self.HomeFlag = QtGui.QLabel(self.centralwidget)
        self.HomeFlag.setGeometry(QtCore.QRect(397, 5, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.HomeFlag.setFont(font)
        self.HomeFlag.setCursor(QtCore.Qt.PointingHandCursor)
        self.HomeFlag.setText(_fromUtf8(""))
        self.HomeFlag.setObjectName(_fromUtf8("HomeFlag"))
        self.airline_image = QtGui.QLabel(self.centralwidget)
        self.airline_image.setGeometry(QtCore.QRect(130, 42, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.airline_image.setFont(font)
        self.airline_image.setCursor(QtCore.Qt.PointingHandCursor)
        self.airline_image.setText(_fromUtf8(""))
        self.airline_image.setObjectName(_fromUtf8("airline_image"))
        self.PobText = QtGui.QLabel(self.centralwidget)
        self.PobText.setGeometry(QtCore.QRect(161, 301, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PobText.setFont(font)
        self.PobText.setCursor(QtCore.Qt.PointingHandCursor)
        self.PobText.setText(_fromUtf8(""))
        self.PobText.setObjectName(_fromUtf8("PobText"))
        self.TransponderText = QtGui.QLabel(self.centralwidget)
        self.TransponderText.setGeometry(QtCore.QRect(358, 300, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TransponderText.setFont(font)
        self.TransponderText.setCursor(QtCore.Qt.PointingHandCursor)
        self.TransponderText.setText(_fromUtf8(""))
        self.TransponderText.setObjectName(_fromUtf8("TransponderText"))
        self.TransponderLabel = QtGui.QLabel(self.centralwidget)
        self.TransponderLabel.setGeometry(QtCore.QRect(270, 302, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.TransponderLabel.setFont(font)
        self.TransponderLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.TransponderLabel.setObjectName(_fromUtf8("TransponderLabel"))
        self.POBLabel = QtGui.QLabel(self.centralwidget)
        self.POBLabel.setGeometry(QtCore.QRect(16, 303, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.POBLabel.setFont(font)
        self.POBLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.POBLabel.setObjectName(_fromUtf8("POBLabel"))
        self.AirplaneLabel = QtGui.QLabel(self.centralwidget)
        self.AirplaneLabel.setGeometry(QtCore.QRect(16, 248, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.AirplaneLabel.setFont(font)
        self.AirplaneLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.AirplaneLabel.setObjectName(_fromUtf8("AirplaneLabel"))
        self.AirplaneText = QtGui.QLabel(self.centralwidget)
        self.AirplaneText.setGeometry(QtCore.QRect(17, 260, 461, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AirplaneText.setFont(font)
        self.AirplaneText.setCursor(QtCore.Qt.PointingHandCursor)
        self.AirplaneText.setText(_fromUtf8(""))
        self.AirplaneText.setObjectName(_fromUtf8("AirplaneText"))
        self.vid_label = QtGui.QLabel(self.centralwidget)
        self.vid_label.setGeometry(QtCore.QRect(11, 28, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.vid_label.setFont(font)
        self.vid_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.vid_label.setObjectName(_fromUtf8("vid_label"))
        self.vidText = QtGui.QLabel(self.centralwidget)
        self.vidText.setGeometry(QtCore.QRect(38, 28, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.vidText.setFont(font)
        self.vidText.setCursor(QtCore.Qt.PointingHandCursor)
        self.vidText.setText(_fromUtf8(""))
        self.vidText.setObjectName(_fromUtf8("vidText"))
        QPilotInfo.setCentralWidget(self.centralwidget)

        self.retranslateUi(QPilotInfo)
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL(_fromUtf8("clicked()")), QPilotInfo.close)
        QtCore.QMetaObject.connectSlotsByName(QPilotInfo)

    def retranslateUi(self, QPilotInfo):
        QPilotInfo.setWindowTitle(QtGui.QApplication.translate("QPilotInfo", "Flight Info", None, QtGui.QApplication.UnicodeUTF8))
        self.callsign_label.setText(QtGui.QApplication.translate("QPilotInfo", "Callsign", None, QtGui.QApplication.UnicodeUTF8))
        self.rating_label.setText(QtGui.QApplication.translate("QPilotInfo", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.Departure_Info.setText(QtGui.QApplication.translate("QPilotInfo", "Departure", None, QtGui.QApplication.UnicodeUTF8))
        self.Destination_Info.setText(QtGui.QApplication.translate("QPilotInfo", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.Route_label.setText(QtGui.QApplication.translate("QPilotInfo", "Route", None, QtGui.QApplication.UnicodeUTF8))
        self.AddFriend.setText(QtGui.QApplication.translate("QPilotInfo", "Add Friend", None, QtGui.QApplication.UnicodeUTF8))
        self.Close.setText(QtGui.QApplication.translate("QPilotInfo", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.GroundSpeed_label.setText(QtGui.QApplication.translate("QPilotInfo", "Ground Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.Altitude_label.setText(QtGui.QApplication.translate("QPilotInfo", "Altitude", None, QtGui.QApplication.UnicodeUTF8))
        self.FlightStatus_label.setText(QtGui.QApplication.translate("QPilotInfo", "Flight Status", None, QtGui.QApplication.UnicodeUTF8))
        self.PilotInfo.setText(QtGui.QApplication.translate("QPilotInfo", "Pilot in Command", None, QtGui.QApplication.UnicodeUTF8))
        self.FlightDetails.setText(QtGui.QApplication.translate("QPilotInfo", "Flight Details", None, QtGui.QApplication.UnicodeUTF8))
        self.Home.setText(QtGui.QApplication.translate("QPilotInfo", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.TransponderLabel.setText(QtGui.QApplication.translate("QPilotInfo", "Transponder", None, QtGui.QApplication.UnicodeUTF8))
        self.POBLabel.setText(QtGui.QApplication.translate("QPilotInfo", "Passengers on Board", None, QtGui.QApplication.UnicodeUTF8))
        self.AirplaneLabel.setText(QtGui.QApplication.translate("QPilotInfo", "Airplane", None, QtGui.QApplication.UnicodeUTF8))
        self.vid_label.setText(QtGui.QApplication.translate("QPilotInfo", "VID", None, QtGui.QApplication.UnicodeUTF8))

