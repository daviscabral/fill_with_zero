from datetime import datetime, timedelta
import pprint

data = [
    {
        "date": "2000-10-31T01:30:00.000-05:00",
        "value": 1,
    },
    {
        "date": "2000-10-31T01:35:00.000-05:00",
        "value": 10,
    },
    {
        "date": "2000-10-31T01:40:00.000-05:00",
        "value": 25,
    },
    {
        "date": "2000-10-31T01:50:00.000-05:00",
        "value": 40,
    },
    {
        "date": "2000-10-31T04:00:00.000-05:00",
        "value": 5,
    },
    {
        "date": "2000-10-29T01:00:00.000-05:00",
        "value": 40,
    },
    {
        "date": "2000-10-25T01:00:00.000-05:00",
        "value": 40,
    },
    {
        "date": "2000-10-18T01:00:00.000-05:00",
        "value": 140,
    },
    {
        "date": "2000-10-17T01:00:00.000-05:00",
        "value": 100,
    },
    {
        "date": "2000-10-16T01:00:00.000-05:00",
        "value": 120,
    },
]

def fill_with_zeros(items, from_date, to_date):
    if len(items) == 0:
        return []
        
    result = []
    initial_date = from_date.date()
    final_date = to_date.date()
    current_date = final_date

    while current_date >= initial_date:
        current_items = list(item for item in items if datetime.fromisoformat(item["date"]).date() == current_date)
        if len(current_items) > 0:
            [result.append(item) for item in current_items]
        else:
            result.append({
                "date": datetime.fromisoformat(current_date.isoformat()).replace(tzinfo=datetime.fromisoformat(items[0]["date"]).tzinfo).isoformat(),
                "value": 0,
            })

        current_date -= timedelta(days=1)

    return result


def main():
    result = fill_with_zeros(data, datetime(2000, 10, 20), datetime(2000, 10, 31))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)

if __name__ == "__main__":
    main()