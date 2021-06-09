"""SQL database functionality"""

class SQL:
    """SQL database class"""

    def __init__(self, data, logger, test=False):
        """SQL database constructor"""
        self.user = data['user']
        self.password = data['password']
        self.host = data['host']
        self.schema = data['schema']
        if test: self.schema = data['schema-test']

    def connect(self, logger):
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

    def get(self, query, logger, all=False):
        """SQL database SELECT querries"""

        # Single values
        connection = self.connect(logger)
        cursor = connection.cursor()
        cursor.execute(query, logger)

        if all: data = cursor.fetchall()
        else: data = cursor.fetchone()

        connection.close()

        return data


        # All values

    def write(self, query, logger):
        """SQL database INSERT querries"""

        connection = self.connect(logger)
        cursor = connection.cursor()
        try:
            cursor.execute(query, logger)
            connection.commit()
            connection.close()
            return True
        except Exception as E:
            self.HandleException(E, query, logger)
            connection.close()
            return False


    def update(self, query, logger):
        """SQL database INSERT querries"""

        connection = self.connect(logger)
        cursor = connection.cursor()
        try:
            cursor.execute(query, logger)
            connection.commit()
            connection.close()
            return True
        except Exception as E:
            self.HandleException(E, query, logger)
            connection.close()
            return False


    def execute(self, query, logger):
        """SQL database other querries"""

        connection = self.connect(logger)
        cursor = connection.cursor()
        cursor.execute(query, logger)
        connection.commit()
        connection.close()


    def HandleException(self, exception, query, logger):
        import mysql.connector

        if type(exception) == mysql.connector.OperationalError: pass
        else: logger.log(msg=query, err=type(exception))
