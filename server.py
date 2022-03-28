from waitress import serve
    
from notegoat.wsgi import application
    
if __name__ == '__main__':
    serve(application, port='0')