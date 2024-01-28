# Fill with zero

Given an ordered list of inputs, fill the gap records with zero.


Example:
```python
    data = [{
        "date": "2000-10-31T01:30:00.000-05:00",
        "value": 1,
    }]
    fill_with_zeros(data, datetime(2000, 10, 20), datetime(2000, 10, 31))
```

Expected result would be:
```python
    [
      {'date': '2000-10-31T01:30:00.000-05:00', 'value': 1},
      {'date': '2000-10-30T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-29T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-28T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-27T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-26T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-25T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-24T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-23T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-22T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-21T00:00:00-05:00', 'value': 0},
      {'date': '2000-10-20T00:00:00-05:00', 'value': 0}
    ]
```
