## System Limits

- CFS-supported file system protocols: NFS v3.0/v4.0, CIFS/SMB.
- Maximum capacity of a single file system: 160 TB.
- A file system can be mounted with a maximum of 200 computing nodes.
- Each user can have a maximum of 10 file systems in a region.
- UID and GID:

  - When NFS v3.0 protocol is used, if UID or GID of the file does not exist in the local account, UID and GID directly appear; if not, relevant user and group names appear based on the mapping relations of the local UID and GID.
  - When NFS v4.0 protocol is used, if the Linux version is later than 3.0, the UID and GID rules are the same as NFS v3.0 protocol; if not, all files' UID and GID will show up as "nobody".
  - Note: When you mount a file system to a Linux version earlier than 3.0 using NFS v4.0 protocol, it is recommended not to perform "change owner" or "change group" to the file or directory. Otherwise, its UID and GID will become "nobody".
  
- Supported CIFS/SMB protocol
 
 	- Supported protocol versions: CIFS/SMB 1.0 and later are supported. But it is not recommended to mount file systems using SMB 1.0, because SMB 1.0 is not as good as SMB 2.0 and later versions in terms of performance and features. Another reason is that Windows products supporting SMB 1.0 or earlier versions have run out of Microsoft support lifecycle.
 	- Users cannot use NFS and SMB to access the same file system or directly access SMB file system via WAN.
 	- Read and write ACL is provided only at the file system level. No ACL is provided at the file/directory level.
 	- IOCTL/FSCTL operations such as file sparsing, file compression, ENI status query, and point reparsing are not supported.
 	- Alternate Data Streams is not supported.
 	- Some protocol features in SMB 3.0 or later (such as SMB Direct, SMB Multichannel, SMB Directory Leasing, and Persistent File Handle) are not supported. 
		
<!--
* Attributes not supported by NFS v4.0 include: FATTR4_MIMETYPE, FATTR4_QUOTA_AVAIL_HARD, FATTR4_QUOTA_AVAIL_SOFT, FATTR4_QUOTA_USED, FATTR4_TIME_BACKUP, and FATTR4_TIME_CREATE. If these attributes are attempted, an NFS4ERR_ATTRNOTSUPP error will display on the client.
* OP not supported by NFS v4.0 include: OP_DELEGPURGE, OP_DELEGRETURN, and NFS4_OP_OPENATTR. If these OPs are attempted, an NFS4ERR_NOTSUPP error will display on the client.
* NFSv4 does not support Lock and Delegation.
-->		
		
		

		
 




