import sys
from PyQt6.QtWidgets import QApplication
from ui.app_ui import YouTubeApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeApp()
    window.show()
    sys.exit(app.exec())
