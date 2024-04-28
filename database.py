from sqlalchemy.orm import declarative_base,sessionmaker

from sqlalchemy import create_engine

DATABASE_URL = declarative_base("postgresql+psycopg2://postgres:2401@localhost/School")

engine = create_engine(DATABASE_URL)


sessionlocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()


