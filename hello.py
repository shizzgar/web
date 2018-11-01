
def hello(environ, start_response):


    d = environ['QUERY_STRING']
    d.pop(0,1)
    d.split("&")
    for i in d:
        a += str(i) + '\n'


    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return a    

    
