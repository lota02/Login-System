from PyQt5 import QtWidgets,QtSql
from Test import Ui_Form
import sys


class mysystem(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mysystem,self).__init__()
        self.setupUi(self)
        self.opend()
        self.Login.clicked.connect(self.checkedUser)

    def opend(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")
        if not self.db.open():
            print("Invalid")
        self.query = QtSql.QSqlQuery()

    def checkedUser(self):
        username1 = self.Username.text()
        password1 = self.Password.text()
        print(username1,password1)
        self.query.exec_("select * from userdata where Username ='%s' and Password = '%s';"%(username1,password1))
        self.query.first()
        if self.query.value("Username") != None and self.query.value("Password") != None:
            print("Logged In :)")
        else:
            print("Login failed :(")    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = mysystem()
    Form.show()
    sys.exit(app.exec_())
