
Insecure deserialization is a vulnerability in which untrusted or unknown data is used to inflict a denial-of-service attack, execute code,
bypass authentication or otherwise abuse the logic behind an application.

Serialization is the process that converts an object to a format that can later be restored. Deserialization is the opposite process, which 
takes data from a file, stream or network and rebuilds it into an object.

NOTE :- 
Serialized objects can be structured in text, such as JSON, XML or YAML. Serialization and deserialization are safe, common processes in web applications. However,
an attacker can abuse the deserialization process if it's left insecure. Attackers could, for example, inject hostile serialized objects into a web app, where the
victim's computer would initialize deserialization of the hostile data. Attackers could then change the angle of attack, making insecure deserialization the initial 
entry point to a victim's computer.

How to detect insecure deserialization
It is hard to detect attacks caused by insecure deserialization because the process of deserialization uses common code libraries found in web development. 
Some ways to identify insecure deserialization include the following:

1. Check deserializations to see if the data is correctly handled as user input instead of trusted internal data.
2. Check deserializations to ensure the data is what it is supposed to be before it is used.
3. Use a monitoring tool for deserializations and set notifications for common vulnerable components.
4. Run regular security scans.

** How to avoid insecure deserialization
Use the following best practices to avoid insecure deserialization:

1. Monitor the deserialization process.
2. Encrypt serialization processes.
3. Do not accept serialized objects from unknown or untrusted sources.
4. Run the deserialization code with limited access permissions.
5. Use a firewall that detects insecure deserialization.


Data which is untrusted cannot be trusted to be well formed. Malformed data or unexpected data could be used to abuse application logic, deny service, 
or execute arbitrary code, when deserialized.


CONSEQUENCES :-
Availability: The logic of deserialization could be abused to create recursive object graphs or never provide data expected to terminate reading.
Authorization: Potentially code could make assumptions that information in the deserialized object about the data is valid. Functions which 
               make this dangerous assumption could be exploited.
Access control (instruction processing): malicious objects can abuse the logic of custom deserializers in order to affect code execution.


Exposure period
Requirements specification: A deserialization library could be used which provides a cryptographic framework to seal serialized data.
Implementation: Not using the safe deserialization/serializing data features of a language can create data integrity problems.
Implementation: Not using the protection accessor functions of an object can cause data integrity problems
Implementation: Not protecting your objects from default overloaded functions - which may provide for raw output streams of objects - may cause data confidentiality problems.
Implementation: Not making fields transient can often cause data confidentiality problems.



Likelihood of exploit
Medium

It is often convenient to serialize objects for convenient communication or to save them for later use. However, deserialized data or code can often be modified without 
using the provided accessor functions if it does not use cryptography to protect itself. Furthermore, any cryptography would still be client-side security - which is of 
course a dangerous security assumption.

An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the non-transient data should be. This is an excellent way to
prevent time, environment-based, or sensitive variables from being carried over and used improperly.

Risk Factors
Does the deserialization take place before authentication?
Does the deserialization limit which types can be deserialized?
Does the deserialization host have types available which can be repurposed towards malicious ends? Sometimes, these types are called “gadgets”, considering their
similarity to abusable bits of code that already exist in machine code in Return-Oriented-Programming attacks.
Examples
The following is an example from Adobe’s BlazeDS AMF deserialization vulnerability (CVE-2011-2092). You can specify arbitrary classes and properties for a BlazeDS
application to deserialize. This particular payload creates an instance of a JFrame object on the target server. The created JFrame object will have a “defaultCloseOperation”
of value 3 – which indicates that the JVM should exit when this JFrame window is closed.









