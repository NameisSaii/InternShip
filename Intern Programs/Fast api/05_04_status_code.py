"""
n HTTP status code is used to
 help the client who is the system or user submitting data to the server
to understand what happened on the server side application.
Well, there is the 100 series, and the 100 series are information responses that a request is processing.

So it might be giving information to the user that something is happening behind the scenes.

There's a 200 series which you may have seen before, which are the successful requests.

There's a 300 series which are read directions, which means further action must be complete.

There's the 400 series which are client errors in error was caused by the client.

And then there's the 500 series, which are typically known as a server errors in that an error occurred

on the server side of the application.


The 200:
Is a standard response for a successful request.

Commonly used for successful get requests when data is being returned back to the client.

201:
Created.
This means that the request has been successful and created a new resource.

204:
means it was successful, but it did not create an entity, nor does the response

400:bad request.

Which means it cannot process the request due to client error.

401:unauthorized.

Which means a client does not have valid authentication for target resource.

 404: not found,
 which means a client requested resources can not be found.

422 :unprocessable entity.

Which means there's some kind of semantic errors in the client request.

 500 server status codes, we're really only going to be using one, and that's the internal

server error.
"""