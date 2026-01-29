# Transcrição de Áudio com Python – Versão PyQt6
## Descrição do Projeto
Este projeto é um transcritor de áudio moderno, que permite converter arquivos de áudio em texto de forma eficiente e prática. Agora com **interface gráfica em PyQt6**, o programa oferece uma experiência mais fluida e visualmente agradável, mantendo toda a funcionalidade de transcrição e geração de documentos Word.
## Funcionalidades
- **Suporte a Vários Formatos:** Aceita arquivos de áudio nos formatos WAV, MP3, FLAC, OGG e AIFF.  
- **Divisão Inteligente de Áudio:** Longos arquivos são divididos em segmentos de 1 minuto para melhorar o desempenho do reconhecimento.  
- **Transcrição de Áudio:** Utiliza a API de reconhecimento de fala do Google para transcrever os segmentos em texto.  
- **Geração de Documentos Word:** Salva a transcrição em um arquivo Word, facilitando edição e compartilhamento.  
- **Interface Gráfica Moderna:** PyQt6 com tema futurista, barra de progresso e notificações para transcrição concluída.  
- **Threading:** O processo de transcrição roda em segundo plano, evitando que a interface trave.
## Tecnologias Utilizadas
- Python  
- [PyQt6](https://pypi.org/project/PyQt6/) – interface gráfica moderna  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – reconhecimento de fala  
- [Pydub](https://pypi.org/project/pydub/) – manipulação de áudio  
- [python-docx](https://python-docx.readthedocs.io/en/latest/) – criação de arquivos Word

## Exemplo de Uso
1. Execute o programa:  
```bash
python main.py
```
2. Na interface, clique em Selecionar Áudio e Transcrever.

3. Escolha o arquivo de áudio que deseja transcrever.

4. Escolha o local e nome do arquivo Word de saída.

5. Acompanhe a barra de progresso até a conclusão da transcrição.

6. O arquivo Word com a transcrição será salvo no local escolhido.

## Instalação

1. Crie e ative um ambiente virtual:
python -m venv venv
.\venv\Scripts\activate

2. Instale as dependências:
pip install -r requirements.txt

3. Certifique-se de que o FFmpeg esteja na pasta correta e configurado no PATH (já definido no main.py).

## Contato

- Email: romariodurck@gmail.com

- LinkedIn: https://www.linkedin.com/in/romariodurck

- Repositório no GitHub: https://github.com/Megadurck/Transcricao-Audio-Python
