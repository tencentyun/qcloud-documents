
You can configure on the Linux or Windows Client that is mounted with the CFS file system to automatically mount the file system when the client is rebooted.

## Automatically Mounting NFS File System on Linux
1. Connect to the CVM instance to be automatically mounted by logging in CVM console or remote login. Open "/etc/fstab" file. Make sure that the account you logged in has "root" permission.

```
//Execute the following command to open fstab file
vi /etc/fstab

```

2. After that, enter "i" (insert) and add the following commands in /etc/fstab.

```
//Mount the file system with NFS4.0

<mount point IP>:/ <target mount directory> nfs4 nfsvers=4,hard,timeo=600,retrans=2,_netdev 0 0

E.g.: 10.10.19.12:/ /local/test nfs4 nfsvers=4,hard,timeo=600,retrans=2,_netdev 0 0

```

```
//Mount the file system with NFS3.0

<mount point IP>:/ <target mount directory> nfs nfsvers=3,hard,timeo=600,retrans=2,_netdev 0 0

E.g.: 10.10.19.12:/ /local/test nfs4 nfsvers=3,hard,timeo=600,retrans=2,_netdev 0 0

```

3. Press "Esc" and enter ":wq" to save the modification. Reboot the client, and the file system is automatically mounted.

> **Note**:
>
> When the command of automatic mounting is added but the shared file system is exceptional, Linux may not be started up because the automatic launch command in fstab is not executed. To solve this problem, enter "Single User Mode" when startup, delete the automatic mounting command in fastb, and then reboot the server.



## Automatically Mounting a File System on Windows
When mounting a file system, select "Reconnect When Login", as shown below. For more information, please see [Use CFS File System (Windows)](https://cloud.tencent.com/document/product/582/11524).

![](https://main.qcloudimg.com/raw/4e4731dddb8efdb7b1770912d9c8b8fd.png)
