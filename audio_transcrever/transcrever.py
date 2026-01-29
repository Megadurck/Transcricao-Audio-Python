# audio_transcrever/transcrever.py
import os
import tempfile
import speech_recognition as sr
from docx import Document
from pydub import AudioSegment

# Configura FFmpeg e FFprobe
AudioSegment.converter = r"E:\Conteudo ADS\programa python\Programa de Transcrever\ffmpeg-8.0.1\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"E:\Conteudo ADS\programa python\Programa de Transcrever\ffmpeg-8.0.1\bin\ffprobe.exe"

print("[INFO] FFmpeg configurado com sucesso!")

def dividir_audio(arquivo_audio, duracao_segmento_ms):
    audio = AudioSegment.from_file(arquivo_audio)
    segmentos = []

    temp_dir = tempfile.TemporaryDirectory()
    for i in range(0, len(audio), duracao_segmento_ms):
        segmento = audio[i:i + duracao_segmento_ms]
        segmento_filename = os.path.join(temp_dir.name, f"segmento_{i // duracao_segmento_ms}.wav")
        segmento.export(segmento_filename, format="wav")
        segmentos.append(segmento_filename)

    return segmentos, temp_dir

def transcrever_audio_segmento(arquivo_segmento):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(arquivo_segmento) as source:
            audio_data = recognizer.record(source)
        texto = recognizer.recognize_google(audio_data, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio."
    except sr.RequestError as e:
        return f"Erro na solicitação ao serviço de reconhecimento: {e}"
    except Exception as e:
        return f"Erro inesperado na transcrição do segmento: {e}"

def transcrever_audio_longos(arquivo_audio, duracao_segmento_ms=60000):
    try:
        segmentos, temp_dir = dividir_audio(arquivo_audio, duracao_segmento_ms)
        transcricao_completa = ""

        for segmento in segmentos:
            transcricao = transcrever_audio_segmento(segmento)
            transcricao_completa += transcricao + "\n"

        temp_dir.cleanup()
        return transcricao_completa
    except Exception as e:
        raise RuntimeError(f"Erro ao transcrever o áudio: {e}")

def salvar_transcricao_no_word(transcricao, nome_arquivo_word):
    try:
        doc = Document()
        doc.add_paragraph(transcricao)
        doc.save(nome_arquivo_word)
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar o arquivo Word: {e}")
