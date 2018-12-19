
## Job
Job is the minimum unit of batch processing work submitted by a user, which is comprised of one or more tasks with sequential dependency. You can set dependencies for multiple batch processing tasks using easy-to-use DAG syntax to form a job, and execute tasks in sequence, so as to finish the job until all tasks are completed. The dependency between tasks can be specified only when you submit a job, which cannot be modified after submission.
![Job Example](https://mc.qcloudimg.com/static/img/cd1eff1cdfb7104c11a1b64473c325fa/image.png)
## Task
A task is the basic unit of a job and contains information about the application that is actually executing on a CVM. Batch scheduling system automatically creates CVMs, installs images and runs programs according to the configurations submitted by users. Tasks must be placed into a job before they can be submitted for execution. A job can contain a single task or multiple tasks.

The most important configurable attributes of a task are as follows:
* ``CVM instance configuration``: Tasks are executed on CVMs. You need to configure the type and parameters of a CVM instance based on the features of your computing task. For example, whether to choose a computing instance (C2) or a high IO instance (IO2), and select what memory and disk size, and the VPC network where the instance resides in.
* ``Running environment``: It includes the configuration of image and commands. Image is generally a custom image, which contains your applications and the environment on which they are relying. Commands specify the way these applications are launched for computing.
* ``Remote storage mapping``: The remote storage address can be mapped to a local file system address. Currently, COS is supported. See below for more explanation.
* ``Standard output``: You can configure the mapping address (COS) of standard output. The message of an application output to stdout and stderr is uploaded to a corresponding address after a task is completed, to trace the computing process.

## Task Instance
A task instance is the minimum unit scheduled and executed by Batch. A task contains one or more task instances. Each task instance runs on a CVM instance and performs corresponding computing tasks. You can set the number of instances required to run concurrently in task configuration. When a task is launched, Batch schedule the specified number of instances with the same configuration. These instances can be differentiated by variables in the running program.

A typical scenario of multiple instances is that the input data can be split and processed concurrently, so that you can make full advantage of flexible resources on the cloud to implement concurrent computing, thus improving work efficiency.
## Image
Image is configured in a task and used when you create an instance. It must be a standard or a custom CVM image. You need to prepare a computing environment and applications before creating a custom image. You can check your custom image in [Image Console>>>](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=1). For more information on how to create a custom image, please see [Create Custom Image>>>](https://cloud.tencent.com/document/product/213/4942).
## Computing Environment
The computing environment (ComputeEnv) is a computing cluster composed of one or more CVM instances. It can be scaled out or in according to business requirements. When the task configuration specifies a computing environment, the task instances are scheduled to execute on the nodes of the specified computing environment. When no computing environment is specified, Batch creates CVM instances to execute the task instances. By default, CVM instances are terminated after the task instances are completed.
## Task Template
You can make common tasks into templates, and customize different tasks based on the task templates for quick job submission.
## Remote Storage Mapping
Remote storage mapping refers to mapping a remote storage address (COS or CFS) to a local file system of CVM, so that you can read the remote storage by operating the local file system.

