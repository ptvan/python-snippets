import sys
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog)


class filerenamer(QWidget):
    def __init__(self, parent = None):
        super(filerenamer, self).__init__(parent)
		
        layout = QVBoxLayout()
        self.le = QLabel("Input files")
        self.btn = QPushButton("select")
        self.btn.clicked.connect(self.getfiles)

        layout.addWidget(self.le)
    
        layout.addWidget(self.btn)

        self.contents = QTableWidget()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Renamer")
        self.contents.setFixedWidth(480)
        self.contents.setColumnCount(2)
        tableHeader = ["original filename","new filename"]
        self.contents.setHorizontalHeaderLabels(tableHeader)
        self.contents.setColumnWidth(0,239)
        self.contents.setColumnWidth(1,239)

    def getfiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"Select files to rename", "","All Files (*)", options=options)
        if files:
            self.contents.setRowCount(len(files))
            print(files)

def main():
    app = QApplication(sys.argv)
    ex = filerenamer()
    ex.setFixedSize(500,500)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()