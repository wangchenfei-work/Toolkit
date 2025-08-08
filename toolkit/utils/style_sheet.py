from enum import Enum
from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    """
    Style sheet
    """

    HOME_VIEW = "home_view"
    PDF_VIEW = "pdf_view"
    SETTING_VIEW = "setting_view"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":/toolkit/qss/{theme.value.lower()}.qss"
