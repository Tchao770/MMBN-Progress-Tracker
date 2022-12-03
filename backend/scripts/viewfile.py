import pandas as pd
import django

print(django.get_version())

def read_file():
    df = pd.read_csv(r'upgrades.csv')
    df.reset_index()
    return df

def clean_data(df):
    return df
    
def export_file(df):
    df.to_csv("")


file = read_file()
file = clean_data(file)
print(file)

#type, location= input("type, location: ").split(',')
#print(location)
#print(type)