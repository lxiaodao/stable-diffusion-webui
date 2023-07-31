# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:10:53 2023

@author: yang
"""


import json
import datetime


format_string="%Y-%m-%d %H:%M:%S"
def date_format(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        date_time_str = o.strftime(format_string)
        return date_time_str
    
    
def convert_object_json(ob):
    account_json = json.dumps(ob.__dict__, default=date_format)
    return account_json