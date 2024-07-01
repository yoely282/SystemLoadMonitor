
# System Load Monitor

This project is a simple Python script that monitors the system load and logs the information to a file. It uses the `psutil` library to get the load averages and logs the data using Python's built-in `logging` module.

## Features

- Monitors the 1-minute, 5-minute, and 15-minute load averages.
- Logs load information to a file named `system_load.log`.
- Prints warnings if any load average exceeds 80%.

## Prerequisites

- Python 3.x
- `psutil` library

## Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/YOUR_USERNAME/SystemLoadMonitor.git
   cd SystemLoadMonitor
Create a Virtual Environment:

python3 -m venv venv
Activate the Virtual Environment:

On macOS/Linux:

source venv/bin/activate
On Windows:

.\venv\Scripts\activate
Install the Dependencies:

pip install psutil
Usage
Create the Python Script:

Create a file named monitor_load.py in the SystemLoadMonitor directory and add the following code:

import psutil
import time
import logging

# Configure logging
logging.basicConfig(filename='system_load.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_system_load():
    load1, load5, load15 = psutil.getloadavg()
    cpu_count = psutil.cpu_count()
    load1_perc = (load1 / cpu_count) * 100
    load5_perc = (load5 / cpu_count) * 100
    load15_perc = (load15 / cpu_count) * 100

    log_message = (
        f"1-minute Load: {load1_perc:.2f}%\n"
        f"5-minute Load: {load5_perc:.2f}%\n"
        f"15-minute Load: {load15_perc:.2f}%\n"
    )

    print(log_message)
    logging.info(log_message)

    if load1_perc > 80:
        warning_message = "Warning: 1-minute load is above 80%"
        print(warning_message)
        logging.warning(warning_message)
    if load5_perc > 80:
        warning_message = "Warning: 5-minute load is above 80%"
        print(warning_message)
        logging.warning(warning_message)
    if load15_perc > 80:
        warning_message = "Warning: 15-minute load is above 80%"
        print(warning_message)
        logging.warning(warning_message)

if __name__ == "__main__":
    while True:
        check_system_load()
        time.sleep(60)
Run the Script:

Ensure your virtual environment is activated and run the script using:

python monitor_load.py
Logging
The script logs the system load information to a file named system_load.log in the same directory. It also prints the load averages to the console. If any load average exceeds 80%, a warning message is printed and logged.

License
This project is licensed under the MIT License.

Replace `YOUR_USERNAME` with your actual GitHub username if you plan to push this to a GitHub repository. This `README.md` provides a clear overview of the project, setup instructions, usage, and logging details.





