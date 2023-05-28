from rich.console import Console
from rich.table import Table


def snake_to_title(s):
    return s.replace("_", " ").title()


def display_data_as_table(data, column_names):
    console = Console()
    table = Table(show_header=True, header_style="bold yellow")

    for column_name in column_names:
        table.add_column(snake_to_title(column_name))

    for index, item in enumerate(data):
        try:
            table.add_row(*(str(item.get(name)) for name in column_names))
            if index < len(data) - 1:
                table.add_row(*[""] * len(column_names))
        except TypeError:
            print(f"Missing data in item: {item}")

    console.print(table)


def user_ok(message):
    while True:
        user_choice = input(f"{message}\n y/n\n")
        match user_choice:
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Please enter 'y' or 'n'.")
