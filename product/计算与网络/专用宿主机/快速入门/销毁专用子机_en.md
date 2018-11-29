You can terminate a dedicated CVM any time you don't need it. When a dedicated CVM instance is terminated, the local disks and non-elastic cloud disks mounted to the instance are terminated as well and the data stored on these disks are lost. But the elastic cloud disks mounted to the instance will be retained and the data will not be affected.

## 1. Terminate instances on CDH console

> 1. Log in to [CDH Console](https://console.cloud.tencent.com/cvm/cdh).
> 2. Click the host ID/name to enter host details page.
> 3. Click "CVM List".
> 4. Select the dedicated CVM and terminate it.



## 2. Terminate instances on CVM console

> 1. Log in to [CVM Console](https://console.cloud.tencent.com/cvm).
> 2. Find the dedicated CVM you want to terminate.
> 3. Click "More" -> "CVM Status" -> "Terminate" in the operation bar to the right side.



## 3. Terminate instances using API

 Please see [ReturnInstance API](https://cloud.tencent.com/doc/api/229/1347).
