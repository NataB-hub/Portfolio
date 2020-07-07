import requests
from django.shortcuts import render


def weather(request):
    api_url = "http://api.openweathermap.org/data/2.5/forecast"
    city = False  # если city пустое значение, то блок с талбицей  и городом выводится не будет

    if request.method == "POST":  # если метод POST, то присваеваем city город, который ввел пользователь
        city = request.POST['city']

    params = {  # перечисляем нужные параметры для URL
        'q': city,
        'appid': 'db02454d60b8de925a9520dd20a48322',
        'units': 'metric',
        'lang': 'ru',
    }
    res = requests.get(api_url, params=params).json()
    # формируем список из дат, если не ввели город или ввели город, которого нет то вернется начальная страница
    days = []
    try:
        n = len(res["list"])
    except KeyError:
        return render(request, 'blog/weather.html')
    for i in range(n):
        one_date = res["list"][i]["dt_txt"].split(' ')[0]
        if one_date not in days:
            days.append(one_date)
    # на каждую дату формируем прогноз погоды по часам
    forecasts = []
    for day in days:
        weather_for_day = []
        for j in range(n):
            date = res["list"][j]["dt_txt"].split(' ')
            if day in date:
                weather_for_hour = {"hour": date[1],
                                    "temperature": int(res["list"][j]["main"]["temp"]),
                                    "weather": res["list"][j]["weather"][0]["description"],
                                    "clouds": res["list"][j]["clouds"]["all"],
                                    "wind": int(res["list"][j]["wind"]["speed"]),
                                    "icon": res["list"][j]["weather"][0]["icon"]
                                    }
                weather_for_day.append(weather_for_hour)
        forecast = {'day': day, 'hours': weather_for_day}
        forecasts.append(forecast)
    context = {'forecasts': forecasts, 'city': city}
    return render(request, 'weather/weather.html', context)
