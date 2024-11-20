from admin import admin_loop
from common import process_user_input
from sessions import sessions, list_sessions
from users_tickets import tickets, list_user_tickets


def list_menu_items():
    print("1. list sessions")
    print("2. search movie")
    print("3. my tickets")
    print("4. admin")
    return process_user_input()


def greetings():
    print("Welcome to the movie ticket booking system")
    print("Please enter EXIT to exit")


def search_movie():
    is_true = False
    movie_title = input("Please enter movie title ")
    for session in sessions:
        if movie_title == session["film_name"]:
            print(f"\tFilm name: {session['film_name']}")
            print(f"\tStart time: {session['start_time']}")
            is_true = True
            while True:
                buying_ticket = input("Do you want to buy the ticket? ")
                match buying_ticket.lower():
                    case "yes":
                        print("Successfully bought ticket.")
                        tickets.append(session)
                        return
                    case "no":
                        return
                    case _:
                        print("Invalid input")
    if not is_true:
        print("The movie is not availale")
        return search_movie()
        

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                search_movie()
            case "3":
                list_user_tickets()
            case "4":
                admin_loop()
            case _:
                print("Invalid input")