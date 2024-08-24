import tkinter as tk


ventana = tk.Tk()
ventana.title("La Calculadora de Hector")
ventana.configure(bg="#000000")

def click_boton(valor):
    actual = etiqueta.cget("text")
    if actual == "0":
        etiqueta.config(text=valor)
    else:
        etiqueta.config(text=actual + valor)

def clear():
    etiqueta.config(text="0")
    
def borrar_ultimo_caracter():
    actual = etiqueta.cget("text")
    if len(actual) > 1:  
        etiqueta.config(text=actual[:-1])
    else:  
        etiqueta.config(text="0")
def porcentaje():
    try:
        expresion = etiqueta.cget("text")
        if not expresion or expresion == "0":
            return
        # Convertir la expresión actual a porcentaje
        if "%" in expresion:
            # Si ya tiene un %, simplemente lo elimina y vuelve a calcular
            expresion = expresion.replace("%", "")
            resultado = eval(expresion) / 100
        else:
            resultado = eval(expresion) / 100

        etiqueta.config(text=str(resultado))
    except Exception as e:
        etiqueta.config(text="Error")


def calcular():
    try:
        expresion = etiqueta.cget("text")
        # Reemplazar X por , / por /, y ^ por * para exponentes
        resultado = eval(expresion.replace("X", "").replace("/", "/").replace("^", "*"))
        if resultado == int(resultado):  
            resultado = int(resultado)   
        etiqueta.config(text=str(resultado))
    except Exception as e:
        etiqueta.config(text="Error")

# Nueva función para manejar la operación exponencial
def exponencial():
    actual = etiqueta.cget("text")
    if actual == "0":
        etiqueta.config(text="Error")
    else:
        etiqueta.config(text=actual + "^")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="0", font="Helvetica 30", width=18, bg="white", 
                    relief="sunken", anchor="e", fg="white", background="#000000")
etiqueta.grid(row=0, column=0, columnspan=10, pady=30, padx=40)
#relief="sunken": Da un efecto de borde hundido
#anchor="e": Este parámetro alinea el texto a la derecha (este) dentro del Label.
#anchor="w": Este parámetro alinea el texto a la izquierda (oeste) dentro del Label.

# Botones
boton1 = tk.Button(ventana, text="7", width=10, height=4, command=lambda: click_boton("7"), bg="#000000", fg="white",font="17")
boton2 = tk.Button(ventana, text="8", width=10, height=4, command=lambda: click_boton("8"), bg="#000000", fg="white",font="17")
boton3 = tk.Button(ventana, text="9", width=10, height=4, command=lambda: click_boton("9"), bg="#000000", fg="white",font="17")
boton4 = tk.Button(ventana, text="/", width=10, height=4, command=lambda: click_boton("/"), bg="#FFA500", fg="white",font="17")
boton5 = tk.Button(ventana, text="4", width=10, height=4, command=lambda: click_boton("4"), bg="#000000", fg="white",font="17")
boton6 = tk.Button(ventana, text="5", width=10, height=4, command=lambda: click_boton("5"), bg="#000000", fg="white",font="17")
boton7 = tk.Button(ventana, text="6", width=10, height=4, command=lambda: click_boton("6"), bg="#000000", fg="white",font="17")
boton8 = tk.Button(ventana, text="X", width=10, height=4, command=lambda: click_boton("X"), bg="#FFA500", fg="white",font="17")
boton9 = tk.Button(ventana, text="1", width=10, height=4, command=lambda: click_boton("1"), bg="#000000", fg="white",font="17")
boton10 = tk.Button(ventana, text="2", width=10, height=4, command=lambda: click_boton("2"), bg="#000000", fg="white",font="17")
boton11 = tk.Button(ventana, text="3", width=10, height=4, command=lambda: click_boton("3"), bg="#000000", fg="white",font="17")
boton12 = tk.Button(ventana, text="-", width=10, height=4, command=lambda: click_boton("-"), bg="#FFA500", fg="white",font="17")
boton13 = tk.Button(ventana, text="0", width=10, height=4, command=lambda: click_boton("0"), bg="#000000", fg="white",font="17")
boton14 = tk.Button(ventana, text=".", width=10, height=4, command=lambda: click_boton("."), bg="#000000", fg="white",font="17")
boton15 = tk.Button(ventana, text="+", width=10, height=4, command=lambda: click_boton("+"), bg="#000000", fg="white",font="17")
boton16 = tk.Button(ventana, text="=", width=10, height=4, command=calcular, bg="#FFA500", fg="white",font="17")
boton17 = tk.Button(ventana, text="AC", width=10, height=4, command=clear, bg="gray", font="17")
boton18 = tk.Button(ventana, text="CE", width=10, height=4, command=borrar_ultimo_caracter, bg="gray", font="17")
boton19 = tk.Button(ventana, text="%", width=10, height=4, command=porcentaje, bg="#FFA500", fg="white",font="17")
boton20 = tk.Button(ventana, text="exp^", width=10, height=4,command=exponencial, bg="gray",font="17")

# Añadir columnas vacías a la izquierda
columna_vacia = 3  # Ajusta este valor según sea necesario

# Ubicar botones en la cuadrícula
boton20.grid(row=1, column=columna_vacia+2, pady=6)
boton19.grid(row=1, column=columna_vacia+3, pady=6)
boton18.grid(row=1, column=columna_vacia+1, pady=6)
boton17.grid(row=1, column=columna_vacia, pady=6)
boton1.grid(row=2, column=columna_vacia, pady=6)
boton2.grid(row=2, column=columna_vacia + 1, pady=6)
boton3.grid(row=2, column=columna_vacia + 2, pady=6)
boton4.grid(row=2, column=columna_vacia + 3, pady=6)

boton5.grid(row=3, column=columna_vacia, pady=6)
boton6.grid(row=3, column=columna_vacia + 1, pady=6)
boton7.grid(row=3, column=columna_vacia + 2, pady=6)
boton8.grid(row=3, column=columna_vacia + 3, pady=6)

boton9.grid(row=4, column=columna_vacia, pady=6)
boton10.grid(row=4, column=columna_vacia + 1, pady=6)
boton11.grid(row=4, column=columna_vacia + 2, pady=6)
boton12.grid(row=4, column=columna_vacia + 3, pady=6)

boton13.grid(row=5, column=columna_vacia, pady=6)
boton14.grid(row=5, column=columna_vacia + 1, pady=6)
boton15.grid(row=5, column=columna_vacia + 2, pady=6)
boton16.grid(row=5, column=columna_vacia + 3, pady=6)

ventana.geometry("500x650")
ventana.mainloop()