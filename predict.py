import requests

def predict(prompt: str):
    # Endpoint tvog RunPod modela
    endpoint = "https://api.runpod.ai/v2/aklfg0z6vp4mvj/run"
    
    # Podaci koje RunPod model očekuje (prompt, ili dodatne opcije)
    payload = {
        "input": {
            "prompt": prompt
        }
    }

    # Headeri — moraš dodati svoj RunPod API ključ ovdje
    headers = {
        import os
headers = {
    "Authorization": f"Bearer {os.getenv('RUNPOD_API_KEY')}",
    "Content-Type": "application/json"
}
        "Content-Type": "application/json"
    }

    # Pošalji zahtjev RunPodu
    response = requests.post(endpoint, headers=headers, json=payload)

    # Vrati rezultat
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": response.text}
