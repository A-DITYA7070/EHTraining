                                                                
                                                                Authorisation :-

Authorization is the process of determining whether a user or system entity has the necessary permissions or privileges to access a specific resource, perform an action, or execute a function within a system, application, or network. In other words, authorization is the mechanism by which access rights are granted or denied to users based on their identity, role, or other attributes.

Authorization typically follows the authentication process, where users are first authenticated to verify their identity. Once authenticated, authorization checks are performed to determine what actions the authenticated user is allowed to perform and what resources they are allowed to access.

Here's how authorization typically works:

Identification and Authentication:
Users or system entities provide their credentials (e.g., username and password) to authenticate themselves to the system.
The system verifies the provided credentials and confirms the user's identity.
                    
Authorization Decision:
After authentication, the system determines what actions the authenticated user is allowed to perform and what resources they are allowed to access.
Authorization decisions are based on access control policies defined by administrators or system owners, which specify who can access what resources under what conditions.

Access Control Policies:
Access control policies define the rules and criteria used to grant or deny access to resources and actions.
These policies may be based on various factors, including user roles, group memberships, attributes, permissions, and the context of the access request (e.g., time of day, location).
                    
Access Enforcement:
The system enforces the access control policies by either granting or denying access to the requested resource or action.
If the user's permissions match the access control policies, access is granted, and the user can proceed with the requested operation.
If the user's permissions do not match the access control policies, access is denied, and the user may be notified of the denial or provided with information on how to request access or obtain additional permissions.
Authorization mechanisms can vary widely depending on the specific system, application, or network architecture. Common authorization mechanisms include:

Role-Based Access Control (RBAC): Users are assigned roles, and access rights are granted based on the roles assigned to them. RBAC simplifies access management by grouping users into roles and assigning permissions to roles rather than individual users.

Attribute-Based Access Control (ABAC): Access decisions are based on the attributes of users, resources, and the environment. ABAC policies can be more flexible and dynamic than RBAC, allowing access decisions to be based on a wide range of attributes and conditions.

Rule-Based Access Control (RuBAC): Access decisions are based on predefined rules or policies that specify conditions under which access is granted or denied.

Mandatory Access Control (MAC): Access decisions are determined by a centralized security policy enforced by the operating system or security kernel. MAC is commonly used in high-security environments where access controls are strictly enforced.

Effective authorization is essential for maintaining the security and integrity of systems and protecting sensitive data from unauthorized access or misuse. By implementing robust access control mechanisms and enforcing least privilege principles, organizations can ensure that users have access only to the resources and actions necessary to perform their tasks while minimizing the risk of unauthorized access or data breaches.



                                                        types:-
                    
There are several types of authorization mechanisms used in computer systems, networks, and applications to control access to resources and actions. These authorization types vary in complexity, granularity, and flexibility, and organizations often use a combination of these mechanisms to enforce access control policies based on their security requirements and operational needs. Here are some common types of authorization:

Role-Based Access Control (RBAC):
RBAC is one of the most widely used authorization models. In RBAC, access rights are assigned to roles, and users are assigned to these roles based on their job functions or responsibilities.
Users inherit the permissions associated with their assigned roles, simplifying access management and administration.
RBAC is well-suited for organizations with clearly defined job roles and hierarchical access structures.
                    
Attribute-Based Access Control (ABAC):
ABAC is a dynamic and flexible authorization model that bases access decisions on attributes associated with users, resources, and the context of the access request.
Attributes can include user roles, group memberships, user characteristics, resource properties, environmental conditions, and relationships between entities.
ABAC policies use rules or conditions to evaluate attributes and make access decisions, allowing for fine-grained control over access permissions.
                    
Rule-Based Access Control (RuBAC):
RuBAC is an authorization model that uses predefined rules or policies to determine access permissions.
Rules specify conditions under which access is granted or denied, often based on combinations of user attributes, resource properties, and environmental factors.
RuBAC policies can be static or dynamic, allowing organizations to define access control rules based on their specific requirements.
                    
