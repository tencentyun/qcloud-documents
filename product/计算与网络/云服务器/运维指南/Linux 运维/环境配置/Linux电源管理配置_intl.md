A Linux system without an acpi management program will suffer failures of soft shutdown.  Therefore, make sure that the acpi (power management for Linux) module has been installed on your CVM.

## Checking method
Check whether the acpi has been installed using the following command:

```
ps -ef|grep -w "acpid"|grep -v "grep"
```

If there's no such process, it hasn't been installed. Then you need to follow the next step to install the module. If there's such process, the next step can be ignored. 

## Installation method
Use the following command to install the acpi module.

1) For Ubuntu/Debian system

```
sudo apt-get install acpid
```

2) For Redhat/CentOS system

```
yum install acpid
```

3) For SUSE system

```
in apcid
```
>Note: The CoreOS system doesn't have such problem.