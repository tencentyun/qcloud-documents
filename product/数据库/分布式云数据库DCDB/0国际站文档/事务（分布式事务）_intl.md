
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).

### Transactions (distributed transactions)

As the data for transaction operations typically spans multiple physical nodes, similar solutions are called distributed transactions in distributed database. By default, DCDB (5.7 or above) supports distributed transactions. It is transparent to clients. Business is used like a stand-alone transaction. For example:
```
	begin; //Enable the transaction
	delete
	update //Operations across sets
	select
	insert
	commit; //Commit the transaction
```

Add SQL for transactions to query the information of a specific transaction:
1. select gtid(). Get the GTID (globally unique identifier of a transaction) of the current distributed transaction. Null is returned if the transaction is not a distributed transaction;
Format of GTID:
'Gateway ID' - 'Random value of gateway' - 'Sequence number' - 'Timestamp' - 'Partition number'. For example, c46535fe-b6-dd-595db6b8-25
2. select gtid_state("gtid"). Get the status of "gtid". Here are the possible results:
a) "COMMIT". Identify that the transaction has been or will be committed
b) "ABORT". Identify that the transaction will be rolled back
c) Null. The status of the transaction will be cleared after one hour, so there are two possibilities:
 1. For query after one hour, it identifies that the transaction status has been cleared
 2. For query within an hour, it identifies that the transaction will be rolled back

	Note: When the "commit" operation times out or fails, you should wait a few seconds before calling the API to query the status of the transaction

3. OPS commands:
	xa recover: Send the command "xa recover" to the backend "set" and summarize the results.
	xa lockwait: Display the wait relationship of the current distributed transaction (you can use the "dot" command to convert the output to a wait diagram).
	xa show: Show the distributed transactions that are currently running on the gateway.

### Note
TDSQL distributed transaction adopts a two-phase commitment algorithm (2PC) with an isolation level configured as "read committed", "repeatable read", or "serializable".

