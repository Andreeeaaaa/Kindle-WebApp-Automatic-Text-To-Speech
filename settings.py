import os, json

WORKSPACE_DIR = os.getcwd()

def get_language():
    with open(os.getcwd() + '/language.json', "r") as lang:
        return json.load(lang)['language']
    