Mandatory Access Control (MAC):
MAC is a strict authorization model used in high-security environments where access control is centrally managed and strictly enforced by the operating system or security kernel.
Access decisions are based on a predefined security policy that specifies the sensitivity levels of objects (e.g., files, processes) and subjects (e.g., users, processes).
MAC policies are typically nondiscretionary, meaning users cannot override or modify access controls, and access decisions are based solely on the security labels assigned to objects and subjects.
                    
Discretionary Access Control (DAC):
DAC is a flexible authorization model where access control decisions are at the discretion of the resource owner or administrator.
Resource owners have the authority to set access permissions and determine who can access their resources.
DAC is commonly used in file systems and network shares, where users have control over access to their files and directories.
                    
Attribute-Based Access Control (ABAC):
ABAC is an authorization model that evaluates access decisions based on attributes associated with users, resources, and environmental factors.
Attributes can include user roles, group memberships, user characteristics, resource properties, and contextual information.
ABAC policies use rules or conditions to evaluate attributes and make access decisions, allowing for dynamic and context-aware access control.
Each type of authorization mechanism has its strengths and weaknesses, and the choice of authorization model depends on factors such as the organization's security requirements, operational needs, and regulatory compliance obligations. By implementing the appropriate authorization mechanisms, organizations can enforce access control policies that align with their security objectives and protect their sensitive data and resources from unauthorized access or misuse.

                                                                Authorisation Tokens :- 

Authorization tokens are credentials used in authentication protocols to provide access to protected resources or services. These tokens are typically issued by an authentication server or identity provider after a user successfully authenticates and proves their identity. Authorization tokens serve as proof of authentication and contain information about the user's identity, permissions, and other attributes required for accessing specific resources.

Here are some common types of authorization tokens:

Bearer Tokens:
Bearer tokens are a type of access token commonly used in OAuth 2.0 and OpenID Connect authentication protocols.
They are issued by an authorization server and are presented by the client (e.g., web browser, mobile app) to access protected resources from a resource server.
Bearer tokens are typically short-lived and are included in the HTTP Authorization header of API requests.
                    
JWT (JSON Web Tokens):
JWT is an open standard for securely transmitting information between parties as a JSON object.
JWTs can be used as authorization tokens in various authentication protocols, including OAuth 2.0 and OpenID Connect.
JWTs consist of three parts: a header, a payload (containing claims about the user), and a signature to verify the integrity of the token.
JWTs are digitally signed and optionally encrypted, making them tamper-proof and secure for transmitting identity and access information.
                    
SAML Assertions:
Security Assertion Markup Language (SAML) assertions are XML-based security tokens used in SAML-based authentication and single sign-on (SSO) protocols.
SAML assertions contain information about the user's identity, attributes, and authentication status, signed by the identity provider (IdP) to ensure integrity and authenticity.
SAML assertions are exchanged between the identity provider and service provider to facilitate authentication and authorization of users accessing web applications and services.
                    
Auth 2.0 Tokens:
OAuth 2.0 defines several types of tokens used for different purposes, including access tokens, refresh tokens, and authorization codes.
Access tokens are used to access protected resources on behalf of the user after successful authentication and authorization.
Refresh tokens are used to obtain new access tokens when access tokens expire, without requiring the user to reauthenticate.
Authorization codes are temporary tokens used to obtain access tokens in OAuth 2.0 authorization code flow.
Authorization tokens play a crucial role in securing access to resources and services in modern authentication and authorization protocols. By using tokens, applications and services can implement fine-grained access control, enforce security policies, and protect sensitive information from unauthorized access or tampering. It's essential to handle authorization tokens securely, including encrypting them during transmission, validating their integrity and authenticity, and implementing appropriate token management and revocation mechanisms to mitigate security risks.

                =>  TYPES OF TOKENS "----

