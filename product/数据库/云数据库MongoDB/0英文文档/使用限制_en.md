## 1 Version & Engine

1) The current domestic regions including Beijing, Shanghai, and Guangzhou support MMAPv1 engine and WiredTiger engine


## 2 Replica Set & Sharding Cluster

### 2.1 Replica Set

There are two options when creating a MongoDB instance:

| Node Configuration | Description |
|:--:|:--:|
| 1 master, 2 slaves | Includes 1 Primary node and 2 Secondary nodes |

There is a group of proxies (mongos in the MongoDB service component) before each replica set, and the URI for service connection appears like this:
```
mongodb://rwuser:password@10.66.77.88:27017/admin?authMechanism=MONGODB-CR
```

You can set up a priority to read from Secondary first in your driver after connecting to the MongoDB service, if required.

### 2.2 Sharding Cluster

[Sharding Introduction](https://cloud.tencent.com/document/product/240/8333)



## 3 Connection User Name

There are two built-in default users: "rwuser" and "mongouser". The role for the built-in users is [readWriteAnyDatabase+dbAdmin](https://docs.mongodb.org/v3.0/reference/built-in-roles/), that is, the users can read and write any database, but are not permitted to perform critical operations.
Depending on the version of Tencent Cloud MongoDB, some instances only have rwuser (we will upgrade such instances and will contact you before doing so).
You can also use the Tencent Cloud MongoDB console for account and permission management to meet your business needs.

## 4 Avoid Filling Up Disk

Write operation will be prohibited when the instance disk is 100% occupied, therefore you need to expand capacity in time according to your business development. If you have such problem, you can contact customer service for help.
