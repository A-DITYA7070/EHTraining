                                                       
                                     
PORTS :- ports are the service windows through which we can get services to access with a physical port we interact with the hardware 
         access and with logical port we access the protocols service 

         Physical ports :- ex :- switch,ethernet port,cpu cooling fan, power connector,ps/2 port,usb port,audio jacks,vga port etc..
         logical ports :- HTTPS - 443
                          HTTP  - 80
                          FTP   - 20/21 
                          SSH   - 22
                          SMTP  - 25
                          DHCP  - 67/68
                          DNS   - 53


                                               HOW DNS SERVER WORKS .......

    DNS, which stands for Domain Name System, is a crucial component of how the internet functions. It serves as a directory that translates human-readable domain names (like "example.com") into IP addresses (like "192.0.2.1") that computers use to identify each other on the network. Here's a simplified explanation of how DNS works:

   1) Request Initiation: When you type a domain name into your web browser or click on a link, your device initiates a DNS lookup to find the corresponding IP address.

   2) Local DNS Cache: Your device first checks its local DNS cache to see if it already has the IP address for the requested domain stored. If it does, the lookup process ends here, and the device can use the cached IP address to connect to the website.

   3) Recursive DNS Servers: If the IP address is not found in the local cache, your device sends a DNS query to a recursive DNS server. These servers are typically provided by your internet service provider (ISP) or a third-party DNS provider like Google DNS or OpenDNS.

   4) Root Servers: If the recursive DNS server doesn't have the IP address cached either, it starts the process of finding the IP address by querying root DNS servers. These servers are the starting point of the DNS hierarchy and contain information about the authoritative DNS servers for top-level domains (TLDs) like .com, .org, .net, etc.

   5) TLD Name Servers: The root DNS servers direct the recursive DNS server to the appropriate TLD name server based on the domain's extension (e.g., .com, .org, .net). The TLD name server stores information about the authoritative DNS servers responsible for specific domain names within that TLD.

   6) Authoritative DNS Servers: The TLD name server provides the recursive DNS server with the IP address of the authoritative DNS server responsible for the specific domain name requested.

   7) Final Resolution: The recursive DNS server sends a query to the authoritative DNS server identified in the previous step, requesting the IP address associated with the domain name.

   8) Response: The authoritative DNS server responds to the recursive DNS server with the requested IP address.

   9) Caching and Response: The recursive DNS server caches the IP address for a period of time (called Time To Live or TTL) and sends the IP address back to your device. Your device also caches the IP address for future use, speeding up subsequent requests to the same domain.

   10) Connection: Finally, your device uses the obtained IP address to establish a connection to the web server hosting the desired website or service.

    This process happens seamlessly and rapidly behind the scenes every time you access a website by its domain name.
                                            
                                           DNS RECORDS...

Diff types of files in hosting...

1. A(address) :- It is most commonly used to map a fully qualified domain name (FQDN) to an ipv4 address and acts as a translator 
                 by converting domain names to ip address..
2. AAAA (quad a) :- similar to A records but maps to an ipv6 address (smart phones prefers ipv6 if available..)
3. ANAME :- This record type allows you to point root of your domain to a hostname or FQDN.
4. CNAME (Canonical Name) :- An alias that points to another domain or subdomain but never an IP address 
                            Alias record mapping FQDN TO FQDN multiple hosts to a single location This record is also good for when
                            you want to change an IP address over Time as it allows to make change without affecting user bookmarks.
5. 