from flet import *

# Se importan los controles
from controls import inputText
# Necesitamos importar la vista MAS el metodo
from view import ChangeRoute, LogInUser


"""
Para mostrar algo en la pantalla, debemos de hacer una función.
Todas las paginas deben tener el mismo nombre de la función para que la lógica funcione
"""

def _view_():
    return View(
        "/login",
        bgcolor='#fafafa',
        horizontal_alignment = CrossAxisAlignment.CENTER,
        vertical_alignment = MainAxisAlignment.CENTER,
        controls=[
            Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=350, 
                        height= 500,
                        border_radius=8,
                        bgcolor="#ffffff",
                        border=border.all(3,"#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Inicio de Sesión",
                                    size=26,
                                    color="black",
                                    weight="w600",
                                ),
                                Text(
                                    "Usa el formulario de abajo para iniciar sesión en tu cuenta.",
                                    size=12,
                                    color="black",
                                    weight="w400",
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        # Se usan controles de Texto
                                        inputText.InputTextField("Correo", False),
                                        inputText.InputTextField("Contraseña", True),
                                    ],
                                ),
                                Row(
                                    width=300,
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        Text(
                                            "Olvido su Contraseña?",
                                            color="black",
                                            weight="bold",
                                            size=10,
                                        )
                                    ],
                                ),
                                Divider(height=5, color="transparent"),
                                inputText.SignInOption("Iniciar Sesión", lambda e: LogInUser(e)),
                                Divider(height=60, color="transparent"),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "No tienes una cuenta?",
                                            color="black",
                                            size=10,
                                            weight="bold",
                                        ),
                                        Container(
                                            on_click=lambda e: ChangeRoute(
                                                e, "/register"
                                            ),
                                    # En el login, queremos ir a la pagina de registro
                                            content=Text(
                                                "Registrarse",
                                                color="blue900",
                                                size=10,
                                                weight="bold",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    # UI del Footer
                    Column(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Divider(height=60, color="transparent"),
                            # Se usan controles de Footer
                            inputText.GetFooter(),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        "© 2024 ᓚᘏᗢ",
                                        size=10,
                                        weight="w500",
                                        color="black",
                                    )
                                ]
                            )
                        ],
                    ),
                ]
            )
        ],
    )