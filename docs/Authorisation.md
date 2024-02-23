
Authorisation :- 

Authorization, often spelled "authorisation" in British English, refers to the process of granting permission or access rights to a resource, system, or data. In various contexts, authorization determines what actions or operations a user, application, or system can perform. It is a crucial aspect of security mechanisms in computer systems, networks, and software applications.

Authorization typically involves verifying the identity of a user or entity and then determining whether that entity has the necessary privileges or permissions to access specific resources or perform certain actions. These permissions are usually defined by an access control policy that dictates who can access what resources under what circumstances.

For example, in a computer system, authorization might involve granting a user the ability to read, write, or delete files, access certain software features, or perform administrative tasks based on their role or level of authority within the organization.

Authorization mechanisms often work hand in hand with authentication, which is the process of verifying the identity of a user or entity. Together, authentication and authorization help ensure that only authorized users can access resources and perform actions within a system, helping to maintain security and privacy.

<!-- Authorisation works post authentication...  -->

                                           Types of Authorisation  .... 

Authorization mechanisms can vary based on the specific context and requirements of a system or organization. Here are some common types of authorization:

1.) Role-based authorization: This approach grants permissions to users based on their roles within an organization. Each role is associated with a set of permissions, and users are assigned to roles that correspond to their responsibilities. For example, an employee might have a "manager" role that grants access to certain administrative functions, while a "regular user" role might only allow access to basic features.

2.) Attribute-based authorization: In this approach, access decisions are based on various attributes of the user, the resource being accessed, and the environment. These attributes can include user characteristics (such as department, job title, or location), resource properties (such as sensitivity or classification), and contextual factors (such as time of day or network location). Access policies are defined based on combinations of these attributes.

3.) Rule-based authorization: Rule-based authorization involves defining explicit rules or conditions that determine access rights. These rules can be based on a wide range of criteria, such as user attributes, resource properties, or environmental factors. For example, a rule might grant access to a resource only if the user's department matches a certain value, or if the request is made during business hours.

4.) Discretionary access control (DAC): DAC allows resource owners to determine who can access their resources and what level of access they have. Resource owners have the discretion to grant or revoke access permissions as they see fit. This approach is commonly used in file systems, where individual users can set permissions on their files and directories.

5.) Mandatory access control (MAC): In MAC systems, access decisions are centrally controlled by a security policy enforced by the operating system or security kernel. Access is based on labels or security classifications assigned to both users and resources, and access permissions are determined by comparing these labels according to predefined rules. MAC is commonly used in environments where strict security requirements must be enforced, such as government or military systems.

6.) Role-based access control (RBAC): RBAC extends role-based authorization by adding the concept of permissions and constraints. Users are assigned to roles, which are then granted permissions to perform specific actions on resources. Constraints can further refine access based on factors such as time, location, or other contextual information.


