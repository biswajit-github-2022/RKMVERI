import os

class FileReaderWithDelimeter:
    def __init__(self,file_name:str,delimeter:str) -> None:
        '''
        -file is read
        -the file name, file size, column headers is stored into instance variables 
        -the file data is read and stored column-wise and row-wise into seperate instance variables
        '''
        self.file_name=file_name
        self.file_size=os.path.getsize(file_name)
        self.file_column_headers=[]
        self.file_column_data={}
        self.file_row_data=[]

        with open(file_name, 'r') as main_file:
            lines=main_file.readlines()
            lines=[line.strip() for line in lines]
        #header
        self.file_column_headers=lines[0].split(delimeter+" ")
        #row wise
        for line in range(1,len(lines)):
            self.file_row_data.append(lines[line].split(delimeter))
        #column wise
        for i in range(len(self.file_column_headers)):
            self.file_column_data[self.file_column_headers[i]]=list(zip(*self.file_row_data))[i]


    def __str__(self) -> str:
        return f'{"-"*50}\nFile Name : {self.file_name},\nFile Size : {self.file_size},\nNumber of columns : {len(self.file_column_headers)},\nNumber of rows : {len(self.file_row_data)}\n{"-"*50}'


    def find_row_using_number(self,*args):
        '''
        1. it receives a variable number of row numbers as paramter(s) and prints the data contained in those rows. 
        '''
        for i in range(len(args)):
            if args[i] not in range(1,len(self.file_row_data)+1):
                print( f'Enter valid Index of rows')
                continue
            print(f"{args[i]}-th Row:",self.file_row_data[args[i]-1],)
        print(f"{'-'*50}")


    def find_column_using_header(self,column_name:str):
        '''
        2. it receives a column name and prints the data for the entire column
        '''
        if column_name in self.file_column_headers:
            print(f"{column_name} : ",self.file_column_data[column_name])
        else :
            print("Enter a valid column name")
        print(f"{'-'*50}")

    def find_row_using_col_name_and_val(self,col_name:str,col_val):
        '''
        3. it receives a column name and a column value as parameters and prints all the rows having that column value.
        '''
        print(f"Rows with val '{col_val}' in column '{col_name}' are: ")
        index_list=[]
        if col_name in self.file_column_headers:
            for i in range(len(self.file_column_data[col_name])):
                if col_val==self.file_column_data[col_name][i]:
                    index_list.append(i+1)
            self.find_row_using_number(*index_list)
        else:
            print(f"Enter valid Column Name")
    
    def find_row_using_multiple_col_name_and_val(self,col_name1:str,col_val1,col_name2:str,col_val2):
        '''
        4. it receives a pair of column names and column values and prints all the rows having the specified column values in the specified columns passed as parameters. The rows printed should satsify BOTH the conditions.
        '''
        print(f"Rows with val '{col_val1}' and '{col_val2}' in column '{col_name1}' and '{col_name2}' are: ")
        index_list=[]
        if col_name1 and col_name2 in self.file_column_headers :
            for i in range(len(self.file_column_data[col_name1])):
                if col_val1==self.file_column_data[col_name1][i] and col_val2==self.file_column_data[col_name2][i]:
                    index_list.append(i+1)
            
            if col_val1 not in self.file_column_data[col_name1] or col_val2 not in self.file_column_data[col_name2] :
                print(f"No data Available")
                return
            
            self.find_row_using_number(*index_list)
        else:
            print(f"Enter valid Column Name")
    

file_data=FileReaderWithDelimeter("marksheet_exercise.txt", ",")
print(file_data)
file_data.find_row_using_number(1,2,3)
file_data.find_column_using_header("Year")
file_data.find_row_using_col_name_and_val("Subject","PDS")
file_data.find_row_using_multiple_col_name_and_val("Subject","PDS","Age","22")
