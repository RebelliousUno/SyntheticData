# read CSV
import csv
import sys


def read_person_csvs():
        start_r = map(lambda x: x * 1000, range(1000))
        rows = list()
        for r in start_r:
            end_r = r + 999
            with open(f'csv/person_{r}_{end_r}.csv', mode='r') as address_file:
                reader = csv.reader(address_file, lineterminator='\n')
                for row in reader:
                    rows.append(row)
        return rows


def read_address_csvs():
    start_r = map(lambda x: x * 1000, range(1000))
    rows = list()
    for r in start_r:
        end_r = r + 999
        with open(f'csv/address_{r}_{end_r}.csv', mode='r') as address_file:
            reader = csv.reader(address_file, lineterminator='\n')
            for row in reader:
                rows.append(row)
    return rows


def write_person_csv(rows):
    with open('person_10k.csv','w') as file_10k:
        with open('person_1m.csv', 'w') as file_1m:
            writer = csv.writer(file_10k, lineterminator='\n')
            writer1m = csv.writer(file_1m, lineterminator='\n')
            for row in rows:
                writer1m.writerow(row)
                if int(row[0]) < 10000:
                    writer.writerow(row)


def write_address_csv(addresses):
    with open('addresses_10k.csv','w') as file_10k:
        with open('address_1m.csv', 'w') as file_1m:
            writer = csv.writer(file_10k, lineterminator='\n')
            writer1m = csv.writer(file_1m, lineterminator='\n')
            for row in addresses:
                writer1m.writerow(row)
                if int(row[0]) < 10000:
                    writer.writerow(row)


def main():
    persons = read_person_csvs()
    write_person_csv(persons)
    addresses = read_address_csvs()
    write_address_csv(addresses)


if __name__ == '__main__':
    try:
        main()
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)
