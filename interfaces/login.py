
import tkinter as tk
from datetime import datetime


# Application colors
DARK_GREEN = "#073B2A"
PRIMARY_GREEN = "#006B4F"
EMERALD_GREEN = "#00A878"
LIGHT_GREEN = "#65D6A6"
PALE_GREEN = "#E8F5EE"
WHITE = "#FFFFFF"
BACKGROUND = "#F1F5F2"
TEXT_COLOR = "#173D30"
ERROR_COLOR = "#C62828"

# Application password
APP_PASSWORD = "Caja"


def exit_application(root):
    """Close the complete application."""
    root.destroy()


def show_about(root):
    """Display application and student information."""

    about_window = tk.Toplevel(root)
    about_window.title("About - Compensándote")
    about_window.geometry("430x280")
    about_window.resizable(False, False)
    about_window.configure(bg=BACKGROUND)

    about_window.transient(root)
    about_window.grab_set()

    # Main frame
    main_frame = tk.Frame(
        about_window,
        bg=WHITE,
        padx=25,
        pady=20
    )
    main_frame.grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )
    

    # Window title
    title_label = tk.Label(
        main_frame,
        text="ABOUT",
        font=("Arial", 17, "bold"),
        fg=PRIMARY_GREEN,
        bg=WHITE
    )
    title_label.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=(0, 18),
        sticky="w"
    )

    # Current date
    current_date = datetime.now().strftime("%d/%m/%Y")

    information = [
        ("Course:", "Proyecto Ingeniería 1"),
        ("Student:", "Carlos Alexander Coral Basallo"),
        ("Collaborative Group:", "298"),
        ("Date:", current_date)
    ]

    for row, (label_text, value) in enumerate(information, start=1):

        label = tk.Label(
            main_frame,
            text=label_text,
            font=("Arial", 10, "bold"),
            bg=WHITE,
            fg=TEXT_COLOR
        )
        label.grid(
            row=row,
            column=0,
            padx=(0, 10),
            pady=7,
            sticky="w"
        )

        value_label = tk.Label(
            main_frame,
            text=value,
            font=("Arial", 10),
            bg=WHITE,
            fg=TEXT_COLOR,
            anchor="w"
        )
        value_label.grid(
            row=row,
            column=1,
            pady=7,
            sticky="w"
        )

    # Accept button
    accept_button = tk.Button(
        main_frame,
        text="Accept",
        font=("Arial", 10, "bold"),
        bg=PRIMARY_GREEN,
        fg=WHITE,
        activebackground=EMERALD_GREEN,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        width=12,
        command=about_window.destroy
    )
    accept_button.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=(20, 0)
    )

    main_frame.columnconfigure(1, weight=1)


