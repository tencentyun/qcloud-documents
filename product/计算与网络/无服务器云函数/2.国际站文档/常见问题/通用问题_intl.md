### What is Tencent SCF?
Tencent Cloud Serverless Cloud Function (SCF) is a serverless execution environment provided by Tencent Cloud. You simply need to compose simple cloud functions with a sole purpose, and then associate them with your Tencent Cloud infrastructures and events created by other cloud services.
You only need to focus on the codes when using SCF. Tencent Cloud completely manages the underlying computing resources, including server CPU, memory, network, and other configuration/resource maintenance, code deployment, auto scaling, load balancing, security update, and resource operation status monitoring. You only need to provide codes using languages supported by the platform (currently supported language is Python). This also means that you cannot log in to or manage the servers, or customize system/environment.

Auto scaling is performed by underlying SCF components based on the number of requests when code is run, achieving service availability and stability under various scenarios with different request volume (from several requests per day to thousands of requests per second), without the need for any manual configuration and intervention. SCFs are automatically deployed in multiple availability zones in the region, which enables extremely high fault tolerance. You only need to pay for the running cloud functions. There is no charge when your code is not running.

You can set to run your code when a file is uploaded to or deleted from a COS Bucket, or when an application calls the code through SDK, or at regular intervals. For this reason, you can use SCF to trigger data processing for COS services and easily implement IFTTT logic. You can also construct flexible and periodical automated tasks to replace manual operations, creating a flexible and controllable software structure.

### What is serverless computing?

With serverless computing, users can build and run applications and services without thinking about servers. Serverless does not mean that there is no server involved. It just means users don't need to manage the underlying resources. This also means that users cannot log in to servers and do not need to consider optimizing them. Developers only need to focus on the most important code snippets and skip complicated and boring work. The code is completely event-triggered. The platform automatically adjusts service resources in a balanced manner based on the number of requests, with virtually unlimited capacity expansion capability. No resource is running when idle. Stateless code running allows quick iteration and deployment. SCF is the core of Tencent Cloud serverless computing, which allows you to run codes without the need to pre-configure or manage servers.

### Which events can trigger SCF?

Currently, manual trigger (API), timed trigger, COS trigger, CMQ trigger, and API gateway trigger are supported. More trigger methods will be available soon.

### What languages does SCF support?

Currently, SCF supports Python 2.7 & 3.6, Node.js 6.10 & 8.9, Java 8, and PHP 5 & 7. More languages will be supported soon.

### Can I access the infrastructure where SCF is running?

No. SCF runs and manages your computing infrastructure on your behalf.

### How does SCF isolate codes?

Each function is running in a unique environment and has its own resources and file systems. SCF uses the same technology as CVM to provide security and isolation at the infrastructure and execution level.
