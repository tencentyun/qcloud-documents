Database instance is a standalone database environment running on the cloud. A database instance can contain multiple user-created databases and can be accessed using the same tools and applications as those in a standalone database instance. Tencent Cloud database for MySQL contains three types of database instances.
### Master Instance
The instance that contains read-only instances is called master instance. A master instance is both readable and writable, and is visible in the instance list. You can manage a master instance's read-only instances on the details page of the master instance.

### Read-only Instance
The instance that only allows read access is called read-only instance. A read-only instance cannot exist alone, and must belong to a master instance. A read-only instance only acquires data through synchronization with the master instance, and is visible in the instance list.

### Regular Instance
The instance that does not contain any read-only instance is called regular instance. A regular instance is both readable and writable, and is visible in the instance list. After the activation of GTID in MySQL 5.6, you can upgrade a regular instance to a master instance by purchasing a read-only instance.

