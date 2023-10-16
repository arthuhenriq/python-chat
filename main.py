import flet as ft


def main(page):
    chat = ft.Column()

    def send_message_tunel(info):
        user = info["user"]
        if info["type"] == "entrada":
            chat.controls.append(ft.Text(f"{user} entrou no chat", size=12, color=ft.colors.BLUE_ACCENT_700, italic=True))
        else:
            message = info["message"]
            chat.controls.append(ft.Text(f"{user}: {message}"))
        page.update()

    page.pubsub.subscribe(send_message_tunel)

    def send_message(e):
        page.pubsub.send_all({"user": user_name.value, "message": text_label.value, "type": "message"})
        text_label.value = ""
        page.update()

    text_label = ft.TextField(label="Digite uma mensage")
    send_button = ft.ElevatedButton("Enviar", on_click=send_message)

    def get_in(e):
        page.add(chat)
        page.add(ft.Row([text_label, send_button]))
        popup.open = False
        page.pubsub.send_all({"user": user_name.value, "type": "entrada"})
        page.remove(init_button)
        page.update()

    user_name = ft.TextField(label="Escreva seu nome no chat")
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Artzap"),
        content=user_name,
        actions=[ft.ElevatedButton("Entrar no chat", on_click=get_in)]
    )

    def open_popup(e):
        page.dialog = popup
        popup.open = True
        page.update()

    init_button = ft.ElevatedButton("Iniciar Chat", on_click=open_popup)

    page.add(init_button)


ft.app(target=main, view=ft.WEB_BROWSER)
