import os                       #comandos nativos del sistema
import json                     #formato de los archivos

# Diccionario con los datos requeridos
# requisitos de la plantilla y valores orientativos

class Wololo:
    def __init__(self) -> None:
        print('Generando objeto cli wizard')
        self.main_wizard()
    
    def main_wizard(self):
        plantilla = {
            "nombre": "",                                # Longitud 3 / 30 (inclusivos)
            "modelo": "",                                # Longitud 3 / 30 (inclusivos)
            "fabricante": "",                            # Longitud 3 / 15 (inclusivos), campo vacío válido
            "cantidad": 0,                               # Int 1 / 999 (inclusivos)
            "cantidadAviso": 0,                          # Int 1 / 999 (inclusivos)
            "cantidadMaxima": 0,                         # Int 1 / 999 (inclusivos)
            "datasheet": "",                             # Longitud 3 / 100, campo vacío válido
            "notas": "",                                 # Longitud de 5 / 400 (inclusivos)
            "localizacion": 0                            # Longitud de 1 / 99
        }

        datos_por_guardar = []

        # Validar la longitud del Input STR (solicita (nombre del campo)+longitud minima+longitud maxima)
        # valor  de la clave a de esta comprendido entre los valores especificos que se daran mas abajo
        # preguntar a juan si quedaria mas limpio con un For en lugar de un while true, asi podria manejar los errores de manera mas especifica y no solo en verdad o falso
        def validar_str(campo, longitud_min, longitud_max):
            while True:
                valor = input(f"Ingrese {campo} ({longitud_min}-{longitud_max} caracteres): ")
                if longitud_min <= len(valor) <= longitud_max:
                    return valor
                else:
                    print(f"Error: La longitud de {campo} debe estar entre {longitud_min} y {longitud_max} caracteres.")

        # Validar el rango del Input INT (solicita (nombre del campo)+longitud minima+longitud maxima)
        # repetir longitud recordar cambiar valores. No seas idiotra... otra vez.
        def validar_int(campo, rango_min, rango_max):
            while True:
                try:
                    valor = int(input(f"Ingrese {campo} ({rango_min}-{rango_max}): "))
                    if rango_min <= valor <= rango_max:
                        return valor
                    else:
                        print(f"Error: {campo} debe estar entre {rango_min} y {rango_max}.")
                except ValueError:
                    print(f"Error: {campo} debe ser un número entero.")

        # Solicitar la carpeta de destino al usuario (maneja donde se almacenan los datos)
        #esto va primero aunque sea la suma de los archivos incompletos (funciona por dependencia)
        carpeta_destino = input("Ingrese la ruta de destino para los archivos JSON: ")
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            
        # Carpeta para archivos incompletos (ruta donde guarda los incompletos)
        # Busca la carpeta de inclompleto si no esta la crea (if not) os (sistema) path (ruta) join (suma los archivos "segmentados")
        #rellena la informacion del archivo segmentado para poder transformarlo en un archivo completo
        carpeta_incompleto = os.path.join(carpeta_destino, "Incompleto")
        if not os.path.exists(carpeta_incompleto):
            os.makedirs(carpeta_incompleto)


        user_input = ''
        # Ingreso de valores
        try:
            #sub-bucle que despues de la introduccion de cada Clave vuelve a realizar la siguiente comprobacion, en caso de rotura del bucle se crea el archivo incompleto
            while user_input != 'exit':
                user_input = input("Ingrese 'exit' en cualquier momento para salir. Presione Enter para continuar.").strip()
                if user_input.lower() == 'exit':
                    break

                plantilla["nombre"] = validar_str("nombre", 3, 30)
                plantilla["modelo"] = validar_str("modelo", 3, 30)
                plantilla["fabricante"] = input("Ingrese fabricante (opcional): ")
                plantilla["cantidad"] = validar_int("cantidad", 1, 999)
                plantilla["cantidadAviso"] = validar_int("cantidadAviso", 1, 999)
                plantilla["cantidadMaxima"] = validar_int("cantidadMaxima", 1, 999)
                plantilla["datasheet"] = input("Ingrese datasheet (opcional): ")
                plantilla["notas"] = validar_str("notas", 5, 400)
                plantilla["localizacion"] = validar_int("localizacion", 1, 99)
                objeto_actual = dict(plantilla)
                datos_por_guardar.append(objeto_actual)
                
        # Guardar la entrada en un archivo JSON incompleto hasta que se complete el formulario, asi siempre se puede salir sin perder la informacion
        # preguntar a GPT porque falla el almacenaje y como interrumpir (fuera de suploop?)
            nombre_archivo_incompleto = os.path.join(carpeta_incompleto, f"incompletos.json")
            with open(nombre_archivo_incompleto, 'w') as archivo_json_incompleto:
                json.dump(datos_por_guardar, archivo_json_incompleto, indent=2)
                print(f"\nLa información incompleta ha sido guardada en la carpeta 'Incompleto': {nombre_archivo_incompleto}")

        # Interrupción (Ctrl+C o exit) para salir (sugerido por gpt,preguntar a juan) si estas leyendo esto, explica en cristiano perro.
        except KeyboardInterrupt:
            nombre_archivo_incompleto = os.path.join(carpeta_incompleto, f"incompletos.json")
            with open(nombre_archivo_incompleto, 'w') as archivo_json_incompleto:
                json.dump(datos_por_guardar, archivo_json_incompleto, indent=2)
                print(f"\nLa información incompleta ha sido guardada en la carpeta 'Incompleto': {nombre_archivo_incompleto}") 

        # Guardar la plantilla completa como un archivo JSON (idem incompleto cambiando ruta)
        nombre_archivo_completo = os.path.join(carpeta_destino, f"completo.json")


        with open(nombre_archivo_completo, 'w') as archivo_json_completo:
            json.dump(datos_por_guardar, archivo_json_completo, indent=2)

        # Muestra la plantilla resultante
        print("\nTus datos son:")
        print(plantilla)
        print(f"\n\nLa información completa ha sido guardada en el archivo JSON: {nombre_archivo_completo}")


        """
        ACTUALIZACIONES Y DUDAS SOBRE EL CODIGO (como subrayar este apartado)

        preguntar para que todo quede mas limpio como sacar la plantilla como modulo externo y llamarlo con import, requiere ser un def?
        intentar operar y retirar redundancia
        estaria bien si se pudiera hacer de manera externa a vs code, como una "aplicacion independiente" (interfaz minima)
        que mostrara los datos complementados a medida que se introduce una nueva variable (hasta que se complete el paquete)
        en caso de haber cometido un error en el articulo anterior opcion de reintroducir los datos del tema anterior
        """