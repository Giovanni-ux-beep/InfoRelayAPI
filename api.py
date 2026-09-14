from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"estado": "API funcionando"}


@app.post("/datos")
def recibir_datos(datos: dict):
    print("Datos recibidos:", datos)
    return {"estado": "recibido", "datos": datos}