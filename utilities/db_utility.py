import pymysql
import logging
from contextlib import closing

class DBUtility:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def open_connection(self):
        self.connection = pymysql.connect(
            host=self.config.get('mysql.url'),
            user=self.config.get('yollhrm.database.username'),
            password=self.config.get('yollhrm.database.password'),
            db=self.config.get('database_name')  # Ensure you add the database name
        )

    def execute_sql_query(self, query):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.logger.info("Closed database connection")
