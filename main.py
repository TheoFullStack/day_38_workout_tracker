import os
import requests
import datetime as dt

GENDER = "Male"
WEIGHT_KG = "66.5"
HEIGHT_CM = "1.71"
AGE = "23"

APP_ID = os.environ['NUTRITION_APP_ID']
API_KEY = os.environ['NUTRITION_API_KEY']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_raw = dt.datetime.now()
today = today_raw.strftime("%Y-%m-%d")
time = today_raw.strftime("%H:%M:%S")
duration = result['exercises'][0]['duration_min']
exercise_type = result['exercises'][0]['name']
calories = result['exercises'][0]['nf_calories']

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#TOKEN COULD BE HIDDEN AS ENV VARIABLE BUT LEFT OPEN FOR TEST PURPOSES.
HEADERS = {
    "Authorization": "Bearer THISISTESTTOKEN_121212"
}




response2 = requests.post(url=f"https://api.sheety.co/2de0dac248f3cd43f3688c3098265705/myWorkouts/workouts",json=sheet_inputs,headers=HEADERS)
response2.raise_for_status()
print(response2.text)