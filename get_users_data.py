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
        dict1 = {}
        for e,r in (i).items():
            if e == "name":
                for w,q in r.items():
                    if w == 'first':
                        dict1["first_name"] = q

                    elif w == 'last':
                        dict1['last_name'] = q
            elif e == "phone":
                dict1["phone_number"] = r
            list1.append(dict1)

    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)

    for i in list2:
        print(i)
    return ''

print(get_users_data(json.loads(open("randomuser_data.json").read())))