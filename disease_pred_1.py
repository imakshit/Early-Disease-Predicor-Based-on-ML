#   HEART ATTACK PREDICTION SYSTEM

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from datetime import datetime as dt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
       # self.frame.setStyleSheet("background-color:black;")
       
       ##################################################################
       
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(135, 153, 250, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit2.setGeometry(QtCore.QRect(135, 183, 250, 21))
        self.textEdit2.setObjectName("textEdit2")
        self.textEdit2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit3.setGeometry(QtCore.QRect(135, 213, 250, 21))
        self.textEdit3.setObjectName("textEdit3")
        self.textEdit3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit4.setGeometry(QtCore.QRect(135, 243, 250, 21))
        self.textEdit4.setObjectName("textEdit4")
        self.textEdit4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit5.setGeometry(QtCore.QRect(135, 273, 250, 21))
        self.textEdit5.setObjectName("textEdit5")
        self.textEdit5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit6 = QtWidgets.QTextEdit(self.frame)
        self.textEdit6.setGeometry(QtCore.QRect(135, 303, 250, 21))
        self.textEdit6.setObjectName("textEdit6")
        self.textEdit6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit7 = QtWidgets.QTextEdit(self.frame)
        self.textEdit7.setGeometry(QtCore.QRect(135, 333, 250, 21))
        self.textEdit7.setObjectName("textEdit7")
        self.textEdit7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit8 = QtWidgets.QTextEdit(self.frame)
        self.textEdit8.setGeometry(QtCore.QRect(135, 363, 250, 21))
        self.textEdit8.setObjectName("textEdit8")
        self.textEdit8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit9 = QtWidgets.QTextEdit(self.frame)
        self.textEdit9.setGeometry(QtCore.QRect(135, 393, 250, 21))
        self.textEdit9.setObjectName("textEdit9")
        self.textEdit9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit10 = QtWidgets.QTextEdit(self.frame)
        self.textEdit10.setGeometry(QtCore.QRect(135, 423, 250, 21))
        self.textEdit10.setObjectName("textEdit10")
        self.textEdit10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit11 = QtWidgets.QTextEdit(self.frame)
        self.textEdit11.setGeometry(QtCore.QRect(135, 453, 250, 21))
        self.textEdit11.setObjectName("textEdit11")
        self.textEdit11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit12 = QtWidgets.QTextEdit(self.frame)
        self.textEdit12.setGeometry(QtCore.QRect(135, 483, 250, 21))
        self.textEdit12.setObjectName("textEdit12")
        self.textEdit12.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        self.textEdit13 = QtWidgets.QTextEdit(self.frame)
        self.textEdit13.setGeometry(QtCore.QRect(135, 513, 250, 21))
        self.textEdit13.setObjectName("textEdit13")
        self.textEdit13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        
        
        self.textEdit15 = QtWidgets.QTextEdit(self.frame)
        self.textEdit15.setGeometry(QtCore.QRect(430, 250, 250, 70))
        self.textEdit15.setObjectName("textEdit15")
        self.textEdit15.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        
        ########################################################################
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(85, 150, 250, 21))
        self.label.setObjectName("label1")
        self.label.setText("Age: ")
        
        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(85, 180, 250, 21))
        self.label2.setObjectName("label2")
        self.label2.setText("Sex: ")
        
        self.label3 = QtWidgets.QLabel(self.frame)
        self.label3.setGeometry(QtCore.QRect(85, 210, 250, 21))
        self.label3.setObjectName("label3")
        self.label3.setText("CP: ")
        
        self.label4 = QtWidgets.QLabel(self.frame)
        self.label4.setGeometry(QtCore.QRect(85, 240, 250, 21))
        self.label4.setObjectName("label4")
        self.label4.setText("Trestbps: ")
        
        self.label5 = QtWidgets.QLabel(self.frame)
        self.label5.setGeometry(QtCore.QRect(85, 270, 250, 21))
        self.label5.setObjectName("label5")
        self.label5.setText("chol: ")
        
        self.label6 = QtWidgets.QLabel(self.frame)
        self.label6.setGeometry(QtCore.QRect(85, 300, 250, 21))
        self.label6.setObjectName("label6")
        self.label6.setText("Fbs: ")
        
        self.label7 = QtWidgets.QLabel(self.frame)
        self.label7.setGeometry(QtCore.QRect(85, 330, 250, 21))
        self.label7.setObjectName("label7")
        self.label7.setText("Restecg: ")
        
        self.label8 = QtWidgets.QLabel(self.frame)
        self.label8.setGeometry(QtCore.QRect(85, 360, 250, 21))
        self.label8.setObjectName("label8")
        self.label8.setText("Thalach: ")
        
        self.label9 = QtWidgets.QLabel(self.frame)
        self.label9.setGeometry(QtCore.QRect(85, 390, 250, 21))
        self.label9.setObjectName("label9")
        self.label9.setText("Exang: ")
        
        self.label10 = QtWidgets.QLabel(self.frame)
        self.label10.setGeometry(QtCore.QRect(85, 420, 250, 21))
        self.label10.setObjectName("label10")
        self.label10.setText("Oldpeak: ")
        
        self.label11 = QtWidgets.QLabel(self.frame)
        self.label11.setGeometry(QtCore.QRect(85, 450, 250, 21))
        self.label11.setObjectName("label11")
        self.label11.setText("Slope: ")
        
        self.label12 = QtWidgets.QLabel(self.frame)
        self.label12.setGeometry(QtCore.QRect(85, 480, 250, 21))
        self.label12.setObjectName("label12")
        self.label12.setText("Ca: ")
        
        self.label13 = QtWidgets.QLabel(self.frame)
        self.label13.setGeometry(QtCore.QRect(85, 510, 250, 21))
        self.label13.setObjectName("label13")
        self.label13.setText("Thal: ")
        
       
        
        ##########################################################################
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(430, 350, 241, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n" "background-color:white;")
        
        #############################################################################
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
      

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Age: "))
        self.pushButton.setText(_translate("MainWindow", "Get Result!"))
        self.menuMenu.setTitle(_translate("MainWindow", "menu"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        
        self.pushButton.clicked.connect(self.block_func)
        self.actionExit.triggered.connect(self.exit)
        
    def block_func(self):
        import numpy as np
        import pandas as pd
        
        #####input#######
        
        val1 = self.textEdit.toPlainText();
        val2 = self.textEdit2.toPlainText();
        val3 = self.textEdit3.toPlainText();
        val4 = self.textEdit4.toPlainText();
        val5 = self.textEdit5.toPlainText();
        val6 = self.textEdit6.toPlainText();
        val7 = self.textEdit7.toPlainText();
        val8 = self.textEdit8.toPlainText();
        val9 = self.textEdit9.toPlainText();
        val10 = self.textEdit10.toPlainText();
        val11 = self.textEdit11.toPlainText();
        val12 = self.textEdit12.toPlainText();
        val13 = self.textEdit13.toPlainText();
  
        
        ################
        
        # import warnings filter
        from warnings import simplefilter
        # ignore all future warnings
        simplefilter(action='ignore', category = FutureWarning)
        # import warnings filter
        from warnings import simplefilter
        # ignore all future warnings
        simplefilter(action='ignore', category = FutureWarning)
        
        
        df = pd.read_csv('cleveland.csv', header = None)
        
        
        df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol',
                      'fbs', 'restecg', 'thalach', 'exang', 
                      'oldpeak', 'slope', 'ca', 'thal', 'target']
        
        
        ### 1 = male, 0 = female
        df.isnull().sum()
        
        
        df['target'] = df.target.map({0: 0, 1: 1, 2: 1, 3: 1, 4: 1})
        df['sex'] = df.sex.map({0: 'female', 1: 'male'})
        df['thal'] = df.thal.fillna(df.thal.mean())
        df['ca'] = df.ca.fillna(df.ca.mean())
        
        
        df['sex'] = df.sex.map({'female': 0, 'male': 1})
        
        #########################################   Logistic Regression  #############################################################
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
        
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)
        
        # Predicting the Test set results
        arr = [float(val1) , float(val2), float(val3), float(val4), float(val5), float(val6), float(val7), float(val8), float(val9), float(val10), float(val11), float(val12), float(val13)]
        arr = np.array(arr).reshape(1,-1)
        print(arr)
        y_pred = classifier.predict(arr)
        print(y_pred)
        ans = np.array_str(y_pred) ##np array to string
        if(ans== "[1]" or ans== "[2]" or ans== "[3]" or ans== "[4]" ):
            self.textEdit15.setText("YOU HAVE A HIGH CHANCE OF HEART ATTACK!\n Find cardiologist near you at: \n https://www.practo.com/delhi/cardiologist")
        else:
            self.textEdit15.setText("YOU HAVE LOW CHANCES OF HEART ATTACK!")
            
            #1,2,3,4 means heart attack
            #0 means no attack, chill




    
        
    def exit(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

