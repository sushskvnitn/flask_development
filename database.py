from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
load_dotenv()
Connection_database = os.getenv("Connection_database")
engine = create_engine(
   Connection_database,
   connect_args={
         "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
         }
   }
)
def load_jobs_from_databases():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        Jobs = []
        column_names = result.keys()  # Retrieve the column names

        for row in result.fetchall():
            row_dict = {column_name: row_value for column_name, row_value in zip(column_names, row)}
            Jobs.append(row_dict)

        return Jobs

def load_job_from_databases(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val":id})
        Jobs = []
        column_names = result.keys()  # Retrieve the column names

        for row in result.fetchall():
            row_dict = {column_name: row_value for column_name, row_value in zip(column_names, row)}
            Jobs.append(row_dict)
        if len(Jobs) == 0:
            return None
        return Jobs[0]



