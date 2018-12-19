LogListener is the agent provided by Tencent Cloud CLS for collecting logs. You can install it to collect logs in real time.

## Supported Systems

LogListener currently supports the following Linux 64-bit operating systems:

- CentOS
- Debian
- SUSE
- OpenSUSE
- Ubuntu

## Instructions

### Installing LogListener

[Click to download LogListener 2.1.1](https://mc.qcloudimg.com/static/archive/520370e2a9e96c9bd36b5ced36ecdb83/loglistener.2.1.1.tar.gz), then decompress the setup package to the specified directory, and execute the following command under the root directory.

```
cd loglistener/tools;
./install.sh $(SecretId) $(SecretKey) $(region)
```

> **Note:**
>
> - "SecretId" and "SecretKey" used in this case are those in your [cloud API key](https://console.cloud.tencent.com/cam/capi). You are recommended to use a collaborator key, and be sure to grant collaborator the read/write permission of CLS before using it.
> - "region" is **the region where CLS is available instead of the region where your server resides**. Region IDs are as follows:
>
> ```
> shanghai - Shanghai
> guangzhou - Guangzhou
> chengdu - Chengdu
> beijing - Beijing
> ```

The installation script uses `rc.local` to ensure that the client starts normally upon server restart.

### Checking Processes

You can check the processes using the following command:

```
cd loglistener/tools; ./p.sh
```

Generally, there are three processes:

```
bin/loglistenerm -d                                                  --Daemon process
bin/loglistener --conf=etc/loglistener.conf                          --Main process
bin/loglisteneru -u --conf=etc/loglistener.conf                      --Update process
```

### Starting and Stopping Client

You can start the client with the following script:

```
cd loglistener/tools; ./start.sh
```

Stop the client:

```
cd loglistener/tools; ./stop.sh
```

### Uninstalling LogListener

```
cd loglistener/tools;
./uninstall
```

Uninstalling LogListener will delete the auto-restart tool from `rc.local`.

## Updating LogListener

We recommend that you update LogListener to the latest version. **Log structuring is not supported for versions below 2.1.1.** You can check the LogListener version in `loglistener/version.txt`.

If your LogListener version is not the latest version but above 2.0.0, update it following the procedures below:

1. Download a new installation package.
2. Decompress the new package to the installation directory (equivalent to LogListener directory).
3. After the decompression, restart LogListener to complete the update process.

If your LogListener version is lower than 2.0.0, update it manually following the procedures below:

1. Stop the lower version of LogListener.
2. Back up the lower version of LogListener.
3. Download and install the latest version of LogListener.

> Auto update of LogListener 2.0.0 or above will be available soon. [User Guide on LogListener Below 2.0.0](https://cloud.tencent.com/document/product/614/13550)

## How Does It Work

LogListener perceives the changes of files through the change event (Inotify) of file system and then starts collecting logs.

## Metrics and Limits

Collection latency: 2 seconds

Latency before the change to collection configuration takes effect: within 1 minute

Maximum log volume: 16 MB/sec

Maximum length: 512 KB for a log. If this length is exceeded, the log is truncated to 512 KB before being collected.

Maximum number of connections: 1,024

Memory usage: 50 MB at the most in general, and 150 MB in case of a failure of backend service.

CPU usage: Not more than 20% of single-core CPU for all of the three processes, if log volume is kept at 5 MB/sec.

