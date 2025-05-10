import sys
import os 
sys.path.append(os.path.abspath(os.path.join(__name__, '..')))
from data_layer.crud import add_summary
from data_layer.session import session


def add_summary( name:str, summary:str):
    add_summary(session, name, summary)

