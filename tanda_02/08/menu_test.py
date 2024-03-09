"""
Author: Enrique Mariño Jiménez
"""
import locale
from menu import Menu
from typeguard import typechecked
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_ = None


def main():
    menu = Menu("Introducir fecha", "Añadir días", "Añadir meses",
                "Añadir años", "Comparar fecha con otra fecha", "Mostrar fecha en formato largo",
                "Acabar", title="Menu")
    while True:
        option = menu.choose()
        if option != 1 and date_ is None and option != menu.last_option:
            print("Debes introducir primero una fecha\n")
            continue
        match option:
            case 1:
                date_to_input()
            case 2:
                add_days()
            case 3:
                add_months()
            case 4:
                add_years()
            case 5:
                compare_dates()
            case 6:
                print_date()
            case 7:
                exit(0)
    print("¡Adiós!")


@typechecked
def date_to_input():
    global date_
    date_str = input("Introduzca una fecha en formato dd/mm/aaaa: ")
    date_ = datetime.strptime(date_str, "%d/%m/%Y").date()


@typechecked
def add_days():
    global date_
    days = int(input(f"Introduzca el número de días a añadir a {date_.strftime('%d/%m/%Y')}: "))
    date_ += relativedelta(days=days)


@typechecked
def add_months():
    global date_
    months = int(input(f"Introduzca el número de meses a añadir a {date_.strftime('%d/%m/%Y')}: "))
    date_ += relativedelta(months=months)


@typechecked
def add_years():
    global date_
    years = int(input(f"Introduzca el número de años a añadir a {date_.strftime('%d/%m/%Y')}: "))
    date_ += relativedelta(years=years)


@typechecked
def compare_dates():
    global date_
    date_to_compare_str = input("Introduzca una fecha a comparar en formato dd/mm/aaaa: ")
    date_to_compare = datetime.strptime(date_to_compare_str, "%d/%m/%Y").date()
    if date_to_compare < date_:
        print("Fecha introducida < fecha almacenada.")
    elif date_to_compare == date_:
        print("Fecha introducida = fecha almacenada.")
    else:
        print("Fecha introducida > fecha almacenada.")


def print_date():
    print(date_.strftime("%A, %d de %B de %Y"))


if __name__ == '__main__':
    main()
