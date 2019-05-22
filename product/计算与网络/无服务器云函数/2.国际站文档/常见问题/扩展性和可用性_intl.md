### How is the availability of SCF?

SCF provides high availability through cross-region deployment, replication and redundancy.

### Is SCF still available when I change codes or configurations?

Yes. There is a short window period (generally less than 1 min) when a function is updated, during which the request is implemented by the old function code or the new function code.

### Is there a limit to the number of functions that can be run at a time?

SCF supports a large number of function instances running concurrently. However, we set a default security threshold: up to 20 concurrent executions per function. You can submit a ticket to increase the threshold.

### What happens when a function fails to handle an event?

When a failure occurs, the function called synchronously returns exception information. The function called asynchronously is retried automatically for another 3 times at the backend.