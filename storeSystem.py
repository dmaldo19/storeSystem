#Maldonado Meléndez Diego Alberto

def atxt():
    import pickle;
    empresas={"Conve Express": ["Número Tel: 33 3589 2595", "Correo: tuconverapi@gmail.com"], "Conve Tienda": ["Número Tel: 33 3999 2595", "Correo: tiendaconve123@gmail.com"]};
    empleados={"0": ["Pedro Gutierrez", "Número Tel: 33 3345 9900", "Correo: pedritoPro@gmail.com", "Salario: $1,500"], "1": ["José Sánchez", "Número Tel: 33 4004 3566", "Correo: joselite@gmail.com", "Salario: $1,750"], "2":["Juan Gomez", "Número Tel: 33 5500 7789", "Correo: juanMax@gmail.com", "Salario: $2,750"]};
    productos={"0": ["Doritos", "Precio: $15", "Pieza(s): 500"], "1" : ["Ruffles De Queso", "Precio: $6", "Pieza(s): 250"], "2" : ["Sklittes", "Precio: $20", "Pieza(s): 300"], "3" : ["Pepsi 600 ml", "Precio: $11", "Pieza(s): 700"], "4" : ["Coca-Cola 600 ml", "Precio: $10", "Pieza(s): 1000"], "5" : ["Fanta 1.75 l", "Precio: $21", "Pieza(s): 300"], "6" : ["Ferrero Rocher", "Precio: $25", "Pieza(s): 100"], "7" : ["Encendedor", "Precio: $28", "Pieza(s): 470"], "8" : ["Springles", "Precio: $30", "Pieza(s): 100"], "9" : ["Saladitas", "Precio: $14", "Pieza(s): 1500"]};
    precios={"0": 15, "1" : 6, "2" : 20, "3" : 11, "4" : 10, "5" : 21, "6" : 25, "7" : 28, "8" : 30, "9" : 14};
    piezas={"0": 500, "1" : 250, "2" : 300, "3" : 700, "4" : 1000, "5" : 300, "6" : 100, "7" : 470, "8" : 100, "9" : 1500};
    dineroencaja = 500;
    archivo=open("d06-p11-equipo-03-T.txt", "wb");
    pickle.dump(empresas, archivo);
    pickle.dump(empleados, archivo);
    pickle.dump(productos, archivo);
    pickle.dump(precios, archivo);
    pickle.dump(piezas, archivo);
    pickle.dump(dineroencaja, archivo);
    archivo.close();

def ventanas(x, y, vx, vy, seccion):
    import os;
    from colorama import Back, Cursor, init, Fore;
    from time import sleep;
    init(autoreset=True);
    backup= vy; #Guardar el valor inicial de vy
    if seccion == 1:
        os.system("cls");
        for i in range(y): #Esta imprime la ventana trasera
            print (Cursor.POS(vx+5,vy-2) + Back.LIGHTGREEN_EX + ' ' + Back.LIGHTGREEN_EX + ' ' * (x-2) + Back.LIGHTGREEN_EX + ' ');
            vy+=1;
        vy = backup;
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ');
            vy+=1;
    elif seccion == 2:
        os.system("cls");
        for i in range(y): #Esta imprime la ventana trasera
            print (Cursor.POS(vx+5,vy-2) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ');
            vy+=1;
        vy = backup;
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTGREEN_EX + ' ' + Back.LIGHTGREEN_EX + ' ' * (x-2) + Back.LIGHTGREEN_EX + ' ');
            vy+=1;
    elif seccion == 3:
        os.system("cls");
        for i in range(y): #Esta imprime la ventana trasera
            print (Cursor.POS(vx+5,vy-2) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ');
            vy+=1;
        vy = backup;
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTCYAN_EX + ' ' + Back.LIGHTCYAN_EX + ' ' * (x-2) + Back.LIGHTCYAN_EX + ' ');
            vy+=1;
    elif seccion == 4:
        os.system("cls");
        for i in range(y): #Esta imprime la ventana trasera
            print (Cursor.POS(vx+5,vy-2) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ');
            vy+=1;
        vy = backup;
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.WHITE + ' ' + Back.WHITE + ' ' * (x-2) + Back.WHITE + ' ');
            vy+=1;
    elif seccion == 5:
        os.system("cls");
        for i in range(y): #Esta imprime la ventana trasera
            print (Cursor.POS(vx+5,vy-2) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ')
            vy+=1;
        vy = backup;
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTYELLOW_EX + ' ' + Back.LIGHTYELLOW_EX + ' ' * (x-2) + Back.LIGHTYELLOW_EX + ' ');
            vy+=1;
    elif seccion == 6:
        os.system("cls");
        for i in range(y): #Esta imprime la ventana trasera
            print (Cursor.POS(vx+5,vy-2) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ');
            vy+=1;
        vy = backup;
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTMAGENTA_EX + ' ' + Back.LIGHTMAGENTA_EX + ' ' * (x-2) + Back.LIGHTMAGENTA_EX + ' ');
            vy+=1;
        sleep(0.5);
        print(Cursor.POS(50, 8) + Back.LIGHTMAGENTA_EX + Fore.BLACK + "¡VUELVA PRONTO!");
        sleep(0.5);
    elif seccion == 7:
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTGREEN_EX + ' ' + Back.LIGHTGREEN_EX + ' ' * (x-2) + Back.LIGHTGREEN_EX + ' ');
            vy+=1;
    elif seccion == 8:
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTCYAN_EX + ' ' + Back.LIGHTCYAN_EX + ' ' * (x-2) + Back.LIGHTCYAN_EX + ' ');
            vy+=1;
    elif seccion == 9:
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.WHITE + ' ' + Back.WHITE + ' ' * (x-2) + Back.WHITE + ' ');
            vy+=1;
    elif seccion == 10:
        for i in range(y): #Esta imprime la ventana delantera
            print (Cursor.POS(vx,vy) + Back.LIGHTYELLOW_EX + ' ' + Back.LIGHTYELLOW_EX + ' ' * (x-2) + Back.LIGHTYELLOW_EX + ' ');
            vy+=1;

def ventanasfactura(x, y, vx, vy):
    import os;
    from colorama import Back, Cursor,init;
    init(autoreset=True);
    os.system("cls");
    backup= vy; #Guardar el valor inicial de vy
    for i in range(y): #Esta imprime la ventana trasera
        print (Cursor.POS(vx+5,vy-2) + Back.LIGHTBLUE_EX + ' ' + Back.LIGHTBLUE_EX + ' ' * (x-2) + Back.LIGHTBLUE_EX + ' ');
        vy+=1;
    vy = backup;
    for i in range(y): #Esta imprime la ventana delantera
        print (Cursor.POS(vx,vy) + Back.WHITE + ' ' + Back.WHITE + ' ' * (x-2) + Back.WHITE + ' ');
        vy+=1;

