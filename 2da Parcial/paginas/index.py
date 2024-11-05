"""
Pagina de Index
Esta es la página que el usuario va a ver cuando se loguee.
"""
from flet import *
from controls import navbar, postControl
from view import ShowMenu, PostText, ChangeRoute, LogUserOut

# Cada componente es aparte
# Ahora cuando el usuario se loguee, queremos pasar el nombre y apellido para usarlo en el UI de posts
# Esto significa que la vista va a tomar dos argumentos que vendran de la función login que creamos en vistas
def _view_(first_name:str, last_name:str):
    return View(
        "/index",
        bgcolor="white54",
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
                                        bgcolor="#1d1d1d",
                                        width=68,
                                        expand=True,
                                        animate=animation.Animation(350,"decelerate"),
                                        on_hover=lambda e: ShowMenu(e),
                                        content=navbar.ModernNavBar(
                                            # pasamos la funciones aca para redireccionar
                                            lambda e: LogUserOut(e),
                                            lambda e: ChangeRoute(e, "/profile"),
                                            lambda e: ChangeRoute(e, "/index"),
                                        ),
                                    )
                                ],
                            ),
                            VerticalDivider(width=60,color="transparent"),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.START,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Divider(height=30, color="transparent"),
                                    # Los controles van aca
                                    postControl.PostControl(
                                        lambda e: PostText(e, first_name, last_name)
                                    ),
                                    Divider(height=30, color="transparent"),
                                    #Esta columna sera en donde el usuario va a postear las tareas y el lugar donde accederemos a los datos y mostraremos cuando se logueen
                                    Column(expand=True, scroll="hidden"),
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
    )