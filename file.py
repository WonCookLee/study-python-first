import csv

def save_to_file(file_name, jobs) :
    file = open(f"{file_name}.csv", "w", encoding="utf-8", newline = "")
    writer = csv.writer(file)
    writer.writerow(["keyword", "title", "company", "reward", "link"])
    
    for job in jobs:
        writer.writerow(job.values())
    
    file.close()