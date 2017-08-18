import os

def make(path):
    if not os.path.exists(path):
        os.makedirs(path)
