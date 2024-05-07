Some systems contain internal APIs that aren't directly accessible from the internet. Server-side parameter pollution occurs 
when a website embeds user input in a server-side request to an internal API without adequate encoding. This means that an 
attacker may be able to manipulate or inject parameters, which may enable them to, for example:

    i)   Override existing parameters.
    ii)  Modify the application behavior.
    iii) Access unauthorized data.
NOTE :- query parameters, form fields, headers, and URL path parameters may all be vulnerable. 

To test for server-side parameter pollution in the query string, place query syntax characters like #, &, and = in your input and
observe how the application responds. 

NOTE :-
Consider a vulnerable application that enables you to search for other users based on their username. When you search for a user, 
your browser makes the following request:
GET /userSearch?name=peter&back=/home
To retrieve user information, the server queries an internal API with the following request:
GET /users/search?name=peter&publicProfile=true

Truncating query strings
You can use a URL-encoded # character to attempt to truncate the server-side request. To help you interpret the response, 
you could also add a string after the # character.

For example, you could modify the query string to the following:
GET /userSearch?name=peter%23foo&back=/home

The front-end will try to access the following URL:
GET /users/search?name=peter#foo&publicProfile=true


Note
It's essential that you URL-encode the # character. Otherwise the front-end application will interpret it as a fragment identifier 
and it won't be passed to the internal API.

Overriding existing parameters
To confirm whether the application is vulnerable to server-side parameter pollution, you could try to override the original parameter.
Do this by injecting a second parameter with the same name.

For example, you could modify the query string to the following:
GET /userSearch?name=peter%26name=carlos&back=/home

This results in the following server-side request to the internal API:
GET /users/search?name=peter&name=carlos&publicProfile=true

The internal API interprets two name parameters. The impact of this depends on how the application processes the second parameter. 
This varies across different web technologies. For example:

 a)   PHP parses the last parameter only. This would result in a user search for carlos.
 b)   ASP.NET combines both parameters. This would result in a user search for peter,carlos, which might result in an Invalid username error message.
 c)   Node.js / express parses the first parameter only. This would result in a user search for peter, giving an unchanged result.









