import csv

filename = input('Enter Your Desired Excel File Name: ')
if not filename.endswith('.csv'):
    filename += '.csv'
col_count = 1
def clm():
    global column
    column = []
    while True:
        col = input('Enter Column Name: ')
        column.append(col)
        choice = int(input('Enter 0 To End The Column Creation: \nEnter 1 To Continue Column Creation: '))
        if choice == 0 or choice != 1 or 0:
            break
        global col_count
        col_count += 1
    print('File Created Successfully...')
    with open(filename, 'w' , newline='')as f:
        fobj = csv.writer(f)
        fobj.writerow(column)
def data():
    global data_column
    data_column = []
    for i in range(col_count):
        val = input(f'Enter {column[i]}: ')
        data_column.append(val)
    with open(filename,'a',newline='')as f:
        fobj = csv.writer(f)
        fobj = fobj.writerow(data_column)
def updater():
    # with open(filename, 'r' )as f:
    #     key = input('Enter Value You Want To Search For: ')
    #     key = key.lower()
    #     flag = 0
    #     to_be_updated = ''
    #     for i in data_column:
    #         if i.lower() == key:
    #             print(i)
    #             to_be_updated = i
    #             flag = 1
    #             break
    #     if flag == 0:
    #         print('Value Not Found.')
    with open(filename,'r')as f:
        reader = list(csv.reader(f))
        key = input('Enter Value You Want To Search For: ')
        key = key.lower()
        flag = 0
        to_be_updated = ''
        for i in data_column:
            if i.lower() == key:
                print(i)
                cell_no = int(input('Which cell would you like to delete?'))
                to_be_updated = i
                flag = 1
                break
        reader.pop(cell_no-1)
        new_val = input(f'Enter New Value at the place of {to_be_updated}')
        reader.insert(cell_no-1,new_val)
        if flag == 0:
            print('Value Not Found.')
            
clm()
data()
updater()