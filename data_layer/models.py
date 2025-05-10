from sqlalchemy import Column, Integer, String, DateTime 
from .base import Base
from sqlalchemy.sql import func
import uuid

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(String(36) , primary_key=True, default=lambda:string(uuid.uuid4()))
    name = Column(String(100))
    summaries = relationship("Summary", back_populates='topic')

class Summary(Base):
    __tablename__ = 'summary'
    id = Columns(String(36), primary_key=True, default=lambda: string(uuid.uuid4()))
    topic_id = Column(String, ForeignKey("topics.id"))
    timestamp = Column(DateTime(timezone=True, server_default=func.now())
    summary = Column(String(300))
    topic = relationship("Topic", back_populates='summaries')


