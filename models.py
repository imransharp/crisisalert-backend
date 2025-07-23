from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class CrisisReport(Base):
    __tablename__ = "crisis_reports"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    district = Column(String)
    crisis = Column(String)

# Setup SQLite database
engine = create_engine("sqlite:///./crisis.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Create the table
Base.metadata.create_all(bind=engine)
