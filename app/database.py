from sqlalchemy import create_engine, Boolean, Column, \
  ForeignKey, Integer, String, Text, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy.sql.expression import text
import os

SQLALCHEMY_DATABASE_URL = os.environ.get('SQL_URI', 'postgresql://postgres:12345@localhost/ucars-test')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(Session)

Base = declarative_base()

class Brand(Base):
  __tablename__ = 'brand'
  
  id = Column(Integer, primary_key = True, index = True)
  name = Column(String, nullable=False)
  description = Column(Text)
  image_url = Column(Text)
  status = Column(Boolean)
  created_at = Column(
        DateTime(timezone=False),
        nullable=False,
        server_default=text("(now() at time zone 'utc')")
    )

  updated_at = Column(DateTime(timezone=False), server_default=text("(now() at time zone 'utc')"))
  models = relationship('Model', back_populates = 'b')
  

class Model(Base):
  __tablename__ = 'model'
  
  id = Column(Integer, primary_key = True, index = True)
  name = Column(String, nullable=False, index =True)
  description = Column(Text, index =True)
  image_url = Column(Text, index =True)
  status = Column(Boolean, index =True)
  price = Column(Numeric, index = True)
  created_at = Column(
        DateTime(timezone=False),
        nullable=False,
        server_default=text("(now() at time zone 'utc')")
  )
  brand_id = Column(Integer, ForeignKey("brand.id"))
  b = relationship('Brand', back_populates = 'models' )

  updated_at = Column(DateTime(timezone=False), server_default=text("(now() at time zone 'utc')"))
  