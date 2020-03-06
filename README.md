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
