import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        return pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME'),
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.MySQLError as err:
        print(f"Error de conexión: {err}")
        return None
