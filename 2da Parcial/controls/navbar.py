"""
Menu de costado
"""
from flet import *
class ModernNavBar(UserControl):
    # Debemos pasar argumentos a la clase del menu lateral para poder redireccionar cuando hacemos click en los iconos
    def __init__(self, func_logout, func_profile, func_home):
        self.func_logout = func_logout
        self.func_profile = func_profile
        self.func_home = func_home
        super().__init__()
    
    def ContainedIcon(self, icon_name, text, func):
        return Container(
            width=100, 
            height=45, 
            border_radius=10, 
            on_click=func, #cambiar luego##
            on_hover=None,
            content=Row(
                controls=[
                    IconButton( # Boton con icono
                        icon=icon_name,
                        icon_size=18,
                        selected=False,
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text( # Texto con descripción de pagina
                        value=text,
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    ),
                ]
            ),
        )
    
    def build(self):
        return Container(
            alignment=alignment.center,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.START,
                spacing=5,
                controls=[
                    self.ContainedIcon(icons.HOME_FILLED, 'Home', self.func_home),
                    self.ContainedIcon(icons.DASHBOARD_ROUNDED, 'Perfil', self.func_profile),
                    Divider(color="white",height=5),
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, 'Logout', self.func_logout),
                ],
            ),
        )