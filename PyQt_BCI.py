import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import *
from random import randint
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams

#과제 수행 프로그램
#화면 구성 
class WindowClass(QMainWindow):
    def __init__(self,serial_port) :
        super().__init__()
        self.setGeometry(1100, 300,1200, 800)
        self.setWindowTitle('Set Protocol')
        self.serial_port=serial_port
        self.timer = QTimer(self)
        self.time = 0
        
        #label
        self.label = QLabel("실험을 시작하려면 시작하기 버튼을 눌러주세요", self)
        font1 = self.label.font()
        font1.setBold(True)
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setGeometry(300,300,700,50)
        
        #button
        self.btn_1= QPushButton("시작하기",self)
        self.btn_1.setGeometry(550,500,100,50)
        self.btn_1.clicked.connect(self.btn_1_clicked)
           
    def btn_1_clicked(self):
        global last
        self.label.clear()
        self.btn_1.hide()
        ref = 0
        last = 0
        for i in range(4):
            randtime=[1500,2000]
            
            ref += last
            QTimer.singleShot(ref, self.point)
            QTimer.singleShot(ref+500, self.close1)
            QTimer.singleShot(ref+500, self.para1)
            QTimer.singleShot(ref+1000, self.close2)
            QTimer.singleShot(ref+1000, self.para2)
            QTimer.singleShot(ref+3500, self.close3)
            QTimer.singleShot(ref+3500,self.para3) 
            QTimer.singleShot(ref+4500,self.close4) 
            last=4500+randtime[randint(0,1)]
            QTimer.singleShot(ref+last,self.p) 
            serial_port="COM3"
            board = EEG.start_board()
            data = board.get_board_data()
            print(data)
                      
    def p(self):
        print()
       
    def point (self):
        protocol.point(self)
        
    def para1(self): 
        protocol.random(self)
        print(self.time,"e")
        
    def para2(self):   
        protocol.point1(self)
        print(self.time,"r")
      
    def para3(self):
        protocol.point_blue(self)
        
             
    def close1(self):
        label2.close()  
       
    def close2(self):
        label3.close() 
      
    def close3(self):
        label4.close()  
    def close4(self):
        label5.close()         
        
class protocol(WindowClass):
    def __init__(self) :
        super().__init__()
    
    def point(self):
        global label2
        label2 = QLabel("·",self)
        font2 = label2.font()
        font2.setBold(True)
        font2.setPointSize(200)
        label2.setFont(font2)
        label2.setGeometry(550,350,700,50)
        label2.show()
                   
    def close1():
        label2.close()
                
    def random(self):
        target=["↑","←","↓","→"] 
        global label3   
        label3=QLabel(target[randint(0,3)],self)
        font2 = label3.font()
        font2.setBold(True)
        font2.setPointSize(100)
        label3.setFont(font2)
        label3.setGeometry(550,50,400,700)
        label3.show()
        
    def close2():
        label3.close()
        
    def point1(self):
        global label4
        label4 = QLabel("·",self)
        font2 = label4.font()
        font2.setBold(True)
        font2.setPointSize(200)
        label4.setFont(font2)
        label4.setGeometry(550,350,700,50)
        label4.show()
        
    def close3():
        label4.close() 
    def point_blue(self):
        global label5
        label5 = QLabel("·",self)
        font2 = label5.font()
        label5.setStyleSheet("color: blue")
        font2.setBold(True)
        font2.setPointSize(200)
        label5.setFont(font2)
        label5.setGeometry(550,350,700,50)
        label5.show()
        
    def close4():
        label5.close()

#방향키 관련 함수수
class Pushbutton():
    def __init__(self) :
        super().__init__()
        
    def Key(self, key):
        if key == Qt.Key_Up:
            
        if key == Qt.Key_Left:
            
        if key == Qt.Key_Down:  
            
        if key == Qt.Key_Right:
                      
            
#EEG 측정 및 제어       
class EEG:
    def start_board():
        #보드를 초기화.
        serial_port = "COM3" # OpenBCI 장비 연결하여 확인을 해야 함.
        params = BrainFlowInputParams() 
        params.serial_port = serial_port 
        params.serial_number = '' 
        params.timeout = 0 
        params.other_info = '' 
        params.file = '' 
        params.mac_address = '' 
        params.ip_address = '' 
        params.ip_port = 0 
        params.ip_protocol = 0
        board = BoardShim(board_id, params) 
        board.config_board('xU060100X') #보드 설정을 한다면, 반드시 보드에 명령어를 전달해야 함.
        board.prepare_session()

if __name__ == "__main__" :
    board_id = 2
    board = EEG.start_board()
    data = board.get_board_data() #버퍼 내에 있는 데이터를 가져옴.
    print(data)
    
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()