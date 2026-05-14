# main.py - Código Final Integrado
gastos = []

def mostrar_menu():
    print("\n--- GESTOR DE GASTOS DE VEHÍCULOS ---")
    print("1. Registrar Gasto")
    print("2. Ver Resumen Total")
    print("3. Buscar Gastos por Placa")
    print("4. Salir")

def buscar_por_placa():
    print("\n--- BÚSQUEDA POR PLACA ---")
    placa_buscada = input("Ingrese la placa a buscar: ").upper()
    encontrado = False

    for gasto in gastos:
        if gasto["placa"] == placa_buscada:
            print(f"- {gasto['concepto']}: ${gasto['valor']}")
            encontrado = True
    
    if not encontrado:
        print(f"No se encontraron gastos para la placa {placa_buscada}.")

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