## Billing Method
CFS (Cloud File Storage) is charged for the storage you actually used, and there is no minimum, traffic or request cost. The billing is based on the peak storage you actually used per hour.

## Storage Space
When a file system is created, it consumes 3 KB of storage by default, which will be counted into the storage you actually use.

## Supported Regions
The following is the regions where CFS is available:

Region | Availability Zone | Notes
------- | ------- | :------
Beijing | Beijing Zone 1 | Stockout. You are recommended to create a subnet within your VPC for Beijing Zone 2 or Beijing Zone 3 to access the CFS file system in either zone. [See mounting help>>](https://intl.cloud.tencent.com/document/product/582/9551#how-can-i-continue-using-cfs-in-an-availability-zone-with-the-cfs-resources-sold-out.3F) 
| Beijing Zone 2 | Available 
| Beijing Zone 3 | Available
Shanghai | Shanghai Zone 2 | Stockout. You are recommended to create a subnet within your VPC for Shanghai Zone 3 to access the CFS file system in the zone. [See mounting help>>](https://intl.cloud.tencent.com/document/product/582/9551#how-can-i-continue-using-cfs-in-an-availability-zone-with-the-cfs-resources-sold-out.3F)
| Shanghai Zone 3 | Available 
Guangzhou | Guangzhou Zone 2 | Stockout
| Guangzhou Zone 3 | Available
| Guangzhou Zone 4 | Available
Hong Kong | Hong Kong Zone 1 | Stockout


## Pricing Details
The pricing of CFS products is shown below. The NFS and CIFS/SMB file systems share the same price.

Billing Method/Region | Mainland China |
------- | ------- | 
Linear price | 0.058 USD/GB/Month (0.00008056 USD/GB/hr) |


## Billing Example
An organization has 20 CVMs to access two file systems in Mainland China. The file system A is used for cold data storage, with a maximum storage of 500 GB. The file system B is used as enterprise cloud storage, with a peak storage of 105.6 GB in the current hour. 

The total cost of CFS for this hour = (500+105.6)*0.00008056 = 0.05 USD



