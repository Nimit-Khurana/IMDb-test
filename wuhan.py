import json
import requests

class VirusData:
    def __init__(self, url):
        self.url = url
        self.data = requests.get(url)
        self.json_data = json.loads(self.data.text)

    def total_cases(self):
        total = 0
        for i in range(len(self.json_data)):
            cases = self.json_data[i]["noOfCases"]
            total += cases
        return total
            
    def total_deaths(self):
        total = 0
        for i in range(len(self.json_data)):
            cases = self.json_data[i]["deaths"]
            total += cases
        return total

    def total_cured(self):
        total = 0
        for i in range(len(self.json_data)):
            cases = self.json_data[i]["cured"]
            total += cases
        return total

    def state_wise_data(self):
        return self.json_data