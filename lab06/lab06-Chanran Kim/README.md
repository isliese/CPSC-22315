# Laboratory 6

## Laboratory Objectives
1. Write Python code using any editor.
2. Execute the program from the command line.
3. Unit test the program.
4. Upload on Canvas for submission

## Getting Started
1. Setting Up Python Environment

     - Verify Python Installation:
     - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
     - Type `python --version` and press Enter.
     - You should see the installed Python version displayed.

2. Configuring Visual Studio Code (VS Code)

     - Install Python Extension:
     - Open VS Code.
     - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
     - Search for `Python` in the Extensions Marketplace.
     - Click “Install” on the Python extension by Microsoft.

3. Running Python in VS Code

     - Create a New Python File:
     - In VS Code, open a folder where you want to save your Python projects.
     - Click on File > New File or press Ctrl+N to create a new file.
     - Save the file with a .py extension (e.g., `hello.py`).
        
## Program Instructions
1. All the functions should accept the weather dictionary data structure as follows:
     ```
	weather dictionary:
		key : datetime as string (formatted as YYYYMMDDhhmmss)
		value : readings dictionary

	readings dictionary
		for key : 't'
		value : temperature as integer

		for key : 'h'
		value : humidity as integer

		for key : 'r'
		value : rainfall as float
     ```
1. Create a `weather` module.
     1. Create a function named `read_data` which receives a keyword parameter `filename`.
          1. The function should open the filename in read mode and return a dictionary of the JSON decoded contents of the file.
          2. If the file does not exist, the function should accept the FileNotFoundError and return an empty dictionary.  

     1. Create a function named `write_data` which receives a keyword parameter `data` and `filename`
          1. The function should open the filename in write mode and write the dictionary data into the file encoded as JSON.  

     1. Create a function named `max_temperature` which receives a keyword parameter `data` and `date`
          1. The function should return the maximum temperature for all dictionary data where the key contains the date as YYYYMMDD.

     1. Create a function named `min_temperature` which receives a keyword parameter `data` and `date`
          1. The function should return the minimum temperature for all dictionary data where the key contains the date as YYYYMMDD.

     1. Create a function named `max_humidity` which receives a keyword parameter `data` and `date`
          1. The function should return the maximum humidity for all dictionary data where the key contains the date as YYYYMMDD.

     1. Create a function named `min_humidity` which receives a keyword parameter `data` and `date`
          1. The function should return the minimum humidity for all dictionary data where the key contains the date as YYYYMMDD.

     1. Create a function named `tot_rain` which receives a keyword parameter `data` and `date`
          1. The function should return the sum of rainfall for all dictionary data where the key contains the date as YYYYMMDD.

     1. Create a function named `report_daily` which receives a keyword parameter `data` and `date`
          1. The function should return a single string which when passed to any print function will display on the screen formatted exactly as indicated in the example output below.  You will most likely be appending strings together using a literal "\n" where a newline is desired.  To get the month name, you can import the builtin `calendar` module and call the `month_name` function passing it the month as an integer.

     1. Create a function named `report_historical` which receives a keyword parameter `data`
          1. The function should return a single string which when passed to any print function will display on the screen formatted exactly as indicated in the example output below.  You will most likely be appending strings together using a literal "\n" where a newline is desired.  To get the month name, you can import the builtin `calendar` module and call the `month_name` function passing it the month as an integer.

1. Create a `main` driver program to meet the following requirements:
     1. Create a file named `main.py`.
     1. Import the `weather` module.
     2. Set a default filename to store the JSON data.
     3. Declare a dictionary to hold the weather data.
     
     4. Implement a menu within a loop with following choices:
          1. Set data filename
               1. Prompt the user for a filename.
               2. Call the weather `read_data` function.
               3. Using the return value set the weather data dictionary.
          2. Add weather data
               1. Prompt the user for the date using the format YYYYMMDD.
               2. Prompt the user for the time using the format hhmmss.
               3. Prompt the user for the temperature.
               4. Prompt the user for the humidity.
               4. Prompt the user for the rainfall.
               5. Add the above readings to the weather dictionary.
               6. Call the weather `write_data` function.
          3. Print daily report
               1. Prompt the user for the date using the format YYYYMMDD.
               2. Call the weather `report_daily` function.
               3. Print out the return string.
          4. Print historical report
               1. Call the weather `report_historical` function.
               1. Print out the return string.
          5. Exit the program
