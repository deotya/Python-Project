import os
import configparser

config_file = "config.ini" # the name of the configuration file

# read configuration file
config = configparser.ConfigParser()
config.read(config_file)
keywords = config.get("settings", "keywords")
log_dir = config.get("settings", "log_dir")
transaction_start = config.get("settings", "transaction_start")
transaction_end = config.get("settings", "transaction_end")
file_extensions = tuple(config.get("settings", "file_extensions").split(","))

events_found = 0
with open("transaction.txt", "w") as output_file: # create or overwrite output file
    for dirpath, dirnames, filenames in os.walk(log_dir):
        for filename in filenames:
            if filename.lower().endswith(file_extensions):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r") as input_file:
                    file_events_found = 0 # keep track of events found in this file
                    within_transaction = False # keep track of whether currently within a transaction
                    for line in input_file:
                        if transaction_start in line:
                            within_transaction = True
                            transaction = []
                        if within_transaction:
                            transaction.append(line)
                            if transaction_end in line:
                                if keywords in "\n".join(transaction):
                                    for transaction_line in transaction:
                                        output_file.write(f"{filename}: {transaction_line}")
                                    output_file.write("=" * 100 + "\n")                                   
                                    events_found += 1
                                within_transaction = False
                    if file_events_found > 0:
                        events_found += file_events_found
                    else:
                        output_file.write(f"Transactions found.: {events_found}")                         
if events_found == 0:
    print("No Transactions found.")
else:
    print(f"{events_found} Transactions found.")
    
