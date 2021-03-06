from pprint import pprint
import datetime
import requests
BASE_URL = "https://api.stackexchange.com/2.3/"
url = BASE_URL + "questions/"
to_date = datetime.datetime.today()
from_date = to_date - datetime.timedelta(days=2)
to_date = str(to_date.date())
from_date = str(from_date.date())
params = {
    "fromdate": from_date,
    "todate": to_date,
    "tagged": "Python",
    "site": "stackoverflow"
    }
response = requests.get(url, params=params)
pprint(response.json())