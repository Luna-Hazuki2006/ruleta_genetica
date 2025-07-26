from pprint import pprint
import random
from fastapi import FastAPI, Form
from fastapi.websockets import WebSocket
from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Annotated
from basico import genetico
from reinas_geneticas import coronar
from reinas_tabu import combinar
from reinas_recocidas import recocer_reinados
from viajero_tabu import tabues
from viajero_recocidas import recocer
from local import mostrar_busqueda

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

@app.get('/reinas_geneticas')
def realeza(request : Request, poblacion = '', generaciones = '', n : int = 4):
    pprint(poblacion)
    pprint(generaciones)
    tableros = coronar(n, poblacion, generaciones)
    return templates.TemplateResponse(request, 'reinas_geneticas.html', {
        'tableros': tableros, 'cantidad': n
    })

@app.get('/reinas_tabu')
def tabues_reales(request : Request, n : int = 4): 
    tableros = combinar(n)
    return templates.TemplateResponse(request, 'reinas_tabu.html', {
        'tableros': tableros, 'cantidad': n
    })

@app.get('/reinas_recocidas')
def realeza_recocida(request : Request, n : int = 4): 
    tableros = recocer_reinados(n)
    return templates.TemplateResponse(request, 'reinas_recocidas.html', {
        'tableros': tableros, 'cantidad': n
    })

@app.get('/viajero_recocido')
def viajero_recocido(request : Request): 
    return templates.TemplateResponse(request, 'viajero_recocido.html')

@app.get('/viajero_tabu')
def viajero_tabu(request : Request): 
    return templates.TemplateResponse(request, 'viajero_tabu.html')

@app.get('/busqueda_local')
def buscar_localidad(request : Request): 
    return templates.TemplateResponse(request, 'busqueda_local.html')

@app.post('/busqueda_local')
def mostrar_localidad(request : Request, inicio : Annotated[int, Form()], 
                      final : Annotated[int, Form()], veces : Annotated[int, Form()], 
                      inicial : Annotated[float, Form()], desplazamiento : Annotated[float, Form()], 
                      movimientos : Annotated[int, Form()]): 
    datos = mostrar_busqueda(inicio, final, veces, inicial, desplazamiento, movimientos)
    return templates.TemplateResponse(request, 'local_respuesta.html', {
        'datos': datos
    })

# @app.get('/prueba')
# def crear(request : Request):
#     matriz = [[0, 0, 0, 0] for esto in range(4)]
#     grafoicar(['a', 'b', 'c', 'd'], matriz, 'noseeeeeeeeeeeeee')
#     return 'si :D'

@app.websocket('/ws')
async def agujero_de_gusano(websocket : WebSocket): 
    await websocket.accept()
    while True: 
        info = await websocket.receive_json()
        print('AQUIIIIIIIIIIIIIII')
        print(info)
        real = {}
        print(info['titulo'])
        if info['titulo'] == 'recocido': real = recocer(info['nodos'], info['matriz'], info['titulo'])
        elif info['titulo'] == 'tabu': real = tabues(info['nodos'], info['matriz'], info['titulo'])
        await websocket.send_json(real)