def altas():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    ventanas(80, 25, 20, 5, 2);
    posicion=1;
    print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "ALTAS");
    print(Cursor.POS(25,7) + Back.LIGHTGREEN_EX + Fore.BLACK + "En esta parte del programa podrás dar de alta alguno de los diferentes");
    print(Cursor.POS(47,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "elementos de las empresas.");
    print(Cursor.POS(21,10) + Back.LIGHTGREEN_EX + Fore.BLACK + "Desplázate entre las opciones usando las flechas del teclado, para seleccionar");
    print(Cursor.POS(23,11) + Back.LIGHTGREEN_EX + Fore.BLACK + "la opción deseada presiona ENTER o presiona el número correspondiente a la");
    print(Cursor.POS(35,12) + Back.LIGHTGREEN_EX + Fore.BLACK + "opción. Para regresar al menú presiona ESC");
    print(Cursor.POS(50,14) + Back.LIGHTRED_EX + Fore.BLACK + "1. EMPRESAS");
    print(Cursor.POS(50,15) + Back.LIGHTGREEN_EX + Fore.BLACK + "2. EMPLEADOS");
    print(Cursor.POS(50,16) + Back.LIGHTGREEN_EX + Fore.BLACK + "3. PRODUCTOS");
    print(Cursor.POS(43,29) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
    while True:
        movimiento = ord(getch());
        if movimiento == 27:
            menu();
            break;
        elif movimiento == 13:
            if posicion == 1:
                altasempresa();
                break;
            if posicion == 2:
                altasempleados();
                break;
            if posicion == 3:
                altasproductos();
                break;
        elif movimiento == 224:
            movimiento = ord(getch());
            if movimiento == 72:
                posicion=posicion-1;
                if posicion<1:
                    posicion=3;
            elif movimiento == 80:
                posicion=posicion+1;
                if(posicion>3):
                    posicion=1;
            if posicion == 1:
                print(Cursor.POS(50,14) + Back.LIGHTRED_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,15) + Back.LIGHTGREEN_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,16) + Back.LIGHTGREEN_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
            if posicion == 2:
                print(Cursor.POS(50,14) + Back.LIGHTGREEN_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,15) + Back.LIGHTRED_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,16) + Back.LIGHTGREEN_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
            if posicion == 3:
                print(Cursor.POS(50,14) + Back.LIGHTGREEN_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,15) + Back.LIGHTGREEN_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,16) + Back.LIGHTRED_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));

