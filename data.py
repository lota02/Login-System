from PyQt5 import QtSql
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("data.sqlite")

if not db.open():
    print("Invalid")
query = QtSql.QSqlQuery()
query.exec_("Create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username VARCHAR(100) NOT NULL);")   
query.exec_("insert int userdata (Username, Password) values('Lota02','012345');")


query.exec_("select * from userdata where id=1;")
query.first()
print(query.value("Username"), query.value("Password"))