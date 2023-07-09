import csv
from algo.hash import HashTable
from model.package import Package


def extract_csv(path, package_hash_table):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)

        for column in csv_reader:
            package_id = column[0]
            address = column[1]
            city = column[2]
            state = column[3]
            zip_code = column[4]
            delivery_deadline = column[5]
            mass = column[6]
            package_status = column[7]
            package = Package(package_id, address, city, state, zip_code, delivery_deadline, mass,
                              package_status)

            value = package

            package_hash_table.insert_item(int(package_id), value)

        return package_hash_table
