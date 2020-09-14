from dbfread import DBF
table = DBF('/home/evil/Documents/Mildred_DataBase/DataBase/del14jal.dbf')

for record in table:
    print(record)