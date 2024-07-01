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
