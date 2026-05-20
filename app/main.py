from fastapi import FastAPI, UploadFile, File
from app.voice import get_answer
from app.stt import transcribe
from app.tts import speak

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kaya AI está online"}

@app.post("/chat")
def chat(text: str):
    return {"response": get_answer(text)}

@app.post("/voice")
async def voice(file: UploadFile = File(...)):
    audio_path = "temp.wav"

    with open(audio_path, "wb") as f:
        f.write(await file.read())

    text = transcribe(audio_path)
    response = get_answer(text)
    audio_file = speak(response)

    return {
        "text": response,
        "audio": audio_file
    }