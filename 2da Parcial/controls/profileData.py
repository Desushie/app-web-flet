"""
Pagina de Controles del Perfil
"""

from flet import *

class ProfileData(UserControl):
    # necesitamos los siguientes argumentos
    def __init__(self, created_on, last_login, first_name, last_name, email):
        self.created_on = created_on
        self.last_login = last_login
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        super().__init__()

    # Esta funcion retorna texto
    def ReturnText(self, name, size):
        return Text(
            value=name,
            size=size,
            color="black",
            weight="bold",
        )
    
    def build(self):
        return Column(
            expand=True,
            horizontal_alignment=CrossAxisAlignment.START,
            controls=[
                # los headers
                Divider(height=30, color="transparent"),
                Row(
                    controls=[
                        Text(
                            "Información del Perfil de Usuario",
                            size=25,
                            color="black",
                            weight="bold",
                        )
                    ]
                ),
                Divider(height=10, color="black"),
                Divider(height=20, color="transparent"),
                # El primer container le mostrará al usuario los datos de cuando se creo la cuenta y el ultimo inicio de sesion
                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Usuario Creado el", 10),
                                    self.ReturnText(self.created_on, 12),
                                ],
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Ultimo inicio de sesión", 10),
                                    self.ReturnText(self.last_login, 12),
                                ],
                            ),
                        ],
                    ),
                ),
                # Luego, el nombre y apellido del usuario
            ],
        )