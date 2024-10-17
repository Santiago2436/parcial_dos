def calcular_bonificacion(salario_base, cargo, nivel_desempeño):
    bonificacion = 0

    cargo = cargo.lower()
    nivel_desempeño = nivel_desempeño.lower()

    if cargo == 'directivo':
        if nivel_desempeño == 'alto':
            bonificacion = salario_base * 0.20
        elif nivel_desempeño == 'medio':
            bonificacion = salario_base * 0.10

    elif cargo == 'operativo':
        if nivel_desempeño == 'alto':
            bonificacion = salario_base * 0.15
        elif nivel_desempeño == 'medio':
            bonificacion = salario_base * 0.05

    total_recibir = salario_base + bonificacion

    return {
        "salario_base": salario_base,
        "bonificacion": bonificacion,
        "total_recibir": total_recibir
    }


def resumen_pago(salario_base, cargo, nivel_desempeño):
    resultado = calcular_bonificacion(salario_base, cargo, nivel_desempeño)

    return f"""
-----Resumen del Pago-----
Cargo: {cargo.capitalize()}
Nivel de Desempeño: {nivel_desempeño.capitalize()}
Salario Base: ${resultado['salario_base']}
Bonificación: ${resultado['bonificacion']}
Total a Recibir: ${resultado['total_recibir']}
------------------------------------
"""


# Datos de prueba
print(resumen_pago(3000000, 'directivo', 'alto'))
print(resumen_pago(2500000, 'directivo', 'medio'))
print(resumen_pago(1300000, 'auxiliar', 'bajo'))
print(resumen_pago(1750000, 'operativo', 'medio'))