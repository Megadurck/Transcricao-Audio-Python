<<<<<<< HEAD
Skip to content
Navigation Menu
Megadurck
Transcricao-Audio-Python

Type / to search
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Settings
Owner avatar
Transcricao-Audio-Python
Public
Megadurck/Transcricao-Audio-Python
Go to file
t
Name		
Megadurck
Megadurck
Create jekyll-docker.yml
32f7cd8
 · 
8 months ago
.github/workflows
Create jekyll-docker.yml
8 months ago
ffmpeg-7.1-essentials_build
Audio Transcrever
8 months ago
LICENSE
LICENSE
8 months ago
README.md
Update README.md
8 months ago
Transcrever Audio.ipynb
Audio Transcrever
8 months ago
ffmpeg-7.1-essentials_build.zip
Audio Transcrever
8 months ago
teste 2.docx
Audio Transcrever
8 months ago
Repository files navigation
README
License
Transcrição de Audio com Python
Descrição do Projeto
Este projeto é um Transcritor de Áudio, uma ferramenta que permite a conversão de arquivos de áudio em texto de forma eficiente e prática. Utilizando bibliotecas de reconhecimento de fala e manipulação de áudio, o programa foi projetado para atender à necessidade de transformar gravações em texto, facilitando o acesso e a análise de conteúdos gravados.

Funcionalidades
Suporte a Vários Formatos: Aceita arquivos de áudio nos formatos WAV, MP3, FLAC, OGG e AIFF.
Divisão Inteligente de Áudio: Longos arquivos de áudio são divididos em segmentos de 1 minuto, o que melhora o desempenho do reconhecimento de fala.
Transcrição de Áudio: Utiliza a API de reconhecimento de fala do Google para transcrever os segmentos de áudio em texto.
Geração de Documentos: Salva a transcrição em um arquivo Word, tornando fácil a edição e o compartilhamento do texto transcrito.
Interface Amigável: Inclui uma interface gráfica que facilita a seleção de arquivos de áudio e o nome do arquivo de saída.
Tecnologias Utilizadas
Python: A linguagem de programação utilizada para o desenvolvimento do projeto.
SpeechRecognition: Biblioteca para reconhecimento de fala.
Pydub: Biblioteca para manipulação de arquivos de áudio.
python-docx: Biblioteca para criar e manipular arquivos Word.
Tkinter: Biblioteca para criar a interface gráfica do usuário.
Exemplo de Uso
Execute o programa e selecione um arquivo de áudio.
Defina o nome do arquivo de saída para a transcrição.
Aguarde a transcrição dos segmentos de áudio.
O arquivo Word com a transcrição será salvo na mesma pasta do projeto.
Este projeto é ideal para jornalistas, estudantes, profissionais de saúde e qualquer pessoa que necessite transcrever gravações de áudio para texto, aumentando a acessibilidade e a usabilidade dos conteúdos gravados.

Instalação
Para instalar as dependências necessárias, você pode usar o pip. Execute o seguinte comando no terminal:

pip install -r requirements.txt
Uso
Após a instalação, você pode executar o programa com o seguinte comando:

python seu_script.py
Aqui está um exemplo de como executar o programa:

Abra o terminal.
Navegue até a pasta do projeto.
Execute o programa e selecione um arquivo de áudio.
A transcrição será gerada e salva em um arquivo Word.
Reconhecimentos
SpeechRecognition para reconhecimento de fala.
Pydub para manipulação de áudio.
python-docx para criação de arquivos Word.
Contribuição
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

Contato
Se você tiver perguntas ou sugestões, sinta-se à vontade para me contatar:

Email: romariodurck@gmail.com
LinkedIn: (https://www.linkedin.com/in/seu-linkedin
About
No description, website, or topics provided.
Resources
 Readme
License
 View license
 Activity
Stars
 1 star
Watchers
 1 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
HTML
99.9%
 
Other
0.1%
Footer
© 2025 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
=======
# Transcrição de Audio com Python

## Descrição do Projeto

Este projeto é um **Transcritor de Áudio**, uma ferramenta que permite a conversão de arquivos de áudio em texto de forma eficiente e prática. Utilizando bibliotecas de reconhecimento de fala e manipulação de áudio, o programa foi projetado para atender à necessidade de transformar gravações em texto, facilitando o acesso e a análise de conteúdos gravados.

### Funcionalidades

- **Suporte a Vários Formatos:** Aceita arquivos de áudio nos formatos WAV, MP3, FLAC, OGG e AIFF.
- **Divisão Inteligente de Áudio:** Longos arquivos de áudio são divididos em segmentos de 1 minuto, o que melhora o desempenho do reconhecimento de fala.
- **Transcrição de Áudio:** Utiliza a API de reconhecimento de fala do Google para transcrever os segmentos de áudio em texto.
- **Geração de Documentos:** Salva a transcrição em um arquivo Word, tornando fácil a edição e o compartilhamento do texto transcrito.
- **Interface Amigável:** Inclui uma interface gráfica que facilita a seleção de arquivos de áudio e o nome do arquivo de saída.

### Tecnologias Utilizadas

- **Python:** A linguagem de programação utilizada para o desenvolvimento do projeto.
- **SpeechRecognition:** Biblioteca para reconhecimento de fala.
- **Pydub:** Biblioteca para manipulação de arquivos de áudio.
- **python-docx:** Biblioteca para criar e manipular arquivos Word.
- **Tkinter:** Biblioteca para criar a interface gráfica do usuário.

### Exemplo de Uso

1. Execute o programa e selecione um arquivo de áudio.
2. Defina o nome do arquivo de saída para a transcrição.
3. Aguarde a transcrição dos segmentos de áudio.
4. O arquivo Word com a transcrição será salvo na mesma pasta do projeto.

Este projeto é ideal para jornalistas, estudantes, profissionais de saúde e qualquer pessoa que necessite transcrever gravações de áudio para texto, aumentando a acessibilidade e a usabilidade dos conteúdos gravados.

## Instalação
Para instalar as dependências necessárias, você pode usar o `pip`. Execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```
## Uso

Após a instalação, você pode executar o programa com o seguinte comando:

```bash
python seu_script.py
```
Aqui está um exemplo de como executar o programa:

1. Abra o terminal.
2. Navegue até a pasta do projeto.
3. Execute o programa e selecione um arquivo de áudio.
4. A transcrição será gerada e salva em um arquivo Word.

## Reconhecimentos

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) para reconhecimento de fala.
- [Pydub](https://github.com/jiaaro/pydub) para manipulação de áudio.
- [python-docx](https://python-docx.readthedocs.io/en/latest/) para criação de arquivos Word.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se você tiver perguntas ou sugestões, sinta-se à vontade para me contatar:

- **Email:** romariodurck@gmail.com
- **LinkedIn:** [(https://www.linkedin.com/in/seu-linkedin](https://www.linkedin.com/in/romario-rezende/)
>>>>>>> 32f7cd843f2764546cec094c50ad7a7c1bc95531
