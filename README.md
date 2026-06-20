   May 2026.LinkedIn Live. First product on Gumroad. First security audit completed.Aevron Security is open for business.         
   May 2026. Completed TryHackMe What is Networking room. Started Kali Linux lab setup. Agency audit rewritten. Medium article skeleton drafted.
    May 2026. Audit finalized with Executive Summary. Medium article drafted. mpesa_validator.py committed. Post 3 live.
   May 2026. Completed TryHackMe network module.Final touches of the agency done.Approach to local business started.
 June 2026 .Cache: A local "cheat sheet" that saves website addresses to speed up future visits.
TTL (Time To Live): An expiration timer that tells your computer when to refresh a cached address.
Domain: The human-friendly name for a website, like google.com.
IP Address: The numerical "street address" of a server on the internet.
DNS: The system that translates domain names into IP addresses.
MX Record: A setting that directs incoming emails to a specific mail server.
Nameserver: The authoritative server that holds the official master list of DNS records for a domain.
Recursive Resolver: The server that performs the search for an IP address on your behalf.
Root Server: The backbone of the internet that directs requests to the correct TLD (like .com or .org).
 June 2026:URL Structure: Parsed components including Scheme, Host, Port (1-65535), Path, and Query Strings.
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
 June 2026.
Web Servers: Learned how servers process HTTP requests and deliver web content to clients.
Load Balancers: Explored how traffic is distributed across multiple servers to ensure high availability and prevent single points of failure.
HTML Injection: Defined as a vulnerability where unsanitized user input allows malicious HTML code to be rendered on a webpage.
Practical: Successfully identified an injection point and executed a basic payload to modify the DOM and verify the vulnerability.
 June 2026
 Linux basic commands and navigation
 I can access a rmote machine using ssh i.e ssh username@ipaddress
 ssh is a protocol between devices in an encrypted form 
 Basic file system interaction commands- touch(create file) mkdir(create a folder) cp(copy a file/folder) mv(move a file/folder) file(determine type of file)
 Permissions - rwx.r-read, w-write  & x-execute.rwx(<-Owner)rwx(<-Group)rwx(<-Others).4-read 2-write 1-execute.
 We use su to switch to a user. su -l to siwtich to the home dir of the new user.
 Common Directories:Directory(virtual container used to store files and folders)./etc(etcetera)- stores system files used by OS .Passswords in linux are stored in an encrypted format known as shao512. /var(variable data) stores data frequently accessed or written by services or apps running on the system . /root actual home for the root system user.Home dir for the root user. /tmp store data that is only needed to be accessed once or twice.Any user can write to this folder by default (useful in pentesting)Once we have access to a machine its a good place to store things like enumeration scripts.
 1. Terminal Text Editors
- How to use editors like Nano and Vi to change files without a desktop interface.

 2. General Utilities
- Downloading files via the command line.
- Serving content instantly using a Python web server: 'python3 -m http.server 8000'.

 3. Process Management
- How to view, monitor, and stop active programs using 'ps', 'top', and 'kill'.

 4. Automation with Crontabs
- Setting up scheduled tasks to run automatically at specific times.

 5. Package Management
- Installing, updating, and removing software using tools like 'apt'.
 6. System Logs
- Reviewing logs in  '/var/log' to troubleshoot errors and see who is accessing the system.
Study Notes: Client-Server Architecture & State Management
1. Client-Server Model

Client: The requester (e.g., your smartphone, laptop, or browser). It asks for data or services.
Server: The provider (a powerful computer). It stores data and "serves" it back to the client upon request.
The Interaction: A simple "Request-Response" cycle.

2. Server Identification

IP Address: The unique digital address of a server on a network. While we use domain names (like google.com), computers use IP addresses to find each other.

3. Statelessness vs. Statefulness

Stateless (HTTP): By default, the web is "forgetful." Every request is treated as if it’s the first time the client and server are meeting.
Stateful: Modern apps need to "remember" users (e.g., keeping you logged in). To do this, they use mechanisms like Cookies and Tokens.

4. Cookies & Authentication

The Mechanism: When you log in, the server sends a small piece of data (a Cookie/Token) to your browser.
The Benefit: Your browser attaches this "digital gate pass" to every future request.
The Result: You don't have to re-authenticate (log in) every time you refresh the page or click a new link.

5. Kenyan Context Analogy

Client: The customer at a Kibanda.
Server: The shopkeeper with the stock.
Cookie: A "loyalty card" or "gate pass" that tells the shopkeeper they already know who you are, so you don't have to introduce yourself every time you walk in.
