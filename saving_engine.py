import json


def save(account):

    new_data = {account.id: {
        "name": account.name,
        "email": account.email,
        "password": account.secret_password,
        "post": account.posts,
        "followers": account.followers,
        "followings": account.following
    }
    }
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            data.update(new_data)

    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_data, file, indent=4)

    else:
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)


def load():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        return None
