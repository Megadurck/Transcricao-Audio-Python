# audio_transcrever/gui.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QMessageBox, QProgressBar
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from audio_transcrever.transcrever import transcrever_audio_longos, salvar_transcricao_no_word

class TranscricaoThread(QThread):
    progresso = pyqtSignal(str)
    concluido = pyqtSignal(str)
    erro = pyqtSignal(str)

    def __init__(self, arquivo_audio, nome_arquivo_word):
        super().__init__()
        self.arquivo_audio = arquivo_audio
        self.nome_arquivo_word = nome_arquivo_word

    def run(self):
        try:
            self.progresso.emit("Iniciando transcrição...")
            transcricao = transcrever_audio_longos(self.arquivo_audio)
            self.progresso.emit("Salvando transcrição...")
            salvar_transcricao_no_word(transcricao, self.nome_arquivo_word)
            self.concluido.emit(self.nome_arquivo_word)
        except Exception as e:
            self.erro.emit(str(e))

class TranscricaoUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transcrição de Áudio")
        self.setFixedSize(500, 200)
        self.setStyleSheet("background-color: #1c1c1c; color: #00ffcc; font-family: Consolas;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_status = QLabel("Pronto para transcrever")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl_status)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        self.btn_transcrever = QPushButton("Selecionar Áudio e Transcrever")
        self.btn_transcrever.setStyleSheet(
            "QPushButton { background-color: #333333; color: #00ffcc; font-size: 14px; padding: 10px; }"
            "QPushButton:hover { background-color: #00ffcc; color: #1c1c1c; }"
        )
        self.btn_transcrever.clicked.connect(self.selecionar_e_transcrever)
        layout.addWidget(self.btn_transcrever)

        self.setLayout(layout)

    def selecionar_e_transcrever(self):
        arquivo_audio, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione o arquivo de áudio",
            "",
            "Áudio (*.wav *.mp3 *.flac *.ogg *.aiff)"
        )
        if not arquivo_audio:
            return

        nome_arquivo_word, ok = QFileDialog.getSaveFileName(
            self,
            "Salvar transcrição como",
            "transcricao.docx",
            "Documento Word (*.docx)"
        )
        if not ok or not nome_arquivo_word:
            return
        if not nome_arquivo_word.endswith(".docx"):
            nome_arquivo_word += ".docx"

        self.btn_transcrever.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.lbl_status.setText("Transcrevendo...")

        self.thread = TranscricaoThread(arquivo_audio, nome_arquivo_word)
        self.thread.progresso.connect(self.atualizar_status)
        self.thread.concluido.connect(self.finalizado)
        self.thread.erro.connect(self.mostrar_erro)
        self.thread.start()

    def atualizar_status(self, texto):
        self.lbl_status.setText(texto)

    def finalizado(self, arquivo_word):
        self.progress_bar.setVisible(False)
        self.lbl_status.setText(f"Transcrição salva: {arquivo_word}")
        self.btn_transcrever.setEnabled(True)
        QMessageBox.information(self, "Sucesso", f"A transcrição foi salva em:\n{arquivo_word}")

    def mostrar_erro(self, mensagem):
        self.progress_bar.setVisible(False)
        self.lbl_status.setText("Erro durante a transcrição")
        self.btn_transcrever.setEnabled(True)
        QMessageBox.critical(self, "Erro", f"Falha ao transcrever o áudio:\n{mensagem}")
