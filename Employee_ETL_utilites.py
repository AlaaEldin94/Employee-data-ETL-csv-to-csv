import pandas as pd


#em_db = pd.read_csv('Employee.csv')
#print(em_db.head())
def extract_csv(file_path):
    '''
    This functuion is created to extract csv files and return DataFrame

    Arguments :
    
    file_path : the path to the csv file to extract , you need to the extension of the file (i.e: .csv) with the quotation marke

    '''
    raw_data = pd.read_csv(file_path)
    
    return raw_data

raw_emdb=extract_csv('Employee.csv')

def transform_csv(clean_data):
    '''
    This function is meant to transform and replace values 

    '''
    clean_data['LeaveOrNot'] = clean_data['LeaveOrNot'].replace({0:False,1:True})
    clean_data['LeaveOrNot'] = clean_data['LeaveOrNot'].astype(bool)

    clean_data['JoiningYear'] = pd.to_datetime(clean_data['JoiningYear'],format='%Y')
    
    return clean_data
raw_emdb=extract_csv('Employee.csv')
print(raw_emdb.head())
print(raw_emdb.dtypes)
cleaned_emdb = transform_csv(raw_emdb)
print('\n **After the modification**\n')
print(cleaned_emdb.head())
print(cleaned_emdb.dtypes)

# Now we need to load the transformed data 
# we  can load to SQLDatabase but we will load it to csv instead

def load_csv(transformed_data):
    '''
    You need to enter the DataFrame after been transformed 
    '''
    return transformed_data.to_csv('transformed_employeed_data.csv',index=False)

load_csv(cleaned_emdb)
print('\n Succefully loading transformed data to CSV file....')