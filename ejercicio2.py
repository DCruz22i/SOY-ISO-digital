def imprimir(Productos,Precios,Stock):
    """ funcion para imprimir Productos """
    lista=""
    for key in Productos:
        lista += "%i\t%s\t%d\t%i \n" % (key,Productos[key],Precios[key],Stock[key])
    return lista

def repeticionProducto(productoNuevo):
    """ funcion verificar que el Producto nuevo no exista """
    for key in Productos:
        if Productos[key]==productoNuevo:
            return True
    return False

def nuevaLlave():
    limit = 0
    for key in Productos:
        limit = key
    return limit + 1

def inputProducto():
    """ funcion para añadir/actualizar un Producto """
    while True:
        producto = input("Ingrese el producto a añadir: ")
        if producto == "":
            print("El producto no puede estar vacio")
        elif repeticionProducto(producto):
            print("El producto ya existe")
        else:
            return producto
 
 
def inputPrecios():
    """ funcion para añadir/actualizar un Precio """
    while True:
        try:
            precio = float(input("Ingrese el precio del producto:"))
            return precio
        except:
            print("el precio tiene que ser un valor numerico")
 
 
def inputStock():
    """ funcion para añadir/actualizar un Stock """
    while True:
        try:
            stock = float(input("Ingrese el stock del producto:"))
            return stock
        except:
            print("el stock tiene que ser un valor numerico")

def inputKey():
    """ funcion para ingresar el key de un Producto """
    while True:
        try:
            key = int(input("Ingrese el Key(Primera Columna) del producto:"))
            if Productos.get(key,"")=="":
                print("El producto no existe.")
            else:
                return key
        except:
            print("el key tiene que ser un valor numerico")

def agregar():
    """ funcion para agregar Producto """

    key = nuevaLlave()

    prod = inputProducto()
    prec = inputPrecios()
    stoc = inputStock()
    Productos[key]=prod
    Precios[key]=prec
    Stock[key]=stoc

def eliminar():
    """ funcion para eliminar Producto """
    key = inputKey()
    Productos.pop(key)

def actualizar():
    """ funcion para actualizar Producto """
    key = inputKey()

    prod = inputProducto()
    prec = inputPrecios()
    stoc = inputStock()
    Productos[key]=prod
    Precios[key]=prec
    Stock[key]=stoc

def gracias():
    print('\n Gracias. \n')

def error():
    print('\n Opción no disponible, ingrese otra opción por favor. \n')


# Se tienen los siguientes diccionarios:
# PROGRAMA PRINCIPAL
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# Elaborar un programa que muestre los diccionarios, y programar las siguientes acciones:
# [1] Agregar
# [2] Eliminar
# [3] Actualizar
# [4] Salir
seleccion=0
while(seleccion != 4):
    opcion = input("========================================\n"+
        "Lista de Productos:\n"+
        "========================================\n"+
        imprimir(Productos,Precios,Stock)+
        "========================================\n"+
        "[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir\n"+
        "Elija opción:"
        )
    try:
        seleccion = int(opcion)
    except:
        seleccion=0

    switch = {
        1: agregar,
        2: eliminar,
        3: actualizar,
        4: gracias
    }

    #tomamos la función asociada a la variable y la invocamos
    switch.get(seleccion, error)()


