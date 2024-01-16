import requests
from tkinter import *

def apple_stock():
    new_window = Toplevel(rootWindow)
    new_window.title("Акции AAPL")
    new_window.geometry("400x300")

    response = requests.get("http://api.marketstack.com/v1/eod?access_key=9712a31df14939f8b8c6ac23cb071ed1&symbols=AAPL")

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        jsonRetrieve = response.json()

        openValue = jsonRetrieve["data"][0]["open"]
        highValue = jsonRetrieve["data"][0]["high"]
        lowValue = jsonRetrieve["data"][0]["low"]
        closeValue = jsonRetrieve["data"][0]["close"]

        label1 = Label(new_window, text=f"Открытая цена на акцию AAPL: {openValue}")
        label2 = Label(new_window, text=f"Наибольшая цена на акцию AAPL за сегодня: {highValue}")
        label3 = Label(new_window, text=f"Наименьшая цена на акцию AAPL за сегодня: {lowValue}")
        label4 = Label(new_window, text=f"Цена на закрытии: {closeValue}")

        label1.pack(padx=10, pady=10)
        label2.pack(padx=10, pady=10)
        label3.pack(padx=10, pady=10)
        label4.pack(padx=10, pady=10)
    else:
        label = Label(new_window, text=f"Ошибка: {result}")
        label.pack(padx=10, pady=10)


def petersburg_weather():
    new_window = Toplevel(rootWindow)
    new_window.title("Погода в Санкт-Петербурге")
    new_window.geometry("400x300")

    response = requests.get("http://api.weatherstack.com/current?access_key=6d06bf8b5b501db2c2c4fffcf153847e&query=Saint%20Petersburg")

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        jsonRetrieve = response.json()

        temperature = jsonRetrieve["current"]["temperature"]
        humidity = jsonRetrieve["current"]["humidity"]
        pressure = jsonRetrieve["current"]["pressure"]

        label1 = Label(new_window, text=f"Температура в Санкт-Петербурге: {temperature}")
        label2 = Label(new_window, text=f"Влажность воздуха в Санкт-Петербурге: {humidity}")
        label3 = Label(new_window, text=f"Атмосферное давление в Санкт-Петербурге: {pressure}")

        label1.pack(padx=10, pady=10)
        label2.pack(padx=10, pady=10)
        label3.pack(padx=10, pady=10)
    else:
        label = Label(new_window, text=f"Ошибка: {result}")
        label.pack(padx=10, pady=10)


def rubWindowValue():
    window = Toplevel(rootWindow)
    window.title("Курс рубля")
    window.geometry("400x300")

    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR,CHF&base=RUB"

    payload = {}
    headers = {
        "apikey": "BL0gDj1di6k57ZGgMaBcVGe8ND9JgCZq"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        jsonRetrieve = response.json()

        usd = jsonRetrieve["rates"]["USD"]
        eur = jsonRetrieve["rates"]["EUR"]
        chf = jsonRetrieve["rates"]["CHF"]

        label1 = Label(window, text=f"Курс рубля к USD: {usd}")
        label2 = Label(window, text=f"Курс рубля к EUR: {eur}")
        label3 = Label(window, text=f"Курс рубля к CHF: {chf}")


        label1.pack(padx=10, pady=10)
        label2.pack(padx=10, pady=10)
        label3.pack(padx=10, pady=10)
    else:
        label = Label(window, text=f"Ошибка: {result}")
        label.pack(padx=10, pady=10)

rootWindow = Tk()
rootWindow.title("API Интерфейс")

appleStockButton = Button(rootWindow, text="Акции APPLE", command=apple_stock)
petersburgWeatherButton = Button(rootWindow, text="Погода в СПБ", command=petersburg_weather)
rubleValueButton = Button(rootWindow, text="Курс Рубля", command=rubWindowValue)

appleStockButton.place(relx=0.5, rely=0.2, anchor=CENTER)
petersburgWeatherButton.place(relx=0.5, rely=0.4, anchor=CENTER)
rubleValueButton.place(relx=0.5, rely=0.6, anchor=CENTER)

rootWindow.mainloop()