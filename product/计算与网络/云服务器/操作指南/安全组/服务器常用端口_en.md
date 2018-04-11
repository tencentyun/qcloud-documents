Here is a description of commonly used server ports. For more information on service application ports on Windows, refer to Microsoft official document ([Windows Service Overview and Network Port Requirements](https://support.microsoft.com/zh-cn/help/832017/service-overview-and-network-port-requirements-for-windows?spm=5176.7740724.2.3.omd4DB%3Fspm%3D5176.7740724.2.3.omd4DB)).

| Port | Service | Description |
|---------|---------|---------|
| 21 | FTP | FTP server uses this port for uploading and downloading. |
| 22 | SSH | Port 22 is the SSH port. It is used to remotely connect to Linux system servers in command-line mode. |
| 25 | SMTP | SMTP server uses this port for sending emails. |
| 80 | HTTP | Web services (IIS, Apache, Nginx) use this port to provide external access. |
| 110 | POP3 | This port is used for POP3 (email protocol 3) service. |
| 137, 138, 139 | NETBIOS protocol | Port 137 and 138 are UDP ports, used to transfer files via **My Network Places**.<br> Port 139: Connections over port 139 attempt to obtain NetBIOS/SMB service. This protocol is used for file and printer sharing on Windows and SAMBA. |
| 143 | IMAP | Port 143 is for "Internet Message Access Protocol" (IMAP) v2, a protocol for receiving emails, similar as POP3. |
| 443 | HTTPS | This port is used for web browsing port. Another type of HTTP that provides encryption and transmission over secure ports. |
| 1433 | SQL Server | This port is the default port for SQL Server. The SQL Server service uses two ports: TCP-1433 and UDP-1434. Port 1433 is used for SQL Server to provide external services, while port 1434 is used to return to the requester which TCP/IP port is used by SQL Server. |
| 3306 | MySQL | This port is the default port for MySQL database, is used by MySQL to provide external services. |
| 3389 | Windows Server Remote Desktop Services | Port 3389 is the service port for remote desktop on Windows 2000 (2003) Server, through which you can connect to a remote server using the "Remote Desktop" connection tool. |
| 8080 | Proxy port | As port 80, port 8080 is used for WWW proxy service for web browsing. Port number ":8080" is often added when users visit a website or use a proxy server. In addition, after Apache Tomcat web server is installed, the default service port is 8080. |

