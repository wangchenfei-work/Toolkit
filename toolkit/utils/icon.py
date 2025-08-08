from enum import Enum
from qfluentwidgets import FluentIconBase, getIconColor, Theme


class Icon(FluentIconBase, Enum):

    PDF = "pdf"

    def path(self, theme=Theme.AUTO):
        return f":/toolkit/icons/{self.value}_{getIconColor(theme)}.svg"
