def entrada_receptor(token_cancelacion: str):
    def recibir_entrada(msg: str, err: str, validacion_fn=None):
        while True:
            entrada = input(f"{msg} : ")
            if entrada == token_cancelacion:
                return False
            if validacion_fn and not validacion_fn(entrada):
                print("\n" + err + "\n")
            else:
                return entrada

    return recibir_entrada

def imprimir_menu_opciones():
    print("\nMenu de opciones\n")
    print("1. Incluir")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Reporte")
    print("5. Salir")