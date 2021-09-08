import csv
import requests
import argparse

def set_headers(key):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": f"Token token={key}"
        }
    return headers

def read_file(csv_file,column):
    numbers = []
    with open(csv_file,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            numbers.append(row[column])
    return numbers

def write_file(csv_file, numbers_and_ids):
    with open(csv_file,'w') as f:
        writer = csv
        dict_writer = csv.DictWriter(f,['number','id'])
        dict_writer.writeheader()
        dict_writer.writerows(numbers_and_ids)

def get_ids(headers,numbers):
    numbers_and_ids = []
    for number in numbers:
        url = f'https://api.pagerduty.com/incidents/{number}'
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            id = None
            print(f'API ERROR: {response.status_code}. Incident number {number} not found.')
        elif response.status_code >= 400:
            print(f'API ERROR: {response.status_code}. Exiting program.')
            exit()
        else:
            data = response.json()
            id = data['incident']['id']
        number_and_id = {'number': number, 'id': id}
        numbers_and_ids.append(number_and_id)
    return numbers_and_ids


def main():

    ap = argparse.ArgumentParser(
        description="Convert Incident Number to Incident ID"
    )
    ap.add_argument("-k",
        "--api-key",
        required=True,
        help="REST API key"
    )
    ap.add_argument('-f',
        '--csv-file',
        required=True,
        help="The CSV containing incident numbers"
    )
    ap.add_argument('-c',
    '--column',
    required=False,
    default=0,
    type=int,
    help="Column where incident numbers are located"
    )
    args = ap.parse_args()
    numbers = read_file(args.csv_file, args.column)
    numbers_and_ids = get_ids(set_headers(args.api_key), numbers)
    print(numbers_and_ids)
    numbers = write_file(f'ids_{args.csv_file}', numbers_and_ids)

if __name__ == '__main__':
    main()
