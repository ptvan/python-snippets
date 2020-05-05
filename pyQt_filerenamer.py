import sys
import os
import ntpath
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTableWidgetItem, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog, QMessageBox)

class filerenamer(QWidget):
    def __init__(self, parent = None):
        super(filerenamer, self).__init__(parent)
		
        layout = QGridLayout()
        self.setLayout(layout)

        self.browseBtn = QPushButton("select files")
        self.browseBtn.clicked.connect(self.getfiles)

        self.prefixChkbox = QCheckBox("prefix")
        self.prefixEdit = QLineEdit("")
        self.prefixEdit.setFixedWidth(50)
        self.suffixChkbox = QCheckBox("suffix")
        self.suffixEdit = QLineEdit("")
        self.suffixEdit.setFixedWidth(50)
        self.replaceChkbox = QCheckBox("replace")
        self.replaceoldEdit = QLineEdit("oldtext")
        self.replaceoldEdit.setFixedWidth(190)
        self.replacenewEdit = QLineEdit("newtext")
        self.replacenewEdit.setFixedWidth(190)
        
        layout.addWidget(self.browseBtn, 0, 0, 1, 3)
        layout.addWidget(self.prefixChkbox, 1, 0, 1, 1)
        layout.addWidget(self.prefixEdit, 1, 1, 1, 1)
        layout.addWidget(self.suffixChkbox, 2, 0, 1, 1) 
        layout.addWidget(self.suffixEdit, 2, 1, 1, 1)
        layout.addWidget(self.replaceChkbox, 3, 0, 1, 1)
        layout.addWidget(self.replaceoldEdit, 3, 1, 1, 1)
        layout.addWidget(self.replacenewEdit, 3, 2, 1, 1) 

        self.contents = QTableWidget()
        layout.addWidget(self.contents,4,0,1,3)
        self.setLayout(layout)
        self.setWindowTitle("File Renamer")
        self.contents.setFixedWidth(600)
        self.contents.setColumnCount(2)
        tableHeader = ["original filename","new filename"]
        self.contents.setHorizontalHeaderLabels(tableHeader)
        self.contents.setColumnWidth(0,299)
        self.contents.setColumnWidth(1,299)

        self.renameBtn = QPushButton("rename")
        self.renameBtn.clicked.connect(self.confirm)

        layout.addWidget(self.renameBtn)

    def getfiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"Select files to rename", "","All Files (*)", options=options)
        if files:
            self.contents.setRowCount(len(files))
            for i in range(len(files)):
                item = QTableWidgetItem(ntpath.basename(files[i]))
                self.contents.setItem(i,0, item)
            print(files)

    def confirm(self):
        reply = QMessageBox()
        reply.setWindowTitle("Confirm file rename")
        reply.setText("Rename files?")
        reply.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        retval = reply.exec_()
        print("value of pressed message box button:", retval)

    def processnames(self):
        return(files)

    def renamefiles(self):
        os.system()

def main():
    app = QApplication(sys.argv)
    ex = filerenamer()
    ex.setFixedSize(620,500)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()