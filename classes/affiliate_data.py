
class Affiliate:
    """Represent an affiliate registered in the system."""

    def __init__(
        self,
        identification_type,
        identification,
        full_name,
        income,
        service,
        employment_type,
        fee,
        registration_date
    ):
        self.identification_type = identification_type
        self.identification = identification
        self.full_name = full_name
        self.income = income
        self.service = service
        self.employment_type = employment_type
        self.fee = fee
        self.registration_date = registration_date

    def get_information(self):
        """Return the affiliate information."""
        return {
            "identification_type": self.identification_type,
            "identification": self.identification,
            "full_name": self.full_name,
            "income": self.income,
            "service": self.service,
            "employment_type": self.employment_type,
            "fee": self.fee,
            "registration_date": self.registration_date
        }

    def __str__(self):
        """Return a readable representation of the affiliate."""
        return (
            f"{self.full_name} - "
            f"{self.identification} - "
            f"${self.fee:,.0f}"
        )
