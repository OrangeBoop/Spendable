import flet as ft
from signup_page import render_signup_page  # Imports your separate sign-up file!


def main(page: ft.Page):
    # region StartPage Settings
    page.title = "Spendable"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    # endregion

    def show_start_page(e=None) -> None:
        page.clean()

        # region StartPage App Header Elements
        title = ft.Text("Spendable :)", size=36, weight="bold", color=ft.Colors.BLUE)

        subtitle = ft.Text(
            "Track your expenses effortlessly, locally on your device.",
            size=14,
            color=ft.Colors.GREY_700,
        )

        # Buttons:
        add_expense_btn = ft.FilledButton(
            content="Create Local User",
            # Calls the sign-up function imported from your other file and passes the page + callback
            on_click=lambda e: render_signup_page(page, show_start_page),
            icon=ft.Icons.ADD_CIRCLE_OUTLINE,
            width=260,
        )

        view_log_btn = ft.OutlinedButton(
            content="Log into User",
            icon=ft.Icons.LIST_ALT,
            width=260,
        )
        # endregion

        # region Creating StartPage using a container
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        title,
                        subtitle,
                        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),  # Spacing
                        add_expense_btn,
                        view_log_btn,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
                expand=True,
            )
        )
        page.update()
        # endregion

    # Start the app on the Start Page
    show_start_page()


ft.run(main)