When **launching a CVM instance for the first time**, you can pass user data to the CVM by passing a text (with no format restriction) and execute the text.
This document uses Linux CVM as an example to describe how to output "Hello Tencent Cloud" by passing a Shell script when launching the CVM for the first time.
The log file (`/var/log/cloud-init-output.log`) output by Cloud-init catches the output of the console.
## Notes
* A command can be executed by passing a text only on the first time of launching a CVM.
* The passed text must be encoded with Base64. **Please encode in Linux environment to avoid format incompatibility.
* The text, which is input as the user data, is executed using the root permission. Therefore, sudo command is not required in the script. Note: All the files you created belong to root. If you need to grant non-root users with the access permission, modify the corresponding permission in the script.
* Adding these tasks to the startup of the CVM will increase its startup time. Wait a few minutes until the tasks complete, and then test whether they are executed successfully.
* In this example, Shell script must start with `#!` and the path directing to the interpreter of the script to be read.

## Step 1: Write Shell script
```
#!/bin/bash
echo "Hello Tencent Cloud."
```
> **Note:**
> Shell script must start with `#!` and the path directing to the interpreter of the script to be read. For more information on Shell script, please see [BASH Programming](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html) of the Linux Documentation Project (tldp.org).

## Step 2: Encode the script file with Base64
> **Note:**
> Please encode in Linux environment to avoid format incompatibility.

Suppose that the script file you created in step 1 is script_text. You can encode the file using Base64 command in Linux environment, as shown below:
```
# Encode the file with Base64
base64 script_text

# The encoded result :
IyEvYmluL2Jhc2gKCmVjaG8gIldlbGNvbWUgVG8gVGVuY2VudCBDbG91ZC4iCg==

# Decode the returned result with Base64 and verify whether it is the command to be executed.
echo "IyEvYmluL2Jhc2gKZWNobyAiSGVsbG8gVGVuY2VudCBDbG91ZC4iCg==" | base64 -d
```
## Step 3: Pass the text
We provide multiple methods to launch an instance and here we introduce two of them. Please choose a method as needed:
### Passing on the official website or the console
When you create a CVM on the official website or the console, select **Advanced Configuration** in **4. Set Security Group and CVM** step. Enter the encoded result (`IyEvYmluL2Jhc2gKCmVjaG8gIldlbGNvbWUgVG8gVGVuY2VudCBDbG91ZC4iCg==` in this example) of step 2 in user defined data item. Finish the creation and launch the CVM.
Tencent Cloud CVM executes the script using the open-source software cloud-init. For more information on cloud-init, please see [cloud-init's official website](https://cloud-init.io/).
![](https://main.qcloudimg.com/raw/51ff9b1a19d71fd532976976000acaba.png)

### Passing via API
When creating a CVM via API, you can pass the text by assigning the value of the encoded result of step 2 to UserData parameter of RunInstances API. The following is an example of the parameter of CVM creation request with UserData.
```
https://cvm.tencentcloudapi.com/?Action=RunInstances
  &Version=2017-03-12
  &Placement.Zone=ap-guangzhou-2
  &ImageId=img-pmqg1cw7
  &UserData=IyEvYmluL2Jhc2gKCmVjaG8gIldlbGNvbWUgVG8gVGVuY2VudCBDbG91ZC4iCg==
  &<Common request parameters>
```

