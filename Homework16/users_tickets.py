from sessions import sessions, list_sessions
tickets = []


def list_user_tickets():
    if not tickets:
        print("You don't have tickets")
        return
    for ticket in tickets:
        print("My tickets: ")
        print(f"\tFilm name: {ticket['film_name']}")
        print(f"\tStart time: {ticket['start_time']}")
        print("\n")