# Miscellanious TKInter-based Python API application.

This is a simple Python app that uses Tkinter's GUI methods to create an interface for displaying info about three APIs of various sources: APPL Stock Prices, RUB value compared to USD/CHF/EUR, and weather in Saint-Petersburg, Russia.

## Installation
To run this application, you need to have Python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/You and will also need to install some Python packages using pip. To do that, open a Powershell terminal or command prompt and run the following command:

pip install requests requests-cache retry-requests
This will install the required packages for making API requests, caching responses, and retrying failed requests.

## Usage

To run the application, navigate to the folder where you have saved the main.py file and run the following command:

python main.py

This will open a window with three buttons: Apple Stock Options, SPB Weather, and RUB Exchange rate. These correspond to API interfaces.

## APPL Stock
This financial interface allows you to get the EOD data for APPL using the [Marketstack API](https://api.marketstack.com You can view high, low, close and current values of APPL stock options.
## Exchange Rate
The exchange rate interface allows you to view current exchange rates using the [Apilayer API](https://apilayer.com/ You will be able to view the exchange of RUB/USD, RUB/EUR, RUB/CHF.
## Saint-Petersburg Weather
The weather GUI allows you to get the weather data using the [Weatherstack API](https://api.weatherstack.com You will be able to view current temperature, humidity, atmospheric pressure.

Postman Link: https://restless-desert-745649.postman.co/workspace/Team-Workspace~7e83226d-b623-4fef-85d3-7e4bc5c2630e/overview