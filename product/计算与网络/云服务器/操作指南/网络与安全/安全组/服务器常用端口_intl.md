The following describes the common server ports. For more information on service application ports on Windows, please see Microsoft official document ([Windows Service Overview and Network Port Requirements](https://support.microsoft.com/zh-cn/help/832017/service-overview-and-network-port-requirements-for-windows?spm=5176.7740724.2.3.omd4DB%3Fspm%3D5176.7740724.2.3.omd4DB)).

| Port | Service | Description |
|---------|---------|---------|
| 21 | FTP | FTP server's open port for upload and download. |
| 22 | SSH | Port 22 is the SSH port, used to remotely connect to Linux system servers in command-line mode. |
| 25 | SMTP | SMTP server's open port for sending emails. |
| 80 | HTTP | Used for Web services, such as IIS, Apache, Nginx, to provide external access. |
| 110 | POP3 | Port 110 is open for POP3 (email protocol 3) service. |
| 137, 138, 139 | NETBIOS protocol | Port 137 and 138 are UDP ports used to transfer files via My Network Places. <br>Port 139: Incoming connections over port 139 attempt to obtain NetBIOS/SMB service. This protocol is used for file and printer sharing on Windows as well as SAMBA service. |
| 143 | IMAP | Port 143 is mainly used for "Internet Message Access Protocol" (IMAP) v2, a protocol for receiving emails as the same as POP3. |
| 443 | HTTPS | Web browsing port. This is another type of HTTP that supports encryption and transfer over secure ports. |
| 1433 | SQL Server | Port 1433 is the default port for SQL Server. The SQL Server service uses two ports: TCP-1433 and UDP-1434. Port 1433 is used by SQL Server to provide external services, and port 1434 is used to send requester a response about which TCP/IP port is used by SQL Server. |
| 3306 | MySQL | Port 3306 is the default port for MySQL database and is used by MySQL to provide external services. |
| 3389 | Windows Server Remote Desktop Services | Port 3389 is the service port for remote desktop on Windows 2000 (2003) Server. You can connect to a remote server using the "Remote Desktop" connection tool via this port. |
| 8080 | Proxy Port | Just like port 80, port 8080 is used for WWW proxy service for web browsing. Port number ":8080" is often added when users visit a website or use a proxy server. In addition, after Apache Tomcat Web server is installed, the default service port is 8080. |

