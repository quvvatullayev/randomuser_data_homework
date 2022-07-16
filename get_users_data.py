import json

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    list1 = []
    for i in data["results"]:
            list1.append({"first_name": i["name"]["first"], "last_name": i["name"]["last"], "phone_number": i["phone"]})

    return list1

print(get_users_data(json.loads(open("randomuser_data.json").read())))











