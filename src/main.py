'''
Archivo para mostrar resultados en consola.

Para la interfaz gráfica, ejecutar el archivo sistema.py
'''

from flujo import simular

tlim = float(input('Tiempo límite de la simulación: '))
pcl = int(input('Cantidad de clientes por tiempo de asignación: '))

simular(tlim, pcl)
