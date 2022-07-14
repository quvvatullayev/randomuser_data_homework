import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    list1 = []
    for i in data["results"]:
        for e,r in dict(i).items():
            if e == "email":
                    list1.append(r)
    return list1

print(get_email(json.loads(open("randomuser_data.json").read())))