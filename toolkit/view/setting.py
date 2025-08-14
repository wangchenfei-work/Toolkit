from toolkit.utils.style_sheet import StyleSheet
from PySide6 import QtGui, QtCore, QtWidgets
from qfluentwidgets import (
    ScrollArea,
)


class SettingView(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """
        初始化UI
        """

        # 设置对象名称
        self.setObjectName("setting_view")

        # 应用QSS美化
        StyleSheet.SETTING_VIEW.apply(self)
