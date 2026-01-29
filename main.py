# main.py
import os
import sys

# Adiciona a pasta bin do ffmpeg à variável PATH
ffmpeg_bin = r"E:\Conteudo ADS\programa python\Programa de Transcrever\ffmpeg-8.0.1\bin"
os.environ["PATH"] = ffmpeg_bin + os.pathsep + os.environ["PATH"]

# Importa a UI PyQt6
from audio_transcrever.gui import TranscricaoUI
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = TranscricaoUI()
    window.show()
    sys.exit(app.exec())
