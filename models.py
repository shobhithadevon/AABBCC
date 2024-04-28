from sqlalchemy import String, Integer, Column

from AABBCC.database import Base


class School(Base):
      __tablename__ = 'school'
      stud_id = Column(autoincrement= 1, nullable=False)
      stud_name = Column(String(40), primary_key=True)
      stud_class = Column(String(40), nullable=False)
      stud_age = Column(Integer)
 

