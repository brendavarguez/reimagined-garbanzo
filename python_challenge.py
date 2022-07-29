import pprint
import requests
import collections
import datetime as dt

def get_data():
    """
    Function to get items from stack exchange url.

    Inputs: None

    Outputs: list of items from url
    """
    # ----- 1. Conectarse al enlace ----- #
    res = requests.get("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow")
    res = res.json()
    items = res['items']
    return items

def main():
    # download data
    items = get_data()

    # ----- 2. Obtener el número de respuestas contestadas y no contestadas ----- #
    # get countings
    counts = collections.Counter((item["is_answered"] for item in items))
    print("1. Get number of answered and unanswered questions")
    print(f"    Answered questions: {counts[True]}")
    print(f"    Unanswered questions: {counts[False]}")

    # ----- 3. Obtener la respuesta con menor número de vistas ----- #
    views_count = [items[i]['view_count'] for i in range(len(items))]
    ans_min_view = views_count.index(min(views_count))
    print(f"\n\n\n2. Answer with least views ({items[ans_min_view]['view_count']} views)")
    pprint.pprint(items[ans_min_view])

    # ----- 4. Obtener la respuesta más vieja y más actual ----- #
    # pass from timestamp to datetime format
    for i in range(len(items)):
        items[i]['creation_date'] = dt.datetime.fromtimestamp(items[i]['creation_date'])

    print("\n\n\n3. Get oldest and newest answers")

    # get min and max dates from answers
    min_date = min(items, key = (lambda k: k["creation_date"]))["creation_date"]
    max_date = max(items, key = (lambda k: k["creation_date"]))["creation_date"]

    print(f"Oldest answer published on {min_date}:\n")
    pprint.pprint(min(items, key = (lambda k: k["creation_date"])))
    print(f"\n\nNewest answer published on {max_date}:\n")
    pprint.pprint(max(items, key = (lambda k: k["creation_date"])))

    # ----- 5. Obtener la respuesta del owner que tenga una mayor reputación ----- #
    print("\n\n\n4. Get answer from owner with highest reputation")
    pprint.pprint(max(items, key = (lambda k: k["owner"]["reputation"])))


if __name__ == '__main__':
    main()