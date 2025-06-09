from tkinter import Tk, filedialog, simpledialog, messagebox
from audio_transcrever.transcrever import (
    transcrever_audio_longos,
    salvar_transcricao_no_word
)

def selecionar_arquivo():
    """
    Abre uma janela para selecionar um arquivo de áudio.

    Returns:
        str: Caminho do arquivo de áudio selecionado.
    """
    root = Tk()
    root.withdraw()
    arquivo_audio = filedialog.askopenfilename(
        title="Selecione o arquivo de áudio",
        filetypes=[("Arquivos de áudio", "*.wav *.mp3 *.flac *.ogg *.aiff")]
    )
    return arquivo_audio

def obter_nome_arquivo():
    """
    Solicita o nome do arquivo de saída ao usuário.

    Returns:
        str: Nome do arquivo fornecido pelo usuário.
    """
    root = Tk()
    root.withdraw()
    nome_arquivo_word = simpledialog.askstring(
        "Nome do Arquivo",
        "Digite o nome do arquivo de saída (sem extensão):"
    )
    return nome_arquivo_word

def iniciar_transcricao():
    """
    Inicia o processo de transcrição do áudio selecionado e salva em um arquivo Word.
    """
    arquivo_audio = selecionar_arquivo()
    if not arquivo_audio:
        print("Arquivo de áudio não selecionado.")
        messagebox.showerror("Erro", "Nenhum arquivo de áudio selecionado.")
        return

    print(f"Arquivo de áudio selecionado: {arquivo_audio}")
    nome_arquivo_word = obter_nome_arquivo()
    if not nome_arquivo_word:
        print("Nome do arquivo de saída não fornecido.")
        messagebox.showerror("Erro", "Nome do arquivo de saída não pode ser vazio.")
        return

    if not nome_arquivo_word.endswith('.docx'):
        nome_arquivo_word += '.docx'

    print(f"Nome do arquivo de saída: {nome_arquivo_word}")
    transcricao = transcrever_audio_longos(arquivo_audio, duracao_segmento_ms=60000)
    print("Transcrição completa do áudio:")
    print(transcricao)
    salvar_transcricao_no_word(transcricao, nome_arquivo_word)
    print(f"A transcrição foi salva no arquivo: {nome_arquivo_word}")
