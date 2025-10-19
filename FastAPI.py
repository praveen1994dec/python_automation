from fastapi import FastAPI
import requests
app = FastAPI()
@app.get("/space-secretdata")
def get_space_data():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    data = response.json()
    person_ISS = []
    person_Tiangong = []
    for person in data.get("people", []):
        if person["craft"] == "ISS":
            person_ISS.append(person["name"])
        else:
            person_Tiangong.append(person["name"])
    return {
        "total_ISS": len(person_ISS),
        "total_Tiangong": len(person_Tiangong),
        "ISS_astronauts": person_ISS,
        "Tiangong_astronauts": person_Tiangong
    }
