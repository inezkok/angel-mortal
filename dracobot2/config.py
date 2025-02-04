import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


SQL_ENGINE_URL = 'mysql://%s:%s@localhost/dragon_trainer' % (
    os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'])
# ref: https://stackoverflow.com/a/55127866
SQL_ENGINE = create_engine(SQL_ENGINE_URL, echo=True, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=SQL_ENGINE, autocommit=False, autoflush=False)
