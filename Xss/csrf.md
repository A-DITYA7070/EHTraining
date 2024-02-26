
                                                CSRF(Cross-Site Request Forgery).
                                                
CSRF stands for Cross-Site Request Forgery. It is a type of malicious exploit of a website where unauthorized commands are transmitted from a user that the web application trusts. This happens because the user is authenticated and the malicious commands are sent without the user's knowledge.

Here's how CSRF attacks typically work:

User Authentication: The victim user is authenticated on a website, usually by logging in and obtaining a session cookie.

Exploitation: While the victim user is still authenticated, they visit a malicious website or click on a link that sends a request (GET or POST) to the targeted website.

Forgery: This request contains commands that the targeted website would normally honor, as it trusts the user's session.

Execution: The targeted website executes the forged request, believing it to be a legitimate action initiated by the authenticated user.

CSRF attacks can have serious consequences, such as unauthorized fund transfers, changing account settings, or making unwanted purchases, depending on the actions permitted by the targeted website.

To mitigate CSRF attacks, web developers can employ several strategies:

CSRF Tokens: Include a unique, unpredictable token with each request that modifies state or performs sensitive actions. The token is validated by the server to ensure that the request originated from the legitimate user and not from a malicious source.

SameSite Cookie Attribute: Setting the SameSite attribute on cookies can prevent CSRF attacks by ensuring that cookies are not sent with cross-site requests, thus reducing the risk of unauthorized actions being performed on behalf of the user.

Custom Headers: Require custom headers in requests that modify state or perform sensitive actions. These headers are not typically present in cross-site requests, making it harder for attackers to forge requests.

Checking Referer Header: Validate the Referer header of incoming requests to ensure they originate from the expected domain. However, note that the Referer header can be spoofed or omitted, so it's not foolproof.
Short-lived Sessions: Keep session durations short to limit the window of opportunity for attackers to exploit CSRF vulnerabilities.
By implementing these and other security measures, web developers can significantly reduce the risk of CSRF attacks on their websites.
