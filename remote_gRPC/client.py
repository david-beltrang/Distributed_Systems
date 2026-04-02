import grpc
import interfaz_pb2
import interfaz_pb2_grpc

# Funcion que muestra el menú de opciones al usuario y devuelve la opción seleccionada
def mostrar_menu():
    print("\n--- Menú de Consultas ---")
    print("1. Consultar promedio de notas")
    print("2. Consultar grupo")
    print("3. Consultar evaluaciones (quiz y taller)")
    print("4. Salir")
    return input("Seleccione una opción: ")

# Función principal del cliente que se encarga de interactuar con el usuario y enviar las solicitudes al servidor
def ejecutar_client():
    # Creamos el canal (el tubo de comunicación)
    with grpc.insecure_channel('localhost:50051') as canal:

        # Creamos el stub (el cliente que nos permite hacer las llamadas al servidor)
        stub = interfaz_pb2_grpc.ConsultaStub(canal)
        
        while True:
            opcion = mostrar_menu()
            
            # Si el usuario selecciona la opción 4, se sale del programa
            if opcion == '4':
                print("Saliendo...")
                break
                
            # Si el usuario selecciona una opción válida (1, 2 o 3), se solicita el nombre o apellido del estudiante y se envía la solicitud al servidor
            if opcion in ['1', '2', '3']:
                estudiante = input("\nIngrese el nombre o apellido del estudiante: ")
                try:
                    # Si se selecciona la opción 1, se envía una solicitud para consultar el promedio de notas del estudiante
                    if opcion == '1':
                        # Se crea la solicitud (petición) con el nombre o apellido del estudiante y se envía al servidor utilizando el stub
                        peticion = interfaz_pb2.NotasRequest(estudiante=estudiante)
                        # Se recibe la respuesta del servidor y se muestra al usuario
                        respuesta = stub.ConsultarNotas(peticion)
                        # Se muestra el promedio de notas que el servidor devuelve como respuesta al cliente
                        print(f"El servidor dice (Promedio): {respuesta.promedio}")
                        
                    # Si se selecciona la opción 2, se envía una solicitud para consultar el grupo del estudiante
                    elif opcion == '2':
                        # Se crea la solicitud (petición) con el nombre o apellido del estudiante y se envía al servidor utilizando el stub
                        peticion = interfaz_pb2.GrupoRequest(estudiante=estudiante)
                        # Se recibe la respuesta del servidor y se muestra al usuario
                        respuesta = stub.ConsultarGrupo(peticion)
                        # Se muestra el grupo que el servidor devuelve como respuesta al cliente
                        print(f"El servidor dice (Grupo): {respuesta.grupo}")
                        
                    # Si se selecciona la opción 3, se envía una solicitud para consultar las evaluaciones (notas del quiz y taller) del estudiante
                    elif opcion == '3':
                        # Se crea la solicitud (petición) con el nombre o apellido del estudiante y se envía al servidor utilizando el stub
                        peticion = interfaz_pb2.EvaluacionesRequest(estudiante=estudiante)
                        # Se recibe la respuesta del servidor y se muestra al usuario
                        respuesta = stub.ConsultarEvaluaciones(peticion)
                        # Se muestran las notas del quiz y taller que el servidor devuelve como respuesta al cliente
                        print(f"El servidor dice:\n  Nota quiz: {respuesta.notaQuiz}\n  Nota taller: {respuesta.notaTaller}")
                    
                # Si el servidor devuelve un error , se captura la excepción y se muestra el mensaje de error al usuario
                except grpc.RpcError as e:
                    print(f"Error devuelto por el servidor: {e.details()}")
                    
            # Si el usuario selecciona una opción no válida, se muestra un mensaje de error y se vuelve a mostrar el menú
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_client()