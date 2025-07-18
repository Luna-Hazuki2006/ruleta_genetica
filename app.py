from pprint import pprint
import random
from fastapi import FastAPI, Form
from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Annotated
from basico import genetico
from reinas_geneticas import coronar
from reinas_tabu import combinar

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="./templates")

class Datos_Iniciales(BaseModel): 
    inicio : int
    final : int
    veces : int
    generaciones : int

@app.get('/')
def iniciar(request : Request): 
    return templates.TemplateResponse(request, 'basico.html')

@app.post('/')
def mostrar(request : Request, datos : Annotated[Datos_Iniciales, Form()]): 
    pprint(datos)
    lista = genetico(datos.inicio, datos.final, datos.veces, datos.generaciones)
    return templates.TemplateResponse(request, 'respuesta.html', {
        'lista': lista
    })

@app.get('/reinas')
def realeza(request : Request):
    cantidad = 4
    tableros = coronar(cantidad)
    return templates.TemplateResponse(request, 'reinas_geneticas.html', {
        'tableros': tableros, 'zip': zip, 'cantidad': cantidad
    })

@app.get('/tabu')
def tabues_reales(request : Request): 
    cantidad = 4
    tableros = combinar(cantidad)
    return templates.TemplateResponse(request, 'reinas_tabu.html', {
        'tableros': tableros, 'cantidad': cantidad
    })