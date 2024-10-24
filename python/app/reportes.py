def imprimir_reporte(
    por_origen_v: int,
    por_origen_e: int,
    impuesto_vencidos: int,
    recaudos_validos: int
):
    d_clientes_v = "Clientes con pasaporte venezolano (V):"
    d_clientes_e = "Clientes con pasaporte extranjero (E):"
    d_clientes_di = "Clientes con declaracion de impuesto vencida:"
    d_clientes_vigentes = "Clientes con recaudos vigentes:"

    print("\nREPORTE CLIENTES\n")
    print(f"Total clientes: {por_origen_v + por_origen_e}")
    print("{} {} {}".format(d_clientes_v, 20 * "-", por_origen_v))
    print("{} {} {}".format(d_clientes_e, 20 * "-", por_origen_e))
    print("{} {} {}".format(d_clientes_di, 13 * "-", impuesto_vencidos))
    print("{} {} {}".format(d_clientes_vigentes, 27 * "-", recaudos_validos))
    input("\npresiona ENTER para continuar")
