class Bank:
    address_static_field = "Kulparkivska"
    number_of_cash_registers_static_field = 5
    colour_private_field = "white"

    def __init__(self, name="none", number_of_customers=0, number_of_loans_issued=0,
                 type_of_safe="Choose,please", working_time=0, currency="UAH"):
        self.name = name
        self.number_of_customers = number_of_customers
        self.number_of_loans_issued = number_of_loans_issued
        self.type_of_safe = type_of_safe
        self.working_time = working_time
        self.currency = currency

    def __del__(self):
        pass

    def __str__(self):
        return "Name is  {} \t Number of customers is {} \t Number of loan issued is {}" \
               "\t Type of safe is {} \t Working time is {}\t Producing Country is {}" \
            .format(self.name, self.number_of_customers, self.number_of_loans_issued, self.type_of_safe,
                    self.working_time, self.currency)

    @staticmethod
    def address_static_method():
        return Bank.address_static_field

    @staticmethod
    def number_of_cash_registers_static_field_static_method():
        return Bank.number_of_cash_registers_static_field

    def colour_getter(self):
        return self.colour_private_field

    def colour_setter(self, colour_private_field):
        self.colour_private_field = colour_private_field
