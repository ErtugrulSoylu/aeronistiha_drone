# Form implementation generated from reading ui file '../drone.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1037, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 48, 63))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 113, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 48, 63))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 113, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 113, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grafik_kamera = QtWidgets.QGraphicsView(self.centralwidget)
        self.grafik_kamera.setGeometry(QtCore.QRect(780, 10, 251, 271))
        self.grafik_kamera.setStyleSheet("background: rgba(61, 56, 70, 0.8);\n"
"border-radius: 10px")
        self.grafik_kamera.setObjectName("grafik_kamera")
        self.label_kamera = QtWidgets.QLabel(self.centralwidget)
        self.label_kamera.setGeometry(QtCore.QRect(790, 20, 55, 16))
        self.label_kamera.setObjectName("label_kamera")
        self.scriptButon_otonomKalkisInis = QtWidgets.QPushButton(self.centralwidget)
        self.scriptButon_otonomKalkisInis.setGeometry(QtCore.QRect(840, 590, 91, 31))
        self.scriptButon_otonomKalkisInis.setObjectName("scriptButon_otonomKalkisInis")
        self.scriptButon_armTest = QtWidgets.QPushButton(self.centralwidget)
        self.scriptButon_armTest.setGeometry(QtCore.QRect(940, 630, 81, 31))
        self.scriptButon_armTest.setObjectName("scriptButon_armTest")
        self.text_durum = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_durum.setGeometry(QtCore.QRect(300, 590, 421, 71))
        self.text_durum.setStyleSheet("background: rgb(61, 56, 70);\n"
"border-radius: 10px")
        self.text_durum.setObjectName("text_durum")
        self.label_durum = QtWidgets.QLabel(self.centralwidget)
        self.label_durum.setGeometry(QtCore.QRect(310, 570, 71, 20))
        self.label_durum.setObjectName("label_durum")
        self.scriptButon_acilInis = QtWidgets.QPushButton(self.centralwidget)
        self.scriptButon_acilInis.setGeometry(QtCore.QRect(840, 630, 91, 31))
        self.scriptButon_acilInis.setObjectName("scriptButon_acilInis")
        self.scriptButon_yuksel = QtWidgets.QPushButton(self.centralwidget)
        self.scriptButon_yuksel.setGeometry(QtCore.QRect(940, 590, 81, 31))
        self.scriptButon_yuksel.setObjectName("scriptButon_yuksel")
        self.modButon_stabilize = QtWidgets.QPushButton(self.centralwidget)
        self.modButon_stabilize.setGeometry(QtCore.QRect(20, 600, 91, 31))
        self.modButon_stabilize.setObjectName("modButon_stabilize")
        self.modButon_guided = QtWidgets.QPushButton(self.centralwidget)
        self.modButon_guided.setGeometry(QtCore.QRect(20, 510, 91, 31))
        self.modButon_guided.setObjectName("modButon_guided")
        self.modButon_loiter = QtWidgets.QPushButton(self.centralwidget)
        self.modButon_loiter.setGeometry(QtCore.QRect(20, 540, 91, 31))
        self.modButon_loiter.setObjectName("modButon_loiter")
        self.modButon_land = QtWidgets.QPushButton(self.centralwidget)
        self.modButon_land.setGeometry(QtCore.QRect(20, 570, 91, 31))
        self.modButon_land.setObjectName("modButon_land")
        self.modButon_poshold = QtWidgets.QPushButton(self.centralwidget)
        self.modButon_poshold.setGeometry(QtCore.QRect(20, 630, 91, 31))
        self.modButon_poshold.setObjectName("modButon_poshold")
        self.attribute_ucusModu = QtWidgets.QTextBrowser(self.centralwidget)
        self.attribute_ucusModu.setGeometry(QtCore.QRect(60, 470, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.attribute_ucusModu.setFont(font)
        self.attribute_ucusModu.setStyleSheet("")
        self.attribute_ucusModu.setObjectName("attribute_ucusModu")
        self.attribute_pilSeviyesi = QtWidgets.QProgressBar(self.centralwidget)
        self.attribute_pilSeviyesi.setGeometry(QtCore.QRect(80, 200, 71, 21))
        self.attribute_pilSeviyesi.setStyleSheet("")
        self.attribute_pilSeviyesi.setProperty("value", 24)
        self.attribute_pilSeviyesi.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.attribute_pilSeviyesi.setInvertedAppearance(False)
        self.attribute_pilSeviyesi.setObjectName("attribute_pilSeviyesi")
        self.attribute_cekilenAkim = QtWidgets.QLCDNumber(self.centralwidget)
        self.attribute_cekilenAkim.setGeometry(QtCore.QRect(80, 120, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        self.attribute_cekilenAkim.setPalette(palette)
        self.attribute_cekilenAkim.setAutoFillBackground(False)
        self.attribute_cekilenAkim.setStyleSheet("background: rgb(61, 56, 70);")
        self.attribute_cekilenAkim.setObjectName("attribute_cekilenAkim")
        self.attribute_yatayHiz = QtWidgets.QLCDNumber(self.centralwidget)
        self.attribute_yatayHiz.setGeometry(QtCore.QRect(80, 20, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        self.attribute_yatayHiz.setPalette(palette)
        self.attribute_yatayHiz.setAutoFillBackground(False)
        self.attribute_yatayHiz.setStyleSheet("background: rgb(61, 56, 70);")
        self.attribute_yatayHiz.setObjectName("attribute_yatayHiz")
        self.attribute_dikeyHiz = QtWidgets.QLCDNumber(self.centralwidget)
        self.attribute_dikeyHiz.setGeometry(QtCore.QRect(80, 60, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        self.attribute_dikeyHiz.setPalette(palette)
        self.attribute_dikeyHiz.setAutoFillBackground(False)
        self.attribute_dikeyHiz.setStyleSheet("background: rgb(61, 56, 70);")
        self.attribute_dikeyHiz.setObjectName("attribute_dikeyHiz")
        self.label_yatayHiz = QtWidgets.QLabel(self.centralwidget)
        self.label_yatayHiz.setGeometry(QtCore.QRect(20, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_yatayHiz.setFont(font)
        self.label_yatayHiz.setObjectName("label_yatayHiz")
        self.label_cekilenAkim = QtWidgets.QLabel(self.centralwidget)
        self.label_cekilenAkim.setGeometry(QtCore.QRect(20, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_cekilenAkim.setFont(font)
        self.label_cekilenAkim.setObjectName("label_cekilenAkim")
        self.label_pil = QtWidgets.QLabel(self.centralwidget)
        self.label_pil.setGeometry(QtCore.QRect(20, 200, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_pil.setFont(font)
        self.label_pil.setObjectName("label_pil")
        self.label_dikeyHiz = QtWidgets.QLabel(self.centralwidget)
        self.label_dikeyHiz.setGeometry(QtCore.QRect(20, 60, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_dikeyHiz.setFont(font)
        self.label_dikeyHiz.setObjectName("label_dikeyHiz")
        self.label_ucusModu = QtWidgets.QLabel(self.centralwidget)
        self.label_ucusModu.setGeometry(QtCore.QRect(20, 470, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_ucusModu.setFont(font)
        self.label_ucusModu.setObjectName("label_ucusModu")
        self.attribute_voltaj = QtWidgets.QLCDNumber(self.centralwidget)
        self.attribute_voltaj.setGeometry(QtCore.QRect(80, 160, 71, 31))
        self.attribute_voltaj.setAutoFillBackground(False)
        self.attribute_voltaj.setStyleSheet("background: rgb(61, 56, 70);")
        self.attribute_voltaj.setObjectName("attribute_voltaj")
        self.label_voltaj = QtWidgets.QLabel(self.centralwidget)
        self.label_voltaj.setGeometry(QtCore.QRect(20, 160, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_voltaj.setFont(font)
        self.label_voltaj.setObjectName("label_voltaj")
        self.mapArea = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.mapArea.setGeometry(QtCore.QRect(0, 0, 1041, 681))
        self.mapArea.setStyleSheet("background: white")
        self.mapArea.setUrl(QtCore.QUrl("about:blank"))
        self.mapArea.setObjectName("mapArea")
        self.label_bg_gray = QtWidgets.QLabel(self.centralwidget)
        self.label_bg_gray.setGeometry(QtCore.QRect(10, 10, 151, 221))
        self.label_bg_gray.setStyleSheet("background: rgba(61, 56, 70, 0.8);\n"
"border-radius: 10px")
        self.label_bg_gray.setText("")
        self.label_bg_gray.setObjectName("label_bg_gray")
        self.label_bg_gray2 = QtWidgets.QLabel(self.centralwidget)
        self.label_bg_gray2.setGeometry(QtCore.QRect(10, 460, 121, 211))
        self.label_bg_gray2.setStyleSheet("background: rgba(61, 56, 70, 0.9 );\n"
"border-radius: 10px")
        self.label_bg_gray2.setText("")
        self.label_bg_gray2.setObjectName("label_bg_gray2")
        self.label_bg_gray3 = QtWidgets.QLabel(self.centralwidget)
        self.label_bg_gray3.setGeometry(QtCore.QRect(290, 570, 441, 101))
        self.label_bg_gray3.setStyleSheet("background: rgba(61, 56, 70, 0.8);\n"
"border-radius: 10px")
        self.label_bg_gray3.setText("")
        self.label_bg_gray3.setObjectName("label_bg_gray3")
        self.label_bg_gray4 = QtWidgets.QLabel(self.centralwidget)
        self.label_bg_gray4.setGeometry(QtCore.QRect(830, 580, 201, 91))
        self.label_bg_gray4.setStyleSheet("background: rgba(61, 56, 70, 0.8);\n"
"border-radius: 10px")
        self.label_bg_gray4.setText("")
        self.label_bg_gray4.setObjectName("label_bg_gray4")
        self.mapArea.raise_()
        self.label_bg_gray4.raise_()
        self.label_bg_gray3.raise_()
        self.label_bg_gray2.raise_()
        self.label_bg_gray.raise_()
        self.grafik_kamera.raise_()
        self.label_kamera.raise_()
        self.scriptButon_otonomKalkisInis.raise_()
        self.scriptButon_armTest.raise_()
        self.text_durum.raise_()
        self.label_durum.raise_()
        self.scriptButon_acilInis.raise_()
        self.scriptButon_yuksel.raise_()
        self.modButon_stabilize.raise_()
        self.modButon_guided.raise_()
        self.modButon_loiter.raise_()
        self.modButon_land.raise_()
        self.modButon_poshold.raise_()
        self.attribute_ucusModu.raise_()
        self.attribute_pilSeviyesi.raise_()
        self.attribute_cekilenAkim.raise_()
        self.attribute_yatayHiz.raise_()
        self.attribute_dikeyHiz.raise_()
        self.label_yatayHiz.raise_()
        self.label_cekilenAkim.raise_()
        self.label_pil.raise_()
        self.label_dikeyHiz.raise_()
        self.label_ucusModu.raise_()
        self.attribute_voltaj.raise_()
        self.label_voltaj.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aeronist Arayuz"))
        self.label_kamera.setText(_translate("MainWindow", "Kamera"))
        self.scriptButon_otonomKalkisInis.setText(_translate("MainWindow", "KALKIS_INIS"))
        self.scriptButon_armTest.setText(_translate("MainWindow", "ARM TEST"))
        self.label_durum.setText(_translate("MainWindow", "Durum"))
        self.scriptButon_acilInis.setText(_translate("MainWindow", "ACIL INIS"))
        self.scriptButon_yuksel.setText(_translate("MainWindow", "YUKSEL"))
        self.modButon_stabilize.setText(_translate("MainWindow", "STABILIZE"))
        self.modButon_guided.setText(_translate("MainWindow", "GUIDED"))
        self.modButon_loiter.setText(_translate("MainWindow", "LOITER"))
        self.modButon_land.setText(_translate("MainWindow", "LAND"))
        self.modButon_poshold.setText(_translate("MainWindow", "POS_HOLD"))
        self.label_yatayHiz.setText(_translate("MainWindow", "Yatay\n"
"  Hız"))
        self.label_cekilenAkim.setText(_translate("MainWindow", "Çekilen\n"
" Akım"))
        self.label_pil.setText(_translate("MainWindow", "Pil"))
        self.label_dikeyHiz.setText(_translate("MainWindow", "Dikey\n"
"  Hız"))
        self.label_ucusModu.setText(_translate("MainWindow", "Mod"))
        self.label_voltaj.setText(_translate("MainWindow", "Voltaj"))
