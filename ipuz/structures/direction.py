

def validate_direction(direction):
    splitted = direction.split(':')
    if len(splitted) > 2:
        return False
    direction_name = direction
    if len(splitted) <= 2:
        direction_name = splitted[0]
    return direction_name in (
        "Across",
        "Down",
        "Diagonal",
        "Diagonal Up",
        "Diagonal Down Left",
        "Diagonal Up Left",
        "Zones",
        "Clues",
    )
