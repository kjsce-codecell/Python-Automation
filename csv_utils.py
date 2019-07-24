import csv

def read_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
                data.append(row)
    
    return data

def write_csv(data, filename):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in data:  
            csv_writer.writerow(row)

def get_unpaid_participants(filename):
    participants = read_csv(filename)
    unpaid_participants = []
    paid_count = 0
    for participant in participants:
        if participant[-1] == 'unpaid':
            unpaid_participants.append(participant)
        else:
            paid_count += 1
    
    return unpaid_participants, paid_count
