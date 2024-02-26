
                                          XSS (cross site scripting)

Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. It allows an attacker to circumvent the same origin policy, which is designed to segregate different websites from each other. Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform, and to access any of the user's data. If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application's functionality and data.

Xss can be carried out using any client side language..

To carry out a cross-site scripting attack, an attacker injects a malicious script into user-provided input. Attackers can also carry out an attack by modifying a request. If the web app is vulnerable to XSS attacks, the user-supplied input executes as code.
There are many ways to trigger an XSS attack. For example, the execution could be triggered automatically when the page loads or when a user hovers over specific elements of the page (e.g., hyperlinks).

Potential cosecuences of xss.'

Capturing the keystrokes of a user
Redirecting a user to a malicious website
Running web browser–based exploits (e.g., crashing the browser)
Obtaining the cookie information of a user who is logged into a website, thus compromising the victim’s account
In some cases, the XSS attack leads to a complete compromise of the victim’s account. Attackers can trick users into entering credentials on a fake form, which provides all the information to the attacker.

                                                Type of xss.

Stored XSS :- takes place when the malicious payload is stored in a database. It renders to other users when data is requested if there is no output encoding or sanitization.

Reflected XSS :- occurs when a web application sends attacker-provided strings to a victim’s browser so that the browser executes part of the string as code. The payload echoes back in response since it doesn’t have any server-side output encoding.

DOM-based XSS :- takes place when an attacker injects a script into a response. The attacker can read and manipulate the document object model (DOM) data to craft a malicious URL. The attacker uses this URL to trick a user into clicking it. If the user clicks the link, the attacker can steal the user’s active session information, keystrokes, and so on. Unlike stored XSS and reflected XSS, the entire DOM-based XSS attack happens on the client browser (i.e., nothing goes back to the server).


Strategies to prevent XSS attacks include :- 

Never trust user input. Always perform input validation and sanitization on input originating from untrusted sources as soon as you receive it. To provide comprehensive coverage, both inbound and outbound input handling should be considered.
Implement output encoding. This step is performed prior to writing user-controllable data. Output encoding escapes user input and ensures that the browser interprets it as benign data and not as code.

Follow the defense-in-depth principle. This strategy utilizes a variety of security controls to ensure the safety of your most valuable assets. Multiple walls of defense (controls) ensure that even if one wall is breached, there are others in place for protection from malicious attacks.

Ensure that web application development aligns with OWASP’s XSS Prevention Cheat Sheet. This is a list of tried and tested techniques to prevent XSS. OWASP advises the use of a combination of techniques as an XSS defense mechanism that can be customized for your specific application. 

Perform penetration testing to confirm remediation was successful. Seasoned penetration testers can implement the right real-world attack scenarios to ensure that your high-risk XSS vulnerabilities are fortified.