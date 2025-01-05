sessions = [{"session_id": 4,
            "film_name": "haikyuu",
            "start_time": "17:30",
            "room_number": 10,
            "room_length": 9,
            "room_width": 8,
            "capacity": 72}, 
            {"session_id": 5,
            "film_name": "sherekilebi",
            "start_time": "17:20",
            "room_number": 10,
            "room_length": 9,
            "room_width": 8,
            "capacity": 72}]


def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")
        print("\n")