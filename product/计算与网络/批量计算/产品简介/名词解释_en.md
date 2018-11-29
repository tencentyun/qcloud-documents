
## Job
Job is the minimum unit of batch processing work submitted by a user, which is comprised of one or more tasks with sequential dependency. You can set dependencies for multiple batch processing tasks using easy-to-use DAG syntax together to form a job, and execute tasks in sequence, so as to finish the job until all tasks are completed. The dependency between tasks can be specified only when you submit a job and cannot be modified after submission.
![Job Example](https://mc.qcloudimg.com/static/img/cd1eff1cdfb7104c11a1b64473c325fa/image.png)
## Task
Task is the information of an application that is actually running on a CVM. Batch scheduling system automatically creates CVMs, installs images and runs programs according to the configurations submitted by users. Tasks cannot be directly submitted for execution before they are placed into a job. A job can contain a single task or multiple tasks.

The most important configurable attributes of a task are as follows:
* ``CVM instance configuration``: Tasks are executed on a CVM. You need to configure the type and parameters of a CVM instance based on the features of your computing task. For example, whether to choose a computing instance (C2) or a high IO instance (IO2), and select what memory and disk size, and the VPC network where the instance resides in.
* ``Running environment``: It includes the configuration of image and commands. Image is generally a custom image, which contains your applications and the environment on which they are relying. Commands specify the way these applications are launched for computing.
* ``Remote storage mapping``: The remote storage address can be mapped to a local file system address. Currently, COS is supported. See below for more explanation.
* ``Standard output``: You can configure the mapping address (COS) of standard output. The message of an application output to stdout and stderr is uploaded to a corresponding address after a task is completed, to trace the computing process.

## Instance
Instance refers to a CVM instance. You can specify one or more instances to execute a single task. Instance is the minimum unit scheduled and executed by Batch. You can set the number of instances required to run concurrently in task configuration. When a task is launched, Batch can create the specified number of instances with the same configuration. These instances can be differentiated by environment variables in the running program.

A typical scenario of multiple instances is that the input data can be split and processed concurrently, so that you can make full advantage of elastic resources on the cloud to implement concurrent computing, thus improving work efficiency.
## Image
Image is configured in a task and used when you create an instance. It must be a standard or a custom CVM image. You need to prepare a computing environment and applications before creating an custom image. You can check your custom image in [Image Console>>>](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=1). For more information on how to create a custom image, please see [Create Custom Image>>>](https://cloud.tencent.com/document/product/213/4942).
## Remote Storage Mapping
Storage mapping is intended to map a remote storage address to a local file system address of CVM, so that you can read the remote storage address in a way of working with the local file system.

For example, if COS directory is cos://mybucket/batchcomputer/, you can map this directory to a local directory /user/batch/, and then the task program processes it as the local directory.
