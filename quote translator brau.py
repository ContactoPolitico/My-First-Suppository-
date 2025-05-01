import flet as ft

def main(page: ft.Page):
    quota_original = "Some people are going to leave, but that's not the end of your story. That's the end of their part in your story."
    traduccion = {
        "english": "Some people are going to leave, but that's not the end of your story. That's the end of their part in your story.",
        "spanish": "Algunas personas se irán, pero eso no es el final de tu historia. Ese es el final de su parte en tu historia.",
        "french": "Certaines personnes vont partir, mais ce n'est pas la fin de votre histoire. C'est la fin de leur rôle dans votre histoire."
    }

    def balls(e):
        selected_language = e.control.value.lower()  
        quote.value = traduccion.get(selected_language, quota_original)
        page.update()

    options = ft.RadioGroup(
        value="english",  
        on_change=balls,
        content=ft.Column(  
            controls=[
                ft.Radio(label="English", value="english"),
                ft.Radio(label="Spanish", value="spanish"),
                ft.Radio(label="French", value="french")
            ]
        )
    )

    quote = ft.Text(quota_original, size=23)
    page.add(ft.Row([quote], alignment=ft.MainAxisAlignment.CENTER), ft.Row([options]))

ft.app(main)