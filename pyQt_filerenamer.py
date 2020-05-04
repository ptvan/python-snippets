import sys
import ntpath
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTableWidgetItem, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog)


class filerenamer(QWidget):
    def __init__(self, parent = None):
        super(filerenamer, self).__init__(parent)
		
        layout = QVBoxLayout()
        self.inputLbl = QLabel("Input files")
        self.browseBtn = QPushButton("select")
        self.browseBtn.clicked.connect(self.getfiles)
        self.prefixChkbox = QCheckBox("prefix")
        self.suffixChkbox = QCheckBox("suffix")
        self.replaceChkbox = QCheckBox("replace")
        self.replaceEditold = QLineEdit("oldtext")
        self.replaceEditnew = QLineEdit("newtext")
        
        self.replaceEditold.setFixedWidth(100)
        self.replaceEditnew.setFixedWidth(100)

             
        layout.addWidget(self.inputLbl)
        layout.addWidget(self.browseBtn)
        layout.addWidget(self.prefixChkbox)
        layout.addWidget(self.suffixChkbox) 
        layout.addWidget(self.replaceChkbox)
        layout.addWidget(self.replaceEditold)
        layout.addWidget(self.replaceEditnew) 

        self.contents = QTableWidget()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Renamer")
        self.contents.setFixedWidth(600)
        self.contents.setColumnCount(2)
        tableHeader = ["original filename","new filename"]
        self.contents.setHorizontalHeaderLabels(tableHeader)
        self.contents.setColumnWidth(0,299)
        self.contents.setColumnWidth(1,299)

        self.renameBtn = QPushButton("rename")

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

def main():
    app = QApplication(sys.argv)
    ex = filerenamer()
    ex.setFixedSize(620,500)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()