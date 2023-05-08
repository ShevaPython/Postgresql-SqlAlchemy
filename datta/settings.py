from dotenv import load_dotenv
import os

load_dotenv()

"""Users Db"""
PGUSER = str( os.getenv( 'PGUSER' ) )
NAME_PGUSER_SQLALCHEMY = str( os.getenv( 'NAME_PGUSER_SQLALCHEMY' ) )

"""Password"""
PGPASSWORD = str( os.getenv( 'PGPASSWORD' ) )

"""Host"""
ip = os.getenv( 'ip' )

"""Database"""
DATABASE = str( os.getenv( 'DATABASE' ) )
Sql_Alchemy_ORM = str( os.getenv( "Sql_Alchemy_ORM" ) )
Sql_Alchemy_CORE = str(os.getenv("Sql_Alchemy_CORE"))

"""Connect"""
POSTGRES_URI_DVD_RENTAL = F"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
POSTGRES_URI_Alchemy_ORM = F"postgresql://{NAME_PGUSER_SQLALCHEMY}:{PGPASSWORD}@{ip}/{Sql_Alchemy_ORM}"
POSTGRES_URI_Alchemy_Core = F"postgresql://{NAME_PGUSER_SQLALCHEMY}:{PGPASSWORD}@{ip}/{Sql_Alchemy_CORE}"
