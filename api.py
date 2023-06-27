import uvicorn
from fastapi import FastAPI

# Criando a instancia 
app = FastAPI()

frota = ["Fox", "Civic", "Polo", "Punto", "Golf", "Gol", "HB20", "Logan", "Fiat Uno"]



@app.get("/carros")
def obter_frota():
    return frota


@app.post("/carros/novo/{veiculo}")
def adicionando_carro(veiculo: str):
    frota.extend({veiculo})
    return {"message": "Carro adicionado com sucesso."}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)