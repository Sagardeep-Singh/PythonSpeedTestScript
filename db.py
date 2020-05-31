import psycopg2


class db:
    connection = None

    def __init__(self, host, username, password, database="postgres", port=5432):
        super().__init__()
        try:
            self.connection = psycopg2.connect(
                database=database, user=username, password=password, host=host, port=port)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute(self, query, bindings=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, bindings)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error while Executing Query", error)