def altasempresa():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    cantidadempresas=0;
    y=0;
    empresasl=[];
    ventanas(80, 25, 20, 5, 7);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "ALTAS EMPRESAS");
    print(Cursor.POS(21,7) + Back.LIGHTGREEN_EX + Fore.BLACK + "Aquí usted podrá dar de alta empresas. Estas son las empresas dadas de alta.");
    print(Cursor.POS(22,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "Presiona ENTER para realizar una alta o ESC para regresar al menú de altas");
    for i in empresas:
        empresasl.append(i);
        cantidadempresas+=1;
    for i in range (cantidadempresas):
        print(Cursor.POS(21,y+10) + Back.LIGHTGREEN_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            altas();
            break;
    ventanas(80, 25, 20, 5, 7);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "ALTAS EMPRESA");
    nombre = str(input(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingrese el nombre de la nueva empresa -> "));
    while True:
        if nombre in empresas:
            print(Cursor.POS(21,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "El nombre de la empresa que usted ingresó ya está registrado.");
            print(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + "                                                             ");
            nombre = str(input(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingrese un nuevo nombre de empresa -> "));
        else:
            break;
    print(Cursor.POS(21,8) + Back.LIGHTGREEN_EX + "                                                             ");
    telefono=str(input(Cursor.POS(21,10) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el número de teléfono -> "));
    telefonoc="Número Tel: "+str(telefono);
    correo=str(input(Cursor.POS(21,11) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el correo -> "));
    correoc="Correo: "+correo;
    print(Cursor.POS(21,13) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Está seguro que desea guardar los cambios?");
    print(Cursor.POS(21,14) + Back.LIGHTGREEN_EX + Fore.BLACK + "Sí guardar(Presione ENTER)      No guardar y volver al menú(ESC)");
    while True:
        decision = getch();

        if decision == b'\r':
            empresas[nombre]=[telefonoc, correoc];
            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            print(Cursor.POS(21,16) + Back.LIGHTGREEN_EX + Fore.BLACK + "¡Cambios Guardados! Presione ENTER para regresar al menú ");
            input();
            menu();
            break;

        elif decision == b'\x1b':
            menu();
            break;

def altasempleados():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    y=0;
    cantidadempleados=0;
    empleadosl=[];
    ventanas(80, 25, 20, 5, 7);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "ALTAS EMPLEADO");
    print(Cursor.POS(21,7) + Back.LIGHTGREEN_EX + Fore.BLACK + "Aquí usted podrá dar de alta empleados. Estos son las empleados.");
    print(Cursor.POS(22,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "Presiona ENTER para realizar una alta o ESC para regresar al menú de altas");
    for i in empleados:
        empleadosl.append(i);
        cantidadempleados+=1;
    for i in range (cantidadempleados):
        print(Cursor.POS(21,y+10) + Back.LIGHTGREEN_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
        print(Cursor.POS(21,y+11) + Back.LIGHTGREEN_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        y+=2;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            altas();
            break;
    ventanas(80, 25, 20, 5, 7);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "ALTAS EMPLEADO");
    ide = str(input(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingrese el ID del nuevo empleado -> "));
    while True:
        if ide in empleados:
            print(Cursor.POS(21,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "El ID del empleado que ingresó ya está registrado.");
            print(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + "                                                             ");
            ide = str(input(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingrese un nuevo ID de empleado -> "));
        else:
            break;

    print(Cursor.POS(21,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "                                                       ");
    nombre = str(input(Cursor.POS(21,10) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingrese el nombre del nuevo empleado -> "));
    telefono=str(input(Cursor.POS(21,11) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el número de teléfono -> "));
    telefonoc="Número Tel: "+telefono;
    correo=str(input(Cursor.POS(21,12) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el correo del nuevo empleado -> "));
    correoc="Correo: "+correo;
    while True:
        try:
            print(Cursor.POS(21,13) + Back.LIGHTGREEN_EX + "                                                                        ");
            salario=int(input(Cursor.POS(21,13) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el nuevo salario del nuevo empleado -> "));
            break;
        except:
            print(Cursor.POS(21,14) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa un salario válido.");

    salarioc="Salario: $"+ str(salario);
    print(Cursor.POS(21,15) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Está seguro que desea guardar los cambios?");
    print(Cursor.POS(21,16) + Back.LIGHTGREEN_EX + Fore.BLACK + "Sí guardar(Presione ENTER)      No guardar y volver al menú(ESC)");
    while True:
        decision = getch();

        if decision == b'\r':
            empleados[ide]=[nombre, telefonoc, correoc, salarioc];
            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            print(Cursor.POS(21,18) + Back.LIGHTGREEN_EX + Fore.BLACK + "¡Cambios Guardados! Presione ENTER para regresar al menú ");
            input();
            menu();
            break;

        elif decision == b'\x1b':
            menu();
            break;

def altasproductos():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    y=0;
    cantidadproductos=0;
    productosl=[];
    ventanas(80, 25, 20, 5, 7);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "ALTAS PRODUCTO");
    print(Cursor.POS(21,7) + Back.LIGHTGREEN_EX + Fore.BLACK + "Aquí usted podrá dar de alta productos. Estos son los productos.");
    print(Cursor.POS(22,8) + Back.LIGHTGREEN_EX + Fore.BLACK + "Presiona ENTER para realizar una alta o ESC para regresar al menú de altas");
    for i in productos:
        productosl.append(i);
        cantidadproductos+=1;
    for i in range (cantidadproductos):
        print(Cursor.POS(21,y+10) + Back.LIGHTGREEN_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            altas();
            break;
    ventanas(80, 25, 20, 5, 7);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "ALTAS PRODUCTO");
    try:
        ide=str(input(Cursor.POS(21,10) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el ID del nuevo producto -> "));
        while True:
            if ide in empleados:
                print(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + Fore.BLACK + "El ID de producto que ingresó ya está registrado.");
                print(Cursor.POS(21,10) + Back.LIGHTGREEN_EX + "                                                             ");
                ide = str(input(Cursor.POS(21,10) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingrese un nuevo ID de producto -> "));
            else:
                break;
        print(Cursor.POS(21,9) + Back.LIGHTGREEN_EX + Fore.BLACK + "                                                             ");
        nombre=str(input(Cursor.POS(21,11) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el nombre del nuevo producto -> "));
        precio=float(input(Cursor.POS(21,12) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el precio del nuevo producto -> "));
        precioc="Precio: $"+str(precio);
        pieza=int(input(Cursor.POS(21,13) + Back.LIGHTGREEN_EX + Fore.BLACK + "Ingresa el número de piezas disponibles del nuevo producto -> "));
        piezac="Pieza(s): "+str(pieza);
    except:
        print(Cursor.POS(21,17) + Back.LIGHTGREEN_EX + Fore.BLACK + "No ingresaste un número... Presiona ENTER para regresar");
        input();
        altasproductos();
    print(Cursor.POS(21,15) + Back.LIGHTGREEN_EX + Fore.BLACK + "¿Está seguro que desea guardar los cambios?");
    print(Cursor.POS(21,16) + Back.LIGHTGREEN_EX + Fore.BLACK + "Sí guardar(Presione ENTER)      No guardar y volver al menú(ESC)");
    while True:
        decision = getch();

        if decision == b'\r':
            productos[ide]=[nombre, precioc, piezac];
            precios[ide]=precio;
            piezas[ide]=pieza;
            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            print(Cursor.POS(21,18) + Back.LIGHTGREEN_EX + Fore.BLACK + "¡Cambios Guardados! Presione ENTER para regresar al menú ");
            input();
            menu();
            break;

        elif decision == b'\x1b':
            menu();
            break;

def bajas():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    ventanas(80, 25, 20, 5, 3);
    posicion=1;
    print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "BAJAS");
    print(Cursor.POS(25,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "En esta parte del programa podrás dar de baja alguno de los diferentes");
    print(Cursor.POS(47,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "elementos de la frutería.");
    print(Cursor.POS(21,10) + Back.LIGHTCYAN_EX + Fore.BLACK + "Desplázate entre las opciones usando las flechas del teclado, para seleccionar");
    print(Cursor.POS(23,11) + Back.LIGHTCYAN_EX + Fore.BLACK + "la opción deseada presiona ENTER o presiona el número correspondiente a la");
    print(Cursor.POS(35,12) + Back.LIGHTCYAN_EX + Fore.BLACK + "opción. Para regresar al menú presiona ESC");
    print(Cursor.POS(50,14) + Back.LIGHTRED_EX + Fore.BLACK + "1. EMPRESAS");
    print(Cursor.POS(50,15) + Back.LIGHTCYAN_EX + Fore.BLACK + "2. EMPLEADOS");
    print(Cursor.POS(50,16) + Back.LIGHTCYAN_EX + Fore.BLACK + "3. PRODUCTOS");
    print(Cursor.POS(43,29) + Back.LIGHTCYAN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
    while True:
        movimiento = ord(getch());
        if movimiento == 27:
            menu();
            break;
        elif movimiento == 13:
            if posicion == 1:
                bajasempresas();
                break;
            if posicion == 2:
                bajasempleados();
                break;
            if posicion == 3:
                bajasproductos();
                break;
        elif movimiento == 224:
            movimiento = ord(getch());
            if movimiento == 72:
                posicion=posicion-1;
                if posicion<1:
                    posicion=3;
            elif movimiento == 80:
                posicion=posicion+1;
                if(posicion>3):
                    posicion=1;
            if posicion == 1:
                print(Cursor.POS(50,14) + Back.LIGHTRED_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,15) + Back.LIGHTCYAN_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,16) + Back.LIGHTCYAN_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTCYAN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
            if posicion == 2:
                print(Cursor.POS(50,14) + Back.LIGHTCYAN_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,15) + Back.LIGHTRED_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,16) + Back.LIGHTCYAN_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTCYAN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
            if posicion == 3:
                print(Cursor.POS(50,14) + Back.LIGHTCYAN_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,15) + Back.LIGHTCYAN_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,16) + Back.LIGHTRED_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTCYAN_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));

def bajasempresas():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    cantidadempresas=0;
    y=0;
    empresasl=[];
    ventanas(80, 25, 20, 5, 8);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS EMPRESA");
    print(Cursor.POS(30,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "Presiona ENTER para dar de baja el elemento seleccionado o");
    print(Cursor.POS(41,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "ESC para regresar al menú de bajas");
    for i in empresas:
        empresasl.append(i);
        cantidadempresas+=1;
    if cantidadempresas == 1:
        print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS EMPRESA");
        print(Cursor.POS(30,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "No puedes dar de baja una EMPRESA ya que solo hay una, da");
        print(Cursor.POS(35,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "de alta o modifica la existente. Presiona ENTER");
        input();
        bajas();
    for i in range (cantidadempresas):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empresasl[i] + " : " + str (empresas[empresasl[i]]));
        else:
            print(Cursor.POS(21,y+10) + Back.LIGHTCYAN_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            bajas();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadempresas-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadempresas-1:
                    color=0;
            for i in range (cantidadempresas):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
                else:
                    print(Cursor.POS(21,y+10) + Back.LIGHTCYAN_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
                y+=1;
            y=0;
    ventanas(80, 25, 20, 5, 8);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS EMPRESA");
    print(Cursor.POS(21,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "Presiona ENTER para dar de baja o presiona ESC para regresar al menú");
    print(Cursor.POS(21,9) + Back.LIGHTCYAN_EX + Fore.BLACK + empresasl[color] + " : " + str(empresas[empresasl[color]]));
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            bajas();
            break;
    del empresas[empresasl[color]];
    archivo=open("d06-p11-equipo-03-T.txt", "wb");
    pickle.dump(empresas, archivo);
    pickle.dump(empleados, archivo);
    pickle.dump(productos, archivo);
    pickle.dump(precios, archivo);
    pickle.dump(piezas, archivo);
    pickle.dump(dineroencaja, archivo);
    archivo.close();
    print(Cursor.POS(21,16) + Back.LIGHTCYAN_EX + Fore.BLACK + "¡Se ha dado de baja! Presione ENTER para regresar al menú ");
    input();
    menu();

def bajasempleados():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    y=0;
    cantidadempleados=0;
    empleadosl=[];
    ventanas(80, 25, 20, 5, 8);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS EMPLEADO");
    print(Cursor.POS(30,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "Presiona ENTER para dar de baja el elemento seleccionado o");
    print(Cursor.POS(41,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "ESC para regresar al menú de bajas");
    for i in empleados:
        empleadosl.append(i);
        cantidadempleados+=1;
    if cantidadempleados == 1:
        print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS EMPLEADO");
        print(Cursor.POS(30,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "No puedes dar de baja un empleado ya que solo hay uno, da");
        print(Cursor.POS(35,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "de alta o modifica el existente. Presiona ENTER");
        input();
        bajas();
    for i in range (cantidadempleados):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
            print(Cursor.POS(21,y+11) + Back.LIGHTRED_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        else:
            print(Cursor.POS(21,y+10) + Back.LIGHTCYAN_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
            print(Cursor.POS(21,y+11) + Back.LIGHTCYAN_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        y+=2;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            bajas();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadempleados-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadempleados-1:
                    color=0;
            for i in range (cantidadempleados):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
                    print(Cursor.POS(21,y+11) + Back.LIGHTRED_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
                else:
                    print(Cursor.POS(21,y+10) + Back.LIGHTCYAN_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
                    print(Cursor.POS(21,y+11) + Back.LIGHTCYAN_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
                y+=2;
            y=0;
    ventanas(80, 25, 20, 5, 8);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS EMPLEADO");
    print(Cursor.POS(21,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "Presiona ENTER para dar de baja o presiona ESC para regresar al menú");
    print(Cursor.POS(21,9) + Back.LIGHTCYAN_EX + Fore.BLACK + empleadosl[color] + " : " + empleados[empleadosl[color]][0]);
    print(Cursor.POS(21,10) + Back.LIGHTCYAN_EX + Fore.BLACK + empleados[empleadosl[color]][1] + " " + empleados[empleadosl[color]][2] + " " + empleados[empleadosl[color]][3]);
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            bajas();
            break;
    del empleados[empleadosl[color]];
    archivo=open("d06-p11-equipo-03-T.txt", "wb");
    pickle.dump(empresas, archivo);
    pickle.dump(empleados, archivo);
    pickle.dump(productos, archivo);
    pickle.dump(precios, archivo);
    pickle.dump(piezas, archivo);
    pickle.dump(dineroencaja, archivo);
    archivo.close();
    print(Cursor.POS(21,19) + Back.LIGHTCYAN_EX + Fore.BLACK + "¡Se ha dado de baja! Presione ENTER para regresar al menú ");
    input();
    menu();

def bajasproductos():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    y=0;
    cantidadproductos=0;
    productosl=[];
    ventanas(80, 25, 20, 5, 8);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS PRODUCTO");
    print(Cursor.POS(30,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "Presiona ENTER para dar de baja el elemento seleccionado o");
    print(Cursor.POS(41,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "ESC para regresar al menú dede bajas");
    for i in productos:
        productosl.append(i);
        cantidadproductos+=1;
    if cantidadproductos == 1:
        print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS PRODUCTO");
        print(Cursor.POS(30,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "No puedes dar de baja un producto ya que solo hay uno, da");
        print(Cursor.POS(35,8) + Back.LIGHTCYAN_EX + Fore.BLACK + "de alta o modifica el existente. Presiona ENTER");
        input();
        bajas();
    for i in range (cantidadproductos):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        else:
            print(Cursor.POS(21,y+10) + Back.LIGHTCYAN_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            bajas();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadproductos-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadproductos-1:
                    color=0;
            for i in range (cantidadproductos):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
                else:
                    print(Cursor.POS(21,y+10) + Back.LIGHTCYAN_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
                y+=1;
            y=0;
    ventanas(80, 25, 20, 5, 8);
    print(Cursor.POS(50,6) + Back.YELLOW + Fore.BLACK + "BAJAS PRODUCTO");
    print(Cursor.POS(21,7) + Back.LIGHTCYAN_EX + Fore.BLACK + "Presiona ENTER para dar de baja o presiona ESC para regresar al menú");
    print(Cursor.POS(21,9) + Back.LIGHTCYAN_EX + Fore.BLACK + productosl[color] + " : " + str(productos[productosl[color]]));
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            bajas();
            break;
    del productos[productosl[color]];
    del precios[productosl[color]];
    del piezas[productosl[color]];
    archivo=open("d06-p11-equipo-03-T.txt", "wb");
    pickle.dump(empresas, archivo);
    pickle.dump(empleados, archivo);
    pickle.dump(productos, archivo);
    pickle.dump(precios, archivo);
    pickle.dump(piezas, archivo);
    pickle.dump(dineroencaja, archivo);
    archivo.close();
    print(Cursor.POS(21,17) + Back.LIGHTCYAN_EX + Fore.BLACK + "¡Se ha dado de baja! Presione ENTER para regresar al menú ");
    input();
    menu();

def ventas():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    import datetime;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    cantidadempresas=0;
    y=0;
    empresasl=[];
    fecha = datetime.datetime.now();
    ventanas(80, 25, 20, 5, 4);
    print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "VENTAS");
    print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "Para realizar una venta tienes que seleccionar la EMPRESA en la que trabajas");
    print(Cursor.POS(48,8) + Back.WHITE + Fore.BLACK + "y cuál empleado eres tú. ");
    print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Desplázate entre las opciones usando las flechas del teclado, para seleccionar");
    print(Cursor.POS(25,10) + Back.WHITE + Fore.BLACK + "la opción deseada presiona ENTER o para regresar al menú presiona ESC");
    for i in empresas:
        empresasl.append(i);
        cantidadempresas+=1;
    for i in range (cantidadempresas):
        if i == color:
            print(Cursor.POS(21,y+12) + Back.LIGHTRED_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
        else:
            print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            menu();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadempresas-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadempresas-1:
                    color=0;
            for i in range (cantidadempresas):
                if i == color:
                    print(Cursor.POS(21,y+12) + Back.LIGHTRED_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
                else:
                    print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
                y+=1;
            y=0;
    empresav=empresasl[color];
    color=0;
    y=0;
    cantidadempleados=0;
    empleadosl=[];
    ventanas(80, 25, 20, 5, 9);
    print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "VENTAS");
    print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "Para realizar una venta tienes que seleccionar la EMPRESA en la que trabajas");
    print(Cursor.POS(48,8) + Back.WHITE + Fore.BLACK + "y cuál empleado eres tú. ");
    print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Desplázate entre las opciones usando las flechas del teclado, para seleccionar");
    print(Cursor.POS(25,10) + Back.WHITE + Fore.BLACK + "la opción deseada presiona ENTER o para regresar al menú presiona ESC");
    for i in empleados:
        empleadosl.append(i);
        cantidadempleados+=1;
    for i in range (cantidadempleados):
        if i == color:
            print(Cursor.POS(21,y+12) + Back.LIGHTRED_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
            print(Cursor.POS(21,y+13) + Back.LIGHTRED_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        else:
            print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
            print(Cursor.POS(21,y+13) + Back.WHITE + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        y+=2;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            menu();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadempleados-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadempleados-1:
                    color=0;
            for i in range (cantidadempleados):
                if i == color:
                    print(Cursor.POS(21,y+12) + Back.LIGHTRED_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
                    print(Cursor.POS(21,y+13) + Back.LIGHTRED_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
                else:
                    print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
                    print(Cursor.POS(21,y+13) + Back.WHITE + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
                y+=2;
            y=0;
    empleadov=empleadosl[color];
    color=0;
    y=0;
    cantidadproductos=0;
    productosl=[];
    total=0;
    ventasr={};
    ventanas(80, 25, 20, 5, 9);
    print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "VENTAS");
    print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "Presiona ENTER para añadir el producto seleccionado a la lista de ventas o");
    print(Cursor.POS(21,8) + Back.WHITE + Fore.BLACK + "presiona 1 para dejar de añadir productos. Para cancelar la venta pulsa ESC");
    for i in productos:
        productosl.append(i);
        cantidadproductos+=1;
    for i in range (cantidadproductos):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        else:
            print(Cursor.POS(21,y+10) + Back.WHITE + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            piezas[productosl[color]] -= 1;
            if piezas[productosl[color]] < 0:
                piezas[productosl[color]] = 0;
                print(Cursor.POS(21,28) + Back.WHITE + Fore.BLACK + "Ya no puedes añadir este producto porque no hay más en inventario.");
                input(Cursor.POS(21,29) + Back.WHITE + Fore.BLACK + "Presione ENTER para seguir comprando otros productos");
                print(Cursor.POS(21,28) + Back.WHITE + Fore.BLACK + "                                                                  ");
                print(Cursor.POS(21,29) + Back.WHITE + Fore.BLACK + "                                                                  ");
            else:
                total+=precios[productosl[color]];
                if productos[productosl[color]][0] in ventasr:
                    ventasr[productos[productosl[color]][0]][0]+=1;
                else:
                    ventasr[productos[productosl[color]][0]]=[1, productosl[color], productos[productosl[color]][1]];
                productos[productosl[color]]=[productos[productosl[color]][0], productos[productosl[color]][1], "Pieza(s): " + str(piezas[productosl[color]])];

        elif flecha == 49:
            break;
        elif flecha == 27:
            menu();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadproductos-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadproductos-1:
                    color=0;
            for i in range (cantidadproductos):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
                else:
                    print(Cursor.POS(21,y+10) + Back.WHITE + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
                y+=1;
            y=0;
    ventanas(80, 25, 20, 5, 9);
    print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "FACTURA");
    print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "EMPRESA:");
    print(Cursor.POS(21,8) + Back.WHITE + Fore.BLACK + empresav + " : " + str(empresas[empresav]));
    print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Atendido por:" + empleados[empleadov][0]);
    print(Cursor.POS(21,10) + Back.WHITE + Fore.BLACK + "Cantidad | Producto | ID");

    for i in ventasr:
        print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + str(ventasr[i][0]) + "  " + i + "  " + ventasr[i][1] + "  " + ventasr[i][2]);
        y+=1;
    y=0;

    print(Cursor.POS(77,25) + Back.WHITE + Fore.BLACK + "Total: $" + str(total));
    print(Cursor.POS(20,26) + Back.WHITE + Fore.BLACK + "Si Desea editar alguna cantidad, presione 1.                        ");
    print(Cursor.POS(20,27) + Back.WHITE + Fore.BLACK + "Si Desea continuar con la venta presione Enter. Para volver presione esc");
    while True:
        decision = ord(getch());
        if decision == 49:
            color=0;
            ventasrl=[];
            cantidadventasr=0;
            print(Cursor.POS(20,26) + Back.WHITE + Fore.BLACK + "                                            ");
            print(Cursor.POS(20,27) + Back.WHITE + Fore.BLACK + "                                                                        ");
            print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "FACTURA");
            print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "EMPRESA:");
            print(Cursor.POS(21,8) + Back.WHITE + Fore.BLACK + empresav + " : " + str(empresas[empresav]));
            print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Presione ENTER para seleccionar el producto a editar. Presione esc para volver.");
            print(Cursor.POS(21,10) + Back.WHITE + Fore.BLACK + "Cantidad | Producto | ID");
            for i in ventasr:
                ventasrl.append(i);
                cantidadventasr+=1;
            for i in range (cantidadventasr):
                if i == color:
                    print(Cursor.POS(21,y+12) + Back.LIGHTRED_EX + Fore.BLACK + str(ventasr[ventasrl[i]][0]) + "  " + ventasrl[i] + "  " + ventasr[ventasrl[i]][1] + "  " + ventasr[ventasrl[i]][2]);
                    y+=1;

                else:
                    print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + str(ventasr[ventasrl[i]][0]) + "  " + ventasrl[i] + "  " + ventasr[ventasrl[i]][1] + "  " + ventasr[ventasrl[i]][2]);
                    y+=1;
            y=0;
            while True:
                flecha = ord(getch());
                if flecha == 13:
                    while True:
                        print(Cursor.POS(20,26) + Back.WHITE + Fore.BLACK + "                                             ");
                        print(Cursor.POS(20,27) + Back.WHITE + Fore.BLACK + "                                                                   ");
                        try:
                            print(Cursor.POS(30,y+24) + Back.WHITE + "                                                                      ");
                            backupc=ventasr[ventasrl[color]][0];
                            cantidadn=int(input(Cursor.POS(21,y+24) + Back.WHITE + Fore.BLACK + "Ingrese la nueva cantidad de " + ventasrl[color] + " a comprar: "))
                            if cantidadn < 0:
                                print(Cursor.POS(21,y+25) + Back.WHITE + Fore.BLACK + "Ingrese una cantidad válida:                                 ");
                            else:
                                piezas[ventasr[ventasrl[color]][1]] += ventasr[ventasrl[color]][0];
                                piezas[ventasr[ventasrl[color]][1]] -= cantidadn;
                                if piezas[ventasr[ventasrl[color]][1]] < 0:
                                    piezas[ventasr[ventasrl[color]][1]] = 0;
                                    cantidadn=backupc;
                                    print(Cursor.POS(21,y+26) + Back.WHITE + Fore.BLACK + "Ya no puedes añadir este producto porque no hay más en inventario.");
                                    input(Cursor.POS(21,y+27) + Back.WHITE + Fore.BLACK + "Presione ENTER para seguir comprando otros productos         ");
                                    print(Cursor.POS(21,28) + Back.WHITE + Fore.BLACK + "                                                                  ");
                                    print(Cursor.POS(21,29) + Back.WHITE + Fore.BLACK + "                                                                  ");
                                productos[ventasr[ventasrl[color]][1]]=[ventasrl[color], ventasr[ventasrl[color]][2], "Pieza(s): " + str(piezas[ventasr[ventasrl[color]][1]])];
                                ventasr[ventasrl[color]]=[cantidadn, ventasr[ventasrl[color]][1], ventasr[ventasrl[color]][2]];
                                break;
                        except:
                            print(Cursor.POS(21,y+12+25) + Back.WHITE + Fore.BLACK + "Ingrese una cantidad válida:                                 ");
                    break;
                elif flecha == 27:
                    break;
                elif flecha == 224:
                    flecha = ord(getch());
                    if flecha == 72:
                        color-=1;
                        if color<0:
                            color=cantidadventasr-1;
                    elif flecha == 80:
                        color+=1;
                        if color > cantidadventasr-1:
                            color=0;
                    for i in range (cantidadventasr):
                        if i == color:
                            print(Cursor.POS(21,y+12) + Back.LIGHTRED_EX + Fore.BLACK + str(ventasr[ventasrl[i]][0]) + "  " + ventasrl[i] + "  " + ventasr[ventasrl[i]][1] + "  " + ventasr[ventasrl[i]][2]);
                            y+=1;

                        else:
                            print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + str(ventasr[ventasrl[i]][0]) + "  " + ventasrl[i] + "  " + ventasr[ventasrl[i]][1] + "  " + ventasr[ventasrl[i]][2]);
                            y+=1;
                    y=0;


            print(Cursor.POS(55,6) + Back.YELLOW + Fore.BLACK + "FACTURA");
            print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "EMPRESA:");
            print(Cursor.POS(21,8) + Back.WHITE + Fore.BLACK + empresav + " : " + str(empresas[empresav]));
            print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Atendido por:" + empleados[empleadov][0]);
            print(Cursor.POS(21,10) + Back.WHITE + Fore.BLACK + "Cantidad | Producto | ID");
            total = 0;
            for i in ventasr:
                total += ventasr[i][0] * float(precios[ventasr[i][1]]);
                print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + str(ventasr[i][0]) + "  " + i + "  " + ventasr[i][1] + "  " + ventasr[i][2]);
                y+=1;
            y=0
            print(Cursor.POS(77,25) + Back.WHITE + Fore.BLACK + "Total: $" + str(total));
            print(Cursor.POS(20,26) + Back.WHITE + Fore.BLACK + "Si Desea editar alguna cantidad, presione 1.                      ");
            print(Cursor.POS(20,27) + Back.WHITE + Fore.BLACK + "Si Desea continuar con la venta presione Enter. Para volver presione esc");

        elif decision == 27:
            menu();

        elif decision == 13:
            ventanasfactura(80, 25, 20, 5);
            print(Cursor.POS(55,6) + Back.WHITE + Fore.BLACK + "FACTURA");
            print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "EMPRESA:");
            print(Cursor.POS(21,8) + Back.WHITE + Fore.BLACK + empresav + " : " + str(empresas[empresav]));
            print(fecha.strftime(Cursor.POS(80,6) + Back.WHITE + Fore.BLACK + "Fecha = %d/%m/20%y"));
            print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Atendido por: " + empleados[empleadov][0] + " ID: " + str(empleadov));
            butotal = total
            while True:

                try:
                    print(Cursor.POS(21,11) + Back.WHITE + "                                                        ");
                    pago=float(input(Cursor.POS(21,11) + Back.WHITE + Fore.BLACK + "Ingrese el pago del cliente: $"));
                    if pago < 0 or (pago - total) <0:
                        print(Cursor.POS(21,12) + Back.WHITE + Fore.BLACK + "El monto pagado no es válido: Ingrese un monto válido");
                    else:
                        print(Cursor.POS(21,12) + Back.WHITE + "                                                     ");
                        break;
                except:
                    print(Cursor.POS(21,12) + Back.WHITE + Fore.BLACK + "El monto pagado no es válido: Ingrese un monto válido");

            cambio = pago - total;
            if (dineroencaja - cambio) < 0:
                print(Cursor.POS(21,10) + Back.WHITE + Fore.BLACK + "Su dinero en caja es de $%.4f " %dineroencaja + "y el cambio es de $%.4f                  " %cambio);
                while True:
                    try:
                        print(Cursor.POS(73,11) + Back.WHITE + "          ");
                        dineroencaja += float(input(Cursor.POS(21,11) + Back.WHITE + Fore.BLACK + "No tiene suficiente dinero en caja. Ingrese dinero: $"));
                        if (dineroencaja - cambio) < 0:
                            print(Cursor.POS(21,10) + Back.WHITE + Fore.BLACK + "Su dinero en caja es de $%.4f " %dineroencaja + "y el cambio es de $%.4f                  " %cambio);
                        else:
                            print(Cursor.POS(21,10) + Back.WHITE + Fore.BLACK + "Su dinero en caja es de $%.4f " %dineroencaja + "y el cambio es de $%.4f                  " %cambio);
                            break;
                    except:
                        print(Cursor.POS(21,11) + Back.WHITE + Fore.BLACK + "                                                     ");

            break;

    print(Cursor.POS(21,12) + Back.WHITE + Fore.BLACK + "                                                       ");
    print(Cursor.POS(55,6) + Back.WHITE + Fore.BLACK + "FACTURA");
    print(Cursor.POS(21,7) + Back.WHITE + Fore.BLACK + "EMPRESA:");
    print(Cursor.POS(21,8) + Back.WHITE + Fore.BLACK + empresav + " : " + str(empresas[empresav]));
    print(Cursor.POS(21,9) + Back.WHITE + Fore.BLACK + "Atendido por: " + empleados[empleadov][0] + " ID: " + str(empleadov));
    cambio = pago - butotal;
    dineroencaja += butotal;
    for i in ventasr:
        total += ventasr[i][0] * float(precios[ventasr[i][1]]);
        print(Cursor.POS(21,y+12) + Back.WHITE + Fore.BLACK + str(ventasr[i][0]) + "  " + i + "  " + ventasr[i][1] + "  " + ventasr[i][2]);
        y+=1;
    print(Cursor.POS(70,24) + Back.WHITE + Fore.BLACK + "Monto Total: $%.2f" %butotal);
    print(Cursor.POS(70,25) + Back.WHITE + Fore.BLACK + "Monto Pagado: $%.2f" %pago);
    print(Cursor.POS(70,26) + Back.WHITE + Fore.BLACK + "Cambio: $%.4f" %cambio);
    input(Cursor.POS(33,28) + Back.WHITE + Fore.BLACK + "¡Gracias por su compra! Presione ENTER para continuar.");
    print(Back.BLACK + "");
    archivo=open("d06-p11-equipo-03-T.txt", "wb");
    pickle.dump(empresas, archivo);
    pickle.dump(empleados, archivo);
    pickle.dump(productos, archivo);
    pickle.dump(precios, archivo);
    pickle.dump(piezas, archivo);
    pickle.dump(dineroencaja, archivo);
    archivo.close();
    menu();

def inventario():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    ventanas(80, 25, 20, 5, 5);
    posicion=1;
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "En esta parte del programa podrás ver y manipular los datos de los diferentes");
    print(Cursor.POS(47,7) + Back.LIGHTYELLOW_EX + Fore.BLACK + "elementos de la frutería.");
    print(Cursor.POS(21,9) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Desplázate entre las opciones usando las flechas del teclado, para seleccionar");
    print(Cursor.POS(23,10) + Back.LIGHTYELLOW_EX + Fore.BLACK + "la opción deseada presiona ENTER o presiona el número correspondiente a la");
    print(Cursor.POS(35,11) + Back.LIGHTYELLOW_EX + Fore.BLACK + "opción. Para regresar al menú presiona ESC");
    print(Cursor.POS(50,13) + Back.LIGHTRED_EX + Fore.BLACK + "1. EMPRESAS");
    print(Cursor.POS(50,14) + Back.LIGHTYELLOW_EX + Fore.BLACK + "2. EMPLEADOS");
    print(Cursor.POS(50,15) + Back.LIGHTYELLOW_EX + Fore.BLACK + "3. PRODUCTOS");
    print(Cursor.POS(43,29) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
    while True:
        movimiento = ord(getch());
        if movimiento == 27:
            menu();
            break;
        elif movimiento == 13:
            if posicion == 1:
                invempresas();
                break;
            if posicion == 2:
                invempleados();
                break;
            if posicion == 3:
                invproductos();
                break;
        elif movimiento == 224:
            movimiento = ord(getch());
            if movimiento == 72:
                posicion=posicion-1;
                if posicion<1:
                    posicion=3;
            elif movimiento == 80:
                posicion=posicion+1;
                if(posicion>3):
                    posicion=1;
            if posicion == 1:
                print(Cursor.POS(50,13) + Back.LIGHTRED_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,14) + Back.LIGHTYELLOW_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,15) + Back.LIGHTYELLOW_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
            if posicion == 2:
                print(Cursor.POS(50,13) + Back.LIGHTYELLOW_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,14) + Back.LIGHTRED_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,15) + Back.LIGHTYELLOW_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));
            if posicion == 3:
                print(Cursor.POS(50,13) + Back.LIGHTYELLOW_EX + Fore.BLACK + "1. EMPRESAS");
                print(Cursor.POS(50,14) + Back.LIGHTYELLOW_EX + Fore.BLACK + "2. EMPLEADOS");
                print(Cursor.POS(50,15) + Back.LIGHTRED_EX + Fore.BLACK + "3. PRODUCTOS");
                print(Cursor.POS(43,29) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(posicion));

def invempresas():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    cantidadempresas=0;
    y=0;
    empresasl=[];
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Presiona ENTER para modificar algún dato del elemento seleccionado o presiona");
    print(Cursor.POS(41,7) + Back.LIGHTYELLOW_EX + Fore.BLACK + "ESC para regresar al menú del inventario");
    for i in empresas:
        empresasl.append(i);
        cantidadempresas+=1;
    for i in range (cantidadempresas):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
        else:
            print(Cursor.POS(21,y+10) + Back.LIGHTYELLOW_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            inventario();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadempresas-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadempresas-1:
                    color=0;
            for i in range (cantidadempresas):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
                else:
                    print(Cursor.POS(21,y+10) + Back.LIGHTYELLOW_EX + Fore.BLACK + empresasl[i] + " : " + str(empresas[empresasl[i]]));
                y+=1;
            y=0;
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Presiona ENTER para confirmar y modificar o presiona ESC para regresar al menú");
    print(Cursor.POS(21,8) + Back.LIGHTYELLOW_EX + Fore.BLACK + empresasl[color] + " : " + str(empresas[empresasl[color]]));
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            inventario();
            break;
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(48,6) + Back.YELLOW + Fore.BLACK + "INVENTARIO EMPRESA");
    print(Cursor.POS(21,8) + Back.LIGHTYELLOW_EX + Fore.BLACK + empresasl[color] + " : " + str(empresas[empresasl[color]]));
    telefono=str(input(Cursor.POS(21,10) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo número de teléfono -> "));
    telefonoc="Número Tel: "+telefono;
    correo=str(input(Cursor.POS(21,11) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo correo -> "));
    correoc="Correo: "+correo;
    print(Cursor.POS(21,13) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Está seguro que desea guardar los cambios?");
    print(Cursor.POS(21,14) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Sí guardar(Presione ENTER)      No guardar y volver al menú(ESC)");
    while True:
        decision = getch();

        if decision == b'\r':
            empresas[empresasl[color]]=[telefonoc, correoc];
            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            print(Cursor.POS(21,16) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¡Cambios Guardados! Presione ENTER para regresar al menú ");
            input();
            menu();
            break;

        elif decision == b'\x1b':
            menu();
            break;

def invempleados():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    y=0;
    cantidadempleados=0;
    empleadosl=[];
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Presiona ENTER para modificar algún dato del elemento seleccionado o presiona");
    print(Cursor.POS(41,7) + Back.LIGHTYELLOW_EX + Fore.BLACK + "ESC para regresar al menú del inventario");
    for i in empleados:
        empleadosl.append(i);
        cantidadempleados+=1;
    for i in range (cantidadempleados):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
            print(Cursor.POS(21,y+11) + Back.LIGHTRED_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        else:
            print(Cursor.POS(21,y+10) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
            print(Cursor.POS(21,y+11) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
        y+=2;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            inventario();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadempleados-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadempleados-1:
                    color=0;
            for i in range (cantidadempleados):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
                    print(Cursor.POS(21,y+11) + Back.LIGHTRED_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
                else:
                    print(Cursor.POS(21,y+10) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleadosl[i] + " : " + empleados[empleadosl[i]][0]);
                    print(Cursor.POS(21,y+11) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleados[empleadosl[i]][1] + " " + empleados[empleadosl[i]][2] + " " + empleados[empleadosl[i]][3]);
                y+=2;
            y=0;
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Presiona ENTER para confirmar y modificar o presiona ESC para regresar al menú");
    print(Cursor.POS(21,8) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleadosl[color] + " : " + empleados[empleadosl[color]][0]);
    print(Cursor.POS(21,9) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleados[empleadosl[color]][1] + " " + empleados[empleadosl[color]][2] + " " + empleados[empleadosl[color]][3]);
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            inventario();
            break;
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(48,6) + Back.YELLOW + Fore.BLACK + "INVENTARIO EMPLEADO");
    print(Cursor.POS(21,8) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleadosl[color] + " : " + empleados[empleadosl[color]][0]);
    print(Cursor.POS(21,9) + Back.LIGHTYELLOW_EX + Fore.BLACK + empleados[empleadosl[color]][1] + " " + empleados[empleadosl[color]][2] + " " + empleados[empleadosl[color]][3]);
    nombre=str(input(Cursor.POS(21,11) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo nombre -> "));
    telefono=str(input(Cursor.POS(21,12) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo número de teléfono -> "));
    telefonoc="Número Tel: "+telefono;
    correo=str(input(Cursor.POS(21,13) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo correo -> "));
    correoc="Correo: "+correo;
    salario=str(input(Cursor.POS(21,14) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo salario -> "));
    salarioc="Salario: $"+salario;
    print(Cursor.POS(21,16) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Está seguro que desea guardar los cambios?");
    print(Cursor.POS(21,17) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Sí guardar(Presione ENTER)      No guardar y volver al menú(ESC)");
    while True:
        decision = getch();

        if decision == b'\r':
            empleados[empleadosl[color]]=[nombre, telefonoc, correoc, salarioc];
            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            print(Cursor.POS(21,19) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¡Cambios Guardados! Presione ENTER para regresar al menú ");
            input();
            menu();
            break;

        elif decision == b'\x1b':
            menu();
            break;

def invproductos():
    import pickle;
    from msvcrt import getch;
    from colorama import Cursor, init, Fore, Back;
    init(autoreset=True);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    color=0;
    y=0;
    cantidadproductos=0;
    productosl=[];
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Presiona ENTER para modificar algún dato del elemento seleccionado o presiona");
    print(Cursor.POS(41,7) + Back.LIGHTYELLOW_EX + Fore.BLACK + "ESC para regresar al menú del inventario");
    for i in productos:
        productosl.append(i);
        cantidadproductos+=1;
    for i in range (cantidadproductos):
        if i == color:
            print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        else:
            print(Cursor.POS(21,y+10) + Back.LIGHTYELLOW_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
        y+=1;
    y=0;
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            inventario();
            break;
        elif flecha == 224:
            flecha = ord(getch());
            if flecha == 72:
                color-=1;
                if color<0:
                    color=cantidadproductos-1;
            elif flecha == 80:
                color+=1;
                if color>cantidadproductos-1:
                    color=0;
            for i in range (cantidadproductos):
                if i == color:
                    print(Cursor.POS(21,y+10) + Back.LIGHTRED_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
                else:
                    print(Cursor.POS(21,y+10) + Back.LIGHTYELLOW_EX + Fore.BLACK + productosl[i] + " : " + str(productos[productosl[i]]));
                y+=1;
            y=0;
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(21,6) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Presiona ENTER para confirmar y modificar o presiona ESC para regresar al menú");
    print(Cursor.POS(21,8) + Back.LIGHTYELLOW_EX + Fore.BLACK + productosl[color] + " : " + str(productos[productosl[color]]));
    while True:
        flecha = ord(getch());
        if flecha == 13:
            break;
        elif flecha == 27:
            inventario();
            break;
    ventanas(80, 25, 20, 5, 10);
    print(Cursor.POS(48,6) + Back.YELLOW + Fore.BLACK + "INVENTARIO PRODUCTO");
    print(Cursor.POS(21,8) + Back.LIGHTYELLOW_EX + Fore.BLACK + productosl[color] + " : " + str(productos[productosl[color]]));
    try:
        nombre=str(input(Cursor.POS(21,10) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo nombre -> "));
        precio=float(input(Cursor.POS(21,11) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el nuevo precio -> "));
        precioc="Precio: $"+str(precio);
        pieza=int(input(Cursor.POS(21,12) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Ingresa el número de piezas disponibles -> "));
        piezac="Pieza(s): "+str(pieza);
    except:
        print(Cursor.POS(21,17) + Back.LIGHTYELLOW_EX + Fore.BLACK + "No ingresaste un número... Presiona ENTER para regresar");
        input();
        invproductos();
    print(Cursor.POS(21,14) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¿Está seguro que desea guardar los cambios?");
    print(Cursor.POS(21,15) + Back.LIGHTYELLOW_EX + Fore.BLACK + "Sí guardar(Presione ENTER)      No guardar y volver al menú(ESC)");
    while True:
        decision = getch();

        if decision == b'\r':
            productos[productosl[color]]=[nombre, precioc, piezac];
            precios[productosl[color]]=precio;
            piezas[productosl[color]]=pieza;
            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            print(Cursor.POS(21,17) + Back.LIGHTYELLOW_EX + Fore.BLACK + "¡Cambios Guardados! Presione ENTER para regresar al menú ");
            input();
            menu();
            break;

        elif decision == b'\x1b':
            menu();
            break;

def ecaja():
    from msvcrt import getch;
    import pickle;
    from colorama import Cursor, Back, init, Fore;
    init(autoreset=True);
    ventanas(80, 25, 20, 5, 1);
    archivo=open("d06-p11-equipo-03-T.txt", "rb");
    empresas=pickle.load(archivo);
    empleados=pickle.load(archivo);
    productos=pickle.load(archivo);
    precios=pickle.load(archivo);
    piezas=pickle.load(archivo);
    dineroencaja=pickle.load(archivo);
    archivo.close();
    print(Cursor.POS(20,5)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Práctica 11 (Examen)");
    print(Cursor.POS(20,6)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Sección: D06");
    print(Cursor.POS(20,7)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Equipo 3:");
    print(Cursor.POS(45,7) + Back.LIGHTBLUE_EX + Fore.BLACK + "EMPRESAS DE ORIENTE A OCCIDENTE.");
    print(Cursor.POS(48,9) + Back.LIGHTBLUE_EX + Fore.BLACK + "Dinero en caja actual: $%.2f" %dineroencaja);
    print(Cursor.POS(22,10) + Back.LIGHTBLUE_EX + Fore.BLACK + "Presiona ENTER para realizar una modificación o ESC para regresar al menú");
    while True:
        flecha = ord(getch());
        if flecha == 13:
            while True:
                try:
                    print(Cursor.POS(22,11) + Back.LIGHTBLUE_EX +  "                                                                ");
                    dineroencaja = float(input(Cursor.POS(45,11) + Back.LIGHTBLUE_EX + Fore.BLACK + "Ingrese el nuevo monto en caja: $"));
                    if dineroencaja < 0:
                        print(Cursor.POS(20,10) + Back.LIGHTBLUE_EX +  "                                                                            ");
                        print(Cursor.POS(50,10) + Back.LIGHTBLUE_EX + Fore.BLACK + "Ingrese un número válido.");
                        print(Cursor.POS(22,11) + Back.LIGHTBLUE_EX +  "                                                                ");
                        dineroencaja = float(input(Cursor.POS(45,11) + Back.LIGHTBLUE_EX + Fore.BLACK + "Ingrese el nuevo monto en caja: $"));
                    break;
                except:
                    print(Cursor.POS(20,10) + Back.LIGHTBLUE_EX +  "                                                                            ");
                    print(Cursor.POS(50,10) + Back.LIGHTBLUE_EX + Fore.BLACK + "Ingrese un número válido.");

            archivo=open("d06-p11-equipo-03-T.txt", "wb");
            pickle.dump(empresas, archivo);
            pickle.dump(empleados, archivo);
            pickle.dump(productos, archivo);
            pickle.dump(precios, archivo);
            pickle.dump(piezas, archivo);
            pickle.dump(dineroencaja, archivo);
            archivo.close();
            break;
        elif flecha == 27:
            break;

def menu():
    import pickle;
    from msvcrt import getch;
    opcion = 0;
    ventanas(80, 25, 20, 5, 1);
    y = 6;
    def movmenu():
        from colorama import Cursor, init, Fore, Back;
        init(autoreset=True);
        nonlocal opcion, y;
        def presentacionmenu(x):
            import pickle;
            archivo=open("d06-p11-equipo-03-T.txt", "rb");
            empresas=pickle.load(archivo);
            empleados=pickle.load(archivo);
            productos=pickle.load(archivo);
            precios=pickle.load(archivo);
            piezas=pickle.load(archivo);
            dineroencaja=pickle.load(archivo);
            archivo.close();
            print(Cursor.POS(20,5)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Práctica 11 (Examen)");
            print(Cursor.POS(20,6)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Sección: D06");
            print(Cursor.POS(20,7)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Equipo 3:");
            print(Cursor.POS(45,7) + Back.LIGHTBLUE_EX + Fore.BLACK + "EMPRESAS DE ORIENTE A OCCIDENTE.");
            print(Cursor.POS(75,5) + Back.LIGHTBLUE_EX + Fore.BLACK + "Dinero en caja: $%.2f" %dineroencaja);
            print(Cursor.POS(21,9) + Back.LIGHTBLUE_EX + Fore.BLACK + "Desplázate entre las opciones usando las flechas del teclado, para seleccionar");
            print(Cursor.POS(23,10) + Back.LIGHTBLUE_EX + Fore.BLACK + "la opción deseada presiona ENTER o presiona el número correspondiente a la");
            print(Cursor.POS(35,11) + Back.LIGHTBLUE_EX + Fore.BLACK + "opción. Para editar el dinero en caja presione E.");
            print(Cursor.POS(20,25)+ Back.LIGHTBLUE_EX + Fore.BLACK +"López Núñez Sergio Jair");
            print(Cursor.POS(20,26)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Macías Ramírez José Luis");
            print(Cursor.POS(20,27)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Macías Ramírez Omar Ulises");
            print(Cursor.POS(20,28)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Magaña Corona Josué Gael");
            print(Cursor.POS(20,29)+ Back.LIGHTBLUE_EX + Fore.BLACK +"Maldonado Meléndez Diego Alberto");
            print(Cursor.POS(45,20) + Back.LIGHTBLUE_EX + Fore.BLACK + "¿Que Acción desea realizar? [%d]" %(x+1));

        for i in range(5):
            if i == opcion:
                print(Cursor.POS(54,y+7) + Back.LIGHTRED_EX + Fore.BLACK + "             <<<");
                if opcion == 0:
                    presentacionmenu(opcion);
                    print(Cursor.POS(50,13) + Back.LIGHTRED_EX + Fore.BLACK + "1.- ALTAS");
                    print(Cursor.POS(50,14) + Back.LIGHTBLUE_EX + Fore.BLACK + "2.- BAJAS                ");
                    print(Cursor.POS(50,15) + Back.LIGHTBLUE_EX + Fore.BLACK + "3.- VENTAS                ");
                    print(Cursor.POS(50,16) + Back.LIGHTBLUE_EX + Fore.BLACK + "4.- EDITAR                ");
                    print(Cursor.POS(50,17) + Back.LIGHTBLUE_EX + Fore.BLACK + "5.- SALIR                ");

                elif opcion == 1:
                    presentacionmenu(opcion);
                    print(Cursor.POS(50,13) + Back.LIGHTBLUE_EX + Fore.BLACK + "1.- ALTAS                ");
                    print(Cursor.POS(50,14) + Back.LIGHTRED_EX + Fore.BLACK + "2.- BAJAS");
                    print(Cursor.POS(50,15) + Back.LIGHTBLUE_EX + Fore.BLACK + "3.- VENTAS                ");
                    print(Cursor.POS(50,16) + Back.LIGHTBLUE_EX + Fore.BLACK + "4.- EDITAR                ");
                    print(Cursor.POS(50,17) + Back.LIGHTBLUE_EX + Fore.BLACK + "5.- SALIR                ");

                elif opcion == 2:
                    presentacionmenu(opcion);
                    print(Cursor.POS(50,13) + Back.LIGHTBLUE_EX + Fore.BLACK + "1.- ALTAS                ");
                    print(Cursor.POS(50,14) + Back.LIGHTBLUE_EX + Fore.BLACK + "2.- BAJAS                ");
                    print(Cursor.POS(50,15) + Back.LIGHTRED_EX + Fore.BLACK + "3.- VENTAS");
                    print(Cursor.POS(50,16) + Back.LIGHTBLUE_EX + Fore.BLACK + "4.- EDITAR                ");
                    print(Cursor.POS(50,17) + Back.LIGHTBLUE_EX + Fore.BLACK + "5.- SALIR                ");

                elif opcion == 3:
                    presentacionmenu(opcion);
                    print(Cursor.POS(50,13) + Back.LIGHTBLUE_EX + Fore.BLACK + "1.- ALTAS                ");
                    print(Cursor.POS(50,14) + Back.LIGHTBLUE_EX + Fore.BLACK + "2.- BAJAS                ");
                    print(Cursor.POS(50,15) + Back.LIGHTBLUE_EX + Fore.BLACK + "3.- VENTAS                ");
                    print(Cursor.POS(50,16) + Back.LIGHTRED_EX + Fore.BLACK + "4.- EDITAR");
                    print(Cursor.POS(50,17) + Back.LIGHTBLUE_EX + Fore.BLACK + "5.- SALIR                ");

                elif opcion == 4:
                    presentacionmenu(opcion);
                    print(Cursor.POS(50,13) + Back.LIGHTBLUE_EX + Fore.BLACK + "1.- ALTAS                ");
                    print(Cursor.POS(50,14) + Back.LIGHTBLUE_EX + Fore.BLACK + "2.- BAJAS                ");
                    print(Cursor.POS(50,15) + Back.LIGHTBLUE_EX + Fore.BLACK + "3.- VENTAS                ");
                    print(Cursor.POS(50,16) + Back.LIGHTBLUE_EX + Fore.BLACK + "4.- EDITAR                ");
                    print(Cursor.POS(50,17) + Back.LIGHTRED_EX + Fore.BLACK + "5.- SALIR");

    movmenu();
    while True:

        movimiento = ord(getch());

        if movimiento == 224:
            movimiento = ord(getch());

            if movimiento == 72:#Arriba
                opcion -= 1;
                y -= 1;

            elif movimiento == 80:#Abajo
                opcion += 1;
                y += 1;

        elif movimiento == 13:#Si presiona Enter
            if opcion == 0:
                altas();
                break;

            elif opcion == 1:
                bajas();
                break;

            elif opcion == 2:
                ventas();
                break;

            elif opcion == 3:
                inventario();
                break;

            elif opcion == 4:
                ventanas(80, 25, 20, 5, 6);
                exit();

        elif movimiento == 101:
            ecaja();

        if opcion > 4:
            opcion = 0;
            y=6;

        elif opcion < 0:
            opcion = 4;
            y = 10;


        movmenu();
menu();
