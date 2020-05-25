from lab_10.Bank import Bank


def main():
    bank1 = Bank("Kolotushkina")
    bank2 = Bank("Pushkina", 2500, 120)
    bank3 = Bank("Moya", 1500, 2300, "Our Super Model", 1)
    banks = [bank1, bank2, bank3]
    [(print(str(quantity)), print(quantity)) for quantity in banks]

    print(bank1.address_static_field())
    print(bank1.number_of_cash_registers_static_field())

    print(bank1.colour_getter())
    bank1.colour_setter("White")
    print(bank1.colour_getter())


if __name__ == "__main__":
    main()
