# Call-one-API-from-another-API-and-check-the-user-is-admin-or-not-and-token-expiration

In the above code I have called another API from some other API.
And used jwt-token for the validations like user is admin or not token is expired after a given time.

I am using POSTMAN to pass the user credentials with a post route. 
I have used decorators to check whether token is passed inside the headers or not if passed the token is valid or not.

The problems faced by me in the above code is that while I am passing body from the json I was enable to pass boolean value
to pass the boolean values use the below lines.

data = {"name":"Rahees Khan",
        "id":33,
        "admin":true
        }
       
In json data if you want to pass a boolean value then use small alphabates insted of True or False as we use in Python.

TO RUN THE ABOVE CODE YOU HAVE TO RUN BOTH THE FLASK APPLICATION PARALLELY
ERRORS:-
        the error you will get if aother flask application is not running ie. another_route.py file is given below

raise ConnectionError(e, request=request)        
requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5001): Max retries exceeded with url: /second_route (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f239e5e07f0>: Failed to establish a new connection: [Errno 111] Connection refused',))        


        
