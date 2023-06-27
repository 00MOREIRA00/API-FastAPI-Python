# API-FastAPI-Python
Repositório destinado ao estudo de criações de APIs utilzando o FastAPI 

1° Importando fast Api
```
from fastapi import FastAPI
```
2° Criando a instancia 
```
app = FastAPI()
```

3° Importamos o unicorn
```
import uvicorn
```

4° Criando modulo de iniciação padrão 
```
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
```


5° Criamos uma lista que será consumida nas operações
```
frota = ["Fox", "Civic", "Polo", "Punto", "Golf", "Gol", "HB20", "Logan", "Fiat Uno"]
```

6° Criamos funções que recebem rotas para que seja chamado a api
```
@app.get("/carros")
def obter_frota():
    return frota


@app.post("/carros/novo/{veiculo}")
def adicionando_carro(veiculo: str):
    frota.extend({veiculo})
    return {"message": "Carro adicionado com sucesso."}
```


>>Para que possamos trabalhar com requisições o FastAPI utiliza uma biblioteca chamada Pydantic que organiza classes que nos trazem diversos debeficios. Como por exemplo: 

