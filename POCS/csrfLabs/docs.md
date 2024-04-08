


 TESTING CSRF (own method) :-
 
 can be possible test first..
 Some servers can generate csrf token based on previous request and send it to response,
 This is vulnerable.
 when :-
     i) attacker can get to know about hashing algorithm used.
    ii) If no salting is used (or size of salting is less).
 In this case attacker can generate his own csrf_token.