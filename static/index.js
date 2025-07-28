"use strict";
if (location.pathname.includes('viajero')) {
    let matriz = [];
    let nodos = [];
    // Create WebSocket connection.
    // let cliente = Date.now()
    // const texto = `ws${location.origin.includes('https') ? 's' : ''}://${location.host}/ws/${cliente}`
    const texto = `ws${location.origin.includes('https') ? 's' : ''}://${location.host}/ws`;
    console.log(texto);
    const socket = new WebSocket(texto);
    let nodear = document.getElementById("nodear");
    let aristear = document.getElementById("aristear");
    let primer = document.getElementById("primer");
    let segundo = document.getElementById("segundo");
    let grafo = document.getElementById("grafo");
    // let grafo_final = document.getElementById('grafo_final') as HTMLImageElement
    function mandar() {
        socket.send(JSON.stringify({
            nodos: nodos,
            matriz: matriz,
            titulo: location.pathname.split('_')[1]
        }));
    }
    function listar() {
        primer.innerHTML = '';
        segundo.innerHTML = '';
        nodos.forEach((nodo) => {
            let option = document.createElement('option');
            option.value = nodo;
            option.innerText = nodo;
            primer.appendChild(option);
            option = document.createElement('option');
            option.value = nodo;
            option.innerText = nodo;
            segundo.appendChild(option);
            nodear.reset();
        });
    }
    nodear.addEventListener("submit", (event) => {
        event.preventDefault();
        let info = new FormData(nodear);
        let dato = info.get('nodo');
        if (nodos.includes(dato))
            return;
        let lista = document.getElementById("nodos");
        let li = document.createElement('li');
        let span = document.createElement('span');
        let boton = document.createElement('button');
        span.innerText = dato;
        boton.innerText = "❌";
        boton.addEventListener("click", () => {
            lista.removeChild(li);
            let index = nodos.indexOf(dato);
            console.log(index);
            matriz.splice(index, 1);
            matriz.forEach((fila) => { fila.splice(index, 1); });
            nodos.splice(nodos.indexOf(dato), 1);
            console.log(matriz);
            listar();
            mandar();
        });
        li.appendChild(span);
        li.appendChild(boton);
        lista.appendChild(li);
        nodos.push(dato);
        let inicial = [];
        matriz.forEach((fila) => { fila.push(0); });
        for (let i = 0; i < nodos.length; i++)
            inicial.push(0);
        matriz.push(inicial);
        console.log(matriz);
        listar();
        mandar();
    });
    aristear.addEventListener("submit", (event) => {
        event.preventDefault();
        let info = new FormData(aristear);
        let primer = info.get('primer');
        let segundo = info.get('segundo');
        let arista = parseFloat(info.get('arista'));
        if (!nodos.includes(primer) || !nodos.includes(segundo))
            return;
        let i = nodos.indexOf(primer);
        let j = nodos.indexOf(segundo);
        if (i === -1 || j === -1 || i === j)
            return;
        if (!matriz[i])
            matriz[i] = [];
        if (!matriz[j])
            matriz[j] = [];
        matriz[i][j] = arista;
        matriz[j][i] = arista; // Asumiendo que la arista es bidireccional
        console.log(matriz);
        aristear.reset();
        mandar();
    });
    if (!location.pathname.includes('viajero')) {
        socket.close();
    }
    else {
        // Connection opened
        socket.addEventListener("open", (event) => {
            // socket.send("Hello Server!");
            socket.send(JSON.stringify({
                nodos: nodos,
                matriz: matriz,
                titulo: location.pathname.split('_')[1]
            }));
        });
        // Listen for messages
        socket.addEventListener("message", (event) => {
            console.log('llegó tu pedido :3');
            let pasado = JSON.parse(event.data);
            console.log(pasado);
            grafo.src = pasado['grafo'];
            // grafo.src = pasado[0]['grafo'];
            // if (pasado.length == 2) {
            //     grafo_final.src = pasado[1]['grafo']
            // }
        });
    }
}
