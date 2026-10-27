import pytest
import psycopg
from psycopg import sql
import os

#DB_PARAMS = {
 #   "host": "localhost",
  #  "port": 5432,
   # "dbname": "testdb",
    #"user": "postgres",
    #"password": "mysecretpassword"
#}
DB_PARAMS = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "port":     int(os.getenv("DB_PORT", 5432)),
    "dbname":   os.getenv("DB_NAME", "testdb"),
    "user":     os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "mysecretpassword"),
}

@pytest.fixture(scope="function")
def db_connection():
    conn = None
    try:
        conn = psycopg.connect(**DB_PARAMS)
        yield conn
    finally:
        if conn:
            conn.close()
@pytest.fixture(params=["select now()"])
def test_query(request):
    return request.param