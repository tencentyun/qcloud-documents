## Problem Description
After a CVM with CentOS 6.x operating system is restarted or the command `service network restart` is executed against the CVM, domain names cannot be resolved for the CVM.
In addition, the DNS information in the configuration file /etc/resolv.conf is found to be cleared.

## Possible Cause
Defects exist in initscripts with versions earlier than 9.03.49-1 in CentOS 6.x operating system due to different grep versions.
## Solution
Upgrade the initscripts to the latest version and regenerate DNS information.
## Procedure
1. Log in to the CVM and execute the following command to check the initscripts version.
```
$rpm -q initscripts
initscripts-9.03.40-2.e16.centos.x86_64
```
As shown in the example above, the initscripts version is initscripts-9.03.40-2, which is earlier than the defective version of initscripts-9.03.49-1, so there involves a risk of cleared DNS.
2. Execute the following command to upgrade initscripts to the latest version and regenerate DNS information.
```
cat /dev/null > /etc/resolv.conf
service network restart
yum makecache
yum -y update initscripts
```
3. Execute the following command after upgrade to check the version information of initscripts and verify whether the initscripts is upgraded successfully.
```
$rpm -q initscripts
initscripts-9.03.58-1.el6.centos.2.x86_64
```
The version displayed is different from that before upgrade and is later than initscripts-9.03.49-1, which indicates that the initscripts is upgraded successfully.
