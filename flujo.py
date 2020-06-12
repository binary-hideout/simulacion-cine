from distribucion import distribucion

def simular(tlim: float, pcl: int) -> None:
    '''
    Simula la fila y las cajas de boletos para un cine.

    tlim: tiempo límite de la simulación.

    pcl: cantidad de personas que llegan por hora.
    '''
    sd = [2.14125, 1.42708, 1.36626]
    m = [5.41935, 4.64516, 6]

    ts = [
        distribucion(sd[0], m[0]),
        distribucion(sd[1], m[1]),
        distribucion(sd[2], m[2])
    ]
    cajas = [False, False, False]

    reloj = 0
    tc = 0
    tas = 60
    fila = pcl
    na = [0, 0, 0]
    to = [0, 0, 0]
    # arroba
    while True:
        delta = min(ts, key=lambda x: x if x > 0 else float('inf'))
        if delta == 0:
            tdif = tas - tc
            reloj += tdif
            tc += tdif
        else:
            reloj += delta
            tc += delta

        if reloj >= tlim:
            tna = sum(na)
            break

        if tc >= tas:
            tc -= tas
            fila += pcl
            ts = [
                distribucion(sd[0], m[0]),
                distribucion(sd[1], m[1]),
                distribucion(sd[2], m[2])
            ]
            cajas = [False, False, False]

        for i in range(3):
            if not cajas[i]:
                fila -= 1
                cajas[i] = True

        for i in range(3):
            if ts[i] == 0:
                to[i] += delta
            else:
                ts[i] -= delta
                if ts[i] == 0:
                    na[i] += 1
                    if fila > 0:
                        ts[i] = distribucion(sd[i], m[i])
                        fila -= 1

    for i in range(3):
        print(f'\nTiempo de ocio de caja {i + 1}: {to[i]}')
        print(f'Clientes atendidas en caja {i + 1}: {na[i]}')
    print(f'\nTotal de clientes atendidos: {tna}')

    return to, na, tna