import csv


def write():
    filename = input("Enter the desired Excel book name: ")
    if not filename.endswith(".csv"):
        filename += ".csv"
    with open(filename, "w", newline='') as f:
        fobj = csv.writer(f)
        fobj.writerow(['S.No.', 'Name', 'Roll No.', 'Marks'])
        while True:
                serial_no = int(input("Enter Serial Number: "))
                name = input("Enter Name: ")
                roll = int(input("Enter Roll Number: "))
                marks = int(input("Enter Marks: "))
                data = [serial_no, name, roll, marks]
                fobj.writerow(data)
                choice = input("1->Input More\n2->Exit\nEnter Your Choice: ")
                if choice == '2':
                    break
        print(f"File '{filename}' Created Successfully...")

def read():
        with open(, 'r') as f:
            fobj = csv.reader(f)
            for row in fobj:
                print(row)
# def search()
#write()
read() 