CAM provides the following features:
	
**1) Authorized access to resources under root account**
	
The access to the resources under a root account can be authorized to other users, including sub-accounts or other root accounts, without sharing the identity credentials of the root account.
	
**2) Refined permission management**
    
Different access permissions to a kind of resources can be granted to different users. For example, some sub-accounts can be granted the read permission for a COS storage bucket, while some other sub-accounts or root accounts can own the write permission for the COS storage bucket. You can work with the resources, access permissions and users in batch.
	
**3) Identity authentication**
	
Confirm the identity of the visitor.
	
**4) Final consistency**
	
CAM currently is available in multiple regions of Tencent Cloud, and implements cross-region data synchronization through the replication of policy data. Any modification of a CAM policy is submitted in time, but the cross-region policy synchronization can lead to the delay of taking effect of the policy. At the same time, CAM uses cache to improve performance (one-minute cache currently), the update does not take effect until the cache expires.

