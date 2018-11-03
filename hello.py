
def hello(environ, start_response):


    d = environ['QUERY_STRING']
    e = d.[2:]
    l = e.split("&")
    for i in l:
        a += str(i) + '\n'


    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return a    

    
