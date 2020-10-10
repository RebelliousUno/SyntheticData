import concurrent.futures
import csv
import gc
import sys
from datetime import datetime
from multiprocessing import Pool

import resource as resource
from mimesis import Address
from mimesis import Person


def generate_people():
    person = Person('en-gb')
    firstname = person.first_name()
    surname = person.surname()
    university = person.university()
    return {
        "id": 0,
        "firstName": firstname,
        "surname": surname,
        "uni": university
    }


def generate_addresses():
    address = Address('en-gb')
    city = address.city()
    country = address.country()
    postal_code = address.postal_code()
    street_name = address.street_name()
    street_number = address.street_number()
    return {
        'id': id,
        "street_number": street_number,
        "street_name": street_name,
        "city": city,
        "postal_code": postal_code,
        "country": country
    }


def write_person(start_r: int):
    end_r = start_r + 999
    # print(gc.get_count())
    print(f"Write Person  {datetime.now()} {start_r}-{end_r}")
    with open(f'person_{start_r}_{end_r}.csv', mode='w', newline='\n') as csvfile:
        person = generate_people()
        writer = csv.DictWriter(csvfile, person.keys())
        # writer.writeheader()
        person_list = []
        for id in range(start_r, end_r + 1):
            person = generate_people()
            person['id'] = id
            person_list.append(person)
        writer.writerows(person_list)
    print(f"Done Person  {datetime.now()} {start_r}-{end_r}")


def write_address(start_r: int):
    end_r = start_r + 999
    # print(gc.get_count())
    print(f"Write Address {datetime.now()} {start_r}-{end_r}")
    with open(f'address_{start_r}_{end_r}.csv', mode='w', newline='\n') as address_file:
        address = generate_addresses()
        address_writer = csv.DictWriter(address_file, address.keys())
        # address_writer.writeheader()
        address_list = []
        for id in range(start_r, end_r + 1):
            address = generate_addresses()
            address['id'] = id
            address_list.append(address)
        address_writer.writerows(address_list)
    print(f"Done Address {datetime.now()} {start_r}-{end_r}")


def generate_data(r: int):
    write_person(r)
    write_address(r)


def generate_csvs(start: int):
    # 0 to 1 million...
    # arr = map(lambda x: x * 1000, range(1000))
    # for r in arr:
    generate_data(start)


def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (int(get_memory() * 1024 / 2), hard))


def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory


def main():
    gc.enable()
    print(f"Starting {datetime.now()}")
    generate_csvs(int(sys.argv[1]))
    print(f"All Done {datetime.now()}")


if __name__ == '__main__':
    try:
        main()
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)
