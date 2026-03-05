import flet as ft

def obtener_prefijos(cadena):
    return [cadena[:i+1] for i in range(len(cadena))] + ["ε (cadena vacía)"]

def obtener_sufijos(cadena):
    return [cadena[i:] for i in range(len(cadena))] + ["ε (cadena vacía)"]

def obtener_subcadenas(cadena):
    n = len(cadena)
    subcadenas = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            subcadenas.add(cadena[i:j])
    return list(subcadenas) + ["ε (cadena vacía)"]

def main(page: ft.Page):
    page.title = "Operaciones Básicas - Teoría de la Computación"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Componentes de la interfaz
    entrada_cadena = ft.TextField(label="Ingresa una cadena", hint_text="Ejemplo: abc")
    resultado_texto = ft.Column()

    def calcular_clic(e):
        cadena = entrada_cadena.value
        if not cadena:
            return

        prefijos = obtener_prefijos(cadena)
        sufijos = obtener_sufijos(cadena)
        subcadenas = obtener_subcadenas(cadena)

        resultado_texto.controls.clear()
        resultado_texto.controls.append(ft.Text(f"Resultados para: {cadena}", weight="bold", size=20))
        resultado_texto.controls.append(ft.Text(f"Prefijos: {', '.join(prefijos)}"))
        resultado_texto.controls.append(ft.Text(f"Sufijos: {', '.join(sufijos)}"))
        resultado_texto.controls.append(ft.Text(f"Subcadenas: {', '.join(subcadenas)}"))
        
        page.update()

    # Botón principal
    boton_calcular = ft.ElevatedButton("Calcular Operaciones", on_click=calcular_clic)

    # Agregar a la página
    page.add(
        ft.Text("Ejercicio 1: Subcadenas, Prefijos y Sufijos", size=25, weight="bold"),
        entrada_cadena,
        boton_calcular,
        ft.Divider(),
        resultado_texto
    )

ft.app(target=main)