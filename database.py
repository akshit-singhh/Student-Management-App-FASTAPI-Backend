from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:[your_password]@localhost/[your_database_name]"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
