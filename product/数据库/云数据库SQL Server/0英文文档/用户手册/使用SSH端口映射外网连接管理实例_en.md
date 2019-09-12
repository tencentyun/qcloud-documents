For data security, public IP has not been enabled for CDB for SQL Server, but you can use SSH2 port mapping to connect, configure and manage instances in public network by following the steps below:
1. Prepare a Linux CVM with a public IP
2. Use an SSH tool (such as SecureCRT or Putty) to configure port mapping, start a service port locally, and then connect the SSH tool to the Linux CVM. By doing so, you can connect to local service port with SSMS.
![](//mccdn.qcloud.com/static/img/3f9a661b42fed1648d8b00091d5ace60/image.png)

**Take SecureCRT as an example:**
1. Enter "Session Attributes" and click "Add"
![](//mccdn.qcloud.com/static/img/072a1ba13c5281b206d70e7ce5294c17/image.png)
2. Enter the "Session Attributes" configuration page and configure the parameters
![](//mccdn.qcloud.com/static/img/edf3d44003eda115015002d28bd98266/image.png)
3. Log in to the Linux CVM and establish a connection
4. Use SSMS to connect to SQL Server instance
![](//mccdn.qcloud.com/static/img/0a25f830093d59d77a2b74f5c3d3e769/image.png)
