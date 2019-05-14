You can create a cloud function by packaging application service codes and relevant dependencies and uploading them to Tencent Cloud SCF. The cloud function contains the codes and dependencies you uploaded, as well as some configuration information associated with the execution of function. This document describes the configurations of cloud functions and their meanings, to help you understand how to create an cloud function that fits your business needs.

## Function Name
Tencent Cloud uses function name to exclusively identify the SCF in each of user's regions. The function name cannot be modified after creation. The function name should follow the rules below:

- The length is limited to 60 characters.
- It can only contain `a-z, A-Z, 0-9, -, _`.
- It must begin with a letter.

## Region
You can specify the region in which you need to run the SCF. Beijing, Shanghai and Guangzhou are supported. The SCF is automatically deployed with high availability in multiple availability zones of a region. The region attribute cannot be changed after the SCF is created.

## Computing Resources
Tencent Cloud allows you to customize the *amount of memory* allocated to SCF. Take the increment of 128 MB to allocate the amount of memory between `128 MB - 1536 MB`. Tencent Cloud automatically assigns the proportional CPU processing capacity for SCF based on the amount of memory you specified. For example, if 1024 MB memory is allocated to SCF, the CPU capacity obtained by the SCF is *twice* the allocated 512 MB memory. Therefore, in regular scenarios, the time to actually run the code is generally shortened by increasing the amount of memory of SCF.

You can change the amount of memory needed by SCF at any time. We strongly recommend that you increase the size of this parameter if you find the memory consumed in running SCF is nearly or reaches the configured memory amount, to prevent error in SCF due to OOM:

- Log in to the Tencent Cloud console, and click **SCF**.
- Select the function whose memory amount needs to be modified.
- Click **Edit** in the **Function Configuration** tab, select the memory amount to be adjusted and then click **Save**.


## Timeout
Cloud functions are charged based on running time and the number of requests. To prevent cloud functions from running for an indefinite period (for example, infinite loop occurs in the code), each cloud function has a user-defined timeout value. The maximum value is 300 seconds. Default is 3 seconds. When timeout is reached, if a cloud function is still running, SCF platform will automatically terminate it.

You can change the timeout of the cloud function at any time. We strongly recommend that you increase the size of this parameter if you find the function times out or the actual running time is close to the configured timeout during test period, so as to prevent interruption of function which is limited by timeout during long running time:

- Log in to the Tencent Cloud console, and click **SCF**.
- Select the function whose timeout needs to be changed.
- Click **Edit** in the **Function Configuration** tab, select the timeout value to be adjusted and then click **Save**.

## Description
You can configure the description information for the function, and change it at any time.


