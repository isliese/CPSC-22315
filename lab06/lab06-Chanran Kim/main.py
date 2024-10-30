# Name : Chanran Kim
# Date : 15/10/2024
# A 'main' driver program that acts on user choices

import weather

def main():
    weather_data = {}
    filename = "weather_data.json"  # Default filename

    while True:
        print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
        print("1. Set data filename\n2. Add weather data\n3. Print daily report\n4. Print historical report\n5. Exit the program")

        user_choice = int(input("Enter menu choice: "))
        
        # according to user choice

        # 1. Set data filename
        if user_choice == 1:
            user_filename = input("Enter data filename: ")
            weather_data = weather.read_data(filename=user_filename)
        
        # 2. Add weather data
        elif user_choice == 2:
            user_date = input("Enter date (YYYYMMDD): ")
            user_time = input("Enter time (hhmmss): ")
            user_temperature = float(input("Enter temperature: "))
            user_humidity = float(input("Enter humidity: "))
            user_rainfall = float(input("Enter rainfall: "))
            
            key = user_date + user_time  # Create unique key
            weather_data[key] = {
                't': user_temperature,
                'h': user_humidity,
                'r': user_rainfall
            }
            weather.write_data(data=weather_data, filename=filename)

        # 3. Print daily report
        elif user_choice == 3:
            user_date = input("Enter date (YYYYMMDD): ")
            report = weather.report_daily(data=weather_data, date=user_date)
            print(report)

        # 4. Print historical report
        elif user_choice == 4:
            report = weather.report_historical(data=weather_data)
            print(report)

        # 5. Exit the program
        elif user_choice == 5:
            break

if __name__ == "__main__":
    main()
