import random

from common import process_user_input
from sessions import list_sessions, sessions


def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")


def signing_in():
    username_input = input("Please enter username: ")
    password_input = input("Please enter admin password: ")
    username = "username@gmail.com"
    password = "user12345"
    if username == username_input and password_input == password:
        print("you signed in succesfully")
    else:
        print("Username or password is incorrect")
        print("Please try again")
        return signing_in()


def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    return process_user_input()


def remove_session():
    if not sessions:
        print("No sessions found")
        return
    is_true = False
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print("\n")
    print("Removing session")
    print("Enter the session details")
    session_id = int(input("Session id: "))
    for session in sessions:
        if session_id == session["session_id"]:
            is_true = True
            sessions.remove(session)
    if is_true:
        print(f"Session with session id {session_id} removed successfully")
    else:
        print("wrong Id")
        return remove_session()


def random_session_id():
    session_id = random.randint(1, 1000)
    is_true = False
    for session in sessions:
        if session_id == session["session_id"]:
            is_true =True
    if is_true:
        return random_session_id()
    else: 
        return session_id


def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    # TODO: session_id may be used already, need to check
    session_id = random_session_id()
    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")
    sessions.append(session)


def edit_session():
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print("\n")
    is_true = False
    print("Editing session")
    print("Enter the session details")
    session_id = int(input("Session id: "))
    for session in sessions:
        if session_id == session["session_id"]:
            is_true = True
            room_length = int(input("Room length: "))
            room_width = int(input("Room width: "))
            capacity = room_length * room_width
            session["room_length"] = room_length
            session["room_width"] = room_width
            session["capacity"] = capacity
    if is_true:
        print("Session edited successfully")
    else:
        print("Wrong id")
        return edit_session()


def admin_loop():
    greetings()
    signing_in()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                remove_session()
            case "3":
                add_session()
            case "4":
                edit_session()
            case _:
                print("Invalid input")