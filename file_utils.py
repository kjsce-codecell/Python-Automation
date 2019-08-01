import csv


def read_csv():
    # opening the file in read mode
    with open("studentdetails.csv", 'r') as csv_file:
        # reading the csv
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
            data.append(row)
    return data


def write_csv(data):
    # opening the file in write mode
    with open("studentdetails.csv", 'w', newline='') as csv_file:
        # writing to the csv
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            csv_writer.writerow(row)


def read_file():
    # opening the file in read mode and reading lines
    with open("sentmails.txt", 'r') as f:
        sent_mails = f.read().split('\n')[:-1]
        # Another way
        # sent_mails = [mail.strip() for mail in f.readlines()]
    return sent_mails


def write_file(mail):
    # opening the file in append mode and appending the mail at the end
    with open("sentmails.txt", 'a') as f:
        f.write(mail + '\n')
