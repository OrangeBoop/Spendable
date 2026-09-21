import flet as ft
import bcrypt


def render_signup_page(page: ft.Page, show_start_page_callback) -> None:
    page.clean()

    # region Setting up our fields
    text_username: ft.TextField = ft.TextField(
        label="Username",
        text_align=ft.TextAlign.LEFT,
        width=200,
        on_change=None
    )

    text_password: ft.TextField = ft.TextField(
        label="Password",
        text_align=ft.TextAlign.LEFT,
        width=200,
        password=True,
        can_reveal_password=True
    )

    checkbox_signup: ft.Checkbox = ft.Checkbox(
        value=False,
        scale=1.2,
    )

    checkbox_label = ft.Text(
        "I Agree to the", 
        size=14, 
        weight=ft.FontWeight.W_500
    )

    submit_button: ft.FilledButton = ft.FilledButton(
        content="Create an Account",
        width=200,
        disabled=True
    )
    # endregion

    # region Validation variables
    valid_username = False
    valid_password = False
    valid_terms = False
    # endregion

    # region Username Validation
    username_icon = ft.Icon(icon=ft.Icons.CLEAR, color=ft.Colors.RED_400, size=28)
    username_text = ft.Text(value="Must be at least 3 characters", color=ft.Colors.RED_400, size=24)
    username_hint = ft.Row(controls=[username_icon, username_text], spacing=5)

    def check_username(e) -> None:
        nonlocal valid_username
        username = e.control.value
        if len(username) >= 3:
            valid_username = True
            username_icon.name = ft.Icons.CHECK
            username_icon.color = ft.Colors.GREEN_400
            username_text.color = ft.Colors.GREEN_400
        else:
            valid_username = False
            username_icon.name = ft.Icons.CLEAR
            username_icon.color = ft.Colors.RED_400
            username_text.color = ft.Colors.RED_400
        username_hint.update()
        validate_form()
    # endregion

    # region Password Validation
    password_length_icon = ft.Icon(icon=ft.Icons.CLEAR, color=ft.Colors.RED_400, size=28)
    password_length_text = ft.Text(value="Must be at least 8 characters", color=ft.Colors.RED_400, size=24)

    password_special_icon = ft.Icon(icon=ft.Icons.CLEAR, color=ft.Colors.RED_400, size=28)
    password_special_text = ft.Text(value="Must contain a special character", color=ft.Colors.RED_400, size=24)

    password_lower_icon = ft.Icon(icon=ft.Icons.CLEAR, color=ft.Colors.RED_400, size=28)
    password_lower_text = ft.Text(value="Must contain a lowercase character", color=ft.Colors.RED_400, size=24)

    password_upper_icon = ft.Icon(icon=ft.Icons.CLEAR, color=ft.Colors.RED_400, size=28)
    password_upper_text = ft.Text(value="Must contain an uppercase character", color=ft.Colors.RED_400, size=24)

    password_hint = ft.Column(
        controls=[
            ft.Row([password_length_icon, password_length_text]),
            ft.Row([password_special_icon, password_special_text]),
            ft.Row([password_lower_icon, password_lower_text]),
            ft.Row([password_upper_icon, password_upper_text])
        ],
        spacing=2
    )

    def check_password(e) -> None:
        nonlocal valid_password
        pwd = e.control.value

        is_long_enough = len(pwd) >= 8
        password_length_icon.name = ft.Icons.CHECK if is_long_enough else ft.Icons.CLEAR
        password_length_icon.color = ft.Colors.GREEN_400 if is_long_enough else ft.Colors.RED_400
        password_length_text.color = ft.Colors.GREEN_400 if is_long_enough else ft.Colors.RED_400

        has_special = any(char in "!@#$%^&*" for char in pwd)
        password_special_icon.name = ft.Icons.CHECK if has_special else ft.Icons.CLEAR
        password_special_icon.color = ft.Colors.GREEN_400 if has_special else ft.Colors.RED_400
        password_special_text.color = ft.Colors.GREEN_400 if has_special else ft.Colors.RED_400

        has_lower = any(char.islower() for char in pwd)
        password_lower_icon.name = ft.Icons.CHECK if has_lower else ft.Icons.CLEAR
        password_lower_icon.color = ft.Colors.GREEN_400 if has_lower else ft.Colors.RED_400
        password_lower_text.color = ft.Colors.GREEN_400 if has_lower else ft.Colors.RED_400

        has_upper = any(char.isupper() for char in pwd)
        password_upper_icon.name = ft.Icons.CHECK if has_upper else ft.Icons.CLEAR
        password_upper_icon.color = ft.Colors.GREEN_400 if has_upper else ft.Colors.RED_400
        password_upper_text.color = ft.Colors.GREEN_400 if has_upper else ft.Colors.RED_400

        valid_password = is_long_enough and has_special and has_lower and has_upper
        password_hint.update()
        validate_form()
    # endregion

    # region Terms Validation
    def check_terms(e) -> None:
        nonlocal valid_terms
        valid_terms = e.control.value
        validate_form()
    # endregion

    # region Validate Form
    def validate_form() -> None:
        if valid_username and valid_password and valid_terms:
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        submit_button.update()
    # endregion

    # region Ridiculous Terms Popup
    terms_tile = ft.ExpansionTile(
        title=ft.Text("View Terms & Conditions", size=16, weight=ft.FontWeight.BOLD, align=ft.Alignment.CENTER),
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("By creating an account, you agree to:", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "• Allow us to judge your username silently.\n"
                            "• Surrender 3 imaginary goats upon request.\n"
                            "• Never microwave the database.\n"
                            "• Accept that our servers may be emotionally unavailable.\n"
                            "• Give us permission to blame bugs on Greg.\n"
                            "• Acknowledge that 'password123' is a crime.\n"
                            "• Fight at least one goose per calendar year.\n"
                            "• Accept absolutely no responsibility for the goose.\n"
                            "• Understand that pressing this button creates an account.",
                            size=14,
                        ),
                        ft.Text("⚠️ These terms are legally questionable.", size=11, italic=True),
                    ],
                    spacing=6,
                    scroll=ft.ScrollMode.AUTO,
                ),
                padding=10,
                height=160,          
                bgcolor=ft.Colors.GREY_900,
                border_radius=8,
            )
        ],
        width=320,
    )

    terms_row = ft.Row(
        controls=[checkbox_signup, checkbox_label],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
    )
    # endregion

    # region Create Account
    def create_account(e) -> None:
        username = text_username.value
        password = text_password.value

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        print("Username:", username)
        print("Hashed password:", hashed_password)

        page.clean()
    # endregion

    # region Connect Events
    text_username.on_change = check_username
    text_password.on_change = check_password
    checkbox_signup.on_change = check_terms
    submit_button.on_click = create_account
    # endregion

    # region Page Layout
    page.add(
        ft.Column(
            controls=[
                ft.Text("Create an Account", size=28, weight=ft.FontWeight.BOLD),
                ft.Column(controls=[text_username, username_hint], width=320, spacing=2),
                ft.Container(height=8),
                ft.Column(controls=[text_password, password_hint], width=320, spacing=2),
                ft.Container(height=10),
                terms_tile,
                terms_row,
                ft.Container(height=5),
                submit_button,
                ft.Container(height=10),
                ft.TextButton("Back to Home", on_click=lambda e: show_start_page_callback())
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        )
    )
    page.update()
    # endregion