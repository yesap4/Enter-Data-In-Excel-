import csv
def clm():
    global column
    column = []
    while True:
        col = input('Enter Column Name: ')
        column.append(col)
        choice = int(input('Enter 0 To End The Column Creation \nEnter 1 To Continue Column Creation: '))
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
    no_of_entry = int(input('Enter Numbers Of Entry You Want To Do: '))
    with open(filename, 'a', newline='') as f:
        fobj = csv.writer(f)
        for i in range(no_of_entry):
            row_data = []
            for col_name in column:
                val = input(f'Enter {col_name}: ')
                row_data.append(val)
            fobj.writerow(row_data)
def search():
    with open(filename, 'r', newline='') as f:
        col_no = int(input('Enter Column Number In Which You Want To Search For The Value: '))
        key = input('Enter Value You Want To Search For: ')
        found = 0 
        reader = csv.reader(f)
        for ele in reader:
            if ele[col_no-1] == key:
                found = 1
                print('\n',ele,'\n')
                break
        if found == 0:
            print('\nValue Not Found.\n')
def updater():
    with open(filename, 'r', newline='') as f:
        col_no = int(input('Enter Column Number In Which You Want To Update The Value: '))
        key = input('Enter Value You Want To Update: ')
        found = 0
        nrec = []
        reader = csv.reader(f)
        for rec in reader:
            if rec[col_no-1]==key:
                print('Current Value: ',rec)
                rec[col_no-1] = input('Enter The New Value: ')
                print('Updated Value: ',rec)
                found = 1
            nrec.append(rec)
    if found == 0:
        print('Value Not Found...')
    else:
        with open(filename, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerows(nrec)
            print('\nValue Updated Successfully...\n')
def ins_last_row():
    global data_column
    data_column = []
    with open(filename,'r')as f:
        reader = csv.reader(f)
        header = next(reader)
    if not header:
        print('File Empty. Create A File First...')
        return
    with open(filename, 'a', newline='') as f:
        fobj = csv.writer(f)
        row_data = []
        for col_name in header:
            val = input(f'Enter {col_name}: ')
            row_data.append(val)
        fobj.writerow(row_data)
        print('\nRow Inserted Successfully...\n')
def ins_pos_row():
    row_no = int(input('Enter Row Number At Which You Want to Enter Values: '))
    with open(filename,'r')as f:
        reader = csv.reader(f)
        rows = list(reader)
    header = rows[0]
    data_row = rows[1:]

    if row_no < 1 or row_no > len(data_row) + 1:
        print('Invalid Row Number.')
        return

    new_row = []
    for col_name in header:
        value = input(f'Enter {col_name}: ')
        new_row.append(value)
    data_row.insert(row_no-1,new_row)
    with open(filename,'w',newline='')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data_row)
    print('\nRow Added Successfully...\n')
def delete():
    key = input('Enter Value You Want To Delete.')
    with open(filename, 'r', newline='') as f:
        rows = list(csv.reader(f))

    header = rows[0]
    data_rows = rows[1:]
    new_data = []
    found = 0
    for row in data_rows:
        if key in row:
            found = 1
            
        else:
            new_data.append(row)
    if found == 0:
        print('Value Not Found.')
        return
    with open(filename,'w',newline='')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(new_data)
    print('\nValue Deleted Successfully...\n')
    
while True:
    task = int(input(
        'Enter 1 To Create A New File.'
        '\nEnter 2 To Search A Value.'
        '\nEnter 3 To Update A Value.'
        '\nEnter 4 To Insert A New Row At a Specific Row Number.'
        '\nEnter 5 To Insert New Row At The Last.'
        '\nEnter 6 To Delete A Value.'
        '\nEnter 7 To Exit. '
        '\nEnter Your Choice: '
    ))

    if task == 7:
        print('\n Thank You! ☻ \n')
        break

    filename = input('Enter Your Desired Excel File Name: ')
    if not filename.endswith('.csv'):
        filename += '.csv'

    if task == 1:
        col_count = 1
        clm()
        data()
    elif task == 2:
        search()
    elif task == 3:
        updater()
    elif task == 4:
        ins_pos_row()
    elif task == 5:
        ins_last_row()
    elif task == 6:
        delete()
