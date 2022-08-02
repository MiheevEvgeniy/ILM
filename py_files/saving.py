from ui import *
import pyodbc


class Saving(UI):
    def __init__(self):
        super(Saving, self).__init__()
        self.filter_category = None
        self.filter_status = None
        self.filter_time = None
        self.filter_mark = None
        self.filter_name = None
        self.config = None
        self.groupbox3 = None
    def save_func(self):
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\User\Desktop\pythonProject\data\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            for row in range(0, self.table.rowCount()):
                # Taking data from rows in table
                Name = (self.table.item(row, 0).text())
                Mark = (self.table.item(row, 1).text())
                Status = (self.table.item(row, 2).text())
                Category = (self.table.item(row, 3).text())
                Time_pole = (self.table.item(row, 4).text())
                # Saving it in db
                cursor.execute('UPDATE Films SET Name = ? WHERE id = ?', (Name, row + 1))
                cursor.execute('UPDATE Films SET Mark = ? WHERE id = ?', (Mark, row + 1))
                cursor.execute('UPDATE Films SET Status = ? WHERE id = ?', (Status, row + 1))
                cursor.execute('UPDATE Films SET Category = ? WHERE id = ?', (Category, row + 1))
                cursor.execute('UPDATE Films SET Time_pole = ? WHERE id = ?', (Time_pole, row + 1))
            conn.commit()
            print("норм все сохранилось")
            self.txt1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)
    def save_settings(self):
        if self.groupbox3.isChecked()==True:
            self.config.set("application", "filters_is_on", "0")
        else:
            self.config.set("application", "filters_is_on", "1")

        if self.groupbox2.isChecked()==True:
            self.config.set("application", "list_del_is_on", "0")
        else:
            self.config.set("application", "list_del_is_on", "1")

        if self.groupbox.isChecked()==True:
            self.config.set("application", "range_del_is_on", "0")
        else:
            self.config.set("application", "range_del_is_on", "1")

        if self.filter_name.isChecked()==True:
            self.config.set("application", "filter_name", "0")
        else:
            self.config.set("application", "filter_name", "1")

        if self.filter_mark.isChecked()==True:
            self.config.set("application", "filter_mark", "0")
        else:
            self.config.set("application", "filter_mark", "1")

        if self.filter_status.isChecked()==True:
            self.config.set("application", "filter_status", "0")
        else:
            self.config.set("application", "filter_status", "1")

        if self.filter_category.isChecked()==True:
            self.config.set("application", "filter_category", "0")
        else:
            self.config.set("application", "filter_category", "1")

        if self.filter_time.isChecked()==True:
            self.config.set("application", "filter_date", "0")
        else:
            self.config.set("application", "filter_date", "1")

        if self.type_adding_btn.isChecked()==True:
            self.config.set("application", "check_add_func", "0")
        else:
            self.config.set("application", "check_add_func", "1")
        with open('C:\\Users\\User\\Desktop\\pythonProject\\data\\config.ini', 'w') \
                as configfile:  # save
            self.config.write(configfile)