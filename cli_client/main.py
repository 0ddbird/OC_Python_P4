from cli_client.menu.menu import display_menu, handle_user_selection
from cli_client.menu.menu_options import main_menu


def main():
    current_menu = main_menu

    while True:
        selected_option = display_menu(current_menu)
        next_menu = handle_user_selection(selected_option)
        if next_menu is None:
            break
        else:
            current_menu = next_menu


if __name__ == "__main__":
    main()
