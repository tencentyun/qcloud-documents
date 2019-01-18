Criteria for Offline Monitoring Components
> If the monitoring component of a cloud service does not report data for 5 minutes, the platform considers that it is offline.

Here lists TOP reasons for offline monitoring component and the corresponding troubleshooting.

### 1. Users Operate CVM via Console or Command Line
The CVM is shut down after operation, which will lead to offline monitoring component with no data.

The common CVM operation and maintenance via the CVM console or by logging into CVM, such as reboot, CVM upgrade, re-installation, image creation, will make CVM monitoring data submission timeout, and the monitoring component will be offline.

**Troubleshooting:** Check whether there is any operation and maintenance described above based on the time point. The operation log can be found in the details page of CVM.

### 2. High Load on CVM
CPU high load, full memory/ bandwidth usage of CVM can cause monitoring component reporting exception.


**Troubleshooting:** Log in to the CVM or go to the monitoring view to check whether the CPU/memory/bandwidth usage has reached `100%`. If so, you can expand the service as needed.



### 3. Internal DNS Configuration Error of CVM

If the intranet DNS configuration of CVM is wrong, the monitoring component may fail to report data.

**Troubleshooting:** For more information on Tencent Cloud's intranet DNS configuration, please see [Intranet DNS Access and Settings](https://cloud.tencent.com/document/product/213/5225#dns-.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.9C.B0.E5.9D.80).


