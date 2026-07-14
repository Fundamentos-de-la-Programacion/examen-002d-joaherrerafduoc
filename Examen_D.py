
recorridos = {
'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True],
}

venta = {
'R001': [7990, 20],
'R002': [25990, 0],
'R003': [1990, 35],
'R004': [12990, 8],
'R005': [18990, 3],
'R006': [4990, 12],
}
p_min = 0
p_max = 0


Origen = ['Santiago', 'La Serena', 'Temuco', 'Iquique']
Destino = ['Valparaíso', 'Concepción', 'Coquimbo', 'Valdivia', 'Arica', 'Rancagua']
Distancia = [120, 500, 15, 165, 310, 90]
Tipo_bus = ['normal', 'cama', 'semi-cama']
Servicio = ['dia', 'noche']
Tiene_wifi = [True, False]
Precio = [7990, 25990, 1990, 12990, 18990, 4990]
Asientos = [0, 20, 35, 8, 3, 12]
Codigo = ['R001', 'R002', 'R003', 'R004', 'R005', 'R006']

def MostrarMenu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Asientos por ciudad de origen
2. Búsqueda de recorridos por rango de precio
3. Actualizar precio de recorrido
4. Agregar recorrido
5. Eliminar recorrido
6. Salir
=====================================
          """)
    
#validaciones

def leer_opcion():
    try:
        op = int(input("Ingrese una opcion:"))
        if op >= 0:
            print("Tu Opcion no puede ser menor que 0 ni 0")
        elif op < 6:
            print("Tu opcion no puede ser mayor que 6")
        else:
            return op
    except ValueError:
        print("Opcion no valida, intente denuevo")

def asientos_origen(Origen):
    parametro = 0
    buscar = input("Ingrese el asiento de origen: ")
    buscar.uppper()
    print(buscar)
    if buscar in Origen:
        
        print()

def busqueda_precio(p_min, p_max):
    p_min = int(input("Ingrese el precio minimo: "))
    p_max = int(input("Ingrese el precio maximo: "))
    if p_min > 0 and p_max > 0:
        print()
    else:
        print("Debe ingresar valores enteros")

def buscar_codigo(Codigo):
    solicodigo = input("Ingrese el codigo del recorrido: ")
    if solicodigo in Codigo:
        return True
    else:
        return False


def actualizar_precio(Codigo, nuevo_precio):
    while True:
        Codigo = buscar_codigo(Codigo)
        if Codigo == True:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            print("El precio hacido actualizado")
        elif Codigo == False:
            print("No salio Codigo actualizado")
        


def agregar_recorrido(Codigo, Origen, Destino, Distancia, Tipo_bus, Servicio, Tiene_wifi, Precio, Asientos):
    Origen = input("ingrese el sitio de origen del viaje: ")
    if Origen.strip() != "":
        return True
    else:
        return False





def eliminar_recorrido(codigo):
    cod = input()











        
    
def main():
    while True:
        MostrarMenu()

        op = leer_opcion()
        if op == 1:
            asientos_origen(Origen)
            print("")
        elif op == 2:
            busqueda_precio(p_min, p_max)
            print("")
        elif op == 3:
            actualizar_precio(Codigo,)
            print("")
        elif op == 4:
            agregar_recorrido(Codigo, Origen, Destino, Distancia, Tipo_bus, Servicio, Tiene_wifi, Precio, Asientos)
            print("")
        elif op == 5:

            print("")
        elif op == 6:
            print("Programa finalizado")
            break
        else:
            print("Opcion invalida")