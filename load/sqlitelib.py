import records

class Database(object):
    def __init__(self):
        # Valid SQLite URL forms are:
        # sqlite:///:memory: (or, sqlite://)
        # sqlite:///relative/path/to/file.db
        # sqlite:////absolute/path/to/file.db
        self.__db__ = records.Database('sqlite:///D:/Develop/data/fdata.db')
        tables = self.__db__.get_table_names()
        print(tables)

    def query(self, sqlQuery):
        self.__db__.query(sqlQuery)

if __name__=="__main__":
    db = Database()
