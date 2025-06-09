import os
import speech_recognition as sr
from pydub import AudioSegment
from docx import Document

def dividir_audio(arquivo_audio, duracao_segmento_ms):
    """
    Divide um arquivo de áudio em segmentos de duração especificada.

    Args:
        arquivo_audio (str): Caminho do arquivo de áudio a ser dividido.
        duracao_segmento_ms (int): Duração de cada segmento em milissegundos.

    Returns:
        list: Lista de caminhos dos arquivos de segmento gerados.
    """
    audio = AudioSegment.from_file(arquivo_audio)
    segmentos = []
    for i in range(0, len(audio), duracao_segmento_ms):
        segmento = audio[i:i + duracao_segmento_ms]
        segmento_filename = f"segmento_{i // duracao_segmento_ms}.wav"
        segmento.export(segmento_filename, format="wav")
        segmentos.append(segmento_filename)
    return segmentos

def transcrever_audio_segmento(arquivo_segmento):
    """
    Transcreve um segmento de áudio usando a API do Google.

    Args:
        arquivo_segmento (str): Caminho do arquivo de áudio a ser transcrito.

    Returns:
        str: Texto transcrito ou mensagem de erro.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(arquivo_segmento) as source:
        audio_data = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio_data, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio."
    except sr.RequestError as e:
        return f"Erro na solicitação ao serviço de reconhecimento: {e}"

def transcrever_audio_longos(arquivo_audio, duracao_segmento_ms=60000):
    """
    Transcreve um arquivo de áudio longo dividindo-o em segmentos menores.

    Args:
        arquivo_audio (str): Caminho do arquivo de áudio.
        duracao_segmento_ms (int): Duração de cada segmento (padrão: 60s).

    Returns:
        str: Transcrição completa.
    """
    segmentos = dividir_audio(arquivo_audio, duracao_segmento_ms)
    transcricao_completa = ""

    for segmento in segmentos:
        transcricao = transcrever_audio_segmento(segmento)
        transcricao_completa += transcricao + "\n"
        print(f"[INFO] Segmento {segmento} transcrito.")
        try:
            os.remove(segmento)
        except OSError as e:
            print(f"[ERRO] Falha ao remover {segmento}: {e}")
    return transcricao_completa

def salvar_transcricao_no_word(transcricao, nome_arquivo_word):
    """
    Salva a transcrição em um arquivo .docx.

    Args:
        transcricao (str): Texto transcrito.
        nome_arquivo_word (str): Nome do arquivo final.
    """
    doc = Document()
    doc.add_paragraph(transcricao)
    doc.save(nome_arquivo_word)
    print(f"[OK] Transcrição salva em: {nome_arquivo_word}")
