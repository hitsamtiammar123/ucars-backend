from typing import Dict
from pydantic import BaseModel

def filterNoneDictValue(dict):
  keys = list(dict.keys())
  for i in keys:
    val = dict[i]
    if(val == None):
      del dict[i]
  return dict