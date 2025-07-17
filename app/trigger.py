import requests

res = requests.post("http://localhost:8000/run-job", params={"duration": 10})
print(res.json())
