import datetime
from datetime import datetime,timedelta
import os.path
from os import path

def file_exists(fn):
    file_valid = open(fn, "a")
    # print ("Name of the file: ", file_valid.name)
    # print ("Closed or not : ", file_valid.closed)
    # print ("Opening mode : ", file_valid.mode)
    # print("Current cursor position is : " + str(file_valid.tell()))
    if (file_valid.tell() == 0):
        print("Empty file")
    else:
        print("Appending existing file")
    file_valid.close()
    
def log_write(fname):
    file_exists(fname)
    fo = open(fname, "a")
    for i in range(0,total_days,1):
        new_date = start_date + timedelta(days=i)
        var_date = new_date.strftime('%b %d, %Y - %A')
        header_string_text = ('Day # ' + str(i+1) + " / " + str(total_days) + ' - ' + var_date + ' (' + str(total_days - i-1) + " days remaining) ")
        header_string="\n"+"-"*len(header_string_text)+"\n"+header_string_text
        header_string=header_string+"\n"+"-"*len(header_string_text)+"\n\n"
        # print(header_string)
        fo.write(header_string)
        
total_days = int(input("Enter total_days for log : "))
input_date = input("Enter start date for log (i.e. 2017,7,15): ")
file_name = str(input("Enter Log file name : "))
year, month, day = map(int, input_date.split(','))
start_date = datetime(year, month, day)
print("Creating / Updating log data in " +  file_name + " starting " + str(start_date.strftime('%b %d, %Y - %A')) + " for " + str(total_days) + " days " )
log_write(file_name)   
