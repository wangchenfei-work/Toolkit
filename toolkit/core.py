import sys
from PySide6 import QtGui, QtCore, QtWidgets
from qfluentwidgets import (
    SplitFluentWindow,
    FluentIcon,
    NavigationItemPosition,
    FluentTranslator,
)
from toolkit.utils import resources
from toolkit.utils.config import cfg
from toolkit.utils.icon import Icon
from toolkit.view.home import HomeView
from toolkit.view.pdf import PDFView
from toolkit.view.setting import SettingView


class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        初始化UI
        """

        # 主页
        self.homeView = HomeView(self)
        self.addSubInterface(
            self.homeView,
            FluentIcon.HOME,
            self.tr("Home"),
            NavigationItemPosition.TOP,
        )

        # PDF
        self.pdfView = PDFView(self)
        self.addSubInterface(
            self.pdfView,
            Icon.PDF,
            self.tr("PDF"),
            NavigationItemPosition.TOP,
        )

        # 设置
        self.settingView = SettingView(self)
        self.addSubInterface(
            self.settingView,
            FluentIcon.SETTING,
            self.tr("Setting"),
            NavigationItemPosition.BOTTOM,
        )


if __name__ == "__main__":
    # 国际化
    ft_translator = FluentTranslator(cfg.get(cfg.language).value)

    app = QtWidgets.QApplication(sys.argv)
    app.installTranslator(ft_translator)
    app.setAttribute(QtCore.Qt.AA_DontCreateNativeWidgetSiblings)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
