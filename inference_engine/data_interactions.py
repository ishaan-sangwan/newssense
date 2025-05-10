import sys
import os
sys.path.append(os.path.abspath(os.path.join(__name__, '..')))

from data_layer.crud import get_topic , add_topic
from data_layer.session import session
from embedding import is_simmilar_topic

def infer_topic(name):
    existing_topics = [i.name for i in  get_topic(session)]
    simmilar = is_simmilar_topic(name)
    if simmilar is not None:
        return simmilar
    else:
        topic = add_topic(session, name)
        return name 
        
