
from datetime import datetime


class AffiliateValidator:
    """Validate the information entered for an affiliate."""

    IDENTIFICATION_TYPES = ["CC", "CE", "NUIP", "PAS"]
    EMPLOYMENT_TYPES = ["Empleado", "Independiente"]

    MIN_IDENTIFICATION_LENGTH = 8
    MAX_IDENTIFICATION_LENGTH = 11
    MIN_INCOME = 1000000

    @staticmethod
    def validate(
        identification_type,
        identification,
        full_name,
        income,
        service,
        employment_type,
        registration_date,
        valid_services=None,
        registered_ids=None
    ):
        """Validate all affiliate fields and return every error."""

        errors = []

        # Identification type validation
        if not identification_type:
            errors.append(
                "Tipo de identificación: debe seleccionar una opción."
            )
        elif identification_type not in (
            AffiliateValidator.IDENTIFICATION_TYPES
        ):
            errors.append(
                "Tipo de identificación: opción no válida."
            )

        # Identification number validation
        identification = str(identification).strip()

        if not identification:
            errors.append(
                "Número de identificación: este campo es obligatorio."
            )
        elif not identification.isdigit():
            errors.append(
                "Número de identificación: solo se permiten números."
            )
        elif not (
            AffiliateValidator.MIN_IDENTIFICATION_LENGTH
            <= len(identification)
            <= AffiliateValidator.MAX_IDENTIFICATION_LENGTH
        ):
            errors.append(
                "Número de identificación: debe tener entre "
                "8 y 11 dígitos."
            )
        elif registered_ids and identification in registered_ids:
            errors.append(
                "Número de identificación: este afiliado ya está registrado."
            )

        # Full name validation
        full_name = str(full_name).strip()

        if not full_name:
            errors.append(
                "Nombre completo: este campo es obligatorio."
            )
        elif not all(
            character.isalpha() or character in " -'’"
            for character in full_name
        ):
            errors.append(
                "Nombre completo: solo se permiten letras, "
                "espacios, guiones y apóstrofes."
            )
        elif len(full_name) < 3 or len(full_name) > 100:
            errors.append(
                "Nombre completo: debe tener entre 3 y 100 caracteres."
            )
        elif not any(character.isalpha() for character in full_name):
            errors.append(
                "Nombre completo: debe contener al menos una letra."
            )

        # Income validation
        income = str(income).strip()

        if not income:
            errors.append(
                "Ingresos actuales: este campo es obligatorio."
            )
        elif not income.isdigit():
            errors.append(
                "Ingresos actuales: solo se permiten números enteros."
            )
        elif int(income) < AffiliateValidator.MIN_INCOME:
            errors.append(
                "Ingresos actuales: debe tener ingresos iguales "
                "o superiores a $1.000.000."
            )

        # Service validation
        if not service:
            errors.append(
                "Servicio: debe seleccionar un servicio."
            )
        elif valid_services is not None and service not in valid_services:
            errors.append(
                "Servicio: la opción seleccionada no es válida."
            )

        # Employment type validation
        if not employment_type:
            errors.append(
                "Modalidad de empleo: debe seleccionar una opción."
            )
        elif employment_type not in (
            AffiliateValidator.EMPLOYMENT_TYPES
        ):
            errors.append(
                "Modalidad de empleo: seleccione Empleado "
                "o Independiente."
            )

        # Registration date validation
        registration_date = str(registration_date).strip()

        if not registration_date:
            errors.append(
                "Fecha de afiliación: este campo es obligatorio."
            )
        else:
            try:
                parsed_date = datetime.strptime(
                    registration_date,
                    "%d/%m/%Y"
                )

                if parsed_date.strftime("%d/%m/%Y") != registration_date:
                    raise ValueError("Invalid date format")

            except ValueError:
                errors.append(
                    "Fecha de afiliación: ingrese una fecha válida "
                    "en formato DD/MM/AAAA."
                )

        return errors
