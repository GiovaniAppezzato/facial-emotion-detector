def translate_emotion(emotion: str) -> str:
    translations = {
        'angry': 'Raiva',
        'disgust': 'Nojo',
        'fear': 'Medo',
        'happy': 'Felicidade',
        'sad': 'Tristeza',
        'surprise': 'Surpresa',
        'neutral': 'Neutro',
    }
    return translations.get(emotion, '')