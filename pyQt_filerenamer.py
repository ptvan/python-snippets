import sys
import os
import re

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
        self.prefixChkbox.stateChanged.connect(self.processnames)
        self.prefixEdit = QLineEdit("pre")
        self.prefixEdit.setFixedWidth(50)
        self.prefixEdit.textEdited.connect(self.processnames)

        self.suffixChkbox = QCheckBox("suffix")
        self.suffixChkbox.stateChanged.connect(self.processnames)
        self.suffixEdit = QLineEdit("suf")
        self.suffixEdit.setFixedWidth(50)
        self.suffixEdit.textEdited.connect(self.processnames)

        self.numberingChkbox = QCheckBox("numbering")
        self.numberingChkbox.stateChanged.connect(self.processnames)
        self.numberingStartEdit = QLineEdit("0")
        self.numberingStartEdit.setFixedWidth(30)
        self.numberingStepEdit = QLineEdit("1")
        self.numberingStepEdit.setFixedWidth(20)

        self.replaceChkbox = QCheckBox("replace")
        self.replaceChkbox.stateChanged.connect(self.processnames)        
        self.replaceoldEdit = QLineEdit("oldtext")
        self.replaceoldEdit.textEdited.connect(self.processnames)
        self.replaceoldEdit.setFixedWidth(190)
        self.replacenewEdit = QLineEdit("newtext")
        self.replacenewEdit.setFixedWidth(190)
        self.replacenewEdit.textEdited.connect(self.processnames)


        layout.addWidget(self.browseBtn, 0, 0, 1, 3)
        layout.addWidget(self.prefixChkbox, 1, 0, 1, 1)
        layout.addWidget(self.prefixEdit, 1, 1, 1, 1)
        layout.addWidget(self.suffixChkbox, 2, 0, 1, 1) 
        layout.addWidget(self.suffixEdit, 2, 1, 1, 1)
        layout.addWidget(self.numberingChkbox, 3, 0, 1, 1)
        layout.addWidget(self.numberingStartEdit, 3, 1, 1, 1)
        layout.addWidget(self.numberingStepEdit, 3, 2, 1, 1)
        layout.addWidget(self.replaceChkbox, 4, 0, 1, 1)
        layout.addWidget(self.replaceoldEdit, 4, 1, 1, 1)
        layout.addWidget(self.replacenewEdit, 4, 2, 1, 1) 

        self.contents = QTableWidget()
        layout.addWidget(self.contents,5,0,1,3)
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
        self.originalNames = []
        self.newNames = []

    def getfiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"Select files to rename", "","All Files (*)", options=options)
        if files:
            self.contents.setRowCount(len(files))
            self.originalNames = files
            self.newNames = files
            for i in range(len(files)):
                short = os.path.basename(files[i])
                self.contents.setItem(i,0, QTableWidgetItem(short))
            # print(files)
            self.processnames()
            

    def confirm(self):
        if self.contents.rowCount() > 0:
            reply = QMessageBox()
            reply.setWindowTitle("Confirm file rename")
            reply.setText("Rename " + str(self.contents.rowCount()) + " files ?")
            reply.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            retval = reply.exec_()
            # if retval == 65536:
            #     print("user cancelled")
            if retval == 16384:
                self.renamefiles()

    def processnames(self):
        self.newNames = self.originalNames
        self.dirName = os.path.dirname(self.originalNames[0])
        if self.prefixChkbox.isChecked(): 
            self.newNames = [self.prefixEdit.text() + os.path.basename(x) for x in self.newNames]

        if self.suffixChkbox.isChecked():
            self.newNames = [os.path.splitext(x)[0] + self.suffixEdit.text() + os.path.splitext(x)[1] for x in self.newNames ]

        if self.numberingChkbox.isChecked():
            self.newNames = [os.path.splitext(os.path.basename(self.newNames[i]))[0] + str(i + int(self.numberingStartEdit.text())) * int(self.numberingStepEdit.text()) + os.path.splitext(os.path.basename(self.newNames[i]))[1] for (i, j) in enumerate(self.originalNames)]

        if self.replaceChkbox.isChecked():
            self.newNames = [os.path.basename(x).replace(self.replaceoldEdit.text(), self.replacenewEdit.text()) for x in self.originalNames]

        for i in range(len(self.newNames)):
            short = os.path.basename(self.newNames[i])
            self.contents.setItem(i,1, QTableWidgetItem(short))

    def renamefiles(self):
        for i in range(len(self.newNames)):
            cmd = 'mv ' + self.originalNames[i] + " " + self.dirName + "/" + self.newNames[i]
            # print(cmd)
            os.system(cmd)

def main():
    app = QApplication(sys.argv)
    ex = filerenamer()
    ex.setFixedSize(620,500)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()