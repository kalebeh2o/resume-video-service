import yt_dlp
import speech_recognition as sr
import requests
from pydub import AudioSegment
import os
from groq import Groq

def download_audio(video_url, output_path="audio.mp3"):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_title = info.get('title', 'Título desconhecido')
        return output_path, video_title
    except Exception as e:
        return None, f"Erro ao baixar o áudio: {e}"

def transcribe_audio(audio_path):
    try:
        audio = AudioSegment.from_file(audio_path)
        wav_dir = "audio_segments"
        os.makedirs(wav_dir, exist_ok=True)
        
        segment_duration = 60 * 1000  
        segments = len(audio) // segment_duration + (1 if len(audio) % segment_duration != 0 else 0)
        recognizer = sr.Recognizer()
        transcription = []

        for i in range(segments):
            start = i * segment_duration
            end = min((i + 1) * segment_duration, len(audio))
            segment_path = os.path.join(wav_dir, f"segment_{i + 1}.wav")

            audio[start:end].export(segment_path, format="wav")
            
            with sr.AudioFile(segment_path) as source:
                audio_data = recognizer.record(source)
                try:
                    segment_text = recognizer.recognize_google(audio_data, language="pt-BR")
                    transcription.append(segment_text)
                except sr.UnknownValueError:
                    transcription.append("[Inaudível]")
                except sr.RequestError as e:
                    transcription.append(f"[Erro na transcrição: {e}]")
            
            os.remove(segment_path)
        
        os.rmdir(wav_dir)
        
        return " ".join(transcription)
    except Exception as e:
        return f"Erro ao transcrever áudio: {e}"

def summarize_text(text, prompt):
    try:
        client = Groq(api_key="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")
        context = "O texto a seguir é a transcrição de um vídeo do YouTube que possui introdução, desenvolvimento e conclusão. A introdução geralmente inclui saudações e apresentações do criador do conteúdo, e a conclusão pode conter despedidas ou mensagens finais. Seu objetivo é trabalhar o texto ignorando partes irrelevantes, como propagandas ou cumprimentos iniciais, e focar no conteúdo principal."
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": f"{context} \n\n prompt: {prompt} \n\n textos: {text}"}],
            model="llama3-8b-8192"
        )
        summary_content = response.choices[0].message.content
        return summary_content
    except Exception as e:
        return f"Erro ao gerar resumo: {e}"

def process_video_and_summarize(video_url, summary_style="Transforme esse texto em um texto para estudo"):
    if not video_url:
        return {"message": "Erro: Nenhum URL de vídeo fornecido."}

    audio_path, video_title = download_audio(video_url)
    if not audio_path:
        return {"message": video_title}

    transcription = transcribe_audio(audio_path)
    if transcription.startswith("Erro"):
        return {"message": transcription, "video_title": video_title}

    summary = summarize_text(transcription, prompt=summary_style)
    if summary.startswith("Erro"):
        return {"message": summary, "video_title": video_title}

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return {
        "message": "Vídeo processado com sucesso!",
        "video_title": video_title,
        "summary": summary
    }
