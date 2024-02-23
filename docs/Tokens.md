
Token :- A token is a digital message sent from a server to a client, which is then stored temporarily by the client. Tokens can be computer-generated or hardware base


In web applications, tokens are used in token-based authentication. This process authenticates users or processes for applications in the cloud. 

Here's how token-based authentication works:
A user's application sends a request to the authentication service
The authentication service confirms the user's identity and issues a token
The client includes a copy of the token in subsequent requests sent to the server to confirm the client's authentication status 
A valid token allows a user to retain access to an online service or web application until the token expires. This offers convenience, as the user can continue to access a resource without re-entering their login credentials every time. 
One of the many benefits of using tokens is that it keeps your users' passwords protecte

                                                  TYPES OF TOKENS :- 

Access tokens :- A security credential that verifies identity and authorizes resource access. Access tokens are often used as bearer tokens.
Bearer tokens :- The most common way that access tokens are used. Bearer tokens grant access to the bearer, who can access authorized resources without further identification.
Refresh tokens :- Used to generate a new access token. When an access token has an expiration date, a user can use a refresh token to get a new access token without having to log in again.
JSON Web Tokens (JWTs) :-An open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
ID tokens :- A type of token that is related to identity. ID tokens are JSON web tokens (JWTs) meant for use by the application only. 


