Welcome to Tencent Cloud Serverless Cloud Function. Serverless Cloud Function hosts user code, uses user-configured triggers, and automatically executes user applications based on triggering events, providing users with FaaS (Function as a Service).

Serverless Cloud Function is a serverless execution environment provided by Tencent Cloud. You can simply make your code run in a secure and elastic way on Tencent Cloud infrastructure by writing key code in the language supported by the platform and setting the running conditions without purchasing and managing servers. Tencent Cloud completely manages the underlying computing resources, such as server CPU, memory, network, and performs other configuration/resource maintenance, code deployment, auto scaling, load balance and so on. Code is run on demand, with no service fee charged when idle.

## Glossary

| Term | Full Name |  Description |
|---------|---------|---------|
| SCF | Serverless Cloud Function |    Serverless Cloud Function hosts user code, uses user-configured triggers, and automatically executes user applications based on triggering events, providing users with FaaS (Function as a Service). |
| Trigger | SCF Trigger |   The SCF cloud function is triggered by an event. The event source is a trigger, which is usually the resource object of other products, such as COS Bucket, CMQ Topic queue, timer. |

## How to Use
To use Serverless Cloud Function via API, you need to complete the configuration as follows:
**1. Create a function**
You can use the API [CreateFunction](https://cloud.tencent.com/document/product/583/9742) to create a cloud function. The function name is the unique ID of the function and cannot conflict with others in the same region.
**2. Create a function trigger**
After the function is created, you can set the function to respond to a triggering event by using the API [SetTrigger](https://cloud.tencent.com/document/product/583/9748).
**3. Test a function**
You can call the function directly using the API [InvokeFunction](https://cloud.tencent.com/document/product/583/9747), or manipulate the trigger object to generate an event and use the API [GetFunctionLogs](https://cloud.tencent.com/document/product/583/9746) to verify whether the function executes properly.
After the above three steps are completed, your function can be put in use.


