"""SQL database functionality"""

class SQL:
    """SQL database class"""

    def __init__(self, data, logger, test=False):
        """SQL database constructor"""
        self.user = data['user']
        self.password = data['password']
        self.host = data['host']
        self.restraint = 10000
        self.schema = data['schema']
        self.logger = logger
        if test: self.schema = data['schema-test']
        if "restraint" in data: self.restraint = data["restraint"]

    def connect(self):
        """SQL database connecting method"""
        import mysql.connector

        connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.schema,
            buffered=True
        )
        return connection

    def get(self, query, all=False):
        """SQL database SELECT querries"""

        # Single values
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)

        if all: data = cursor.fetchall()
        else: data = cursor.fetchone()

        connection.close()

        return data



    def write(self, query):
        """SQL database INSERT querries"""

        connection = self.connect()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            connection.close()
            return True
        except Exception as E:
            self.handleException(E, query)
            connection.close()
            return False


    def update(self, query):
        """SQL database INSERT querries"""

        connection = self.connect()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            connection.close()
            return True
        except Exception as E:
            self.handleException(E, query)
            connection.close()
            return False


    def execute(self, query):
        """SQL database other querries"""

        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.close()


    def handleException(self, exception, query):
        import mysql.connector

        if type(exception) == mysql.connector.OperationalError: pass
        else: self.logger.log(msg=query, err=type(exception))

    def optimize(self):
        tables = self.get("show tables", all=True)
        for table in tables:
            print("Lost internet connection. Optimizing {}".format(table[0]))
            self.execute("optimize table {}".format(table[0]))
            print(" "*100, end ="\r")
        self.logger.log(msg="Optimized database")
