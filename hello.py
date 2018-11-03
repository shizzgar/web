
def hello(environ, start_response):


    d = environ['QUERY_STRING']
    l = d.split("&")
    ans = []
    for i in l:
        ans.append(bytes(i + '\n', 'ascii'))


    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return ans

    
