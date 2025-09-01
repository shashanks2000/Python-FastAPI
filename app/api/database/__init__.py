from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

db_config = 'sqlite:///mangu.db'
engine = create_engine(db_config, echo= True)

Base = declarative_base()

Base.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
