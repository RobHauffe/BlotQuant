import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from BlotQuant import BlotQuant

def setup_taskbar_icon():
    if os.name == 'nt':
        try:
            import ctypes
            myappid = 'hauffe.blotquant.1.0'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass

if __name__ == "__main__":
    setup_taskbar_icon()
    app = QApplication(sys.argv)
    
    # Set application-wide icon
    icon_path = "Blot.ico"
    if hasattr(sys, '_MEIPASS'):
        icon_path = os.path.join(sys._MEIPASS, "Blot.ico")
    
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    window = BlotQuant()
    window.show()
    sys.exit(app.exec())
