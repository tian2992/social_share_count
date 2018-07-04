import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite://'

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    print("No DB!")
    pass

engine = create_engine(DATABASE_URL, convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
metadata.create_all(engine)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import social_share_count.models
    Base.metadata.create_all(bind=engine)
