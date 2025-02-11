import os
from pprint import pprint
from bs4 import BeautifulSoup
import json
import os


class Scraper:
    def __init__(self):
        self.files = os.listdir('resources')

    def get_data(self):
        if not os.path.exists("results"):
            # Create the directory
            os.makedirs("results")
        for file in self.files:
            previous_date: int | None = None
            with open(f"resources/{file}", 'r', encoding='utf-8') as file_obj:
                html_content: str = file_obj.read()
            weather_data: dict = {}
            soup = BeautifulSoup(html_content, 'html.parser')
            monthly_daypanels = soup.find_all('a',
                                              class_='monthly-daypanel')
            for panel in monthly_daypanels:
                date: int = int(panel.find('div', class_='monthly-panel-top').find('div', class_='date').text.strip())
                if date > 1 and not weather_data:
                    continue
                if not date:
                    continue
                if previous_date and previous_date > date:
                    break
                else:
                    previous_date: int = date
                high_temp = panel.find('div', class_='temp').find('div', class_='high').text.strip().replace("°", "")
                low_temp = panel.find('div', class_='temp').find('div', class_='low').text.strip().replace("°", "")

                if date in weather_data:
                    continue
                weather_data[date] = {
                    'high': high_temp,
                    'low': low_temp
                }
            with open(f"results/{file.replace(".html", "")}.json", 'w', encoding='utf-8') as json_file:
                json.dump(weather_data, json_file, indent=4)


if __name__ == "__main__":
    runner = Scraper()
    runner.get_data()
