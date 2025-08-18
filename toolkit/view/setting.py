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

        # 界面设置
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        # 缩放界面
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setObjectName('scroll_widget')
        self.setWidget(self.scroll_widget)

        # 窗口标题
        self.setting_label = QtWidgets.QLabel(self.tr("Settings"), self)
        self.setting_label.setObjectName('setting_label')

        # 个性化分组
        self.personal_group = SettingCardGroup(
            self.tr("Personalization"), self.scroll_widget
        )

        # 主题卡
        self.theme_card = OptionsSettingCard(
            cfg.themeMode,
            FluentIcon.BRUSH,
            self.tr("Application theme"),
            self.tr("Change the appearance of your application"),
            texts=[
                self.tr("Light"),
                self.tr("Dark"),
            ],
            parent=self.personal_group,
        )

        # 主题颜色卡
        self.theme_color_card = CustomColorSettingCard(
            cfg.themeColor,
            FluentIcon.PALETTE,
            self.tr("Theme color"),
            self.tr("Change the theme color of you application"),
            self.personal_group,
        )

        # 语言卡
        self.language_card = ComboBoxSettingCard(
            cfg.language,
            FluentIcon.LANGUAGE,
            self.tr("Language"),
            self.tr("Set your preferred language for UI"),
            texts=["简体中文", "English"],
            parent=self.personal_group,
        )

        # 布局组装
        self.setting_label.move(36, 30)
        self.expandLayout = ExpandLayout(self.scroll_widget)
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.personal_group.addSettingCard(self.theme_card)
        self.personal_group.addSettingCard(self.theme_color_card)
        self.personal_group.addSettingCard(self.language_card)
        self.expandLayout.addWidget(self.personal_group)
        self.expandLayout.setSpacing(28)
        self.setViewportMargins(0, 80, 0, 20)

    def init_signal(self):
        """
        初始化信号
        """

        cfg.themeChanged.connect(setTheme)
        cfg.appRestartSig.connect(self.show_restart_tooltip)

    def show_restart_tooltip(self):
        """
        显示重启提示
        """

        InfoBar.success(
            self.tr("Updated successfully"),
            self.tr("Configuration takes effect after restart"),
            duration=1500,
            parent=self,
        )
