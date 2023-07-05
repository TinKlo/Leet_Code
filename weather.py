import requests
import pandas as pd

url = 'https://api.tomorrow.io/v4/timelines'
params = {
    'location': '40.75872069597532,-73.98529171943665',
    'fields': 'temperature,precipitationProbability,humidity',
    'timesteps': '1h',
    'units': 'metric',
    'apikey': 'C7xzr7unAyWTX4JCHGvIJ3BLkpUEv7xv'
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'application/json'
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Extract the relevant data from the response
    timeline = data['data']['timelines'][0]
    intervals = timeline['intervals']

    # Create a list of dictionaries to hold the data
    data_list = []
    for interval in intervals:
        data_dict = {'Timestamp': interval['startTime']}
        values = interval['values']
        for field, value in values.items():
            data_dict[field] = value
        data_list.append(data_dict)

    # Create a dataframe from the data list
    df = pd.DataFrame(data_list)
    print(df)
else:
    print('Request failed with status code:', response.status_code)