def create_login(root, on_success):
    """Create the application login window."""

    
    root.title("Login - Compensándote")

    root.state("zoomed")

    root.resizable(True, True)

    root.minsize(500, 500)

    root.configure(bg=BACKGROUND)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)


    root.protocol(
        "WM_DELETE_WINDOW",
        lambda: exit_application(root)
    )

    # Menu bar
    menu_bar = tk.Menu(root)

    about_menu = tk.Menu(
        menu_bar,
        tearoff=0
    )

    about_menu.add_command(
        label="About",
        command=lambda: show_about(root)
    )

    menu_bar.add_cascade(
        label="About",
        menu=about_menu
    )

    root.config(menu=menu_bar)

    # Main frame
    main_frame = tk.Frame(
        root,
        bg=DARK_GREEN,
        padx=30,
        pady=25
    )
    main_frame.grid(
        row=0,
        column=0,
        padx=20,
        pady=20,
        sticky="nsew"
    )

    # Application name
    title_label = tk.Label(
        main_frame,
        text="COMPENSÁNDOTE",
        font=("Arial", 24, "bold"),
        fg=LIGHT_GREEN,
        bg=DARK_GREEN
    )
    title_label.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=(10, 5)
    )

    # Subtitle
    subtitle_label = tk.Label(
        main_frame,
        text="Family Compensation Fund - Affiliation Control",
        font=("Arial", 9),
        fg=WHITE,
        bg=DARK_GREEN
    )
    subtitle_label.grid(
        row=1,
        column=0,
        columnspan=2,
        pady=(0, 25)
    )

    # Project information frame
    information_frame = tk.Frame(
        main_frame,
        bg=PRIMARY_GREEN,
        padx=12,
        pady=12
    )
    information_frame.grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(0, 20)
    )

    information = [
        ("Application:", "Compensándote"),
        ("Student:", "Carlos Alexander Coral Basallo"),
        ("Course:", "Proyecto Ingeniería 1"),
        ("Group:", "298")
    ]

    for row, (label_text, value) in enumerate(information):

        tk.Label(
            information_frame,
            text=label_text,
            font=("Arial", 9, "bold"),
            fg=LIGHT_GREEN,
            bg=PRIMARY_GREEN
        ).grid(
            row=row,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        tk.Label(
            information_frame,
            text=value,
            font=("Arial", 9),
            fg=WHITE,
            bg=PRIMARY_GREEN
        ).grid(
            row=row,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

    # Password label
    password_label = tk.Label(
        main_frame,
        text="Password",
        font=("Arial", 10, "bold"),
        fg=WHITE,
        bg=DARK_GREEN
    )
    password_label.grid(
        row=3,
        column=0,
        columnspan=2,
        sticky="w",
        pady=(0, 7)
    )

    # Password entry
    password_entry = tk.Entry(
        main_frame,
        font=("Arial", 13),
        show="*",
        bg=PALE_GREEN,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief="flat",
        width=35
    )
    password_entry.grid(
        row=4,
        column=0,
        columnspan=2,
        sticky="ew",
        ipady=9
    )

    password_entry.focus_set()

    # Error message
    error_label = tk.Label(
        main_frame,
        text="",
        font=("Arial", 9),
        fg="#FF9999",
        bg=DARK_GREEN
    )
    error_label.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=5
    )

    def validate_login():
        """Check the entered application password."""

        entered_password = password_entry.get()

        if entered_password == APP_PASSWORD:

            error_label.config(text="")
            on_success()

        else:
            error_label.config(
                text="Incorrect password. Please try again."
            )
            password_entry.delete(0, tk.END)
            password_entry.focus_set()

    # Buttons frame
    buttons_frame = tk.Frame(
        main_frame,
        bg=DARK_GREEN
    )
    buttons_frame.grid(
        row=6,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(10, 15)
    )

    # Login button
    login_button = tk.Button(
        buttons_frame,
        text="Login",
        font=("Arial", 11, "bold"),
        bg=EMERALD_GREEN,
        fg=WHITE,
        activebackground=LIGHT_GREEN,
        activeforeground=DARK_GREEN,
        relief="flat",
        cursor="hand2",
        command=validate_login
    )
    login_button.grid(
        row=0,
        column=0,
        padx=(0, 5),
        sticky="ew",
        ipadx=25,
        ipady=8
    )

    # Exit button
    exit_button = tk.Button(
        buttons_frame,
        text="Exit",
        font=("Arial", 11, "bold"),
        bg="#555555",
        fg=WHITE,
        activebackground="#777777",
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        command=lambda: exit_application(root)
    )
    exit_button.grid(
        row=0,
        column=1,
        padx=(5, 0),
        sticky="ew",
        ipadx=25,
        ipady=8
    )

    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)

    # Footer
    footer_label = tk.Label(
        main_frame,
        text="UNAD - Systems Engineering",
        font=("Arial", 8),
        fg=LIGHT_GREEN,
        bg=DARK_GREEN
    )
    footer_label.grid(
        row=7,
        column=0,
        columnspan=2,
        pady=(5, 0)
    )

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)

    # Press Enter to log in
    password_entry.bind(
        "<Return>",
        lambda event: validate_login()
    )
