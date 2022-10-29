# kullanisli araclar
import threading
import math
import sys
import os
# kullanici arayuzu
import cv2
from fileinput import filename
# PyQt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, pyqtSignal, QObject, QCoreApplication, QTimer, QUrl, QEvent, pyqtSlot, QThread
from PyQt6.QtWebEngineWidgets import QWebEngineView
from inc.ui_drone import Ui_MainWindow
# drone
from dronekit import connect, VehicleMode
from src.ucus_komutlari import aero
# veriler
import pandas as pd

connection = None
simulation = True

if connection:
    vehicle = connection
elif simulation:
    vehicle = connect("127.0.0.1:14550")
    print('IHA SIMULASYON ORTAMINA HAZIR')
else:
    vehicle = connect("/dev/serial0", baudrate=57600)
    print('IHA PIXHAWKA BAGLANDI\n')
ui = Ui_MainWindow()

veriDict = {'yatay hiz':[],'dikey hiz':[], 'pil seviyesi':[], 'cekilen akim':[], 'voltaj':[] , 'zaman':[]}
time = 0

class Attributes(QObject):
    # Sinyaller
    bataryaGonder = pyqtSignal(list)
    hizGonder = pyqtSignal(list)
    modGonder = pyqtSignal(list)
    haritaGonder = pyqtSignal(list)
    kameraGonder = pyqtSignal(QImage)

def bataryaGuncelle(value):
    ui.attribute_cekilenAkim.display(value[0])
    ui.attribute_pilSeviyesi.setValue(value[1])
    ui.attribute_voltaj.display(value[2])

def hizGuncelle(value):
    yatayHiz = (int)(math.sqrt(value[0]**2 + value[1]**2) * 10) / 10
    dikeyHiz = (int)((-value[2]) * 10) / 10
    ui.attribute_yatayHiz.display(yatayHiz)
    ui.attribute_dikeyHiz.display(dikeyHiz)

def modGuncelle(value):
    ui.attribute_ucusModu.setText(value[0])

def haritaGuncelle(value):
    ui.mapArea.page().runJavaScript("changeLocation({}, {})".format(value[0], value[1]))
    return

def kameraGuncelle(image):
    ui.label_kameracv2.setPixmap(QPixmap.fromImage(image))


# Sinyaller
attr = Attributes()
attr.bataryaGonder.connect(bataryaGuncelle)
attr.hizGonder.connect(hizGuncelle)
attr.modGonder.connect(modGuncelle)
attr.haritaGonder.connect(haritaGuncelle)
attr.kameraGonder.connect(kameraGuncelle)

class CamReader(QThread):
    def run(self):
        cap = cv2.VideoCapture("/dev/video2")
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
                p = convertToQtFormat.scaled(251, 200)
                attr.kameraGonder.emit(p)

