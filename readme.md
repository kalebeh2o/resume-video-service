# Video Summarization and Transcription 🎥📄

Este é um programa que pega um vídeo, realiza a transcrição do áudio presente no vídeo e utiliza IA para gerar um resumo conciso do conteúdo transcrito.

## Funcionalidades ✨

- **Transcrição de áudio**: O áudio extraído de vídeos é transcrito utilizando a biblioteca `SpeechRecognition`. 🎙️
- **Resumir conteúdo**: O conteúdo transcrito é processado e resumido usando IA, gerando um resumo conciso. 🤖
- **Download de vídeos**: O programa utiliza `yt-dlp` para fazer o download de vídeos de várias plataformas de streaming, como o YouTube. ⬇️
- **API Flask**: A aplicação é construída com o Flask, oferecendo uma API para o processo de transcrição e resumo de vídeos. ⚡

## Tecnologias Utilizadas ⚙️

- **Flask**: Framework web para criar a API. 🖥️
- **yt-dlp**: Biblioteca para baixar vídeos de plataformas como YouTube. 📹
- **SpeechRecognition**: Biblioteca para transcrição de áudio. 🗣️
- **pydub**: Biblioteca para manipulação de áudio, como corte e conversão de formatos. 🔊
- **groq**: Ferramenta de inteligência artificial para gerar resumos. 🧠

## Instalação 🚀

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/video-summarization.git

2. Navegue até o diretório do projeto:

   ```bash
   cd video-summarization

3. Crie e ative um ambiente virtual (opcional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

4. Instale as dependências:

   ```bash
    pip install -r requirements.txt

## Uso ⚡

1. Inicie a aplicação Flask:

   ```bash
   python run.py



