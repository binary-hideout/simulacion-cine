import tkinter as tk
import tkinter.messagebox

from flujo import simular
from validaciones import formatear_hora
from validaciones import validar_pcl
from validaciones import validar_tlim

class Sistema:
    def __init__(self, master):
        self.frame = tk.Frame(master, width=800, height=500)
        self.frame.pack()

    def inicializar(self):
        self.minutos = tk.Label(self.frame, text="Ingresa los minutos")
        self.minutos.place(x=0, y=100)

        self.minutos_entry = tk.Entry(self.frame)
        self.minutos_entry.place(x=200, y=100)

        self.clientes = tk.Label(self.frame, text="Ingresa los clientes por hora")
        self.clientes.place(x=0, y=150)

        self.clientes_entry = tk.Entry(self.frame)
        self.clientes_entry.place(x=200, y=150)

        # Salida caja 1
        self.tiempo_caja_1 = tk.Label(self.frame, text="Tiempo de ocio caja #1")
        self.tiempo_caja_1.place(x=400, y=0)

        self.salida_caja_1 = tk.StringVar()
        self.tiempo_caja_1_text = tk.Label(self.frame, textvariable=self.salida_caja_1, fg="blue")
        self.tiempo_caja_1_text.place(x=600, y=0)

        self.clientes_caja_1 = tk.Label(self.frame, text="Clientes atendidos caja #1")
        self.clientes_caja_1.place(x=400, y=50)

        self.salida_clientes_caja_1 = tk.StringVar()
        self.clientes_caja_1_text = tk.Label(self.frame, textvariable=self.salida_clientes_caja_1, fg="blue")
        self.clientes_caja_1_text.place(x=600, y=50)

        # Salida caja 2
        self.tiempo_caja_2 = tk.Label(self.frame, text="Tiempo de ocio caja #2")
        self.tiempo_caja_2.place(x=400, y=150)

        self.salida_caja_2 = tk.StringVar()
        self.tiempo_caja_2_text = tk.Label(self.frame, textvariable=self.salida_caja_2, fg="blue")
        self.tiempo_caja_2_text.place(x=600, y=150)

        self.clientes_caja_2 = tk.Label(self.frame, text="Clientes atendidos caja #2")
        self.clientes_caja_2.place(x=400, y=200)

        self.salida_clientes_caja_2 = tk.StringVar()
        self.clientes_caja_2_text = tk.Label(self.frame, textvariable=self.salida_clientes_caja_2, fg="blue")
        self.clientes_caja_2_text.place(x=600, y=200) 

        # Salida caja 3
        self.tiempo_caja_3 = tk.Label(self.frame, text="Tiempo de ocio caja #3")
        self.tiempo_caja_3.place(x=400, y=300)

        self.salida_caja_3 = tk.StringVar()
        self.tiempo_caja_3_text = tk.Label(self.frame, textvariable=self.salida_caja_3, fg="blue")
        self.tiempo_caja_3_text.place(x=600, y=300)

        self.clientes_caja_3 = tk.Label(self.frame, text="Clientes atendidos caja #3")
        self.clientes_caja_3.place(x=400, y=350)

        self.salida_clientes_caja_3 = tk.StringVar()
        self.clientes_caja_3_text = tk.Label(self.frame, textvariable=self.salida_clientes_caja_3, fg="blue")
        self.clientes_caja_3_text.place(x=600, y=350)

        # Salida clientes
        self.clientes_total = tk.Label(self.frame, text="Total de clientes atendidos")
        self.clientes_total.place(x=400, y=400)

        self.salida_clientes = tk.StringVar()
        self.salida_clientes_text = tk.Label(self.frame, textvariable=self.salida_clientes, fg="blue")
        self.salida_clientes_text.place(x=600, y=400)

        # Salida tiempo total
        self.tiempo_total = tk.Label(self.frame, text="Tiempo de ocio total")
        self.tiempo_total.place(x=400, y=450)

        self.salida_tiempos = tk.StringVar()
        self.salida_tiempos_text = tk.Label(self.frame, textvariable=self.salida_tiempos, fg="blue")
        self.salida_tiempos_text.place(x=600, y=450)


        self.button = tk.Button(self.frame, text="CORRER", fg="blue", command=self.correr_simulacion)
        self.button.place(x=50, y=400)

    def correr_simulacion(self):
        tiempo_limite = self.minutos_entry.get()
        cantidad_clientes = self.clientes_entry.get()

        if (validar_tlim(tiempo_limite) and validar_pcl(cantidad_clientes)):
            tiempo_limite = float(tiempo_limite)
            cantidad_clientes = int(cantidad_clientes)
        else:
            self.error = tkinter.messagebox.showerror(title="ERROR", message="Verificar entrada")
            return

        to, na = simular(tiempo_limite, cantidad_clientes)

        self.tiempo_ocio_total = sum(to)
        print(to[0])
        print(to[1])
        print(to[2])

        self.salida_caja_1.set(formatear_hora(to[0]))
        self.salida_caja_2.set(formatear_hora(to[1]))
        self.salida_caja_3.set(formatear_hora(to[2]))

        self.salida_clientes_caja_1.set(str(na[0]) + " clientes")
        self.salida_clientes_caja_2.set(str(na[1]) + " clientes")
        self.salida_clientes_caja_3.set(str(na[2]) + " clientes")

        self.salida_clientes.set(str(sum(na)) + " clientes")
        self.salida_tiempos.set(formatear_hora(self.tiempo_ocio_total))

root = tk.Tk()
root.title("Cinema Queue Simulator PRO")
app = Sistema(root)
app.inicializar()
root.mainloop()
