import pandas as pd
import requests
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

series = {
    "selic": 432,
    "ipca": 433,
    "dolar": 1
}

for nome, codigo in series.items():

    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"
        "?formato=json"
        "&dataInicial=01/01/2020"
        "&dataFinal=31/12/2025"
    )

    try:
        response = requests.get(url, timeout=30)

        response.raise_for_status()

        dados = response.json()

        df = pd.DataFrame(dados)

        arquivo = f"data/raw/{nome}.csv"

        df.to_csv(arquivo, index=False)

        print(f"✓ Salvo: {arquivo}")

    except Exception as e:
        print(f"✗ Erro em {nome}: {e}")