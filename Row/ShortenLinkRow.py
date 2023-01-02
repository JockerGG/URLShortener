import flet as ft


class ShortenLinkRow(ft.Row):
    def __init__(self, shortened_link, link_source):
        super().__init__()
        self.tooltip = link_source
        self.alignment = "center"

        self.controls = [
            ft.Text(value=shortened_link, size=16, selectable=True, italic=True),
            ft.IconButton(
                icon=ft.icons.COPY,
                on_click=lambda e: self.copy(shortened_link),
                bgcolor = ft.colors.WHITE,
                tooltip="Copy to clipboard"
            ),
            ft.IconButton(
                icon=ft.icons.OPEN_IN_BROWSER_OUTLINED,
                tooltip="Open in browser",
                on_click=lambda e: e.page.launch_url(shortened_link)
            )
        ]

    def copy(self, value):
        self.page.set_clipboard(value)
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.SnackBar(
                    ft.Text("Link copied to clipboard!"),
                    open=True
                )
            )
        )
