import sip
import sys
import m4a2aac
sip.setapi('QString',2)
from PyQt4 import QtCore,QtGui

class Dialog(QtGui.QDialog):
    MESSAGE = "test get open file name"
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        frameStyle = QtGui.QFrame.Sunken|QtGui.QFrame.Panel
        self.fileName = ''
        self.openFileNameLabel = QtGui.QLabel()
        self.openFileNameLabel.setFrameStyle(frameStyle)
        self.openFileNameButton = QtGui.QPushButton("Browse")
        self.openFileNameButton.clicked.connect(self.setOpenFileName)
        self.ConvertButton = QtGui.QPushButton("convert")
        self.ConvertButton.clicked.connect(self.m4a2aacconvert)

        layout = QtGui.QGridLayout()
        layout.setColumnStretch(1,1)
        layout.setColumnMinimumWidth(1,250)
        layout.addWidget(self.openFileNameButton,0,0)
        layout.addWidget(self.openFileNameLabel,0,1)
        layout.addWidget(self.ConvertButton,0,2)
        self.setLayout(layout)
        self.setWindowTitle("m4a2aac convert tool")
        
    def setOpenFileName(self):    
        options = QtGui.QFileDialog.Options()
        self.fileName = QtGui.QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileName()",
                self.openFileNameLabel.text(),
                "All Files (*);;Text Files (*.txt)", options)
        if self.fileName:
            self.openFileNameLabel.setText(self.fileName)
            print self.fileName
    def m4a2aacconvert(self):
        if(len(self.fileName) == 0):
            print 'invliad file path'
            return
        else:
            print 'converting...'
            m4a2aac.m4a2aac_main(self.fileName)
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())






