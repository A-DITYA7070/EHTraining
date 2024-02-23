

Authentication :- 
Authentication is the process of confirming that a user or device is who they say they are. It's a way to ensure that only authorized users have access to secure systems. 

Authentication factors can be classified into three types:

Something you know: For example, a password
Something you have: For example, a smartphone
Something you are: For example, biometric authentication 

Some examples of authentication factors include:
Biometric authentication :- 
Verifies a person's identity by checking their biological or behavioral characteristics. For example, many people use their finger or thumb to sign in to their phones, and some computers scan a person's face or retina to verify their identity.
Cookie-based authentication :- 
Also known as session-based authentication, this method assigns a unique identifier to the user and stores it on the server in memory. The client sends this session ID in all requests and the server uses it to identify the user.
Passwordless authentication :- 
Verifies a user's identity without using a password. Instead, it uses more secure alternatives like possession factors (one-time passwords [OTP], registered smartphones), or biometrics (fingerprint, retina scans). 


                                                  Types of Authentication :- 

1. Token-based authentication :-A user is issued a unique token after verification. The token allows the user to access a service until it expires.
2. Certificate authentication
A digital certificate is used to verify a person's identity. Digital certificates are a virtual form of identification, like a passport or driver's license.
3. Basic authentication
This is the simplest approach to authentication. It sends a username and password with every API call.
4. OAuth
This is one of the most secure methods of API authentication. It supports both authentication and authorization.
5. Token authentication
This is a property-based authentication that uses a unique access token to verify a user's identity.
6. Risk-based authentication (RBA)
This process dynamically changes and evaluates the level of verification based on the risk associated with a transaction or user session.
7. LDAP (lightweight directory access protocol)
This helps manage and authenticate user data in distributed directory information services.
8. OpenID
This is an HTTP-based protocol that uses an identity provider (IDP) to validate a user. The IDP is responsible for protecting the user credentials
9.  2FA (2 Factor Authentication) :- 
2FA is an extra layer of security to ensure that people trying to gain access to an online account are who they say they are. Even if someone else finds your password, they'll be stopped if they don't have access to your security info. 

Two-factor authentication (2FA) is a security system that requires two forms of identification to access something. The first factor is a password, and the second is usually a security token or biometric factor, such as a fingerprint or facial scan

10. MultiFactor Authentication :- 
Multi-factor authentication (MFA) is a security measure that requires users to provide more than one factor of authentication to access accounts. MFA is a key part of a strong identity and access management (IAM) polic
It can include  :- 
           a) otp 
           b) fingerprint
           c) security questions
           d) facial recognition etc...



HTTP authentication is a method used by a server to authenticate the identity of clients making requests to access resources over the HTTP protocol. It allows servers to restrict access to resources based on credentials provided by the client. There are several commonly used HTTP authentication methods:

    Basic Authentication:

    Basic Authentication is the simplest form of HTTP authentication.
    The client sends a request to the server with a Authorization header containing a Base64-encoded username and password.
    Example Authorization header: Authorization: Basic base64(username:password)
    Despite its simplicity, Basic Authentication has security vulnerabilities, such as transmitting credentials in plaintext, which makes it susceptible to interception.

    Digest Authentication:
    Digest Authentication is an improvement over Basic Authentication in terms of security.
    It uses a challenge-response mechanism to authenticate clients without sending passwords in plaintext.
    The server sends a challenge containing a nonce (a one-time token), and the client responds with a hashed value of the nonce, username, password, and other information.
    Digest Authentication is more secure than Basic Authentication, but it is still vulnerable to certain attacks, such as replay attacks.

    Bearer Authentication:
    Bearer Authentication is commonly used with OAuth 2.0 and JSON Web Tokens (JWT).
    The client receives an access token from an authorization server and includes it in the Authorization header of subsequent requests.
    Example Authorization header: Authorization: Bearer <access_token>
    Bearer tokens are typically short-lived and can be revoked by the authorization server.

    OAuth 2.0:
    OAuth 2.0 is an authorization framework that allows third-party applications to access resources on behalf of the resource owner.
    It involves multiple parties: the client (application), the resource owner (user), the authorization server, and the resource server.
    OAuth 2.0 defines different grant types (such as authorization code, implicit, client credentials, and password) for different use cases.

    Token-Based Authentication:
    Token-Based Authentication involves issuing tokens to clients upon successful authentication.
    These tokens are then used by clients to access protected resources.
    Tokens can be implemented using various technologies, such as JWT (JSON Web Tokens), OAuth 2.0, or custom token formats.
    Each HTTP authentication method has its advantages, disadvantages, and use cases. The choice of authentication method depends on factors such as security requirements, user experience, and compatibility with existing systems. It's essential to choose the appropriate authentication method based on the specific needs of your application.
