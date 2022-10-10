# kullanisli araclar
import threading
import math
import sys
import os
sys.path.append('./src')
sys.path.append('./inc')
# kullanici arayuzu
from fileinput import filename
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, pyqtSignal, QObject, QCoreApplication, QTimer, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from ui_drone import Ui_MainWindow
# drone
from dronekit import connect, VehicleMode
from ucus_komutlari import aero
# veriler
import pandas as pd

connection_string="127.0.0.1:14550"
vehicle = connect(connection_string,wait_ready=True,timeout=100)
ui = Ui_MainWindow()

veriDict = {'yatay hiz':[],'dikey hiz':[], 'pil seviyesi':[], 'cekilen akim':[], 'voltaj':[] , 'zaman':[]}
time = 0

class Attributes(QObject):
    # Sinyaller
    bataryaGonder = pyqtSignal(list)
    hizGonder = pyqtSignal(list)
    modGonder = pyqtSignal(list)
    # haritaGonder = pyqtSignal(list)


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

# def haritaGuncelle(value):
#     vehicleLon = value[0]
#     vehicleLat = value[1]

# Sinyaller
attr = Attributes()
attr.bataryaGonder.connect(bataryaGuncelle)
attr.hizGonder.connect(hizGuncelle)
attr.modGonder.connect(modGuncelle)
# attr.haritaGonder.connect(haritaGuncelle)

# Window
class MainWindow:
    def __init__(self):
        self.drone = aero(vehicle)
        self.main_win = QMainWindow()
        ui.setupUi(self.main_win)

        self.main_win.m_flag = False
        self.droneThreadFlag = False
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

        self.initMap()
        self.main_win.closeEvent = self.exit

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
    
    # @vehicle.on_attribute('location.global_frame')
    # def haritaGuncelle(self, attr_name, value):
    #     if (vehicleLat != value.lat or vehicleLon != value.lon):
    #         attr.haritaGonder.emit([value.lat, value.lon])

    ############################################################################################################
    ######################################             HARITA             ######################################
    ############################################################################################################

    def initMap(self):
        global vehicleLon
        global vehicleLat

        vehicleLon = vehicle.location.global_frame.lon
        vehicleLat = vehicle.location.global_frame.lat
    
        webView = ui.mapArea
        with open('index.html', 'r') as f:
            html = f.read()
            webView.setHtml(html)


    ############################################################################################################
    ######################################            BUTONLAR            ######################################
    ############################################################################################################

    ## SCRIPTS ##

    def scriptThread(self, target):
        if self.droneThreadFlag is False:
            self.droneThreadFlag = True
            target()
            self.droneThreadFlag = False

    def armTest(self):
        threading.Thread(target=self.scriptThread, args=(self.drone.test, )).start()

    def otonomKalkisInis(self):
        threading.Thread(target=self.scriptThread, args=(self.drone.otonom_kalkis_inis, )).start()

    def acilInis(self):
        self.droneThreadFlag = True
        self.drone.acil_inis()
        self.droneThreadFlag = False

    def yuksel(self):
        threading.Thread(target=self.scriptThread, args=(self.drone.otonom_yuksel, )).start()

    ## MODES ##

    def stabilizeMode(self):
        self.drone.vehicle.mode = VehicleMode('STABILIZE')

    def loiterMode(self):
        self.drone.vehicle.mode = VehicleMode('LOITER')

    def guidedMode(self):
        self.drone.vehicle.mode = VehicleMode('GUIDED')

    def landMode(self):
        self.drone.vehicle.mode = VehicleMode('LAND')

    def posHoldMode(self):
        self.drone.vehicle.mode = VehicleMode('POSHOLD')
    
    ############################################################################################################
    ######################################          LOG DOSYALARI         ######################################
    ############################################################################################################

    def exit(self, event=None):
        self.closing = True
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
        QCoreApplication.instance().quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
