import csv
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f = open('fruits.csv')
    d=csv.reader(f)
    a=[]
    l=0
    for i in d:
        a.append(i[-1])
        for i in a[1:]:
            l+=float(i)
    return l    
print(get_total_price("fruits.csv"))