from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
engine = create_engine(
    "sqlite:///./test.db", connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()