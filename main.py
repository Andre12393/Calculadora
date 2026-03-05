import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Propina"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campos
    total_cuenta = ft.TextField(label="Total de la cuenta", width=200)
    porcentaje = ft.TextField(label="Porcentaje de propina (%)", width=200)
    resultado = ft.Text(value="", size=20, weight="bold")

    def calcular(e):
        try:
            total = float(total_cuenta.value)
            porc = float(porcentaje.value)

            propina = total * (porc / 100)
            total_final = total + propina

            resultado.value = (
                f"Propina: ${propina:.2f}\n"
                f"Total a pagar: ${total_final:.2f}"
            )
        except:
            resultado.value = "⚠️ Ingresa valores numéricos válidos"

        page.update()

    boton_calcular = ft.ElevatedButton("Calcular", on_click=calcular)

    page.add(
        total_cuenta,
        porcentaje,
        boton_calcular,
        resultado
    )

ft.run(main)