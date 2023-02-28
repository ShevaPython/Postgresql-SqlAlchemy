from dotenv import load_dotenv
import os

load_dotenv()

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
ip = os.getenv('ip')
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = F"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"