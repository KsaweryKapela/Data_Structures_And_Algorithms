class AverageTemperatures:

    def __init__(self):
        self.no_of_days = int(input('How many days temperature? '))
        self.temperatures = []
        self.temperatures_above_average = []
        self.average_temp = 0
        self.no_of_days_above = 0

    def ask_for_temp(self):
        for day in range(self.no_of_days):
            self.temperatures.append(int(input(f'Day {day + 1} highest temperature: ')))

    def calculate_average_temp(self):
        self.average_temp = sum(self.temperatures) / len(self.temperatures)
        print(f'Average {self.average_temp}')

    def no_of_warmer_days(self):
        for temperature in self.temperatures:
            if temperature > self.average_temp:
                self.temperatures_above_average.append(int(temperature))
                self.no_of_days_above += 1
        print(f'There were {self.no_of_days_above} days above average.'
              f'\n The temperatures were {self.temperatures_above_average}')

    def everything(self):
        self.ask_for_temp()
        self.calculate_average_temp()
        self.no_of_warmer_days()


AverageTemperatures().everything()
