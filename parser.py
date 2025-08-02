def parse_command(message):
    parts = message.split()
    if not parts:
        return None, []

    cmd = parts[0].upper()
    args = parts[1:]

    if cmd == "LIST" and len(args) == 1:
        return "LIST", args
    elif cmd == "DELETE" and len(args) == 1:
        return "DELETE", args
    elif cmd == "MOVE" and len(args) == 2:
        return "MOVE", args
    elif cmd == "SUMMARY" and len(args) == 1:
        return "SUMMARY", args
    else:
        return None, []
