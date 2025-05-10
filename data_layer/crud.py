from .models import Topic, Summary

def get_topic(session):
    topics = session.query(Topic).all()
    return topics

def add_topic(session, name:str):
    topic = Topic(name)
    session.add(topic)
    session.commit()

def add_summary(session, name:str, summary:str):
   topic = session.query(Topic).filter_by(name=name).first()
   topic_id = topic.id
   summary_entry = Summary(topic_id=topic_id, summary=summary)
   session.add(summary_entry)
   session.commit()

def get_summaries(session, name:str):
    topic = session.query(Topic).filter(name=name).first()
    return topic.summaries
    
