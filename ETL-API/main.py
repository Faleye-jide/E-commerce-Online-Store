from extract import Url, ExtractData
from Transform import create_df, load_df_to_csv, load_df_to_excel
# get data from extract

url = Url()
url_link = url.read_json_file()
extract = ExtractData(url_link)
# print("EXTRACT", extract)
extracted_data = extract.extract_data()
# print(items)
items = create_df(extracted_data)


# Load data to excel
# load_df_to_excel(items)

# Load data to csv
# load_df_to_csv(items)

# print(items)

