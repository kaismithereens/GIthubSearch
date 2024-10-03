import sys
from tabulate import tabulate
from options import search_by_username, most_popular_python_repos, store_most_popular_python_repos, most_popular_harvard_repos, store_most_popular_harvard_repos, write_img_to_local, search_for_term, search_for_owner
from welcome import welcome_screen, welcome_screen_options
#tabulate.WIDE_CHARS_MODE = False

def main():

    welcome = welcome_screen()
    print(welcome)

    message = 'To display options click "y".'
    print(message)

    while True:
        try:
            selection = input()
            if selection.lower() == "y":

                my_options_message = welcome_screen_options()
                print()
                print("Select an option:")
                print()
                print(my_options_message[1])
                print(my_options_message[2])
                print(my_options_message[3])
                print(my_options_message[4])
                print(my_options_message[5])
                print(my_options_message[6])
                print(my_options_message[7])
                print(my_options_message[8])
                print()
                print(my_options_message[9])


            elif selection == "1":

                my_options_message = welcome_screen_options()
                username = "kaismithereens"
                owner_repos = search_by_username(username)
                print(tabulate(owner_repos, headers = 'keys',  maxcolwidths=[30, 50, 50],tablefmt="rounded_grid"))
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "2":

                my_options_message = welcome_screen_options()
                harvard_repos = most_popular_harvard_repos()
                print(tabulate(harvard_repos, headers = "keys", maxcolwidths=[None, 30, None], tablefmt="rounded_grid"))
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "3":

                my_options_message = welcome_screen_options()
                python_repos = most_popular_python_repos()
                print(tabulate(python_repos, headers = "keys", maxcolwidths=[21, 30, None], tablefmt="rounded_grid"))
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "4":

                my_options_message = welcome_screen_options()
                store_most_popular_python_repos()
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "5":

                my_options_message = welcome_screen_options()
                store_most_popular_harvard_repos()
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "6":

                my_options_message = welcome_screen_options()
                write_img_to_local()
                print("Your profile picture has been stored locally.")
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "7":

                my_options_message = welcome_screen_options()
                search_response = search_for_term()
                if search_response != []:
                    print(tabulate(search_response, headers = "keys", maxcolwidths=[21, 30, 50], tablefmt="rounded_grid"))
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            elif selection == "8":

                my_options_message = welcome_screen_options()
                owner_repos = search_for_owner()
                if owner_repos != []:
                    print(tabulate(owner_repos, headers = 'keys',  maxcolwidths=[30, 50, 50],tablefmt="rounded_grid"))
                print()
                print(my_options_message[0])
                print()
                print(my_options_message[9])
                print()

            else:
                my_options_message = welcome_screen_options()
                print()
                print("Select an option:")
                print()
                print(my_options_message[1])
                print(my_options_message[2])
                print(my_options_message[3])
                print(my_options_message[4])
                print(my_options_message[5])
                print(my_options_message[6])
                print(my_options_message[7])
                print(my_options_message[8])
                print()
                print(my_options_message[9])

        except EOFError:
            sys.exit("Goodbye.")
        except KeyboardInterrupt:
            sys.exit("Goodbye.")


if __name__ == "__main__":
    main()
