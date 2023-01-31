from private.config import admins


def verification(user_id):
    for admin in admins:
        if admin == user_id: return True
    return False

