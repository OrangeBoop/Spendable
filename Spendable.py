# region Imports
import flet as ft
from signup_page import render_signup_page  # Imports separate sign-up file
from database import SessionLocal, User, init_db # Imports Table Blueprints and Local Session
#endregion 


# region Start Page Menu

def show_start_page(page: ft.Page) -> None:
    page.clean()
    # region StartPage General Settings
    page.title = "Spendable"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.theme_mode='dark'
    # endregionThe

    # region StartPage Database Settings
    init_db()
    # endregion

#region StartPage App Header Settings
    title = ft.Text("Spendable :)", size=36, weight="bold", color=ft.Colors.BLUE)

    subtitle = ft.Text(
        "Track your expenses effortlessly, locally on your device.",
        size=14,
        color=ft.Colors.GREY_700,
    )

    # Buttons:
    add_expense_btn = ft.FilledButton(
        content="Create Local User",
        # Calls the sign-up function imported the signup_page file and passes the page + callback
        on_click=lambda e: render_signup_page(page, show_start_page),
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        width=260,
    )

    view_log_btn = ft.OutlinedButton(
        content="Log into User",
        icon=ft.Icons.LIST_ALT,
        width=260,
    )
#endregion

# region StartPage Design
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

def main(page:ft.Page):
    show_start_page(page)
ft.run(main)