Tokens are widely used in various contexts in computer science, cryptography, and security to represent data, authenticate users, authorize access to resources, and facilitate secure communication. Depending on their purpose and usage, tokens can take different forms and serve different functions. Here are some common types of tokens:

Access Tokens:
Access tokens are credentials used to access protected resources or services in authentication and authorization protocols.
Examples include bearer tokens in OAuth 2.0, JWT (JSON Web Tokens), SAML assertions, and OAuth 2.0 authorization codes.
                    
Session Tokens:
Session tokens are temporary identifiers used to establish and maintain a session between a client (e.g., web browser, mobile app) and a server.                   Session tokens are typically issued after successful authentication and are used to authenticate subsequent requests within the same session.
Examples include session cookies, session IDs, and tokens generated by session management systems.
                    
Refresh Tokens:
Refresh tokens are credentials used to obtain new access tokens after access tokens expire in authentication protocols like OAuth 2.0.
Refresh tokens are issued alongside access tokens during the initial authentication process and are used to obtain fresh access tokens without requiring the user to reauthenticate.
Refresh tokens are typically long-lived and have stricter security requirements than access tokens.
                    
Identity Tokens:
Identity tokens are used to represent user identity information, including user attributes, claims, and authentication status.
Identity tokens are often issued alongside access tokens in authentication protocols like OpenID Connect to provide additional information about the authenticated user.
Examples include ID tokens in OpenID Connect, which are JWTs containing user identity claims.

API Tokens:
API tokens are credentials used to authenticate and authorize access to APIs (Application Programming Interfaces) or web services.                    
API tokens are often used in API authentication schemes to identify and authenticate clients making requests to APIs.
API tokens can be long-lived or short-lived and may be issued to individual users, applications, or services.
                    
Cryptographic Tokens:
Cryptographic tokens are used in cryptographic systems and protocols to represent cryptographic keys, digital signatures, or other cryptographic data.
Examples include security tokens used in cryptographic authentication schemes like HMAC (Hash-based Message Authentication Code) and digital signature tokens used in digital signatures and certificate-based authentication.
                    
Hardware Tokens:
Hardware tokens are physical devices used to generate or store authentication credentials, cryptographic keys, or other sensitive data.
Examples include hardware security keys, smart cards, USB tokens, and security tokens used in two-factor authentication (2FA) and multi-factor authentication (MFA) systems.
These are just a few examples of the various types of tokens used in computer science, cryptography, and security. Tokens play a crucial rolein authentication, authorization, secure communication, and identity management, and understanding their different types and functions is essential for building secure and robust systems and applications.


OAuth 2.0: If you’ve ever signed up to a new application and agreed to let it automatically source new contacts via Facebook or your phone contacts, then you’ve likely used OAuth 2.0. This standard provides secure delegated access. That means an application can take actions or access resources from a server on behalf of the user, without them having to share their credentials. It does this by allowing the identity provider (IdP) to issue tokens to third-party applications with the user’s approval.

OpenID Connect: If you’ve used your Google to sign in to applications like YouTube, or Facebook to log into an online shopping cart, then you’re familiar with this authentication option. OpenID Connect is an open standard that organizations use to authenticate users. IdPs use this so that users can sign in to the IdP, and then access other websites and apps without having to log in or share their sign-in information. 

SAML: You’ve more likely experienced SAML authentication in action in the work environment. For example, it enables you to log into your corporate intranet or IdP and then access numerous additional services, such as Salesforce, Box, or Workday, without having to re-enter your credentials. SAML is an XML-based standard for exchanging authentication and authorization data between IdPs and service providers to verify the user’s identity and permissions, then grant or deny their access to services.

Enterprises rely on web frameworks and protocols like OAuth 2.0, OpenID, and SAML to bring structure and security to federated identity. Knowing when to use each is a key step towards protecting your organization’s data from the ground up.






