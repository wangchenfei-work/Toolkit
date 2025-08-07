"""
Configuration of application
"""

import os
from enum import Enum
from PySide6.QtCore import QLocale
from qfluentwidgets import (
    qconfig,
    QConfig,
    OptionsConfigItem,
    OptionsValidator,
    ConfigSerializer,
)


ApplicationName = "Toolkit"
ApplicationCacheDir = os.path.join(os.environ["APPDATA"], ApplicationName)
ConfigFile = os.path.join(ApplicationCacheDir, "config.json")


class Language(Enum):
    """
    Language enumeration
    """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    ENGLISH = QLocale(QLocale.English)


class LanguageSerializer(ConfigSerializer):
    """
    Language serializer
    """

    def serialize(self, language):
        return language.value.name()

    def deserialize(self, value):
        return Language(QLocale(value))


class Config(QConfig):
    """
    Config of application
    """

    language = OptionsConfigItem(
        ApplicationName,
        "Language",
        Language.CHINESE_SIMPLIFIED,
        OptionsValidator(Language),
        LanguageSerializer(),
        restart=True,
    )


cfg = Config()
qconfig.load(ConfigFile, cfg)
