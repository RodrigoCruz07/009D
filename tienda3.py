import json
idboleta=0
opcion =0
idvendedor=0
opcionmantenedores=0
opciontienda=0
while opcion!=4:
    print("1 - Mantenedor de Servicios")
    print("2 - Tienda")
    print("3 - Servicios")
    print("4 - Salir")
    opcion=int(input(""))

    if opcion==1:
        while opcionmantenedores!=5:
            print("1 - Mantenedor de Productos")
            print("2 - Mantenedor de Usuarios")
            print("3 - Mantenedor de Vendedores")
            print("4 - Mantenedor de Boletas")
            print("5 - Salir")
            opcionmantenedores=int(input(""))
            if opcionmantenedores==1:
                with open ("diccionario/compras.json","r") as archivojsproduc:
                    leerproductos=json.load(archivojsproduc)
                    productos=[]
                    productos.append(leerproductos["productos"])
                with open ("diccionario/comprasproduc.json","w") as archivojsproduc:
                    json.dump(productos,archivojsproduc,indent=4)
            elif opcionmantenedores==2:
                with open ("diccionario/compras.json","r") as archivojsusuario:
                    leerusuarios=json.load(archivojsusuario)
                    usuarios=[]
                    usuarios.append(leerproductos["clientes"])
                with open ("diccionario/comprasusuarios.json","w") as archivojsusuario:
                    json.dump(usuarios,archivojsusuario,indent=4)
            elif opcionmantenedores==3:
                with open ("diccionario/compras.json","r") as archivojsvendedores:
                    leervendedores=json.load(archivojsvendedores)
                    vendedores=[]
                    vendedores.append(leervendedores["vendedores"])
                with open ("diccionario/comprasVendedores.json","w") as archivojsvendedores:
                    json.dump(vendedores,archivojsvendedores,indent=4)
            elif opcionmantenedores==4:
                print("Dame la id de la boleta")
                idboleta=int(input(""))
                with open("diccionario/compras.json","r") as boletaid:
                    leerjson=json.load(boletaid)
                    for i in leerjson["detalle_boletas"]:
                        if i['id_boleta']== idboleta:
                            print(i)


    elif opcion==2:
        productoscliente=[]
        cantidaddecompra=0
        productoid=0
        print("Si es que no tiene id ponga No")
        try:
            idcliente=int(input("Me da su id de cliente: "))
            with open("diccionario/compras.json","r")as idcliente:
                leerid=json.load(idcliente)
                for i in leerid["clientes"]:
                    if i["id"] == idcliente:
                        print("Su id de cliente fue encontrada")
                else: 
                        print("")
        except ValueError:
                print("Su id no fue encontrada")
        with open("diccionario/compras.json","r") as mostrarproductos:
            mostrarproduc=json.load(mostrarproductos) 
            for producto in mostrarproduc["productos"]:
                print(f"id: {producto['id']}, nombre: {producto['nombre']}, precio: {producto['precio']}")
        print("Cuantos productos quiere añadir al carro?")
        cantidaddecompra=int(input(""))
        for i in range(cantidaddecompra):
            productoid=int(input("Dame su id: "))
            with open("diccionario/compras.json","r") as productoids:
                leerjson=json.load(productoids)
                for i in leerjson["productos"]:
                        if i['id']== productoid:
                            productoscliente.append(i)
        print("Quiere ver lo que lleva en el carro")
        print("1-Si")
        print("2-No")
        opciontienda=int(input(""))
        if opciontienda==1:
            for producto in productoscliente:
                print(f"id: {producto['id']}, nombre: {producto['nombre']}, precio: {producto['precio']}")
        else: 
            print("")
        print("""Cual va a ser tu forma de pagar?
        1- Debito
        2- Credito
        """)
        formapagar=input("")
        with open("diccionario/compras.json", "r") as pagar:
            pagarleer=json.load(pagar)
            for i in pagarleer["formas_pago"]: 
                if i ==formapagar:
                    input("me da su tarjeta")
        
        
        