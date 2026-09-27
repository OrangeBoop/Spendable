# region Imports
import flet as ft
from database import SessionLocal, User, init_db # Imports Table Blueprints and Local Session
#endregion 


#region Setting Error page
def error(page: ft.Page,type_error="0",show_start_page_callback=None)->None:
    page.clean()

    # region StartPage General Settings
    page.title = "Error!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.theme_mode = "dark"
    # endregion

    # region Error Handling
    # Determining the error message based on the error code
    error_message = "An unknown error occurred."
    if type_error == "u1":
        error_message = (
            "That username is already taken! Please choose a different one."
        )
    if type_error=="u2":
        error_message = (
                    "Failed user creation - Error:u2"
                )
    #endregion
    
    # region Back Route Handling
    # Define what happens when user clicks "Back to Home"
    def go_back_home(e):
        if show_start_page_callback:
            page.clean()
            show_start_page_callback(page)
        else:
            return
    # endregion

    # region Page Design
    page.add(
        ft.Text(
            error_message, color=ft.Colors.RED_400, size=16, weight="bold"
        ),
        ft.Button(content="Back to Home",icon=ft.Icons.ARROW_BACK, on_click=lambda e: go_back_home(page))
    )
    # endregion
    page.update()
#endregion
