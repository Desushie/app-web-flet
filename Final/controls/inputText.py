# Este es un archivo python creado en la carpeta controles
# Almacenará algunos elementos UI reutilizables que usaremos en la App

from flet import *

def InputTextField(text, hide):
    return Container(
        alignment=alignment.center,
        content=TextField(
            height=48,
            width=300,
            text_size=12,
            color="#5c4033",
            border_radius=6,
            bgcolor="#fff2d8",
            border_color="transparent",
            filled=True,
            cursor_color="#5c4033",
            cursor_width=1,
            hint_text=text,
            hint_style=TextStyle(
                size=11,
                color="#a47551",
            ),
            password=hide,
        ),
    )

def SignInOption(btn_name, func):
    return Container(
        content=ElevatedButton(
            on_click=func,
            content=Text(
                btn_name,
                size=11,
                weight="bold",
                color="#fffaf0"
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=8),
                },
                color={
                    "": "#b85c38",
                },
                bgcolor={
                    "": "#b85c38",
                },
                overlay_color={
                    "": "#91442a",  # Más oscuro al hacer click
                },
            ),
            height=42,
            width=300,
        )
    )

# Componentes UI del Footer
def GetFooter():
    footer_list = [
        "Acerca de",
        "Contacto",
        "Privacidad",
        "Ubicación",
        "Noticias",
    ]
    
    footer_row = Row(alignment=MainAxisAlignment.CENTER, spacing=20)
    
    for item in footer_list:
        footer_row.controls.append(
            Text(
                item,
                color="#5c4033",
                size=10,
                weight="w500",
            )
        )
    
    return footer_row