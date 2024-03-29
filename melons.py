"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    order_type = None
    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total
    
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A deal with the US Government. """
    order_type = "government"
    taxes = 0

    # no taxes.
    # variable passed_inspection which is False until a successful inspection occurs
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
    
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    


