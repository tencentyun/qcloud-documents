## Overview

###  Overview
Cloud File Storage (CFS) provides a scalable shared file storage service that can be used with Tencent Cloud's services including CVM. CFS provides standard NFS and CIFS/SMB file system access protocols as well as shared data sources for multiple CVM instances or other computing services. It supports elastic capacity and performance expansion. The existing applications can be mounted for use without modification. As a highly available and reliable distributed file system, CFS is suitable for scenarios such as big data analysis, media processing, and content management.

CFS is easy to integrate, so you do not need to adjust your business structure or make complex configurations. To integrate and use CFS, just follow three steps: create a file system and mount point; launch the file system client on the server; and mount the created file system.

###  Features
#### Integrated management
CFS supports NFS v3.0/v4.0 and CIFS/SMB protocols, and provides standard POSIX access syntax (such as strong data consistency and file locking). Users can mount the file system by using the mount command for the standard operating system.

#### Automatic expansion
CFS can automatically expand the storage capacity of the file system based on file size without interrupting requests and applications during the process. It ensures exclusive storage resources while reducing management workload.

#### Security settings
CFS has high availability and persistency. Each file stored in a CFS instance has 3 redundant copies in multiple availability zones.
It supports VPCs, basic gateways, and access control.

#### Pay-as-you-go
CFS is billed by actual usage with no minimum spend, and does not have deployment or OPS fees. It allows CVMs to share the same storage space via the NFS or CIFS/SMB protocol, eliminating the need of purchasing other storage services or considering cache. 



