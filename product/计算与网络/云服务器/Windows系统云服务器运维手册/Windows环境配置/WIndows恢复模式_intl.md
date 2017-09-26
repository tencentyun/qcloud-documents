## 1. What is a Windows recovery mode?

Windows System Recovery is a mode in which Windows detects system issues and prevents the system from starting by using the automatic repair function, and provides users with the access to System Recovery Options for repair, backup or system restore if the system is started up. The System Recovery Options include several tools, such as Startup Repair, System Restore and Windows Memory Diagnostic, which can be used to address exceptions that may arise in the Windows system.

## 2. Why the system enters recovery mode
Auto repair is a default function in Windows. When system issues are detected, this function prevents Windows from starting since continued use of Windows is believed to cause damage to the system. Common issues include damage to system-related key data on the Window file system and some key data not being written back by the system due to careless shutdown. Since Windows believes the system is missing key data or damaged, the system will enter recovery mode upon next restart, which allows users to use the tools to fix issues, back up data, or restore the system.

## 3. Why Windows enters recovery mode automatically
Here are some scenarios:
- Forced power-off while Windows is running or being shut down or "hard shutdown" while the system is still running on the CVM and not closed may compromise the system's ability to write back key data.
- The system experiences a power failure or is powered off when Window Update is in progress updating key information
- The system is broken into by Trojans or viruses
- Windows does not work properly due to bugs in core Windows services

## 4. Precautions
The following measures are recommended to Windows CVM users:

1) While the system is being shut down, open VNC to check if there is any Windows Update going on or if the shutdown is slow, etc. Tencent Cloud adopts a timeout mechanism for soft shutdown. If the soft shutdown does not lead the system to shut down at the specified time, a failure will be returned. The soft shutdown may fail due to a long shutdown process. In case of such a failure, just ignore it and wait until the CVM is shut down.

2) Check if there is any Trojan, virus or other abnormal programs, or if the management and anti-virus software is working properly.

3) Update Windows update packages in a timely manner, especially those key updates and security updates.

4) Periodically check the system event log for any error with core services.

## 5. What to do when in recovery mode
Generally, you can either continue to go with the startup or allow for auto repair and try to start up the computer again when Windows is in the recovery mode. Windows can automatically repair minor issues. If the startup fails, please back up your data before performing any actions.