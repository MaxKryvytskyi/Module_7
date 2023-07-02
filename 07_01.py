'''
Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict), 
яка буде викликати функцію setup з параметрами зі словника args_dict.

Структура словника для параметра args_dicts має бути наступною

{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''

from setuptools import setup

args = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}

def do_setup(args_dict):
    setup(**args_dict)
          
          

do_setup(args)
          
          
          
          
          