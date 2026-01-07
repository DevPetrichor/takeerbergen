import serial
import pandas as pd
from datetime import datetime
import os

ser = serial.Serial('COM7', 9600) 
file_name = 'timing_log.xlsx'

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith("Time: "):
            elapsed_time = float(line.split(" ")[1])
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            new_entry = pd.DataFrame({'Time': [current_time], 'Elapsed Time (s)': [elapsed_time]})
            
            if os.path.exists(file_name):
                with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                    new_entry.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
            else:
                new_entry.to_excel(file_name, index=False)
            
            print(f"Logged: {current_time} - {elapsed_time}s")
