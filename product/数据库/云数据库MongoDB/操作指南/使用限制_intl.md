## 1 Engine

Support WiredTiger engine and Rocks engine.


## 2 Cluster Types
There are two options when creating a MongoDB instance:

| Node Configuration | Description |
|:--:|:--:|
| Replica set cluster | 1 master, 2 slaves. Includes 1 Primary node and 2 Secondary nodes |
| Sharding cluster | A single instance contains at least 5 shards, and each shard consists of at least 3 nodes. It is expandable. |
For replica set instances, you can set up a priority to read from Secondary first in your driver after connecting to the MongoDB service. For replica set instances, nodes can be expanded vertically. For sharding instances, nodes can be expanded vertically and shards can be expanded horizontally to support business scenarios of massive data.

## 3. Limit on Number of Connections
| MEM specification | Max connections |
|:--:|:--:|
|2G|1500|
|4G|1500|
|6G|1500|
|8G|1500|
|12G|1500|
|16G|2500|
|24G|3500|
|32G|4500|
|48G|6000|
|64G|9000|
|128G|15000|
|240G|15000|
|512G|15000|
Note: The upper limit on number of connections is applicable to instances rather than nodes.

## 4 Connection User Name

There are two built-in default users: "rwuser" and "mongouser". The role for the built-in users is [readWriteAnyDatabase+dbAdmin](https://docs.mongodb.org/v3.0/reference/built-in-roles/), that is, the users can read and write any database, but are not permitted to perform critical operations.
Depending on the version of TencentDB for MongoDB, some instances only have rwuser (we will upgrade such instances and will contact you before doing so).
You can also use the Tencent Cloud MongoDB console for account authorization and permission management to meet requirements in various business scenarios.

## 5 Avoid Filling Up Disk

Write operation will be prohibited when the instance disk is 100% occupied, thus please expand capacity in time according to your business development. Contact customer service if you encounter such situation.

