## Instance Types
* Regular Instance
> The instance that does not contain any read-only instance. A regular instance is both readable and writable, and is visible in the instance list. After the activation of GTID in MySQL 5.6, you can upgrade a regular instance to a master instance by purchasing a read-only instance.

* Master Instance
> The instance that contains read-only instance. A master instance is both readable and writable, and is visible in the instance list. You can manage a master instance's read-only instances on the details page of the master instance.

* Read-only Instance
> The instance that only allows read access. A read-only instance cannot exist alone, and must belong to a master instance. A read-only instance only acquires data through the synchronization with the master instance, and is invisible in the instance list.
