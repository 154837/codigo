
import tkinter as tk

from interfaces.login import create_login
from interfaces.affiliate_form import AffiliateForm


class Aplicacion:
    """Clase principal que controla el inicio de la aplicación."""

    def __init__(self):
        """Inicializar la aplicación."""

        self.ventana = tk.Tk()

        self.ventana.title("Compensándote")
        self.ventana.state("zoomed")

        self.formulario = None

        # Mostrar la ventana de inicio de sesión
        create_login(
            self.ventana,
            self.iniciar_sesion
        )

        self.ventana.mainloop()

    def iniciar_sesion(self):
        """Abrir el formulario principal después del ingreso."""

        # Ocultar la ventana de inicio de sesión
        self.ventana.withdraw()

        # Crear el formulario principal
        self.formulario = AffiliateForm(self.ventana)


if __name__ == "__main__":
    Aplicacion()
