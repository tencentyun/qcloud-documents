### Q: Is there a charge for Batch?

**A: **Batch itself is free of charge. The CVMs created during job execution is billed on a postpaid basis. For more information, please see [Billing Method>>>](https://cloud.tencent.com/document/product/599/10447).

### Q: What is the relationship between a job and a task?

**A: **Job is a carrier for a submitted computing job in Batch. A job consists of one or more tasks. Multiple tasks are executed in sequence. The configuration of a job contains the configuration of all tasks in it and the execution sequence of these tasks.

### Q: What is the relationship between a task and an instance?

**A: **A task is mainly used to describe that a user's application is launched by executing what command under what image environment in a CVM with what configurations. The auxiliary features, such as redirection of standard output and remote storage mapping, can also be configured in a task.

An instance is created based on a task. It is a CVM used to actually run the application. The number of instances required to be launched concurrently can be specified in a task. All instances are created to run applications according to the configurations of the task. Instances can be differentiated via the numbers in environment variables.

### Q: Must I input and output data by configuring remote storage mapping? Are any other data read/write modes available?

**A: **Remote storage mapping is a configuration option provided by Batch. It is designed to reduce the difficulty of developing storage services. Users can directly access data on various storage services (such as CBS, CFS and COS) through applications, instead of using storage mapping capacity.

### Q: What types of instances in Batch can be purchased?

**A: **All instances can be used except FPGA, GPU, network-boosted instances and those under internal trial. For information about the instances supported in each availability zone, please see [CVM Instance Configuration](https://cloud.tencent.com/document/product/213/2177).
