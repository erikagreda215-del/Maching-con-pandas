import datos


def main():
    while True:
        print("\n--- MENÚ")
        print("1: Generar informes CSV y JSON")
        print("2: Mostrar gráfico de medias")
        print("0: Salir")
        opcion = input("Elige una opción: ").strip()

        try:
            if opcion == "1":
                informe = datos.preparar_datos()
                datos.guardar_informes(informe)
                datos.mostrar_informe(informe)
            elif opcion == "2":
                informe = datos.preparar_datos()
                datos.mostrar_grafico(informe)
            elif opcion == "0":
                print("Bye Bye")
                break
            else:
                print("Opción no mala")
        except ValueError as error:
            print("Aviso:", error)


if __name__ == "__main__":
    main()