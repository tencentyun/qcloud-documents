## Container Model During Function Execution
When an event is triggered, SCF executes the functions for you, in which case the platform allocates resources based on your configuration information (such as memory size), then launches and manages the container (which is the execution environment for the functions). The SCF platform is responsible for creation, management and deletion operations for all function execution containers. Users do not have permission to manage the platform.

It takes some time to launch a container, which creates a delay every time a function is called. However, you will only notice such delay when a function is called for the first time, is updated, or is called after being unused for a long time. This is because after a function is called, the platform will keep the container up for some time to reuse it in subsequent calls, in order to reduce the delay. Calls initiated during this period will use these retained containers.

The significance of container reuse mechanism:

- In the user code, the initialization status of all declarations outside the [Execution Method](https://cloud.tencent.com/document/product/583/9210#.E6.89.A7.E8.A1.8C.E6.96.B9.E6.B3.95) are retained. These declarations can be directly reused when the function is called again. For example, if you have already established database connection in your function code, then this connection can be directly used when the container is reused. You can add logic in your code to check whether a connection already exists before you create a new connection.
- Each container provides certain amount of disk space in the `/tmp` directory. Contents in this directory are used as temporary caches when a container is kept, in which case the contents are retained and can be used in multiple calls. When a function is called again, there is a chance that such content can be directly used. You can add additional code to check if the cache contains data you stored before.

```
Note:
Do not assume that container is always reused in your function code. This is because whether a container is reused depends on each actual call, which may create a new container instead.
```
## Temporary Disk Space
Each serverless cloud function has a temporary disk space of 512 MB in the `/tmp` directory during execution. Users may write to or read from this space during the execution process, but data in this directory will **not** be retained after the execution completes. Thus, if you want to permanently store the data generated in the execution process, use external persistent storage such as COS or Redis/Memcached.

## Call Type
The SCF platform supports two methods for calling cloud functions: `synchronous` and `asynchronous`. This method is unrelated to the configuration of the function. You can only control it when calling the function.

- For synchronous function call, the platform waits for returned execution result of the function once the call request is sent.
- For asynchronous function call, the platform only sends the request but does not wait for result.

You can define function call method at will in the following scenarios:

- Call serverless cloud functions for your composed applications. For synchronous calling, pass the `invokeType=RequestResponse` parameter in the InvokeFunction API; for asynchronous calling, pass the `invokeType=Event` parameter.
- Calling serverless cloud functions manually (by using API or CLI) for testing purposes. Use the same parameters as mentioned above.

However if you are using another Tencent Cloud service as event source, the calling method for the cloud service will be predefined in which case users cannot specify calling method on their own. For example, COS and timer always call serverless cloud functions asynchronously.

## User Limit

Resource limits during the internal trial period are listed in the table below.

| Resource | Default Limit |
|--|--|
| Number of functions in a region | 20 |
| Number of triggers that can be created at the same time upon function creation | 1 |
| Number of COS triggers for a function | 2 |
| Number of timer triggers for a function | 2 |
| Temporary disk capacity (/tmp) | 512 MB |
| Maximum operation time | 300 seconds |
| Size of code package uploaded via console | 5 MB |
| Maximum number of concurrent containers | 20. Users may [Contact Us](https://cloud.tencent.com/document/product/583/9712) to increase this number. |

## Number of Concurrent Functions
This means the number of function code operations within any specified time period. Currently, each published event request executes serverless cloud function for once. So the number of events (number of requests) published by the triggers affects the number of concurrent functions. You can estimate the total number of concurrent function instances using the following formula.
```
Number of requests per second * function operation time (in seconds) 
```
Assume that a function which handles COS event costs an average of 0.2 second (200 millisecond), and the COS sends 300 requests to the function per second. In this case, 300*0.2=60 function instances are generated.


## Concurrency Limit

By default, the concurrency for each function is limited to 20 by SCF. You can [Contact Us](https://cloud.tencent.com/document/product/583/9712) to increase this number.

A call that causes the function concurrency to exceed the default limit will be blocked and will not by executed by SCF. Limited calls are handled differently based on the function calling method:

- If a synchronous function call is limited, a 429 error will be returned.
- If an asynchronous function call is limited, SCF will automatically retry the limited event within a certain period of time, using a fixed frequency.
 
## Retry

Your function may fail due to internal limitations such as exceeded max concurrency and insufficient platform resource. If the function is called synchronously, an error will be directly returned (refer to the concurrent operation limit described above). If the function is called asynchronously by an internal cloud service, the call will be automatically placed into a retry queue, and SCF will retry this call.

## Operation Environment and Available Library

The current SCF operation environment is based on the following:

- Standard CentOS 7.2 image
- Python 2.7 runtime environment

You can use the `import` statement to directly import and use the following libraries and dependent packages in SCF operation environment:

- [Python Standard Library](http://usyiyi.cn/translate/python_278/library/index.html)
- [Qcloud COS SDK](https://cloud.tencent.com/document/product/436/6275)
- [Qcloud API SDK](https://cloud.tencent.com/document/developer-resource/494/7244)



