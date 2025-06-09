# Transcrição de Áudio com Python

## Descrição do Projeto
Este projeto é um transcritor de áudio, uma ferramenta que permite a conversão de arquivos de áudio em texto de forma eficiente e prática. Utilizando bibliotecas de reconhecimento de fala e manipulação de áudio, o programa foi projetado para transformar gravações em texto, facilitando o acesso e a análise dos conteúdos gravados.

## Funcionalidades
- **Suporte a Vários Formatos:** Aceita arquivos de áudio nos formatos WAV, MP3, FLAC, OGG e AIFF.  
- **Divisão Inteligente de Áudio:** Longos arquivos são divididos em segmentos de 1 minuto para melhorar o desempenho do reconhecimento.  
- **Transcrição de Áudio:** Utiliza a API de reconhecimento de fala do Google para transcrever os segmentos em texto.  
- **Geração de Documentos:** Salva a transcrição em um arquivo Word, facilitando a edição e o compartilhamento.  
- **Interface Amigável:** Possui uma interface gráfica para seleção do arquivo de áudio e definição do nome do arquivo de saída.

## Tecnologias Utilizadas
- Python  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – biblioteca para reconhecimento de fala  
- [Pydub](https://pypi.org/project/pydub/) – manipulação de áudio  
- [python-docx](https://python-docx.readthedocs.io/en/latest/) – criação de arquivos Word  
- Tkinter – interface gráfica

## Exemplo de Uso
1. Execute o programa.  
2. Selecione um arquivo de áudio.  
3. Defina o nome do arquivo de saída.  
4. Aguarde a transcrição ser gerada.  
5. O arquivo Word com a transcrição será salvo na pasta do projeto.

Ideal para jornalistas, estudantes, profissionais da saúde e qualquer pessoa que precise transcrever gravações de áudio para texto.

## Instalação
Para instalar as dependências, rode no terminal:
```bash
pip install -r requirements.txt 
```

## Contato

- Email: romariodurck@gmail.com  
- LinkedIn: [https://www.linkedin.com/in/romariodurck](https://www.linkedin.com/in/romariodurck)  
- Repositório do projeto no GitHub: [https://github.com/Megadurck/Transcricao-Audio-Python](https://github.com/Megadurck/Transcricao-Audio-Python)


  