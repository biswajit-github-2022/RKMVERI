import os

class MyRecordHolder:
    def __init__(self,filename,delim):
        with open(filename) as file:
            lines = file.readlines()
        self._headers = [x.strip() for x in lines[0].strip().split(delim)]
        self._filesize = os.path.getsize(filename)
        self._filename = filename
        #print(self._headers)
        num_col = len(self._headers)
        data_colwise = [[] for _ in range(num_col)]
        #print(data_colwise)
        for l in lines[1:]:
            cols = l.strip().split(delim)
            for i,c in enumerate(cols):
                if c != '':
                    data_colwise[i].append(c)
                else:
                    data_colwise[i].append('NA')
        #print(data_colwise)
        self._coldata = dict(zip(self._headers,data_colwise))
        self._rowdata = [l.strip().split(delim) for l in lines[1:]]
        #print(self._coldata)
        #print(self._rowdata)

    def get_by_one_col(self,colname,colvalue):
        col_values= self._coldata[colname]
        indices = [i for i,e in enumerate(col_values) if e == colvalue]
        selected_data = [self._rowdata[i] for i in indices]
        print(selected_data)

    def get_by_two_col(self,colname1,colvalue1,colname2,colvalue2):
        col_index2 = self._headers.index(colname2)
        col_values1= self._coldata[colname1]
        indices1 = [i for i,e in enumerate(col_values1) if e == colvalue1]
        selected_data1 = [self._rowdata[i] for i in indices1]
        print([x for x in selected_data1 if x[col_index2] == colvalue2])

    def get_by_col_name(self,colname):
        print(self._coldata[colname])
    
    def get_by_row_index(self,*args):
        if max(args) <= len(self._rowdata)-1:
            print([self._rowdata[i] for i in args])
        else:
            print(f'there are only {len(self._rowdata)} rows')

    def __str__(self):
        return f'the current file: {self._filename} and has {len(self._coldata)-1} rows and {len(self._headers)} columns and is of size {self._filesize} Bytes'





mrh = MyRecordHolder('marksheet_exercise.txt',',')
mrh.get_by_one_col('Name','rajeev')
mrh.get_by_one_col('Subject', 'PDS')
mrh.get_by_one_col('Stream', 'BDA')

print('\n')
mrh.get_by_two_col('Subject','PDS','Stream','BDA')
mrh.get_by_col_name('Stream')
mrh.get_by_row_index(1,3)
mrh.get_by_row_index(1,100)
print(mrh)
print('*'*20)

mrh = MyRecordHolder('marksheet_exercise copy.txt','::')
mrh.get_by_one_col('Name','rajeev')
mrh.get_by_one_col('Subject', 'PDS')
mrh.get_by_one_col('Stream', 'BDA'); print('\n')
mrh.get_by_one_col('Year', '1st year')


print('\n')
mrh.get_by_two_col('Subject','PDS','Stream','BDA')
mrh.get_by_col_name('Stream')
mrh.get_by_row_index(1,3)
mrh.get_by_row_index(1,100)
print(mrh)

    


            

