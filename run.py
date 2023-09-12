import pandas as pd
import argparse
import json

# Adding parser to pass fields as an argument
parser = argparse.ArgumentParser(description="Parser for FetchDataApp",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--fields", help="selected fields to find")
args = parser.parse_args()
selected_fields = args.fields if args.fields else ""

# URL link to the .csv file
url = "https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view"
url = "https://drive.google.com/uc?id=" + url.split("/")[-2]

# Read .csv file and convert to dict using pandas
df = pd.read_csv(url)
all_records = df.to_dict(orient="records")


def fetch_data(fields: str, records: list) -> str | dict:
    if not fields:
        return "No 'fields' argument passed to fetch"
    fields_lst = fields.lower().split(",")
    entries_lst = []
    for record in records:
        fields_dct = {}
        for field in fields_lst:
            if record.get(field):
                fields_dct[field] = record.get(field)
                entries_lst.append(fields_dct)
    return {"data": entries_lst}


# Convert the fetched data to JSON
result_json = json.dumps(fetch_data(selected_fields, all_records))
print(result_json)
