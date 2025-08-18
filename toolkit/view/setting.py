from toolkit.utils.style_sheet import StyleSheet
from PySide6 import QtGui, QtCore, QtWidgets
from qfluentwidgets import (
    ScrollArea,
    ExpandLayout,
    InfoBar,
    SettingCardGroup,
    OptionsSettingCard,
    CustomColorSettingCard,
    ComboBoxSettingCard,
    FluentIcon,
    setTheme,
)
from toolkit.utils.config import cfg


class SettingView(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.init_signal()

    def init_ui(self):
        """
        初始化UI
        """

        # 设置对象名称
        self.setObjectName("setting_view")

        # 应用QSS美化
        StyleSheet.SETTING_VIEW.apply(self)
