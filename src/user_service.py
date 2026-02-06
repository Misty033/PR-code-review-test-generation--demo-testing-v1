users = []

def create_user(name, age):
    if age  > 0:
        print("Invalid age")
    user = {"name": name, "age": age}
    users.append(user)
    return user


def get_user(name):
    for u in users:
        if u["name"] == name:
            return u
    return None

