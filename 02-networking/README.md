# 02 · Networking

**Estimate:** 2 weeks

## Objectives

- Explain how a request travels from a browser to an application.
- Design IP ranges for a cloud network.
- Troubleshoot connectivity methodically.

## Labs and checkpoints

### Lab 02.1 — TCP/IP and addressing

- [ ] Explain the OSI / TCP-IP layers with one protocol per layer
- [ ] Calculate subnets in CIDR notation (e.g. split `10.0.0.0/16` into four `/18` and several `/24`)
- [ ] Explain private vs public IP ranges and NAT

### Lab 02.2 — DNS

- [ ] Resolve a name with `dig` and explain A, AAAA, CNAME, MX, TXT, NS records
- [ ] Explain TTL and DNS propagation
- [ ] Trace a full resolution with `dig +trace`

### Lab 02.3 — HTTP and TLS

- [ ] Call the [Tasks API](../app/) with `curl -v` and explain each line of the request and response
- [ ] Explain status code families and common headers
- [ ] Inspect a TLS certificate with `openssl s_client` and explain the chain of trust

### Lab 02.4 — Reverse proxy and firewall

- [ ] Put **Nginx** in front of the Tasks API as a reverse proxy
- [ ] Enable HTTPS with a self-signed certificate (or Let's Encrypt on a real domain)
- [ ] Configure `ufw` to allow only SSH and HTTP(S)

### Lab 02.5 — Troubleshooting

- [ ] Use `ping`, `traceroute`/`mtr`, `ss`, `nc`, `curl` and `tcpdump` on a real problem
- [ ] Write a troubleshooting checklist: DNS → network → port → service → application

## Module done when

- [ ] I can explain, without notes, what happens when I type a URL and press Enter
- [ ] I can plan a VPC address range with public and private subnets

## Resources

- [Cloudflare Learning Center](https://www.cloudflare.com/learning/)
- [MDN — HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
