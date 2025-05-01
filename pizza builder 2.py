import flet as ft

def main(page: ft.Page):
    page.title = "Pizza Customizer"
    page.padding = 20 
   
    base_pizza_url = "https://valentispizza.net/wp-content/themes/valentis-child/images/arma-tu-pizza/pizza-base.png"
    
   
    pepperoni_url = "https://spagalimis.co.nz/wp-content/plugins/pizzatime/images/pepperoni.png"
    mushrooms_url = "https://spagalimis.co.nz/wp-content/plugins/pizzatime/images/mushrooms.png"
    olives_url = "https://d1wv361rfnmm1x.cloudfront.net/productImages/2022/10/6359054e815df_1666778446.png"
    bacon_url = "https://spagalimis.co.nz/wp-content/plugins/pizzatime/images/bacon.png"

    
    pizza_image = ft.Image(width=300, height=300, src=base_pizza_url)

   
    pepperoni_image = ft.Image(width=300, height=300, src=pepperoni_url, opacity=0)
    mushrooms_image = ft.Image(width=280, height=280, src=mushrooms_url, opacity=0)
    olives_image = ft.Image(width=280, height=280, src=olives_url, opacity=0)
    bacon_image = ft.Image(width=280, height=280, src=bacon_url, opacity=0)
  
    pepperoni_switch = ft.Switch(label="Pepperoni", value=False)
    mushrooms_switch = ft.Switch(label="Mushrooms", value=False)
    olives_switch = ft.Switch(label="Olives", value=False)
    bacon_switch = ft.Switch(label="Bacon", value=False)


    def update_pizza(e):
        if pepperoni_switch.value:
            pepperoni_image.opacity = 1  
        else:
            pepperoni_image.opacity = 0  
        
        if mushrooms_switch.value:
            mushrooms_image.opacity = 1  
        else:
            mushrooms_image.opacity = 0  
        
        if olives_switch.value:
            olives_image.opacity = 1
        else:
            olives_image.opacity = 0
            
        if bacon_switch.value:
            bacon_image.opacity = 1
        else:
            bacon_image.opacity = 0 
        
        page.update()

    pepperoni_switch.on_change = update_pizza
    mushrooms_switch.on_change = update_pizza
    olives_switch.on_change = update_pizza
    bacon_switch.on_change = update_pizza

    update_pizza(None)

    page.add(
        ft.Column([
            ft.Stack([
                pizza_image,
                pepperoni_image,
                mushrooms_image,
                olives_image,
                bacon_image,
            ]),
            ft.Row([pepperoni_switch, mushrooms_switch, olives_switch, bacon_switch], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )

ft.app(target=main)