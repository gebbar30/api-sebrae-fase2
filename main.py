from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="API SEBRAE - Motor de NLP (Fase 2)")

print("Carregando o Cérebro da IA...")
modelo_rf = joblib.load('modelo_sentimento.pkl')
vetorizador = joblib.load('vetorizador.pkl')

class AvaliacaoCliente(BaseModel):
    texto: str

@app.get("/")
def status_api():
    return {
        "status": "Online",
        "motor_ia": "Random Forest Classifier"
    }

@app.post("/analisar-sentimento")
def prever_sentimento(avaliacao: AvaliacaoCliente):
    texto_matematica = vetorizador.transform([avaliacao.texto])
    predicao = modelo_rf.predict(texto_matematica)[0]
    
    if predicao == 1:
        resultado = "POSITIVO (Cliente Satisfeita)"
    else:
        resultado = "NEGATIVO (Alerta de Detrator)"
        
    return {
        "status": "Sucesso",
        "texto_analisado": avaliacao.texto,
        "sentimento_predito": resultado
    }