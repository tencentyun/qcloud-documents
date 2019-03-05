### 1. If I select multiple CDHs when creating a CVM, which CDH exactly will the CVM be created on?

If multiple CDHs are selected while creating a CVM, the selected CDHs are considered as a resource pool. formed by all selected CDHs. The CVM with your desired specifications is created on a random CDH in the resource pool.

![ziyuanchi](http://mc.qcloudimg.com/static/img/f2e627ac5fa74d007d7fb0462f748907/image.jpg)



### 2. Why each CVM takes up 2 GB more storage than its specification?

![qcow2](http://mc.qcloudimg.com/static/img/f39fa2a36e6899340bd6e8c0cd51f4fa/image.jpg)

You can specify the sizes of system disk and data disk when you create your CVMs. When a CVM is created, beside the storage allocated by the users, additional 2 GB of storage is spared for configuration information.
