Tencent Cloud Serverless Cloud Function (SCF) helps you run your code without the need to purchase and manage servers. You can simply make your code run automatically and securely on Tencent Cloud infrastructure by writing core code and setting the code running conditions. It is an ideal computing platform for many scenarios.

## Changes in Computing Resources
As cloud services develop, computing resources have become highly abstract. Tencent Cloud provides computing resources across different abstraction levels, from CPMs to cloud functions, for users to choose from.

- CPM: Physical machines are used as expansion units. CPM provides the highest security, which allows users to possess the entire physical computing resources.
- CVM: Cloud virtual machines are used as expansion units, in which case hardware devices are virtualized. Users can configure the metrics of their own CVMs even when they share physical machine resources with other tenants. Deployment and iteration are simpler.
- Container: Services are used as expansion units, in which case operating systems are virtualized. The test and production environments are completely the same, which makes tests and deployment extremely easier.
- SCF: Functions are used as expansion units, in which case the runtime environment is virtualized. This is currently the smallest unit of computing resources, featuring full automation, one-click deployment and high scalability, and is an excellent choice for light-weight service development.

## What Does Serverless Mean?

Serverless does not mean that there is no server involved. It just means users don't need to manage the underlying resources. This also means that users cannot log in to servers and do not need to consider optimizing them. Developers only need to focus on the most important code snippets and skip other complicated and boring work. The code is completely event-triggered. The platform automatically adjusts service resources in a balanced manner based on the number of requests, with virtually unlimited capacity expansion capability. No resource is running when idle. Stateless code running allows quick iteration and deployment.

## Tencent Cloud SCF Overview

Tencent Cloud SCF is a serverless execution environment provided by Tencent Cloud. You simply need to compose simple cloud functions with a sole purpose, and then associate them with your Tencent Cloud infrastructures and events created by other cloud services.
You only need to focus on the codes when using SCF. Tencent Cloud completely manages the underlying computing resources, including server CPU, memory, network, and other configuration/resource maintenance, code deployment, auto scaling, load balance, security update, and resource operation status monitoring. You only need to provide codes using languages supported by the platform (currently supported languages are Python, Nodejs and Java). This also means that you cannot log in to or manage the servers, or customize system/environment.

Auto scaling is performed by underlying SCF components based on the number of requests when code is run, achieving service availability and stability under various scenarios with different request volume (from several requests per day to thousands of requests per second), without the need for any manual configuration and intervention. SCFs are automatically deployed in multiple availability zones in the region, which enables extremely high fault tolerance. You only need to pay for the running cloud functions. There is no charge when your code is not running.

You can set to run your code when a file is uploaded to or deleted from a COS Bucket, or when an application calls the code through SDK, or at regular intervals. For this reason, you can use SCF to trigger data processing for COS services and easily implement IFTTT logic. You can also construct flexible and periodical automated tasks to replace manual operations, creating a flexible and controllable software structure.

Tencent Cloud also provides the following services for you to manage your computing resources:

- [CVM](https://cloud.tencent.com/product/cvm) provides various instance configurations. You can customize the CPU, memory, operating system, network, security and other configuration items of your computing resources, and also customize policies to achieve cross-availability zone disaster recovery, resource scaling, etc.
- [CCS](https://cloud.tencent.com/product/ccs) provides highly scalable container management service. You can deploy containers in your cluster according to the resource and availability requirements of your business or application.

