"""
Pagina de Registro
Podemos reutilizar la mayor parte del UI del login aca, con unos cambios básicos
"""

from flet import *

# Se importan los controles
from controls import inputText
from view import ChangeRoute, RegisterUser

"""
Para mostrar algo en la pantalla, debemos de hacer una función.
Todas las paginas deben tener el mismo nombre de la función para que la lógica funcione
"""

def _view_():
    return View(
        "/register",
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
                        height= 600,
                        border_radius=8,
                        bgcolor="#ffffff",
                        border=border.all(3,"#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Registro",
                                    size=26,
                                    color="black",
                                    weight="w600",
                                ),
                                Text(
                                    "Rellena el formulario de abajo para crear una cuenta.",
                                    size=12,
                                    color="black",
                                    weight="w400",
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        # Se usan controles de Texto
                                        inputText.InputTextField("Nombres", False),
                                        inputText.InputTextField("Apellidos", False),
                                        inputText.InputTextField("Correo", False),
                                        inputText.InputTextField("Contraseña", True),
                                    ],
                                ),
                                Divider(height=5, color="transparent"),
                                # Es necesario otro control aca
                                inputText.SignInOption("Registrarse", lambda e: RegisterUser(e)),
                                Divider(height=60, color="transparent"),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "Ya tienes una cuenta?",
                                            color="black",
                                            size=10,
                                            weight="bold",
                                        ),
                                        Container(
                                            on_click=lambda e: ChangeRoute(e, "/login"), 
                                            content=Text(
                                                "Iniciar Sesión",
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