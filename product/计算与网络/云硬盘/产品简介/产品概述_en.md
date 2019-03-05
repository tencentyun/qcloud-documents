Cloud Block Storage provides a highly efficient and reliable [storage](/doc/product/213/4952) device for the CVM instance. It is a highly available, highly reliable, low-cost, and customizable block storage device that can be used as an independent scalable disk for CVM. It provides data storage at data block level and employs a three-copy distributed mechanism, thus ensuring the data reliability for CVM.

CBS can automatically copy your data in the availability zone to different machines as backup, to avoid data loss resulting from failure of a single machine and improve data availability and persistency. CBS is classified into HDD cloud storage and SSD cloud storage by performance. You can easily purchase, adjust, and manage your CBS devices via console, and create a storage space that is larger than the volume of a single CBS device by building a file system.

Tencent Cloud CBS provides persistent block-level storage that can be mounted on any running instances in an availability zone. CBS is often used as a main storage device (such as file system and database) for the data that requires frequent and fine-grained updates. It is featured by high availability, high reliability, and high performance.

The non-elastic cloud storage is created/terminated depending on the creation/termination of the CVM instance, while the life cycle of the elastic cloud storage is independent of the CVM instance and is always not affected by the instance runtime. For the non-elastic cloud storage, it is recommended that you purchase and use it when creating the instance;  for the elastic cloud storage, you can mount multiple cloud storages to one instance, or unmount the cloud storages from the current instance and mount them to another one.

Tencent Cloud imposes restrictions on the quantity of cloud storages and the total storage volume users can enjoy. For details on such restriction, refer to [Usage Constraints](/doc/product/362/5145).


