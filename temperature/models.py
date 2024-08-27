from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Temperature(Base):
    __tablename__ = "temperatures"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    date_time = Column(DateTime, default=datetime.now, nullable=False)
    temperature = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="temperatures")
