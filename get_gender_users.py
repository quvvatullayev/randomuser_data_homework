import json
def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    list1 = []
    dict1 = {}
    for i in data["results"]:
        for k,q in i.items():
            if k == "gender":
                if q == "female":
                    dict1[q.capitalize()] = 0


                else:
                    dict1[q.capitalize()] = 1
                list1.append(dict1)
    return list1
print(get_gender_users(json.loads(open("randomuser_data.json").read())))