# Window
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.main_win.closeEvent = self.exit
        ui.setupUi(self.main_win)

        self.main_win.m_flag = False
        vehicleThreadFlag = False
        self.coordinates = (0, 0)
        
        # Zamanlayici
        self.timer = QTimer()
        self.timer.timeout.connect(self.zamanGuncelle)
        self.timer.timeout.connect(self.veriGuncelle)
        self.timer.start(1000)
        self.closing = False

        # Butonlar
        ui.scriptButon_armTest.clicked.connect(self.armTest)
        ui.scriptButon_otonomKalkisInis.clicked.connect(self.otonomKalkisInis)
        ui.scriptButon_acilInis.clicked.connect(self.acilInis)
        ui.scriptButon_yuksel.clicked.connect(self.yuksel)
        
        ui.modButon_guided.clicked.connect(self.guidedMode)     
        ui.modButon_loiter.clicked.connect(self.loiterMode)
        ui.modButon_poshold.clicked.connect(self.posHoldMode)
        ui.modButon_land.clicked.connect(self.landMode)
        ui.modButon_stabilize.clicked.connect(self.stabilizeMode)

        # Harita
        ui.mapArea.loadFinished.connect(self.initMap)
        ui.mapArea.setHtml(open('index.html', 'r').read())
        
        # Kamera
        self.cam = CamReader(ui.grafik_kamera)
        self.cam.start()

    ############################################################################################################
    ######################################            GEREKLI              #####################################
    ############################################################################################################

    def show(self):
        self.main_win.show()

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.main_win.m_flag=True
            self.main_win.m_Position=event.globalPos()-self.main_win.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.main_win.m_flag:  
            self.main_win.move(QMouseEvent.globalPos()-self.main_win.m_Position)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.main_win.m_flag=False

    ############################################################################################################
    #####################################       ATTRIBUTE LISTENERS        #####################################
    ############################################################################################################

    @vehicle.on_attribute('velocity')
    def hizOku(self, attr_name, value):
        attr.hizGonder.emit(value)

    @vehicle.on_attribute('battery')
    def bataryaOku(self, attr_name, value):
        attr.bataryaGonder.emit([value.current, value.level,    value.voltage])
    
    def zamanGuncelle(self):
        global time
        time += 1

    def veriGuncelle(self):
        if self.closing is False:
            veriDict['cekilen akim'].append(vehicle.battery.current)
            veriDict['pil seviyesi'].append(vehicle.battery.level)
            veriDict['voltaj'].append(vehicle.battery.voltage)
            veriDict['yatay hiz'].append((int)(math.sqrt(vehicle.velocity[0]**2 + vehicle.velocity[1]**2) * 10) / 10)
            veriDict['dikey hiz'].append((int)((-vehicle.velocity[2]) * 10) / 10)
            veriDict['zaman'].append(time)

    def durumGuncelle(self, text = ""):
        return

    def kameraGuncelle(self, image):
        return

    @vehicle.on_attribute('mode')
    def modOku(self, attr_name, value):
        attr.modGonder.emit([value.name])
    

    ############################################################################################################
    ######################################             HARITA             ######################################
    ############################################################################################################

    def initMap(self, ok):
        lat = vehicle.location.global_frame.lat
        lon = vehicle.location.global_frame.lon

        print(lat, lon)
        ui.mapArea.page().runJavaScript("changeLocation({}, {})".format(lat, lon))

        if ok:
            ui.mapArea.page().runJavaScript("loadMap({}, {})".format(lat, lon))

    @vehicle.on_attribute('location.global_frame')
    def haritaGuncelle(self, attr_name, value):
        lat = vehicle.location.global_frame.lat
        lon = vehicle.location.global_frame.lon
        
        attr.haritaGonder.emit([lat, lon])

    ############################################################################################################
    ######################################            BUTONLAR            ######################################
    ############################################################################################################

    ## SCRIPTS ##

    def scriptThread(self, target):
        if vehicleThreadFlag is False:
            vehicleThreadFlag = True
            target()
            vehicleThreadFlag = False

    def armTest(self):
        threading.Thread(target=self.scriptThread, args=(vehicle.test, )).start()

    def otonomKalkisInis(self):
        threading.Thread(target=self.scriptThread, args=(vehicle.otonom_kalkis_inis, )).start()

    def acilInis(self):
        vehicleThreadFlag = True
        vehicle.acil_inis()
        vehicleThreadFlag = False

    def yuksel(self):
        threading.Thread(target=self.scriptThread, args=(vehicle.otonom_yuksel, )).start()

    ## MODES ##

    def stabilizeMode(self):    
        vehicle.mode = VehicleMode('STABILIZE')

    def loiterMode(self):
        vehicle.mode = VehicleMode('LOITER')

    def guidedMode(self):
        vehicle.mode = VehicleMode('GUIDED')

    def landMode(self):
        vehicle.mode = VehicleMode('LAND')

    def posHoldMode(self):
        vehicle.mode = VehicleMode('POSHOLD')
    
    ############################################################################################################
    ######################################          LOG DOSYALARI         ######################################
    ############################################################################################################

    def logging(self):
        if not os.path.isdir("logs"):
            os.makedirs("logs")

        files = os.listdir('./logs/')
        
        # en son tutulan logu bulma
        try:
            fileNum = max([int(''.join(filter(str.isdigit, files[i]))) for i in range(len(files))])
        except:
            fileNum = '-1'
        fileNum = str(int(fileNum) + 1)
        
        dataframe = pd.DataFrame.from_dict(veriDict)

        # pandas ile excel dosyasi acma
        file_name = './logs/' + fileNum + '_log.xlsx'
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

        # icini doldurma
        sheet_name='grafikler'
        dataframe.to_excel(writer, sheet_name=sheet_name)
        
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        
        (max_row, max_col) = dataframe.shape
        chart = workbook.add_chart({'type': 'line'})

        for col in range(1, max_col+1):
            chart.add_series({
                'name':       [sheet_name, 0, col],
                'categories': [sheet_name, 1, 0,   max_row, 0],
                'values':     [sheet_name, 1, col, max_row, col],
            })

        chart.set_x_axis({'name': 'Zaman(s)'})
        chart.set_y_axis({'name': 'Değerler', 'major_gridlines': {'visible': False}})

        worksheet.insert_chart(1, 8, chart)

        # excel dosyasini kapama
        workbook.close()

    def exit(self, event=None):
        self.closing = True

        # kamera threadini kapatma
        self.cam.isRunning = False
        self.cam.exit()
        self.cam.wait()

        # log dosyalari olusturma
        self.logging()

        QCoreApplication.instance().quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
