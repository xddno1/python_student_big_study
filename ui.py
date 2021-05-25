import sys
from PyQt5.QtWidgets import (QWidget, QTextEdit, QFileDialog, QApplication, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
import main


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("选择文件")
        self.textEdit = QTextEdit()
        okButton.clicked.connect(self.showDialog)
        vvbox = QVBoxLayout()
        vvbox.addWidget(okButton)
        vvbox.addStretch(1)
        hbox = QHBoxLayout()
        hbox.addLayout(vvbox)
        hbox.addWidget(self.textEdit)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle("青年大学习获取未学习名单")
        self.setWindowIcon(QIcon("head.ico"))
        self.show()

    def showDialog(self):
        # 弹出文件选择器
        fname = QFileDialog.getOpenFileName(self, "Open file")
        # 如果选择了文件
        if fname[0]:
            # 打开第一个文件
            f = open(fname[0], "r")
            mylist = main.getnostudytxt(f.name)
            for i in mylist:
                self.textEdit.append(i['name']+'  '+i['no'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
