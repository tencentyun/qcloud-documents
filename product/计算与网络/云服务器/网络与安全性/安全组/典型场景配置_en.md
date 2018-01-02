### Remotely Logging in to Linux Instances via SSH

To log in to a Linux instance via SSH remotely, you need to add the following inbound rule to the security group associated with the instance:

| Source | Protocol Port | Policy |
|---------|---------|---------|
| 0.0.0.0/0 | TCP:22 | 	Allow |
> **Note:** You can set **IP range** or **security group** for the Source.

### Logging in to Windows Instances via MSTSC

To log in to a Windows instance via MSTSC, you need to add the following inbound rule to the security group associated with the instance:

| Source | Protocol Port | Policy |
|---------|---------|---------|
| 0.0.0.0/0 | TCP:3389 | 	Allow |
 > **Note:** You can set **IP range** or **security group** for the Source.
 
### Pinging a CVM Instance on Public Network

To test the communication status of the CVM instance using ping program, you need to add the following inbound rule to the security group associated with the instance:

| Source | Protocol Port | Policy |
|---------|---------|---------|
| 0.0.0.0/0  | ICMP | 	Allow |

> **Note:** You can set **IP range** or **security group** for the Source.

### Using CVM Instance as Web Server
If you create an instance as a Web server, you need to install the Web server program on the instance, and add the following inbound rule to the security group associated with the instance:

> **Note:** You need to start the Web server program first, and check whether the port is set to be 80.

| Source | Protocol Port | Policy |
|---------|---------|---------|
| 0.0.0.0/0  | TCP:80 | 	Allow |

### Uploading or Downloading Files with FTP
To upload/download files to/from a CVM instance with FTP, please add the following inbound rule to the security group associated with the instance:

> **Note:** You need to install the FTP server program on the instance, and then check whether the port 20/21 works properly.

| Source | Protocol Port | Policy |
|---------|---------|---------|
| 0.0.0.0/0  | TCP:22,21 | 	Allow |


