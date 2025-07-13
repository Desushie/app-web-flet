"""
Pagina de Perfil
"""
from flet import *
from controls import navbar, profileData
from view import ShowMenu, ChangeRoute, LogUserOut

def _view_(created_on, last_login, first_name, last_name, email):
    return View(
        "/profile",
        bgcolor="#fcefe3",
        controls=[
            Column(
                expand=True,
                controls=[
                    Row(
                        expand=True,
                        controls=[
                            Column(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        margin=-10,
                                        bgcolor="#a47551",
                                        width=68,
                                        expand=True,
                                        animate=animation.Animation(350,"decelerate"),
                                        on_hover=lambda e: ShowMenu(e),
                                        content=navbar.ModernNavBar(
                                            lambda e: LogUserOut(e),
                                            lambda e: ChangeRoute(e, "/profile"),
                                            lambda e: ChangeRoute(e, "/index"),
                                        ),
                                    )
                                ],
                            ),
                            VerticalDivider(width=60, color="transparent"),
                            profileData.ProfileData(
                                created_on, last_login, first_name, last_name, email
                            )
                        ],
                    )
                ],
            )
        ]
    )