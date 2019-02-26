You can create a SCF by packaging application service codes and relevant dependencies and uploading them to Tencent Cloud's cloud function. The cloud function contains the codes and dependencies you uploaded, as well as some configuration information associated with the execution of function. This document describes the specific configurations of cloud function and their meanings, to help you understand how to create a cloud function that fits your business needs.

## Function Name
Tencent Cloud uses function name to exclusively identify the SCF in each of user's regions. The function name cannot be modified after creation. The function name should follow the rules below:

- The length is limited to 60 characters.
- It can only contain `a-z, A-Z, 0-9, -, _`.
- It must begin with a letter.

## Region
You can specify the region in which you need to run the SCF. Beijing, Shanghai and Guangzhou are supported. The cloud function automatically performs deployment with high availability in multiple availability zones of a region. The region attribute cannot be changed after SCF is created.

## Computing Resources
Tencent Cloud allows you to customize the *amount of memory* allocated by SCF. Take the increment of 128 MB to allocate the amount of memory between`128 MB - 1536 MB`. Tencent Cloud automatically assigns the proportional CPU processing capacity for SCF based on the amount of memory you specified. For example, if 1024 MB memory is allocated to SCF, the CPU capacity obtained by the SCF is twice the allocated 512 MB memory. Therefore, in regular scenarios, the time to actually run the code is generally shortened by increasing the amount of memory of SCF.

You can change the amount of memory needed by SCF at any time. We strongly recommend that you increase the size of this parameter if you find the memory consumed in running SCF is nearly or reaches the configured memory amount, to prevent error in SCF due to 00M:

- Log in to Tencent Cloud console, and click "SCF" option.
- Select the function whose memory amount needs to be modified.
- Click "Edit" button in "Function Configuration" tab, select the memory amount to be adjusted and then click "Save".

```
This parameter is not available during internal trial. We will assign the same computing resources for each function by default.
```

## Timeout
The cloud function is charged based on running time and the number of requests. To prevent the cloud function from running for an indefinite period (for example, infinite loop occurs in the code), each cloud function has a user-defined timeout value. Currently, the maximum value is 300 seconds. Default is 3 seconds. When timeout is reached, if the cloud function is still running, SCF platform will automatically terminate the function.

You can change the timeout of the cloud function at any time. We strongly recommend that you increase the size of this parameter if you find the function times out or the actual running time is close to the configured timeout during test period, so as to prevent interruption of function which is limited by timeout during long running time:

- Log in to Tencent Cloud console, and click "SCF" option.
- Select the function whose timeout needs to be changed.
- Click "Edit" button in "Function Configuration" tab, select the timeout value to be adjusted and then click "Save".

## Description
You can configure the description information for the function, and change it at any time.


