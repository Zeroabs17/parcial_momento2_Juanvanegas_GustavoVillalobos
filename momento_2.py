# main.py - Código Final Integrado
gastos = []

def mostrar_menu():
    print("\n--- GESTOR DE GASTOS DE VEHÍCULOS ---")
    print("1. Registrar Gasto")
    print("2. Ver Resumen Total")
    print("3. Buscar Gastos por Placa")
    print("4. Salir")

def registrar_gasto():
    print("\n--- REGISTRO DE GASTO ---")
    placa = input("Ingrese la placa del vehículo: ").upper()
    concepto = input("Concepto (Gasolina, Peaje, etc.): ")
    try:
        valor = float(input("Ingrese el valor del gasto: "))
        
        nuevo_gasto = {
            "placa": placa,
            "concepto": concepto,
            "valor": valor
        }
        
        gastos.append(nuevo_gasto)
        print("¡Gasto registrado con éxito!")
    except ValueError:
        print("Error: El valor debe ser un número.")



def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            buscar_por_placa()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# --- ESTA LÍNEA ES LA QUE ACTIVA TODO EL PROGRAMA ---
if __name__ == "__main__":
    main()