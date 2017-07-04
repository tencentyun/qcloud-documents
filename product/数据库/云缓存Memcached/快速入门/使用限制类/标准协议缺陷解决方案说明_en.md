## 1 Background

There are defects in the design of standard Memcached protocols. The GET operations do not have any error codes, thus they cannot clearly describe the situation when they fail to pull data. Therefore, do not fully trust NO_DATA returned by Memcached API as this may be caused by network problems.

The following procedure is extremely dangerous because it will initialize user data:
if(NO_DATA) InitData();   

## 2 Solution

(1) To address the problem mentioned above, developers need to distinguish between "add" and "set" operations when storing data

"add" operations: Store data according to corresponding <key>, and only store the data when the data does not exist.

"set" operations: Store data according to corresponding <key>, whether the data exists or not.

Developers must use "add" API to add data, instead of "set" API. The latter will reset user data and cause business loss.

(2) Cloud Memcached service also provides Memcached text extension protocols (see [Cloud Memcached Compatible Protocol Instruction](/doc/product/241/兼容的协议说明)). Clients can use the two new extension commands (get_ext, gets_ext) to determine whether the data exists according to error code. This avoids accidental user data initialization when GET operation fails to acquire data due to network and device problems. Note that users need to modify APIs on their own to support the use of extension protocols.

## 3 Use Case

1. Business A doesn't distinguish between "add" and "set" operations. Some connections were disconnected when changing access layers, which affected queries and caused certain user data to be initialized.
2. Business B doesn't distinguish between "add" and "set" operations. Queries could not acquire data when Cloud Memcached device failed, which caused certain user data to be initialized.
3. Business C often receives reports that certain data is reset. Investigation proved that this is caused by using "set" to add data, which will lead to data reset during brief network disconnections.
These cases all brought huge damage and loss to their businesses, and the services need to be stopped for several hours to roll back data. Therefore, developers must remember to use "add" API to add data.
