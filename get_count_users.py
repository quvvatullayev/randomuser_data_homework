import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    sum = 0
    for i in data["results"]:
        for e,r in dict(i).items():
            if e == "email":
                sum += 1
    return sum
print(get_count_users(get_data.get_data("randomuser_data.json")))