from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from core.downloader import YouTubeDownloader

class YouTubeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 500, 300)
        self.downloader = YouTubeDownloader()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.url_label = QLabel("Enter YouTube URL:")
        layout.addWidget(self.url_label)
        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)
        self.quality_label = QLabel("Select Quality:")
        layout.addWidget(self.quality_label)
        self.quality_selector = QComboBox()
        self.quality_selector.addItems(["Audio Only (MP3)", "360p", "720p", "1080p"])
        layout.addWidget(self.quality_selector)
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_download(self):
        url = self.url_input.text()
        quality = self.quality_selector.currentText()
        message = self.downloader.download(url, quality)
        self.status_label.setText(message)
