## Use SQL Server Management Studio in CVM
CDB for SQL Server does not come with SQL Server Management Studio (SSMS). If you need one, you can directly install the SSMS supporting SQL Server 2008 R2 in the CVM.

**Recommended installation environment**: Windows Server 2012 R2 Standard Edition, 64-bit
**Recommended configuration**: 1 core CPU, 2GB memory

**Official download address**: https: //download.microsoft.com/download/3/1/D/31D734E0-BFE8-4C33-A9DE-2392808ADEE6/SSMS-Setup-CHS.exe

**Official instructions**: Microsoft official documents
https://msdn.microsoft.com/zh-cn/library/ms174173(v=sql.105).aspx

## Use SQL Server Management Studio locally
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
4. Connect to SQL Server instance with SSMS
![](//mccdn.qcloud.com/static/img/0a25f830093d59d77a2b74f5c3d3e769/image.png)
 


