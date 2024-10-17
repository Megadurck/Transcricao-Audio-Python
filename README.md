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

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.


## Contato

Se você tiver perguntas ou sugestões, sinta-se à vontade para me contatar:

- **Email:** romariodurck@gmail.com
- **LinkedIn:** [(https://www.linkedin.com/in/seu-linkedin](https://www.linkedin.com/in/romario-rezende/)
