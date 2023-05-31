import pandas as pd

# transfrm data from a dictionary format to pandas 
def create_df(items: dict):
    df = pd.DataFrame.from_dict(
    items
    )
    return df

def load_df_to_csv(df):
    df.to_csv("url.csv", index=False)
    print("Loaded to csv successfully")
    return 

def load_df_to_excel(df):
    df.to_excel("url.xlsx")
    print("Loaded to excel successfully")
    return 
