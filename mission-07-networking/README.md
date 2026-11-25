# Mission 7 — How computers communicate

## 1. Task / objective

Explain eight key networking concepts using a table. Run a connectivity test and a DNS lookup for `example.com` and record the actual results. Describe in five to seven steps what happens when you open a website in a browser.

## 2. Work completed

- Completed the network concepts table with plain-language explanations and examples.
- Ran `ping -c 4 example.com` and recorded the actual output.
- Ran `nslookup example.com` and recorded the actual output.
- Wrote a seven-step explanation of how a website opens.

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `ping -c 4 example.com` | Send four ICMP packets to `example.com` and report round-trip times and packet loss |
| `nslookup example.com` | Query a DNS server to find the IP address(es) associated with `example.com` |

## 4. My understanding

### Task 7.1 — Network concepts

| Concept | Explanation | Example |
|---------|------------|---------|
| **LAN** (Local Area Network) | A network that covers a small physical area such as a home, classroom or office. Devices on a LAN can communicate quickly because they are close together and connected by cables or Wi-Fi. | All the computers and phones connected to a home Wi-Fi router form a LAN. |
| **MAN** (Metropolitan Area Network) | A network that covers a larger area than a LAN, typically a city or large campus. It connects multiple LANs across that area. | A city library system connecting all its branch libraries with a shared network. |
| **WAN** (Wide Area Network) | A network that spans large geographical areas, often crossing countries or continents. The internet itself is the largest WAN. | The internet — connecting millions of networks worldwide so that a computer in one country can communicate with a server in another. |
| **DNS** (Domain Name System) | A service that translates human-readable domain names (like `example.com`) into the numeric IP addresses that computers use to find each other on a network. It works like a phone directory. | Typing `www.google.com` in a browser — DNS looks up the IP address so the browser knows which server to contact. |
| **Router** | A device that connects multiple networks together and decides the best path for data to travel from source to destination. It reads the destination address of each data packet and forwards it toward the correct network. | A home Wi-Fi router connects your home devices to your internet service provider's network and routes traffic between them. |
| **Protocol** | A set of agreed rules that devices must follow in order to communicate with each other. Without common rules, devices from different manufacturers could not exchange data. | HTTP (HyperText Transfer Protocol) defines how web browsers and servers exchange web pages. |
| **Packet switching** | A method of sending data where the message is broken into small pieces called packets. Each packet may travel a different path through the network and they are reassembled at the destination. This makes the network efficient and resilient. | Sending an email — the email is split into packets, each takes the best available path to the destination server, and they are reassembled into the full email there. |
| **Client-server** | An architecture where one device (the client) requests a service and another device (the server) provides it. The server waits for requests and the client initiates them. | A web browser (client) sends a request to a web server; the server responds with the HTML of the web page. |

---

### Task 7.2 — Network observations

#### Connectivity test

Command run:
```bash
ping -c 4 example.com
```

Actual output:
```
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=54 time=20.775 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=54 time=20.961 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=54 time=21.358 ms
64 bytes from 172.66.147.243: icmp_seq=3 ttl=54 time=20.799 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 20.775/20.973/21.358/0.233 ms
```

**Observation:** All 4 packets were received with 0% packet loss. The average round-trip time was about 21 milliseconds, which means the connection is fast and reliable.

A **connectivity test** (`ping`) checks whether a destination host is reachable over the network. It sends small test packets and measures whether they come back and how long they take. It is useful for diagnosing whether a network connection or a server is working.

#### DNS lookup

Command run:
```bash
nslookup example.com
```

Actual output:
```
Server:    8.8.8.8
Address:   8.8.8.8#53

Non-authoritative answer:
Name:  example.com
Address: 172.66.147.243
Name:  example.com
Address: 104.20.23.154
```

**Observation:** The DNS server used was 8.8.8.8 (Google's public DNS server). It returned two IP addresses for `example.com`: `172.66.147.243` and `104.20.23.154`. Having two addresses is common — it means the site can be reached from multiple servers (for reliability and speed).

A **DNS lookup** queries the DNS system and returns the IP address(es) linked to a domain name. This information tells us that `example.com` currently maps to those two IP addresses.

**Why DNS is needed:** Humans remember names like `example.com` more easily than numbers like `172.66.147.243`. DNS acts as a directory service that translates names into the numeric addresses that computers actually use to route data across the network. Without DNS, every user would need to know and type the exact IP address of every website.

*(Note: Private IP address, Wi-Fi name and local network details have not been included in this output.)*

---

### Task 7.3 — What happens when you open a website?

1. **You type the URL in the browser.** The browser (the client) reads the web address you typed, for example `https://example.com`, and prepares to send a request.

2. **DNS lookup.** The browser asks the DNS resolver (usually provided by your internet service provider or a public server such as 8.8.8.8) to translate `example.com` into an IP address. The resolver returns `172.66.147.243`.

3. **The browser contacts the server.** Using the IP address, the browser sends a connection request across the network to the web server at that address. The data travels through your home router, then across your ISP's network, then across the internet using packet switching — the request is broken into packets that find their way to the server.

4. **The server receives the request.** The web server receives the HTTP (or HTTPS) request. It looks up the requested page and prepares the response — the HTML, CSS and any images that make up the page.

5. **The server sends the response.** The server sends the response back across the internet to your computer. Again, the data is split into packets which travel back and are reassembled by your computer's network stack.

6. **The browser receives and renders the page.** Your browser reassembles the response packets, reads the HTML and CSS, and builds the visual page you see on screen.

7. **You see the website.** The page appears in the browser window. If you click a link, the whole process starts again for the new address. The protocol that governs all this communication (the rules for how request and response are formatted) is HTTP or its secure version HTTPS.

## 5. Difficulties faced

No major difficulties. I made sure to redact private network details (such as my local IP address and Wi-Fi name) from the output before recording it.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

| File | Description |
|------|-------------|
| `mission-07-networking/README.md` | This file containing the network concepts table, actual ping and nslookup output, and website explanation |

## 8. Commit details

**Commit message:** `Explain networking concepts and website communication`

Commit pushed to the `main` branch on GitHub. The file is visible in the `mission-07-networking/` folder.
