from dotenv import load_dotenv
import os

load_dotenv()

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
ip = os.getenv('ip')
DATABASE = str(os.getenv('DATABASE'))
SQL_ALCHEMY_DATABASE = str(os.getenv("SQL_ALCHEMY_DATABASE"))
NAME_PGUSER_SQLALCHEMY = str(os.getenv('NAME_PGUSER_SQLALCHEMY'))
POSTGRES_URI = F"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"