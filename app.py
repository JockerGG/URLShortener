import flet as ft
import pyshorteners
from Row.ShortenLinkRow import ShortenLinkRow

shortener = pyshorteners.Shortener()

def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "URL Shortener"
    page.horizontal_alignment = "center"

    page.appbar = ft.AppBar(
        title=ft.Text("URL Shortener", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.BLUE
    )

    def onshorturl(e):
        shorten(text_field=text_field, page=page)

    text_field = ft.TextField(
        label="Long URL",
        hint_text="Type your URL here",
        max_length=200,
        keyboard_type="url",
        suffix=ft.FilledButton("Shorten!", on_click=onshorturl),
        on_submit=onshorturl
    )

    page.add(
        text_field,
        ft.Text("Generated URLs:", weight="bold", size=23)
    )


def shorten(text_field, page):
    user_link = text_field.value
    if user_link:
        try:
            page.add(ft.Text(f"Long URL: {user_link}", italic=False, weight='bold'))
            page.add(ShortenLinkRow(shortened_link=shortener.tinyurl.short(user_link), link_source="By tinyurl.com"))
            page.add(ShortenLinkRow(shortened_link=shortener.chilpit.short(user_link), link_source="By chilp.it"))
            page.add(ShortenLinkRow(shortened_link=shortener.clckru.short(user_link), link_source="By clck.ru"))
            page.add(ShortenLinkRow(shortened_link=shortener.dagd.short(user_link), link_source="By da.dg"))
        except Exception as exception:
            print(exception)
            page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("Sorry, but an error occurred. Please retry, or refresh the page."),
                    open=True
                )
            )


ft.app(target=main, view=ft.WEB_BROWSER)
