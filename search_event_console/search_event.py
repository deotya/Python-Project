import os
import configparser

config_file = "config.ini" # the name of the configuration file

# read configuration file
config = configparser.ConfigParser()
config.read(config_file)
keywords = input("Enter keyword :").split(",") # input console
# keywords = config.get("settings", "keywords").split(",") # config.ini
log_dir = config.get("settings", "log_dir")
file_extensions = tuple(config.get("settings", "file_extensions").split(","))

events_found = 0
with open("events.txt", "w") as output_file: # create or overwrite output file
    for dirpath, dirnames, filenames in os.walk(log_dir):
        for filename in filenames:
            if filename.lower().endswith(file_extensions):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r") as input_file:
                    file_events_found = 0 # keep track of events found in this file
                    for line in input_file:
                        keywords_found = 0 # keep track of keywords found in this line
                        for keyword in keywords:
                            if keyword in line:
                                output_file.write(f"{filename}: {line}") # include file name with event
                                keywords_found += 1
                        if keywords_found > 0:
                            file_events_found += 1
                    if file_events_found > 0:
                        events_found += file_events_found
if events_found == 0:
    print("No events found.")
else:
    print(f"{events_found} events found.")