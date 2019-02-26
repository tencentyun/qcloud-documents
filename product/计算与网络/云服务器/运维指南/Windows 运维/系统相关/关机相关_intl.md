## 1. Analysis on the Shutdown of Virtual Clients
The following is the shutdown process of Windows virtual machine on Tencent Cloud.

1) Libvirt on the parent host sends shutdown command to qemu component via qmp protocol; 
2) Qemu component transfers shutdown command to child host by injecting acpi interruption (For details, see technical documents on vmcs);
3) When receiving the shutdown signal, Windows tells applications and service processes to exit;
4) Close the core service process;
5) Turn off the power.

The shutdown process on Windows is basically the same as shown above. The sequence in which the applications and services are closed in step 3-4 may vary with the settings of system.

As a closed-source system, Windows provides some APIs to allow the programs with kernel mode and user mode to intervene in the shutdown process. And some services of Windows will also affect the shutdown process during operation, making the shutdown impossible. In some cases, Windows shutdown process can be very time-consuming to prevent the computer from being shut down.

In virtual scenarios, besides informing the Windows itself to shut down by sending a message, another means, which is similar to powering off a physical machine, is provided to stop a virtual client. This means is called "hard shutdown". Correspondingly, the shutdown action initiated by a system signal is called "soft shutdown".

Hard shutdown has some impact on the Windows itself and the user experience, mainly in the following two ways:

1) A hard shutdown interrupts some services and applications, which as a result may operate improperly, such as unsaved documents, and unfinished Windows Update processes;

2) As the NTFS system (or the earlier FAT32 system) of Windows writes some key data during the shutdown process, a hard shutdown may result in the failure to write such key data to the disk, which would lead Windows to determine that the NTFS file system is damaged.

For these reasons, it's recommended Tencent Cloud users <font color="red">take soft shutdown as the preferred way</font> to shut down Windows.

## 2. Several Scenarios of Shutdown Failure
However, as mentioned above, there may be some issues within the Windows system that interfere with the shutdown process and result in shutdown failure. The scenarios include but not limited to:

1) A Windows Update process may extend the shutdown time. For some patch operations, the Windows system may take some actions during the shutdown process, by which time messages like "Please do not power off or unplug your machine" will display.

2) If "Shutdown Event Tracker" mechanism is enabled on the Windows system, when the system is shut down due to any error in the system service and driver, the system will provide user with a prompt box based on the configuration or fill in the error description to wait for the user to complete these operations. Windows will not turn off the power until the user has completed these operations.

3) Windows can be set to not allow shutdown while the user is not logged in to the system. In this case, the soft-shutdown command sent from the virtual host will be discarded by Windows so that the shutdown cannot be achieved.

4) Before the shutdown, Windows will broadcast a message to every service and application. If the applications responding to this message do not send a response that allows the shutdown, Windows will not initiate the shutdown. In this scenario, some settings can be made on Windows to ignore this process.


5) In the power management-related operation "What will Windows do when you press the power button ", if Windows is set to ignore it or do nothing, Windows will ignore the shutdown event of the virtualized parent host.

6) Based on the settings of power management, Windows will go into Sleep and not handle shutdown event.

7) In case of initial purchase of Windows, the initialization process is slightly longer due to the use of sysprep for distributing images. Windows will ignore the shutdown event until the initialization has been finished.

8) If the Windows system itself is damaged due to some malicious software installed within it or infection with Trojan virus or other viruses, Windows can be prevented from shutdown.

Tencent Cloud has optimized most of the above scenarios when publishing Windows public images so that the soft-shutdown can be completed successfully. These optimization measures are integrated into the script of [Windows Power Management](http://cloud.tencent.com/doc/product/213/Windows%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#4.-配置高性能电源管理) to be used for making adjustments to Windows features such as power management, turn-off of "Shutdown Event Tracker" and shutdown while user is not logged in to the system.

But these optimization measures cannot solve the scenarios where Windows is infected with viruses and Trojans or the system is damaged; In addition, if these relevant settings in the Windows virtual machine of user are adjusted again, there is no guarantee that the soft-shutdown can be completed successfully. In some cases, forced shutdown would pose a risk. For example, in the process of Windows Update, it is necessary to wait for the update to complete. During the soft-shutdown process, user needs to check the scenarios of shutdown failure by opening VNC, so as to conduct appropriate processing as required. Please perform hard-shutdown only if it is very necessary to do so.
