from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.post("/prueba")
async def crear_base():
    return "creando crud"


