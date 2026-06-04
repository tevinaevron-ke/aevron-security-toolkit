Day 1 - 26th May 2026.LinkedIn Live. First product on Gumroad. First security audit completed.Aevron Security is open for business.         
Day 2 — 27th May 2026. Completed TryHackMe What is Networking room. Started Kali Linux lab setup. Agency audit rewritten. Medium article skeleton drafted.
Day 3 — 28th  May 2026. Audit finalized with Executive Summary. Medium article drafted. mpesa_validator.py committed. Post 3 live.
Day 4 - 29th May 2026. Completed TryHackMe network module.Final touches of the agency done.Approach to local business started.
Day 5- 3rd June 2026 .Cache: A local "cheat sheet" that saves website addresses to speed up future visits.
TTL (Time To Live): An expiration timer that tells your computer when to refresh a cached address.
Domain: The human-friendly name for a website, like google.com.
IP Address: The numerical "street address" of a server on the internet.
DNS: The system that translates domain names into IP addresses.
MX Record: A setting that directs incoming emails to a specific mail server.
Nameserver: The authoritative server that holds the official master list of DNS records for a domain.
Recursive Resolver: The server that performs the search for an IP address on your behalf.
Root Server: The backbone of the internet that directs requests to the correct TLD (like .com or .org).
Day 6 4th June 2026:URL Structure: Parsed components including Scheme, Host, Port (1-65535), Path, and Query Strings.
Port Mechanics: Learned that ports below 1024 require root privileges and that a single port can handle multiple sessions via the 5-tuple identifier.
Request-Response Model: HTTP is a stateless protocol where the client sends a request and the server returns a status code (e.g., 200 OK) and the requested data.
DNS vs. HTTP: DNS translates names to IPs, while HTTP handles the communication between the browser and the server.The 5-tuple is a set of five distinct values used to uniquely identify a network connection. It allows a server to handle thousands of simultaneous sessions on a single port without mixing up data between different users.

The five components are:

Source IP Address: The IP address of the device sending the data (the client).
Source Port: A random port assigned by the client's device for that specific connection.
Destination IP Address: The IP address of the server receiving the data.
Destination Port: The specific service port on the server (e.g., 80 for HTTP or 443 for HTTPS).
Protocol: The communication standard being used (typically TCP or UDP).
As long as one of these five values is different, the operating system treats it as a unique session.
