"""
Servidor Flask para detecção de emoções.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask('Emotion analyzer')


@app.route('/emotionDetector')
def get_emotion():
    """
    Endpoint para detectar emoções em texto.
    
    Returns:
        str: Resposta formatada com as emoções detectadas
    """
    text = request.args.get('textToAnalyze')
    print(text)

    response = emotion_detector(text)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    return (f"For the given statement, the system response is 'anger':{anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