5. Example input and output: 

    ```
	      *** TUFFY TITAN WEATHER LOGGER MAIN MENU

	1. Set data filename
	2. Add weather data
	3. Print daily report
	4. Print historical report
	9. Exit the program

	Enter menu choice: 1

	Enter data filename: w.dat
	      *** TUFFY TITAN WEATHER LOGGER MAIN MENU

	1. Set data filename
	2. Add weather data
	3. Print daily report
	4. Print historical report
	9. Exit the program

	Enter menu choice: 2

	Enter date (YYYYMMDD): 20220107
	Enter time (hhmmss): 133059
	Enter temperature: 82
	Enter humidity: 56
	Enter rainfall: 0.2
	      *** TUFFY TITAN WEATHER LOGGER MAIN MENU

	1. Set data filename
	2. Add weather data
	3. Print daily report
	4. Print historical report
	9. Exit the program

	Enter menu choice: 3

	Enter date (YYYYMMDD): 20210203
	========================= DAILY REPORT ========================
	Date                      Time  Temperature  Humidity  Rainfall
	====================  ========  ===========  ========  ======== 
	February 3, 2021      07:55:01           55        87      0.00
	February 3, 2021      09:06:02           63        84      0.00
	February 3, 2021      10:29:03           71        79      0.00
	February 3, 2021      12:55:04           72        69      0.00
	February 3, 2021      18:39:05           59        75      0.00

	      *** TUFFY TITAN WEATHER LOGGER MAIN MENU

	1. Set data filename
	2. Add weather data
	3. Print daily report
	4. Print historical report
	9. Exit the program

	Enter menu choice: 4

	============================== HISTORICAL REPORT ===========================
				  Minimum      Maximum   Minumum   Maximum     Total
	Date                  Temperature  Temperature  Humidity  Humidity  Rainfall
	====================  ===========  ===========  ========  ========  ======== 
	February 3, 2021               55           72        69        87      0.00
	February 5, 2021               57           74        56        68      0.36
	May 17, 2021                   65           82        31        43      0.00
	September 1, 2021              73          101        82        94      0.52
	November 26, 2021              62           73        20        32      0.00
	December 25, 2021              34           46         2        11      0.01
	January 1, 2022                56           56        33        33      0.00
	January 7, 2022                82           82        56        56      0.20

	      *** TUFFY TITAN WEATHER LOGGER MAIN MENU

	1. Set data filename
	2. Add weather data
	3. Print daily report
	4. Print historical report
	9. Exit the program

	Enter menu choice: 9
    ```


1. Run the unit testing program to ensure that your program runs as expected.
    
    For Linux and Mac users
    ```
    ./test.sh or source ./test.sh
    ```
       
    For windows users
    ```
    ./win_test.bat
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` or `./win_test.bat` repeatedly until it passes all the test.

## Submission
Submit a zip file containing all the code files on canvas 

Naming Convention: <CWID>_<LastName>.zip

You should have the following files:

CWID_LASTNAME.zip -
                  | > test.py
                  | > test.sh
                  | > main.py
                  | > weather.py
                  | > test.txt
                  | > win_test.bat
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|10|main.py file submitted and meets the program requirements |
|10|weather.py file submitted and meets the program requirements |
|3|unit test passes Test01_weather_read_data_errorhandle|
|2|unit test passes Test02_weather_write_data|
|3|unit test passes Test03_max_temperature|
|3|unit test passes Test04_min_temperature|
|3|unit test passes Test05_max_humidity|
|3|unit test passes Test06_min_humidity|
|3|unit test passes Test07_tot_rain|
|5|unit test passes Test08_report_daily|
|5|unit test passes Test09_report_historical|
