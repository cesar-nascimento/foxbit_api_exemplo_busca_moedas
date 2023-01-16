import asyncio
import json
import subprocess
import sys


try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
    import pandas as pd

try:
    import websockets
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'websockets'])
    import websockets


async def buscar_moedas():
    uri = "wss://api.foxbit.com.br/"
    async with websockets.connect(uri, ssl=True) as websocket:
        msg = '{"m":0,"i":0,"n":"GetProducts","o":""}'
        await websocket.send(msg)
        resposta = await websocket.recv()
        moedas = json.loads(resposta).get("o")
        return json.loads(moedas)

if __name__ == "__main__":
    # Busca moedas na API
    print("\n>>> Enviando requisição para a API...")
    moedas = asyncio.run(buscar_moedas())

    # Formatando para csv
    df = pd.DataFrame(moedas)
    print("\n>>> Resumo dos dados obtidos pela API:\n")
    print(df.head())
    
    # Salvando arquivo
    arquivo = "moedas_foxbit.csv"
    print(f"\n>>> Salvando dados em {arquivo!r}...")
    df.to_csv(arquivo, index=False)