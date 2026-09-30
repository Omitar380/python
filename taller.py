import flet as ft


def main(page: ft.Page):
    # Se define una paleta sencilla y se deja espacio alrededor del contenido
    # para que la pantalla sea legible y no se vea amontonada.
    page.title = "Propuesta de interfaz"
    page.bgcolor = "#F3F6F2"
    page.padding = 28

    # El texto de estado permite mostrar que el botón realmente responde.
    texto_estado = ft.Text(
        "Elige una opción para comenzar.",
        size=14,
        color="#D9E7E3",
    )

    def mostrar_confirmacion(e):
        texto_estado.value = "¡Listo! La interfaz respondió a tu acción."
        page.update()

    # El encabezado identifica el proyecto sin competir visualmente con el título.
    encabezado = ft.Row(
        controls=[
            ft.Text("TALLER / UI", size=14, weight=ft.FontWeight.BOLD, color="#174B45"),
            ft.Text("PROPUESTA", size=12, color="#64736E"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # El bloque principal concentra el mensaje y la acción más importante.
    portada = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("BIENVENIDO", size=12, weight=ft.FontWeight.BOLD, color="#B8D7C8"),
                ft.Text(
                    "Un espacio claro\npara empezar.",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF",
                ),
                ft.Text(
                    "Una propuesta sencilla que organiza el contenido y destaca la siguiente acción.",
                    size=16,
                    color="#E1ECE8",
                ),
                ft.Button(
                    content="Probar interacción",
                    on_click=mostrar_confirmacion,
                    bgcolor="#F2B66D",
                    color="#263832",
                ),
                texto_estado,
            ],
            spacing=16,
        ),
        bgcolor="#174B45",
        padding=30,
        border_radius=16,
    )

    # Las opciones se presentan como una lista para facilitar su lectura rápida.
    opciones = ft.Column(
        controls=[
            ft.Text("¿Qué encontrarás?", size=22, weight=ft.FontWeight.BOLD, color="#21332E"),
            ft.Row(
                controls=[
                    ft.Text("01", width=42, size=14, weight=ft.FontWeight.BOLD, color="#16806D"),
                    ft.Column(
                        controls=[
                            ft.Text("Contenido organizado", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text("La información principal aparece primero.", size=14, color="#64736E"),
                        ],
                        spacing=4,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Row(
                controls=[
                    ft.Text("02", width=42, size=14, weight=ft.FontWeight.BOLD, color="#16806D"),
                    ft.Column(
                        controls=[
                            ft.Text("Navegación sencilla", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text("Cada sección tiene un propósito claro.", size=14, color="#64736E"),
                        ],
                        spacing=4,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Row(
                controls=[
                    ft.Text("03", width=42, size=14, weight=ft.FontWeight.BOLD, color="#16806D"),
                    ft.Column(
                        controls=[
                            ft.Text("Acción visible", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text("El botón principal ofrece una respuesta inmediata.", size=14, color="#64736E"),
                        ],
                        spacing=4,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=18,
    )

    # Una columna mantiene el orden de lectura: identidad, propuesta y detalles.
    page.add(
        ft.Column(
            controls=[encabezado, portada, opciones],
            spacing=28,
            width=760,
        )
    )


ft.app(target=main)