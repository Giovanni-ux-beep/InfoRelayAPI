from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "alb_it-arg.ment908#345(521)"

datos_guardados = []


@app.get("/")
def inicio():
    return {"estado": "API funcionando"}


@app.post("/datos")
def recibir_datos(datos: dict, x_api_key: str | None = Header(default=None)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key incorrecta")

    datos_guardados.append(datos)

    print("Datos recibidos:", datos)

    return {
        "estado": "recibido",
        "datos": datos
    }


@app.get("/datos")
def obtener_datos(x_api_key: str | None = Header(default=None)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key incorrecta")

    datos = datos_guardados.copy()
    datos_guardados.clear()

    return {
        "cantidad": len(datos),
        "datos": datos
    }