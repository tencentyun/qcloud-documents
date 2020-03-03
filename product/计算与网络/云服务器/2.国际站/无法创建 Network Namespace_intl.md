## Problem Description
The command for creating a network namespace got stuck and did not continue. dmesg message: "unregister_netdevice: waiting for lo to become free. Usage count = 1"

## Cause of the Problem
It is caused by a bug of the kernel.
The following kernel versions have this bug:
- Ubuntu 16.04 x86_64 kernel version: 4.4.0-91-generic.
- Ubuntu 16.04 x86_32 kernel version: 4.4.0-92-generic.

## Solution
Upgrade the kernel version to 4.4.0-98-generic, in which the bug has been fixed.
### Procedure
1. Check the current kernel version.
```
uname -r
```

2. Check whether version 4.4.0-98-generic is available for upgrade.
```
sudo apt-get update
sudo apt-cache search linux-image-4.4.0-98-generic
```
If the following information is shown, it means the version to upgrade to exists in the source:
```
linux-image-4.4.0-98-generic - Linux kernel image for version 4.4.0 on 64 bit x86 SMP
```

3. Install the new version kernel and corresponding Header package.
```
sudo apt-get install linux-image-4.4.0-98-generic linux-headers-4.4.0-98-generic
```

4. Restart the system.
```
sudo reboot
```

5. Enter the system to check the kernel version.
```
uname -r
```
If the following result is displayed, it means the version upgrade is successful:
```
4.4.0-98-generic
```

