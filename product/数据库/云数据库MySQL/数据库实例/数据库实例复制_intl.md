## Replication Methods for Database Instances
For CDB for MySQL database instances, data replication can be achieved by three ways:
* Asynchronous Replication
> An application initiates a data update (including insert, update and delete operations) request. After completing the update operation, the Master sends a response to the application immediately, and then replicates the data to the Slave.
> During the data update, the Master needs not to wait for a response from the Slave, so the database instance replicated in an asynchronous way often has a higher performance and the unavailability of Slave does not prevent the Master from providing services. However, since the data is not synchronized to the Slave in real time, if the Master fails when a latency occurs on the Slave, there is a little chance of data inconsistency.
> Asynchronous replication of CDB for MySQL uses a "One Master, One Slave" architecture.
 
* Strong Synchronous Replication
> An application initiates a data update (including insert, update and delete operations) request. After completing the update operation, the Master replicates the data to a Slave immediately. After receiving the data, the Slave returns success message to the Master. Only after receiving the message from the Slave the Master can return a response to the application.
> Since the data is replicated synchronously from the Master to the Slave, for each update operation of the Master, the success of update on the Slave must be ensured. As a result, strong synchronous replication can maximize the data consistency between the Master and the Slave. However, each update request of the Master cannot be executed until it gets the response of the Slave, so the unavailability of the Slave can greatly affect the operations on the Master.
> Strong synchronous replication of CDB for MySQL uses a "One Master, Two Slaves" architecture to prevent the unavailability of a single Slave from affecting the operations on the Master, improving the availability of strong synchronous replication cluster.

* Semi-synchronous Replication
> Generally, strong synchronous replication is employed. Only when an exception occurs with the data replication (a Slave node becomes unavailable or an exception occurs with the network used for data replication), the Master will suspend the response to the application (for about 10 seconds by default in MySQL), and the replication will be downgraded to asynchronous replication. When the data replication returns to a normal state, strong synchronous replication will be restored.
> Semi-synchronous replication of CDB for MySQL uses a "One Master, One Slave" architecture.

