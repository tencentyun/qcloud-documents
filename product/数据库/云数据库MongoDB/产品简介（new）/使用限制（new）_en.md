## 1 Version & Engine

1) Currently, only the MMAPv1 engine is supported. WiredTiger engine will be supported in the near future.
2)	MMAPv1 engine uses the newest version of MongoDB 3.0 major version.

## 2 Replica Set & Sharding Cluster

### 2.1 Replica Set

There are two options when creating a MongoDB instance:

| Node Configuration | Description |
|:--:|:--:|
| 1 master, 1 salve, 1 arbiter | Includes 1 Primary node, 1 Secondary node and 1 Arbiter node |
| 1 master, 2 slaves | Includes 1 Primary node and 2 Secondary nodes |

There is a group of proxies (mongos in the MongoDB service component) before each replica set, and the URI for service connection appears like this:
```
mongodb://rwuser:password@10.66.77.88:27017/admin?authMechanism=MONGODB-CR
```

You can set up a priority to read from Secondary in your driver after connecting to the MongoDB service, if required.

### 2.2 Sharding Cluster

Sharding cluster will become available soon.

## 3 Connection User Name

Currently you can only use the default user "rwuser", the role is [readWriteAnyDatabase+dbAdmin](https://docs.mongodb.org/v3.0/reference/built-in-roles/), which means this user can read and write any database, but is not permitted to perform critical operations.
User custom account management feature will become available soon.


## 4 Avoid Filling Up Disk

Write operation will be prohibited when the instance disk is 100% occupied, thus please expand capacity in time according to your business development. Contact customer service if you encounter such situation.
