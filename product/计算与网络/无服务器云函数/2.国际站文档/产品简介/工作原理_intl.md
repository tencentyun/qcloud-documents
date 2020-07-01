## Container Model During Function Running
When an event is triggered, SCF runs the function for you, allocates resources based on your configuration information (such as memory size), and launches and manages the container (which is the running environment for the function). The SCF platform is responsible for creating, managing and deleting function running containers. Users do not have permission to manage the containers.

It takes some time to launch a container, which creates a delay every time a function is called. But you will only notice such delay when a function is called for the first time, is updated, or is called after being unused for a long time. The platform will retain a container for a period of time to reuse it in subsequent calls in order to reduce the delay. The retained container will be directly reused for the calls initiated during this period.

The significance of container reuse mechanism:

- In the user code, all the declarations outside the [execution method](https://cloud.tencent.com/document/product/583/9210#.E6.89.A7.E8.A1.8C.E6.96.B9.E6.B3.95) will remain initialized, and can be directly reused when the function is called again. For example, if you have already established a database connection in your function code, this connection can be directly used when the container is reused. You can add logic in your code to check whether a connection already exists before you create a new connection.
- Each container provides a certain amount of disk space in the `/tmp` directory. The contents in this directory are retained during the retention of a container and are used as temporary caches for multiple calls. Such contents may be directly used when a function is called again. You can add additional code to check if the cache contains the data you stored before.


```
Note:
Do not assume that a container is always reused in your function code, because whether a container is reused depends on each actual call, which may create a new container instead.
```

## Temporary Disk Space
Each SCF has a temporary disk space of 512 MB in the `/tmp` directory during execution. Users can write to or read from this space during the execution process, but the data in this directory will *not* be retained after the execution completes. Thus, if you want to permanently store the data generated in the execution process, use external persistent storage such as COS or Redis/Memcached.

## Call Types
The SCF platform supports two methods for calling cloud functions: `synchronous` and `asynchronous`. The call type is unrelated to the configuration of a function, and can only be determined when a function is called.

- For a synchronous function call, the platform waits for the returned execution results of the function once the call request is sent.
- For an asynchronous function call, the platform only sends the request but does not wait for results.

You can define the function call type in the following scenarios:

- Serverless cloud functions are called by your composed applications. For synchronous calls, pass the `invokeType=RequestResponse` parameter in the InvokeFunction API; for asynchronous calls, pass the `invokeType=Event` parameter.
- Serverless cloud functions are called manually (using API or CLI) for testing purposes. Use the same parameters as mentioned above.

When you use other Tencent Cloud services as event sources, the call type of cloud services is predefined but not user-defined. For example, COS and timer always call serverless cloud functions asynchronously.

## Use Limits

For the quotas and environment limits related to functions, see [Quotas and Limits](https://cloud.tencent.com/document/product/583/11637)

## Number of Concurrent Functions
This means the number of function code executions within any specified time period. The current serverless cloud function runs one time for each event request issued. So the number of events (number of requests) issued by triggers affects the number of concurrent functions. You can estimate the total number of concurrent function instances using the following formula.

```
Number of requests per second * Function execution duration (in seconds) 
```

For example, if it takes 0.2 seconds (200 milliseconds) for a function to handle a COS event on average, and COS issues 300 requests to the function per second, 60 (300*0.2) function instances are generated at the same time.


## Concurrency Limit

SCF has a default concurrency limit for each function. You can view [Quotas and Limits](https://cloud.tencent.com/document/product/583/11637) to find out the concurrency limit of the current function. You can [contact us](https://cloud.tencent.com/document/product/583/9712) to increase this limit.

A call that causes the function concurrency to exceed the default limit will be blocked and will not be executed by SCF. Blocked calls are handled differently based on the function call type:

- If a synchronous function call is blocked, a 429 error will be returned.
- If an asynchronous function call is blocked, SCF will automatically retry the blocked event within a certain period of time at a fixed frequency.
 
## Retry

When your function fails to be called due to internal limitations such as max concurrency exceeded and insufficient platform resources, an error will be directly returned in case of a synchronous call (see the Concurrency Limit above). But if the function is called asynchronously by an internal cloud service, the call is automatically placed into a retry queue, and SCF will retry this call.

## Running Environment and Available Libraries

The current SCF running environment is based on the following:

- Standard CentOS 7.2 image
- Python 2.7 runtime environment

The SCF running environment for different language environments contains corresponding basic library and additional library. You can check the additional library already installed in the environment in each language description:

- [Python](https://cloud.tencent.com/document/product/583/11061)
- [Node.js](https://cloud.tencent.com/document/product/583/11060)
- [PHP](https://cloud.tencent.com/document/product/583/11060)
- [JAVA](https://cloud.tencent.com/document/product/583/12214)



