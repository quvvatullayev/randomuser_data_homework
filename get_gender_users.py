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
    list_gender = []
    for i in data["results"]:
        if i["gender"] == "male":
            list_gender.append({"Male":1})
        elif i["gender"] == "female":
            list_gender.append({"Female":0})

    return list_gender
print(get_gender_users(json.loads(open("randomuser_data.json").read())))