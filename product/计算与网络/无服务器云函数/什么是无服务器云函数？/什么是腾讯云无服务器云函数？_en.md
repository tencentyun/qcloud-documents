Tencent Cloud Serverless Cloud Function helps you execute your code without the need to purchase and manage servers. This is an ideal computing platform suitable in many scenarios. You simply need to compose the core code and configure the execution conditions for the code to be executed on Tencent Cloud infrastructures automatically and securely.

## Changes in Computing Resources
As cloud services develop, computing resources have become highly abstract. Tencent Cloud provides computing resources across different abstraction levels, from CPMs to cloud functions, for users to choose from.

- CPM: Physical machines are used as expansion units. This approach has the best security, where a user possesses the entire physical machine as computing resource. Deployment requires several weeks, and can be used for several years.
- CVM: Virtual machines are used as expansion units, in which case hardware devices are virtualized. A user shares physical machine resources with other tenants, while the user can still configure the metrics of their CVM. Deployment and iteration are relatively easier. Deployment requires dozens of seconds to several minutes, and can be used for several years.
- Container: Services are used as expansion units, in which case the operation systems are virtualized. Testing and production use the same environment, which makes testing and deployment extremely simple.
- Serverless Cloud Function: Functions are used as expansion units, in which case the runtime environment is virtualized. This is currently the smallest unit for computing resources, an excellent choice for light-weight service development with features such as full-auto, one-click deployment, high scalability and do on.

## What is Serverless?
Serverless doesn't necessarily mean that there is no server. It is just that users no longer need to be concerned about these underlying resources. Of course, this also means that users cannot log in to the servers and do not need to think about server optimization. Developers only need to focus on the most important code segments, while skipping all the other complicated and boring works. The code is completely event-triggered. The platform automatically adjusts service resources in a balanced manner based on the number of requests, with almost no expansion limit. No resource is run when idle. Stateless code execution allows quick iteration and deployment.

## Tencent Cloud SCF Introduction

Tencent Cloud SCF is a serverless execution environment provided by Tencent Cloud. You simply need to compose simple cloud functions with sole purposes, then associate them with your Tencent Cloud infrastructures and events created by other cloud services.
Users only need to focus on their own code when using cloud functions. Underlying computing resources, including server CPU, memory, network, and other configuration/resource maintenance works such as code deployment, auto scaling, load balancing, security update, resource operation status monitoring, are completely handled by Tencent Cloud. Users only need to provide their code using languages supported by the platform (currently supported language is Python). This also means that you cannot log in to or manage the servers, or customize system/environment.

Auto scaling is performed by underlying cloud function components based on the number of requests when code is executed, achieving service availability and stability under various scenarios with different request volume (from several requests per day to thousands of requests per second), without the need for any manual configuration and intervention. Cloud functions are automatically deployed in multiple availability zones in the region, providing extremely high disaster tolerance. Users only need to pay for running cloud functions. Code does not incur any service fee when not running.

You can customize when to execute your code. For example, when a file is uploaded to or deleted from a COS Bucket, when an application calls the code through SDK, or specify the code to be executed periodically. For this reason, you can use SCF as data process trigger program for COS services and realize IFTTT logic with ease. You can also construct flexible, periodical automated tasks to replace manual operations, creating a flexible and controllable software structure.

Tencent Cloud also provides the following services for users to manage their computing resources:

- [CVM](https://cloud.tencent.com/product/cvm) provides instance configurations of different specifications. You can customize the configuration options for your computing resources such as CPU, memory, operating system, network, security and so on. However, you need custom policies to achieve cross-zone disaster recovery, resource scaling, etc.
- [Container Service](https://cloud.tencent.com/product/ccs) provides highly extendable container management service which allows you to schedule containers in your cluster according to resource and availability requirement, to satisfy specific demand of businesses or applications.

