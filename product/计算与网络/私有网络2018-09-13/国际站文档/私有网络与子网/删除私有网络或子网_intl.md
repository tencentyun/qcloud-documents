You can delete VPC/subnet at any time, but you need to remove the cloud computing resources from the VPC/subnet in advance, such as CVM, cloud database, and cloud load balancer.
Under any of the following circumstances, the deletion of VPC/subnet may fail:
- There is an unpaid order related to this VPC/subnet
- There is a CVM with a status of "charges owed" and unavailability (including isolated and deleted CVMs) under the VPC/subnet
- Some operations within the VPC/subnet are in process
