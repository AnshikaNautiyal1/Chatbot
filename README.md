# Maa-Mate – The Emotional Chatbot

## Project Overview  
Maa-Mate is an AI-powered emotional chatbot designed to detect emotions from text and provide emotional support, mindfulness exercises, mood-based music, and stress-relief features.

### Problem Statement  
Many individuals struggle with emotional well-being and lack access to immediate support or guidance. Maa-Mate aims to bridge this gap by offering a virtual emotional companion that understands users' moods and provides comforting interactions.

### Key Features  
- **Emotion Detection** – Analyzes text input to determine the user’s emotional state.  
- **Mood-Based Music Player** – Suggests songs based on the user’s current mood.  
- **AI-Powered Chatbot** – Engages in supportive, uplifting conversations.  
- **Mood Tracker & Analytics** – Tracks mood trends over time and provides insights.  
- **Stress-Relief & Gamification** – Includes relaxation exercises and interactive games.  
- **Multi-Modal Communication** – Supports text and voice input for a personalized experience.  

---

## Dependencies  
To ensure smooth execution, install the following dependencies:

```bash
Python 3.9+
Flask==2.2.3  
TensorFlow==2.10.0  
Transformers==4.26.1  
NLTK==3.8.1  
requests==2.28.1  
SpeechRecognition==3.10.0  
Flask-SocketIO==5.3.0  
```

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Setup Instructions  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/maa-mate.git
cd maa-mate
```

### 2. Create a Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables  
Create a **.env** file and add the following variables:
```
OPENAI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

### 5. Run the Application  
```bash
python app.py
```
The chatbot will be accessible at **http://127.0.0.1:5000/**.

### 6. Using Maa-Mate  
- Enter a text input to chat with the AI.  
- View emotion-based responses and support suggestions.  
- Access the mood tracker and listen to recommended music.  

---

## Team Members  
- **Anshika Nautiyal** – AI & Backend Development  
- **[Teammate 1]** – Frontend Development  
- **[Teammate 2]** – UI/UX Design  

---

## License  
This project is licensed under the **MIT License**.

---

## Contribution Guidelines  
We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a new branch (`feature-xyz`).  
3. Make your changes and commit them.  
4. Submit a pull request.  

---

## Future Plans  
- Enhance emotion detection accuracy using deep learning models.  
- Improve chatbot memory retention for personalized conversations.  
- Introduce guided meditation and relaxation exercises.  
- Deploy a mobile version for easy accessibility.
