# Toolkit
Toolkit

### 编译资源
```powershell
pyside6-rcc.exe .\toolkit\resources\resources.qrc -o .\toolkit\utils\resources.py
```

### 国际化
```powershell
pyside6-lupdate.exe .\toolkit\core.py .\toolkit\view\setting.py -ts .\toolkit\resources\i18n\zh_CN.ts
pyside6-lrelease.exe .\toolkit\resources\i18n\zh_CN.ts -qm .\toolkit\resources\i18n\zh_CN.qm
```
