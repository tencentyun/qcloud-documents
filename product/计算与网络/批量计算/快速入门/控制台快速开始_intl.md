## Quick Start
This document describes how to submit a job with the BatchCompute Console. The detailed steps are as follows.
### Preparations
Prepare a [COS](https://cloud.tencent.com/document/product/436) bucket. If you haven't created a bucket, see [Create a Bucket](https://cloud.tencent.com/document/product/436/6232) to create one first.

### Log in to the [Console](https://console.cloud.tencent.com/batch/task)
If you haven't activated the BatchCompute service, activate it according to the prompts on the BatchCompute Console page.

### Creating a Task Template

1. Click the **Task Template** option in the left navigation bar, select the target region, and then click the **New** button.

2. Configure the basic information.
  * Name: Such as hello
  * Description: Such as hello demo
  * Resource configuration: Default value
  * Number of resources: Such as 1
  * Timeout: Default value
  * Number of retry attempts: Default value
  * Image: img-i91njcmx
![](https://mc.qcloudimg.com/static/img/d12041618aeba32ecd52f61d84656e40/image.jpg)

3. Configure the program information.
  * Execution method: Local
  * Stdout log: For more information on the format, please see [How to Enter COS and CFS Paths](https://cloud.tencent.com/document/product/599/13996).
  * Stderr log: The same as Stdout log
  * Command line: echo 'hello, world'
![](https://mc.qcloudimg.com/static/img/374f5532c7ee7af1211e91b2ff20ddd3/image.jpg)

4. Configure storage mapping, and then click the **Next** button.
   ![](https://mc.qcloudimg.com/static/img/4fa9b5f5516a4ca3e0c04dd6e85481c7/image.jpg)

5. After you preview and confirm the task in JSON file, click the **Save** button.
  ![](https://mc.qcloudimg.com/static/img/7a462bf1530b0d867473fc95e316943e/image.jpg)

6. View the task template.
  ![](https://mc.qcloudimg.com/static/img/2138233d9271bc270abe0a2ba7deebdc/image.jpg)

### Submitting a Job
1. Click the **Job** option in the left navigation bar, select the target region, and then click the **New** button.

2. Configure the basic information for the job.
  * Job Name: Such as hello
  * Priority: Default value
  * Description: Such as hello job
  ![](https://mc.qcloudimg.com/static/img/adfad5bef466330a4f5583a84531f4af/image.jpg)

3. Select the task **hello** on the left side of **Task Flow** and drag the task to the canvas on the right.
  ![](https://mc.qcloudimg.com/static/img/f853b543e328755b0f15b6f62e5b2b8e/image.jpg)

4. Open **Task Details** on the right side of **Task Flow**. Confirm the information, and then click the **OK** button.
![](https://mc.qcloudimg.com/static/img/7e8faba3818f7ff2ada687ed7602be2e/image.jpg)

5. Query results. You can view the running status of a job on the Job List page.
  ![](https://mc.qcloudimg.com/static/img/6513237516f727b80f3a095ed18f5b77/image.jpg)
 - Click the job ID to view the running status of each task instance in the **Task Running Status** tab.
 - Click the **Query Log** button to view the standard output and standard error of a task instance.

  ![](https://mc.qcloudimg.com/static/img/3e743ad83c975d57b7ad9f56d78b8933/image.jpg)

## What's Next?

In this simplest example, the job only contains a single task. It does not use remote storage mapping, but only shows the most basic capabilities. You can continue to test higher level of capacities of Batch by following the Console Operation Guide.
- **Various CVM configurations**: Batch provides a variety of CVM configuration options. You can customize your own CVM configuration based on your business scenario.
- **Execute remote code package**: Technically, Batch can fully satisfy your business needs by combining **custom image and remote code package and command line**.
- **Remote storage mapping**: Batch optimizes the storage access by simplifying the access to remote storage service to an operation on local file system.

