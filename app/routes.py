from . import app, render_template,  request, jsonify, send_file
from .bot import process_video_and_summarize
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recept-files', methods=['POST'])
def receptData():
    link = request.form.get('link')  
    text = request.form.get('text')

    if link:
        try:
            summary = process_video_and_summarize(video_url=link, summary_style=text)
            return jsonify({'message': 'Vídeo processado com sucesso!', 'response': summary})
        except Exception as e:
            return jsonify({'message': f'Ocorreu um erro ao processar o vídeo: {str(e)}'}), 500
    
    return jsonify({'message': 'Nenhum link de vídeo fornecido.'}), 400
