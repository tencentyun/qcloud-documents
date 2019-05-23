
If you cannot connect to an instance, you are recommended to conduct troubleshooting as follows:


<span id = "jump1"></span>
## Port
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Remote connection to the port fails.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This problem is probably caused by non-default port used for remote access or inconsistent port settings.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For more information, please see [Remote Connection Failure due to Port Issues](/doc/product/213/10232).

<span id = "jump2"></span>
## Excessive CPU/Memory Utilization
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Login to the CVM fails, the service response slows down, or the instance disconnects suddenly.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; It may be caused by high CPU or memory load. Please check the resource utilization.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For Windows CVMs, please see [Login Failure due to Excessive CPU/Memory Utilization in Windows](/doc/product/213/10233).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For Linux CVMs, please see [Login Failure due to Excessive CPU/Memory Utilization in Linux](/doc/product/213/10310).

<span id = "jump3"></span>
## Isolated Public Network
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The CVM is partially isolated in case of violations or risks.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For more information, please see [Remote Connection Failure due to Isolated Public Network](/doc/product/213/10318).

<span id = "jump4"></span>
## High Bandwidth Usage of Public Network
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Login fails due to full or high bandwidth usage.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For more information, please see [Login Failure due to High Bandwidth Usage of Public Network](/doc/product/213/10334).

<span id = "jump5"></span>
## Security Group Configuration
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Server telnet connection fails, and the problem persists after the firewall and the ENI configurations are checked and the system rolls back.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For more information, please see [Remote Connection Failure due to Security Group Configuration](/doc/product/213/10337).

<span id = "jump6"></span>
## Password Cannot Be Used after Key Is Associated
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The CVM cannot be logged in to by password after it is associated with a key. Firewall and ENI IP configurations are correct.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After the CVM is associated with the key, login by user name and password is disabled by default for the CVM SSH service. Use the key to log in to the CVM. 
For more information on login by key, please see [SSH Key](/doc/product/213/2036). 

<span id = "jump7"></span>
## Network Level Authentication for Remote Login
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Connection to remote computers through Windows Remote Desktop Connector fails sometimes.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For more information, please see [Network Level Authentication for Remote Login](/doc/product/213/11330).

<span id = "jump8"></span>
## Login by Password Through xshell Failed
**Problem:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The CVM cannot be logged in to by password through xshell.
 
**Solution:**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You have chosen to log in by key when installing the system. For how to use the key, please see [SSH Key](/doc/product/213/6092). If you need to log in by password, you can choose this option when reinstalling the system, or modify the sshd configuration file.


