import os


templates = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')
)
print (templates, os.path.dirname(__file__), __file__, __name__)