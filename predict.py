import requests
import os

RUNPOD_ENDPOINT = "https://api.runpod.ai/v2/aklfg0z6vp4mvj/run"
RUNPOD_API_KEY = os.environ.get("RUNPOD_API_KEY")

def predict(prompt: str):
    headers = {
        "Authorization": f"Bearer {RUNPOD_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"input": {"prompt": prompt}}
    response = requests.post(RUNPOD_ENDPOINT, json=payload, headers=headers)
    try:
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}
