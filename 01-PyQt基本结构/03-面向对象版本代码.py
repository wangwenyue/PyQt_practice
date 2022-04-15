import sys

from PyQt5.Qt import *


class Window(QWidget):
    """自定义的窗口类，继承自QWidget"""

    def __init__(self):
        super().__init__()  # 进行父类的初始化
        self.setWindowTitle("小试牛刀一哈")
        self.resize(500, 600)
        self.move(1500, 250) # 窗口相对于屏幕左上角的位移

    def setup_ui(self):
        label = QLabel(self)
        label.setText("我可没有刮胡子的闲工夫")
        label.move(100, 240)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()  # 实例化一个Window对象
    window.setup_ui()  # 调用setup_ui方法，设置窗口内所有的子控件
    window.show()  # 把window显示出来

    sys.exit(app.exec_())
