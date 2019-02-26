Failure to shut down or restart a CVM is a rare event. Here are possible reasons for such failure and troubleshooting methods.

### Possible reasons for shutdown or restart failure

1. Check the CPU/memory usage of the CVM. Excessive CPU utilization or memory exhaustion may cause shutdown or restart failure of the CVM on the console.

2. For Linux operating systems, you can check whether the ACPI management application is installed by running the `ps -ef | grep -w "acpid" | grep -v "grep"` command. Install the acpid module if no ACPI process exists.

3. For Windows operating systems, you can check whether such failure is caused by WindowsUpdate taking too long. Windows usually performs patch-related operations by the time when the system is about to shut down, and if the update takes a long time, shutdown/restart failure may occur.

4. In case of initial purchase of Windows, the initialization process is slightly longer due to the use of Sysprep for distributing images. Windows will ignore the shutdown/restart event until the initialization has been finished, thus causing CVM shutdown/restart failure.

5. If the operating system is broken due to some software installed or attacks from Trojans or other viruses, shutdown/restart failure may also occur.


### Forced shutdown/restart

The forced shutdown/restart feature provided by Tencent Cloud can be used in case of multiple failed attempts to shut down or restart the CVM. This feature allows you to forcibly **shut down/restart** the CVM, which however may cause data loss or file system damage.

Select **Forced Shutdown** in the shutdown operation window on the CVM console.
![](https://mc.qcloudimg.com/static/img/e54e611f35c0b6772b42f40943cfb5b1/image.png)

Select **Forced Restart** in the restart operation window on the CVM console.
![](https://mc.qcloudimg.com/static/img/53c38635086c7faee2e90bf24f8dbca6/image.png)


