from datetime import datetime


def snake_to_regular_dict(d):
    new_dict = {}
    for key, value in d.items():
        new_key = key.replace('_', ' ').title()
        new_dict[new_key] = value
    return new_dict


def sort_by_date(list_of_dicts, date_key):
    """
    Sorts a list of dictionaries based on a date key-value.

    Args:
        list_of_dicts (list): A list of dictionaries to be sorted.
        date_key (str): The key in the dictionaries that contains the date value.

    Returns:
        list: The sorted list of dictionaries.
    """
    # Convert the date strings to datetime objects
    for d in list_of_dicts:
        d[date_key] = datetime.strptime(d[date_key], '%Y-%m-%d')

    # Sort the list of dictionaries based on the date key-value
    sorted_list = sorted(list_of_dicts, key=lambda x: x[date_key], reverse=True)

    # Convert the datetime objects back to date strings
    for d in sorted_list:
        d[date_key] = d[date_key].strftime('%Y-%m-%d')

    return sorted_list
