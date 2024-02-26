
The target of an HTTP request is called a "resource", whose nature isn't defined further; it can be a document, a photo, or anything else. Each resource is identified by a Uniform Resource Identifier (URI) used throughout HTTP for identifying resources.

URLs and URNs
URLs:- 
The most common form of URI is the Uniform Resource Locator (URL), which is known as the web address.
A URL is composed of different parts, some mandatory and others optional.
ex :- http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument

URNs
A Uniform Resource Name (URN) is a URI that identifies a resource by name in a particular namespace.
ex:- 
urn:isbn:9780141036144
urn:ietf:rfc:7230

Scheme or protocol
Protocol
http:// is the protocol. It indicates which protocol the browser must use. Usually it is the HTTP protocol or its secured version, HTTPS. The Web requires one of these two, but browsers also know how to handle other protocols such as mailto: (to open a mail client) or ftp: to handle a file transfer. 

Common schemes are:
Scheme	        Description
data	          Data URLs
file	          Host-specific file names
ftp	            File Transfer Protocol
http/https	    Hyper text transfer protocol (Secure)
javascript	    URL-embedded JavaScript code
mailto	        Electronic mail address
ssh	            Secure shell
tel	            telephone
urn	            Uniform Resource Names
view-source	    Source code of the resource

Authority
Domaine Name
www.example.com is the domain name or authority that governs the namespace. It indicates which Web server is being requested. Alternatively, it is possible to directly use an IP address, but because it is less convenient, it is not often used on the Web.

Port
:80 is the port in this instance. It indicates the technical "gate" used to access the resources on the web server. It is usually omitted if the web server uses the standard ports of the HTTP protocol (80 for HTTP and 443 for HTTPS) to grant access to its resources. Otherwise, it is mandatory

Path
Path to the file
/path/to/myfile.html is the path to the resource on the Web server. In the early days of the Web, a path like this represented a physical file location on the Web server. Nowadays, it is mostly an abstraction handled by Web servers without any physical reality.

Query
Parameters
?key1=value1&key2=value2 are extra parameters provided to the Web server. Those parameters are a list of key/value pairs separated with the & symbol. The Web server can use those parameters to do extra stuff before returning the resource to the user. Each Web server has its own rules regarding parameters, and the only reliable way to know how a specific Web server is handling parameters is by asking the Web server owner.




ws/wss	WebSocket connections (Secure)
