import requests

url = (
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados"
    "?formato=json"
    "&dataInicial=01/01/2020"
    "&dataFinal=31/12/2025"
)

r = requests.get(url)

print("STATUS:", r.status_code)
print("HEADERS:")
print(r.headers)

print("\nTEXTO:")
print(repr(r.text))