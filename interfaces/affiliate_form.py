import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from classes.affiliate_data import Affiliate
from classes.affiliate_validator import AffiliateValidator
from structures.data_structures import Stack, Queue, AffiliateList


# =========================================================
# COLORES DE LA APLICACION
# =========================================================

DARK_GREEN = "#073B2A"
PRIMARY_GREEN = "#006B4F"
EMERALD_GREEN = "#00A878"
LIGHT_GREEN = "#65D6A6"
PALE_GREEN = "#E8F5EE"
BACKGROUND = "#F1F5F2"
WHITE = "#FFFFFF"
TEXT_COLOR = "#173D30"
RED = "#C62828"
GRAY = "#555555"


# =========================================================
# CLASE PRINCIPAL
# =========================================================

class AffiliateForm:
    """Ventana principal para registrar y administrar afiliados."""

    IDENTIFICATION_OPTIONS = [
        "CC",
        "CE",
        "NUIP",
        "PAS"
    ]

    EMPLOYMENT_OPTIONS = [
        "Empleado",
        "Independiente"
    ]

    SERVICE_OPTIONS = [
        "Subsidio de desempleo",
        "Ingreso a parque",
        "Curso de formación",
        "Paquete de viaje",
        "Medicina preventiva"
    ]

    STRUCTURE_OPTIONS = [
        "Pila",
        "Cola",
        "Lista"
    ]

    INCOME_RANGES = {
        "$1.000.000 – $2.000.000": 1000000,
        "Más de $2.000.000 – $3.000.000": 2000001,
        "Más de $3.000.000 – $4.000.000": 3000001,
        "Más de $4.000.000 – $5.000.000": 4000001,
        "Más de $5.000.000": 5000001
    }

    def __init__(self, root):
        """Inicializar la ventana principal."""

        self.root = root

        self.window = tk.Toplevel(root)
        self.window.title(
            "Compensándote - Control de Afiliados"
        )

        self.window.state("zoomed")
        self.window.minsize(1000, 600)
        self.window.configure(bg=BACKGROUND)

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.exit_application
        )

        # Estructuras de datos
        self.stack = Stack()
        self.queue = Queue()
        self.affiliate_list = AffiliateList()

        # Variables del formulario
        self.identification_type = tk.StringVar()
        self.identification = tk.StringVar()
        self.full_name = tk.StringVar()

        self.income = tk.StringVar()
        self.income_range = tk.StringVar()
        self.exact_income = tk.StringVar()

        self.employment_type = tk.StringVar()
        self.service = tk.StringVar()

        self.registration_date = tk.StringVar(
            value=datetime.now().strftime("%d/%m/%Y")
        )

        self.fee = tk.StringVar(
            value="Pendiente"
        )

        self.structure_type = tk.StringVar(
            value="Lista"
        )

        # Actualización automática de la tarifa
        self.income.trace_add(
            "write",
            self.update_fee
        )

        self.income_range.trace_add(
            "write",
            self.update_income_value
        )

        self.exact_income.trace_add(
            "write",
            self.update_income_value
        )

        self.employment_type.trace_add(
            "write",
            self.update_fee
        )

        self.service.trace_add(
            "write",
            self.update_income_visibility
        )

        self.service.trace_add(
            "write",
            self.update_fee
        )

        # Construir interfaz
        self.create_interface()

    # =====================================================
    # INTERFAZ PRINCIPAL
    # =====================================================

    def create_interface(self):
        """Crear la interfaz completa."""

        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.create_header()
        self.create_content()
        self.create_buttons()

    # =====================================================
    # ENCABEZADO
    # =====================================================

    def create_header(self):
        """Crear el encabezado verde."""

        header_frame = tk.Frame(
            self.window,
            bg=DARK_GREEN,
            height=65
        )

        header_frame.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        header_frame.grid_propagate(False)
        header_frame.columnconfigure(0, weight=1)

        title = tk.Label(
            header_frame,
            text="COMPENSÁNDOTE - CONTROL DE AFILIADOS",
            font=("Arial", 17, "bold"),
            fg=LIGHT_GREEN,
            bg=DARK_GREEN
        )

        title.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="w"
        )

        student = tk.Label(
            header_frame,
            text="Carlos Alexander Coral Basallo | Grupo 298",
            font=("Arial", 9),
            fg=WHITE,
            bg=DARK_GREEN
        )

        student.grid(
            row=0,
            column=1,
            padx=20,
            sticky="e"
        )

    # =====================================================
    # AREA DE CONTENIDO
    # =====================================================

    def create_content(self):
        """Crear el formulario y la tabla de afiliados."""

        content_frame = tk.Frame(
            self.window,
            bg=BACKGROUND
        )

        content_frame.grid(
            row=1,
            column=0,
            padx=12,
            pady=10,
            sticky="nsew"
        )

        content_frame.rowconfigure(0, weight=1)
        content_frame.columnconfigure(0, weight=0)
        content_frame.columnconfigure(1, weight=1)

        self.create_form(content_frame)
        self.create_table(content_frame)

    # =====================================================
    # FORMULARIO DE AFILIACION
    # =====================================================

    def create_form(self, parent):
        """Crear los campos de registro."""

        form_frame = tk.LabelFrame(
            parent,
            text="REGISTRO DE AFILIADOS",
            font=("Arial", 11, "bold"),
            fg=PRIMARY_GREEN,
            bg=WHITE,
            padx=12,
            pady=10,
            width=355
        )

        form_frame.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="ns"
        )

        form_frame.grid_propagate(False)
        form_frame.columnconfigure(1, weight=1)

        # Tipo de identificación
        self.add_label(
            form_frame,
            "Tipo identificación:",
            0
        )

        self.identification_combo = ttk.Combobox(
            form_frame,
            textvariable=self.identification_type,
            values=self.IDENTIFICATION_OPTIONS,
            state="readonly",
            font=("Arial", 10)
        )

        self.identification_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        # Número de identificación
        self.add_label(
            form_frame,
            "Número identificación:",
            1
        )

        self.identification_entry = tk.Entry(
            form_frame,
            textvariable=self.identification,
            font=("Arial", 10)
        )

        self.identification_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        # Nombre completo
        self.add_label(
            form_frame,
            "Nombre completo:",
            2
        )

        self.name_entry = tk.Entry(
            form_frame,
            textvariable=self.full_name,
            font=("Arial", 10)
        )

        self.name_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        # Rango de ingresos
        self.add_label(
            form_frame,
            "Ingresos actuales:",
            3
        )

        self.income_combo = ttk.Combobox(
            form_frame,
            textvariable=self.income_range,
            values=list(self.INCOME_RANGES.keys()),
            state="readonly",
            font=("Arial", 9)
        )

        self.income_combo.grid(
            row=3,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        self.income_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.update_income_value()
        )

        # Ingreso exacto para medicina preventiva
        self.exact_income_label = tk.Label(
            form_frame,
            text="Ingreso exacto:",
            font=("Arial", 9, "bold"),
            fg=TEXT_COLOR,
            bg=WHITE
        )

        self.exact_income_entry = tk.Entry(
            form_frame,
            textvariable=self.exact_income,
            font=("Arial", 10)
        )

        # Modalidad de empleo
        self.add_label(
            form_frame,
            "Modalidad de empleo:",
            5
        )

        self.employment_combo = ttk.Combobox(
            form_frame,
            textvariable=self.employment_type,
            values=self.EMPLOYMENT_OPTIONS,
            state="readonly",
            font=("Arial", 10)
        )

        self.employment_combo.grid(
            row=5,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        # Servicio de afiliación
        self.add_label(
            form_frame,
            "Servicio de afiliación:",
            6
        )

        self.service_combo = ttk.Combobox(
            form_frame,
            textvariable=self.service,
            values=self.SERVICE_OPTIONS,
            state="readonly",
            font=("Arial", 10)
        )

        self.service_combo.grid(
            row=6,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        self.service_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.update_income_visibility()
        )

        # Fecha de afiliación
        self.add_label(
            form_frame,
            "Fecha de afiliación:",
            7
        )

        date_entry = tk.Entry(
            form_frame,
            textvariable=self.registration_date,
            state="readonly",
            font=("Arial", 10),
            readonlybackground=PALE_GREEN
        )

        date_entry.grid(
            row=7,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        # Tarifa de afiliación
        self.add_label(
            form_frame,
            "Tarifa de afiliación:",
            8
        )

        fee_entry = tk.Entry(
            form_frame,
            textvariable=self.fee,
            state="readonly",
            font=("Arial", 10, "bold"),
            readonlybackground=PALE_GREEN,
            fg=PRIMARY_GREEN
        )

        fee_entry.grid(
            row=8,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        # Estructura de datos
        self.add_label(
            form_frame,
            "Estructura de datos:",
            9
        )

        structure_combo = ttk.Combobox(
            form_frame,
            textvariable=self.structure_type,
            values=self.STRUCTURE_OPTIONS,
            state="readonly",
            font=("Arial", 10)
        )

        structure_combo.grid(
            row=9,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        structure_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_table()
        )

    # =====================================================
    # ETIQUETAS DEL FORMULARIO
    # =====================================================

    @staticmethod
    def add_label(parent, text, row):
        """Crear una etiqueta."""

        label = tk.Label(
            parent,
            text=text,
            font=("Arial", 9, "bold"),
            fg=TEXT_COLOR,
            bg=WHITE
        )

        label.grid(
            row=row,
            column=0,
            padx=5,
            pady=7,
            sticky="w"
        )

    # =====================================================
    # INGRESOS POR RANGO Y VALOR EXACTO
    # =====================================================

    def update_income_visibility(self, *_):
        """Mostrar el ingreso exacto solo para medicina preventiva."""

        if self.service.get() == "Medicina preventiva":

            self.exact_income_label.grid(
                row=4,
                column=0,
                padx=5,
                pady=7,
                sticky="w"
            )

            self.exact_income_entry.grid(
                row=4,
                column=1,
                padx=5,
                pady=7,
                sticky="ew"
            )

        else:
            self.exact_income_label.grid_remove()
            self.exact_income_entry.grid_remove()

        self.update_income_value()

    def update_income_value(self, *_):
        """Actualizar el ingreso numérico utilizado en los cálculos."""

        selected_range = self.income_range.get()

        if not selected_range:
            self.income.set("")
            self.update_fee()
            return

        if self.service.get() == "Medicina preventiva":

            self.income.set(
                self.exact_income.get().strip()
            )

        else:

            self.income.set(
                str(self.INCOME_RANGES[selected_range])
            )

        self.update_fee()

    # =====================================================
    # CALCULO DE TARIFAS BASE
    # =====================================================

    @staticmethod
    def calculate_base_fee(income, employment_type):
        """Calcular la tarifa base según ingresos y empleo."""

        if income < 1000000:
            raise ValueError(
                "Los ingresos deben ser iguales o superiores "
                "a $1.000.000."
            )

        if employment_type == "Empleado":

            if income <= 2000000:
                return 45000

            if income <= 3000000:
                return 60000

            if income <= 4000000:
                return 75000

            if income <= 5000000:
                return 90000

            return 150000

        if employment_type == "Independiente":

            if income <= 2000000:
                return 10000

            if income <= 3000000:
                return 20000

            if income <= 4000000:
                return 30000

            if income <= 5000000:
                return 40000

            return 80000

        raise ValueError(
            "Debe seleccionar una modalidad de empleo válida."
        )

    # =====================================================
    # CALCULO DE SERVICIOS ADICIONALES
    # =====================================================

    @staticmethod
    def calculate_additional_fee(income, service):
        """Calcular el costo adicional del servicio."""

        additional_fees = {
            "Subsidio de desempleo": 0,
            "Ingreso a parque": 2500,
            "Curso de formación": 7500,
            "Paquete de viaje": 10000
        }

        if service == "Medicina preventiva":
            return income // 10

        if service in additional_fees:
            return additional_fees[service]

        raise ValueError(
            "Debe seleccionar un servicio válido."
        )

    # =====================================================
    # CALCULO TOTAL
    # =====================================================

    def calculate_total_fee(self):
        """Calcular el valor total de afiliación."""

        income = int(self.income.get())

        base_fee = self.calculate_base_fee(
            income,
            self.employment_type.get()
        )

        additional_fee = self.calculate_additional_fee(
            income,
            self.service.get()
        )

        return base_fee + additional_fee

    # =====================================================
    # ACTUALIZACION AUTOMATICA DE TARIFA
    # =====================================================

    def update_fee(self, *_):
        """Actualizar la tarifa cuando cambien los valores."""

        try:

            if (
                not self.income.get()
                or not self.employment_type.get()
                or not self.service.get()
            ):
                self.fee.set("Pendiente")
                return

            income = int(self.income.get())

            if income < 1000000:
                self.fee.set("No permitido")
                return

            total = self.calculate_total_fee()

            formatted = f"${total:,.0f}".replace(",", ".")

            self.fee.set(formatted)

        except (ValueError, TypeError):
            self.fee.set("Pendiente")

    # =====================================================
    # TABLA DE AFILIADOS
    # =====================================================

    def create_table(self, parent):
        """Crear la tabla de afiliados."""

        table_frame = tk.LabelFrame(
            parent,
            text="AFILIADOS REGISTRADOS",
            font=("Arial", 11, "bold"),
            fg=PRIMARY_GREEN,
            bg=BACKGROUND,
            padx=8,
            pady=8
        )

        table_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        columns = (
            "type",
            "identification",
            "name",
            "income",
            "employment",
            "service",
            "fee",
            "date"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "type": "Tipo ID",
            "identification": "Identificación",
            "name": "Nombre completo",
            "income": "Ingresos",
            "employment": "Modalidad",
            "service": "Servicio",
            "fee": "Tarifa",
            "date": "Fecha"
        }

        widths = {
            "type": 75,
            "identification": 110,
            "name": 180,
            "income": 110,
            "employment": 110,
            "service": 150,
            "fee": 110,
            "date": 100
        }

        for column in columns:

            self.tree.heading(
                column,
                text=headings[column]
            )

            self.tree.column(
                column,
                width=widths[column],
                minwidth=65,
                anchor="center"
            )

        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scroll.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scroll.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Arial", 9),
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 9, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", EMERALD_GREEN)],
            foreground=[("selected", WHITE)]
        )

    # =====================================================
    # BOTONES INFERIORES
    # =====================================================

    def create_buttons(self):
        """Crear los botones inferiores."""

        buttons_frame = tk.Frame(
            self.window,
            bg=BACKGROUND,
            padx=12,
            pady=10
        )

        buttons_frame.grid(
            row=2,
            column=0,
            sticky="ew"
        )

        buttons = [
            ("Registrar", EMERALD_GREEN, self.register_affiliate),
            ("Eliminar", RED, self.delete_affiliate),
            ("Reporte", PRIMARY_GREEN, self.generate_report),
            ("Limpiar", LIGHT_GREEN, self.clear_form),
            ("Salir", GRAY, self.exit_application)
        ]

        for column, (text, color, command) in enumerate(buttons):

            button = tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 10, "bold"),
                bg=color,
                fg=DARK_GREEN if color == LIGHT_GREEN else WHITE,
                activebackground=LIGHT_GREEN,
                relief="flat",
                cursor="hand2",
                command=command
            )

            button.grid(
                row=0,
                column=column,
                padx=5,
                pady=5,
                sticky="ew",
                ipady=8
            )

            buttons_frame.columnconfigure(
                column,
                weight=1
            )

    # =====================================================
    # OBTENER ESTRUCTURA SELECCIONADA
    # =====================================================

    def get_selected_structure(self):
        """Retornar la estructura de datos seleccionada."""

        structure = self.structure_type.get()

        if structure == "Pila":
            return self.stack

        if structure == "Cola":
            return self.queue

        return self.affiliate_list

    # =====================================================
    # OBTENER IDENTIFICACIONES REGISTRADAS
    # =====================================================

    def get_all_registered_ids(self):
        """Obtener todas las identificaciones registradas."""

        identifiers = []

        for structure in (
            self.stack,
            self.queue,
            self.affiliate_list
        ):

            for affiliate in structure.get_all():

                identifiers.append(
                    affiliate.identification
                )

        return identifiers

    # =====================================================
    # VENTANA PERSONALIZADA DE ERRORES
    # =====================================================

    def show_validation_errors(self, errors):
        """Mostrar todos los errores en una ventana."""

        error_window = tk.Toplevel(self.window)

        error_window.title("Errores de validación")
        error_window.geometry("560x400")
        error_window.minsize(400, 250)
        error_window.configure(bg=BACKGROUND)

        error_window.transient(self.window)
        error_window.grab_set()

        error_window.rowconfigure(1, weight=1)
        error_window.columnconfigure(0, weight=1)

        title = tk.Label(
            error_window,
            text="NO SE PUDO REGISTRAR EL AFILIADO",
            font=("Arial", 13, "bold"),
            fg=RED,
            bg=BACKGROUND
        )

        title.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="w"
        )

        errors_frame = tk.Frame(
            error_window,
            bg=WHITE,
            padx=15,
            pady=10
        )

        errors_frame.grid(
            row=1,
            column=0,
            padx=15,
            pady=5,
            sticky="nsew"
        )

        errors_frame.columnconfigure(0, weight=1)

        for row, error in enumerate(errors):

            error_label = tk.Label(
                errors_frame,
                text=f"• {error}",
                font=("Arial", 10),
                fg=RED,
                bg=WHITE,
                wraplength=480,
                justify="left",
                anchor="w"
            )

            error_label.grid(
                row=row,
                column=0,
                padx=5,
                pady=7,
                sticky="ew"
            )

        buttons_frame = tk.Frame(
            error_window,
            bg=BACKGROUND
        )

        buttons_frame.grid(
            row=2,
            column=0,
            pady=15
        )

        tk.Button(
            buttons_frame,
            text="Aceptar",
            bg=PRIMARY_GREEN,
            fg=WHITE,
            width=12,
            command=error_window.destroy
        ).grid(
            row=0,
            column=0,
            padx=8
        )

        tk.Button(
            buttons_frame,
            text="Salir",
            bg=GRAY,
            fg=WHITE,
            width=12,
            command=self.exit_application
        ).grid(
            row=0,
            column=1,
            padx=8
        )

    # =====================================================
    # REGISTRAR AFILIADO
    # =====================================================

    def register_affiliate(self):
        """Validar y registrar un afiliado."""

        errors = AffiliateValidator.validate(
            self.identification_type.get(),
            self.identification.get(),
            self.full_name.get(),
            self.income.get(),
            self.service.get(),
            self.employment_type.get(),
            self.registration_date.get(),
            valid_services=self.SERVICE_OPTIONS,
            registered_ids=self.get_all_registered_ids()
        )

        if not self.income_range.get():

            errors.append(
                "Ingresos mensuales: debe seleccionar un rango."
            )

        if self.service.get() == "Medicina preventiva":

            if not self.exact_income.get().strip():

                errors.append(
                    "Ingreso exacto: es obligatorio para calcular "
                    "el 10% de medicina preventiva."
                )

            elif not self.exact_income.get().strip().isdigit():

                errors.append(
                    "Ingreso exacto: solamente debe contener números."
                )

            elif self.income_range.get() in self.INCOME_RANGES:

                exact_value = int(
                    self.exact_income.get().strip()
                )

                lower_bound = self.INCOME_RANGES[
                    self.income_range.get()
                ]

                range_labels = list(
                    self.INCOME_RANGES.keys()
                )

                range_index = range_labels.index(
                    self.income_range.get()
                )

                upper_bounds = [
                    2000000,
                    3000000,
                    4000000,
                    5000000,
                    None
                ]

                upper_bound = upper_bounds[range_index]

                if exact_value < lower_bound or (
                    upper_bound is not None
                    and exact_value > upper_bound
                ):

                    errors.append(
                        "Ingreso exacto: el valor debe estar dentro "
                        "del rango mensual seleccionado."
                    )

        if errors:

            self.show_validation_errors(errors)
            return

        try:

            total_fee = self.calculate_total_fee()

            affiliate = Affiliate(
                identification_type=self.identification_type.get(),
                identification=self.identification.get(),
                full_name=self.full_name.get(),
                income=int(self.income.get()),
                service=self.service.get(),
                employment_type=self.employment_type.get(),
                fee=total_fee,
                registration_date=self.registration_date.get()
            )

            structure = self.get_selected_structure()

            if self.structure_type.get() == "Pila":

                structure.push(affiliate)

            elif self.structure_type.get() == "Cola":

                structure.enqueue(affiliate)

            else:

                structure.add(affiliate)

            self.refresh_table()
            self.clear_form()

            formatted_fee = (
                f"${total_fee:,.0f}".replace(",", ".")
            )

            messagebox.showinfo(
                "Registro exitoso",
                "El afiliado se registró correctamente.\n\n"
                f"Nombre: {affiliate.full_name}\n"
                f"Tarifa: {formatted_fee}",
                parent=self.window
            )

        except (ValueError, TypeError, AttributeError) as error:

            self.show_validation_errors([
                f"No fue posible registrar el afiliado: {error}"
            ])

    # =====================================================
    # LIMPIAR FORMULARIO
    # =====================================================

    def clear_form(self):
        """Limpiar todos los campos."""

        self.identification_type.set("")
        self.identification.set("")
        self.full_name.set("")

        self.income.set("")
        self.income_range.set("")
        self.exact_income.set("")

        self.employment_type.set("")
        self.service.set("")

        self.exact_income_label.grid_remove()
        self.exact_income_entry.grid_remove()

        self.registration_date.set(
            datetime.now().strftime("%d/%m/%Y")
        )

        self.fee.set("Pendiente")

        self.identification_entry.focus_set()

    # =====================================================
    # OBTENER ETIQUETA DEL RANGO DE INGRESOS
    # =====================================================

    def get_income_range_label(self, income):
        """Retornar el rango correspondiente al ingreso guardado."""

        if income <= 2000000:
            return "$1M - $2M"

        if income <= 3000000:
            return ">$2M - $3M"

        if income <= 4000000:
            return ">$3M - $4M"

        if income <= 5000000:
            return ">$4M - $5M"

        return ">$5M"

    # =====================================================
    # ACTUALIZAR TABLA
    # =====================================================

    def refresh_table(self):
        """Actualizar la tabla con los afiliados registrados."""

        for item in self.tree.get_children():
            self.tree.delete(item)

        affiliates = self.get_selected_structure().get_all()

        for affiliate in affiliates:

            if affiliate.service == "Medicina preventiva":

                income_formatted = (
                    f"${affiliate.income:,.0f}".replace(",", ".")
                )

            else:

                income_formatted = self.get_income_range_label(
                    affiliate.income
                )

            fee_formatted = (
                f"${affiliate.fee:,.0f}".replace(",", ".")
            )

            self.tree.insert(
                "",
                tk.END,
                iid=affiliate.identification,
                values=(
                    affiliate.identification_type,
                    affiliate.identification,
                    affiliate.full_name,
                    income_formatted,
                    affiliate.employment_type,
                    affiliate.service,
                    fee_formatted,
                    affiliate.registration_date
                )
            )

    # =====================================================
    # ELIMINAR AFILIADO
    # =====================================================

    def delete_affiliate(self):
        """Eliminar un afiliado según la estructura seleccionada."""

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "Atención",
                "Seleccione un afiliado de la tabla.",
                parent=self.window
            )

            return

        identification = selected[0]
        structure_name = self.structure_type.get()

        if not messagebox.askyesno(
            "Confirmar eliminación",
            "¿Desea eliminar el afiliado seleccionado?",
            parent=self.window
        ):
            return

        structure = self.get_selected_structure()
        affiliates = structure.get_all()

        # Pila: solo se puede eliminar el último elemento.
        if structure_name == "Pila":

            if not affiliates or (
                affiliates[-1].identification != identification
            ):

                messagebox.showwarning(
                    "Operación no permitida",
                    "En una pila solamente se puede eliminar "
                    "el último afiliado registrado.",
                    parent=self.window
                )

                return

            removed = structure.pop()

        # Cola: solo se puede eliminar el primer elemento.
        elif structure_name == "Cola":

            if not affiliates or (
                affiliates[0].identification != identification
            ):

                messagebox.showwarning(
                    "Operación no permitida",
                    "En una cola solamente se puede eliminar "
                    "el primer afiliado registrado.",
                    parent=self.window
                )

                return

            removed = structure.dequeue()

        # Lista: se puede eliminar el afiliado seleccionado.
        else:

            removed = structure.remove(identification)

        if removed is None:

            messagebox.showerror(
                "Error",
                "No fue posible eliminar el afiliado.",
                parent=self.window
            )

            return

        self.refresh_table()

        messagebox.showinfo(
            "Eliminación exitosa",
            f"Se eliminó a {removed.full_name}.",
            parent=self.window
        )

    # =====================================================
    # GENERAR REPORTE
    # =====================================================

    def generate_report(self):
        """Generar un reporte básico de afiliados."""

        structure = self.get_selected_structure()
        affiliates = structure.get_all()

        if not affiliates:

            messagebox.showinfo(
                "Reporte",
                "No existen afiliados registrados.",
                parent=self.window
            )

            return

        report = (
            f"Estructura: {self.structure_type.get()}\n"
            f"Total de afiliados: {structure.size()}\n\n"
        )

        for affiliate in affiliates:

            report += (
                f"Nombre: {affiliate.full_name}\n"
                f"Identificación: {affiliate.identification}\n"
                f"Tarifa: ${affiliate.fee:,.0f}\n\n"
            )

        messagebox.showinfo(
            "Reporte de afiliados",
            report,
            parent=self.window
        )

    # =====================================================
    # CERRAR APLICACION
    # =====================================================

    def exit_application(self):
        """Cerrar la aplicación completa."""

        self.root.destroy()