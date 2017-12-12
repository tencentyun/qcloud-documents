## 1 Foreword 
With the rise and development of mobile Internet and online games, people around the world are caught up in the wave of entrepreneurship. Those who can handle the explosive growth of users and provide stable OPS have a better chance for success. In the field of basic OPS platform, Job Platform is a stable and reliable operation platform with a high concurrency processing capacity, which has been running within Tencent IEG for many years.
## 2. Overview  
### 2.1 Product Overview 
   "[Job Platform (Job)](http://o.qcloud.com/console?app=job)" is a basic operation platform based on BlueKing Control Platform GSE channel, featuring a high concurrency processing capacity. Job Platform supports a variety of basic OPS scenarios such as script execution, file pulling/distribution and timed task, and can also streamline individual tasks into a job process. Each task considered as an atomic node is provided to other systems and platforms for scheduling, thus achieving automatic scheduling.
### 2.2 Key Advantages 
1. More flexible and rapid file transfer
Both task execution and file transfer of Job Platform are triggered by GSE agent. GSE-agent uses BT (BitTorrent) solution to handle large file transfer, making file pulling and transfer more efficient and faster.
No longer limited to "one-to-many" mode, file pulling and transfer have adopted unique and innovative "many-to-many, many-to-one" modes, so that the scattered and complicated file distribution tasks can be executed in a more convenient and faster way.
2. Clearer web-based script management
Cloud-based script management mode helps make collaborative management much clearer for OPS team. The platform implements script sharing among multiple collaborators. In addition to executing a single script, it can also assemble multiple scripts or file transfer processes into a job.
3. More efficient batch execution with 10k-level concurrency
With the support for 10k-level concurrent tasks execution in practice, you do not need to worry about the performance and efficiency problems brought by the accelerated development of businesses and the expansion of server management scale.
4. Job is everything to process management
In the specific scenario of version releasing or changing, we usually need to perform multiple steps. For example, we need to stop the process, pull the version files, distribute the version files to each node's server, and finally restart the process to formally provide external service. In this case, multiple steps are required to perform these actions. You can also encapsulate all the steps into a large script, which however is inefficient and the maintenance is costly.
The job management module of Job Platform can solve this problem well. You only need to assemble the script or file transfer operation of a particular business scenario into a job in sequence, so that the whole operation can be completed by just one click, which is convenient and easy for management.
5. More accurate Timing of task execution with "second-level" timing
Superior than traditional minute-level timed task native to Linux system, Job Platform supports second-level timed tasks with second as the minimum time granularity. The execution process of each timed task is recorded to make all operations traceable.
6. APIs are available to connect everything in atomic form
Job Platform provides APIs to other systems and platforms in atomic form for scheduling, realizing the true connection of everything.

## 3. Product Features
### 3.1 Description
![](https://mc.qcloudimg.com/static/img/1cc6e289ae218496a8e236a0d3f1dc58/1.jpg)
### 3.2 Product Screenshots

(1) Business overview: View the devices of business and job execution status.
![Product Screenshot](https://mc.qcloudimg.com/static/img/76074cea3a151f6b728c751d0634eeb9/2.jpg)
(2) Quick script execution: Perform batch script execution quickly.
![Product Screenshot](https://mc.qcloudimg.com/static/img/8245755b294dd14461bab07fb1f5a217/3.jpg)
(3) Quick file distribution: Distribute files to multiple servers (Linux/Windows) quickly.
![Product Screenshot](https://mc.qcloudimg.com/static/img/cadc941ed00ba57407fa4f3d09225cd0/4.jpg)
(4) Common job execution:
![Product Screenshot](https://mc.qcloudimg.com/static/img/ce3c9c2cc07fa4f49b02efc0aac442d5/5.jpg)
(5) Job creation:
![Product Screenshot](https://mc.qcloudimg.com/static/img/7c2c511f2c611e9ed6a1f04c728de006/6.jpg)
(6) Timed job:
![Product Screenshot](https://mc.qcloudimg.com/static/img/6679451c022cb5b8b6117b8e40cff524/7.jpg)
(7) Account management:
![Product Screenshot](https://mc.qcloudimg.com/static/img/37fa1d1c02a3cdb493d0e8d11ad404b7/8.jpg)
(8) Script management:
![Product Screenshot](https://mc.qcloudimg.com/static/img/2aa45ed66039c4db92e07b70f4d22f0e/9.jpg)
(9) Group management:
![Product Screenshot](https://mc.qcloudimg.com/static/img/de08673c22dfdd592f86480ea604ba3d/10.jpg)
(10) Execution history:
![Product Screenshot](https://mc.qcloudimg.com/static/img/fbd4f7d6252a5db7fdfb4a122723adf5/11.jpg) 



## 4. Conclusion
BlueKing Job Platform allows you to manage your basic OPS operations with an advantage of 10k-level high-concurrency performance. Instead of traditional repetitive selection, it provides a flexible dynamic grouping feature to assemble the operation process into a complete job. Meanwhile, various APIs are also available to make your job atomic, and your business can be applicable to more scenarios. Now, let Job Platform to help with your jobs!



