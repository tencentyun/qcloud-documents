When the CVM chooses 0Mbps bandwidth, the public network cannot be accessed. The CVM can only access the external network through a CVM with a Public IP.

## 1. Principle

- A CVM without a Public IP can access the public network through a CVM with a Public IP by using proxy on a CVM with a Public IP or via vpn.
- The proxy is easy to configure but complicated to use. It is suggested that you use pptp vpn to do this.  (i.e., A CVM without a Public IP can be connected with a CVM with a Public IP through pptp protocol, and the CVM with a Public IP will be set to the gateway in pptp network)

## 2. Configuration
Assume that a CVM with a Public IP is A, and a CVM without a Public IP is B.

1) Install pptpd on A, on CentOS for example (other Linux release versions are similar) using the following command:

```
yum install pptpd
```

2) Modify the configuration file /etc/pptpd.conf by adding the following two lines

```
localip 192.168.0.1
remoteip 192.168.0.234-238,192.168.0.245
```

3) Modify the configuration file /etc/ppp/chap-secrets by adding the username and password (the 1st column indicates the username, and the 3rd column indicates the password)

```
user    pptpd   pass    *
```

4) Start services

```
service pptpd start
```

5) Enable the forward capability

```
# echo 1 > /proc/sys/net/ipv4/ip_forward
# iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
```

6) Install the client on B, on CentOS for example, using the following command:

```
# yum install pptp pptp-setup
```

7) Create a configuration file

```
# pptpsetup --create pptp --server 10.10.10.10 --username user --password pass --encrypt
```

**Note: --server is followed by A's IP address.**

8) Connect pptpd

```
# pppd call pptp
```

9) Set the route:

```
# route add -net 10.0.0.0/8 dev eth0
# route add -net 172.16.0.0/12 dev eth0
# route add -net 192.168.0.0/16 dev eth0
# route add -net 0.0.0.0 dev ppp0
```

In addition, if B is Windows CVM, a network "Connecting to Workspace" can be created to connect to the pptpd server

