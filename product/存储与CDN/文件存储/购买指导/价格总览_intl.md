## Billing Method
CFS (Cloud File Storage) is charged for the storage you actually used, and there is no minimum, traffic or request cost. The billing is based on the peak storage you actually used per hour.

## Storage Space
When a file system is created, it consumes 3 KB of storage by default, which will be counted into the storage you actually use.

## Supported Regions
The following is the regions where CFS is available:

Region | Availability Zone | Notes
------- | ------- | :------
Beijing | Beijing Zone 1 | Stockout. You are recommended to create a subnet within your VPC for Beijing Zone 2 or Beijing Zone 3 to access the CFS file system in either zone. [See mounting help>>](https://intl.cloud.tencent.com/document/product/582/9551#.E6.9F.90.E5.8F.AF.E7.94.A8.E5.8C.BA.E4.B8.8B-cfs-.E8.B5.84.E6.BA.90.E5.B7.B2.E5.94.AE.E7.BD.84.EF.BC.8C.E5.A6.82.E4.BD.95.E7.BB.A7.E7.BB.AD.E4.BD.BF.E7.94.A8.EF.BC.9F) 
| Beijing Zone 2 | Available 
| Beijing Zone 3 | Available
Shanghai | Shanghai Zone 2 | Stockout. You are recommended to create a subnet within your VPC for Shanghai Zone 3 to access the CFS file system in the zone. [See mounting help>>](https://intl.cloud.tencent.com/document/product/582/9551#.E6.9F.90.E5.8F.AF.E7.94.A8.E5.8C.BA.E4.B8.8B-cfs-.E8.B5.84.E6.BA.90.E5.B7.B2.E5.94.AE.E7.BD.84.EF.BC.8C.E5.A6.82.E4.BD.95.E7.BB.A7.E7.BB.AD.E4.BD.BF.E7.94.A8.EF.BC.9F)
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



