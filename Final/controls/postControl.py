"""
Aca vamos a tener dos clases de UI que manejaran los posts de usuarios
"""

from flet import *
import view

class PostControl(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()
    
    def build(self):
        return Container(
            bgcolor="#fff2d8",
            width=500,
            height=52,
            border_radius=6,
            padding=5,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        alignment=alignment.center,
                        content=TextField(
                            content_padding=10,
                            height=42,
                            width=328,
                            text_size=12,
                            color="#5c4033",
                            border_radius=6,
                            bgcolor="#fff6e5",
                            border_color="transparent",
                            filled=True,
                            cursor_color="#5c4033",
                            cursor_width=1,
                            hint_text="Empieza escribiendo algo aqui ...",
                            hint_style=TextStyle(
                                size=11,
                                color="#a47551",
                            ),
                        ),
                    ),
                    Container(
                        content=ElevatedButton(
                            on_click=self.func,
                            content=Text(
                                "Post",
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
                                    "": "#91442a",
                                },
                            ),
                            height=42,
                            width=100,
                        )
                    ),
                ],
            ),
        )

# Aca creamos el UI para el display del Post
class DisplayPost(UserControl):
    # Estos son argumentos necesarios para enviar a la clase
    def __init__(
            self,
            first_name: str,
            last_name: str,
            post_date: str,
            user_post: str,
            post_node: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.post_date = post_date
        self.user_post = user_post
        self.post_node = post_node
        super().__init__()

    def DeletePostData(self, post_node, e):
        view.DeletePostData(self, post_node, e)

    def build(self):
        return Container(
            width=500,
            bgcolor="#fff6e5",
            padding=15,
            border_radius=8,
            border=border.all(1, "#e0c3a6"),
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Text(
                                value=f"{self.first_name} {self.last_name}",
                                size=10,
                                color="#5c4033",
                            ),
                            Text(
                                value=f"{self.post_date}",
                                size=10,
                                color="#a47551",
                            ),
                        ]
                    ),
                    Row(
                        wrap=True,
                        controls=[
                            Text(
                                value=self.user_post,
                                size=11,
                                weight="w400",
                                color="#5c4033",
                            )
                        ],
                    ),
                    Divider(height=1, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            IconButton(
                                icon=icons.DELETE_ROUNDED,
                                width=26,
                                icon_size=18,
                                icon_color="#b85c38",
                                on_click= lambda e: self.DeletePostData(
                                    self.post_node, e
                                )
                            )
                        ]
                    )
                ]
            ),
        )