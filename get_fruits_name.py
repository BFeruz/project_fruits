import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f = open('fruits.csv')
    d=csv.reader(f)
    a=[]
    for i in d:
        a.append(i[0])
    return a[1:]
print(get_frutis_name("fruits.csv"))   