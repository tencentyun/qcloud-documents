## Glossary
### Mount point
Each file system provides a mount point, which can be a destination address (i.e. an IP address) for access on a private network or a basic network. Users mount the file system to the local machine by specifying the IP of the mount point.

### Permission group
A permission group is a whitelist for access control provided by the file storage. Users can create permission groups and add rules for them to allow CVMs to access the file system with different permissions. **Note that each file system must be bound to one permission group.** 

### NFS file system
CFS supports NFS 4.0/3.0 protocol, which is better applicable to Linux and Unix clients.

### CIFS/SMB file systems
SMB (Server Message Block) protocol is an application-level communication protocol introduced by Microsoft for accessing files, printers, and other shared network resources on the network. CIFS (Common Internet File System) protocol is a public or open version of the SMB protocol. CIFS/SMB file systems can better support the access from Windows clients. CIFS/SMB protocols are now under public trial. [Click to apply for a trial](https://cloud.tencent.com/act/apply/CFS_CIFS).

	




