LogListener is the agent provided by Tencent Cloud's CLS for collecting logs. You can install it to collect logs in real time.

## Supported Systems

LogListener currently supports the following Linux 64-bit operating systems:

CentOS

Debian

SUSE

OpenSUSE

Ubuntu

## Instructions for Using LogListener

### Install LogListener

[Click here to download LogListener 1.1.2](https://mc.qcloudimg.com/static/archive/64065f325335ce4fb1ed96433eb691fd/loglistener.1.1.2.tar.gz), decompress the setup package to the specified directory, and then execute the setup file under the root directory.

```
cd loglistener/tools/op;
./install ($SecretId)($SecretKey)($region)
```

Note: The SecretId and SecretKey used in this case are same as those in your cloud API key. region is the region where CLS is available, with the following ID:

```
shanghai - Shanghai
```

When setup script is executed, `crontab` is registered to ensure the client is enabled normally after the restart of machine.

```
*/1 * * * *  cd /…/loglistener/tools/cron; ./check_all.sh  > /dev/null 2>&1
```

### Check processes

You can check the processes using the following command:

```
cd loglistener/tools/op; ./p.sh
```

Generally, there are three processes:

```
./loglistener_watchdog                                   
--Daemon
./loglistener_dcc ../etc/loglistener_dcc.conf nofork     
--Inbound/outbound packets of network
./loglistener_mcd ../etc/loglistener_mcd.conf nofork    
--Log listening
```

### Enable and disable client

You can enable and disable client with script.

```
cd loglistener/tools/op; ./start.sh
cd loglistener/tools/op; ./stop.sh
```

### Uninstall LogListener

```
cd loglistener/tools/op;
./uninstall
```

Uninstalling LogListener will delete the client, unregister `crontab`, and clear the whole module and its shared memory, intermediate files and logs.

## How LogListener Works

LogListener perceives the changes of files through the change event (Inotify) of file system and then starts collecting logs.

## Use Limits and Metrics of LogListener

Collection latency: 2 seconds

Latency before the change to collection configuration takes effect: within 1 minute

Maximum log volume: 16 MB/sec

Maximum log length: 512 KB for a log. If this length is exceeded, the log is truncated to 512 KB before being collected.

Maximum number of connections: 1024

Memory usage: A maximum of 50 MB in normal situation, and 150 MB in case of the failure of backend service.

CPU usage: Not greater than 20% of single-core CPU for all of the three processes, if log volume is kept at 5 MB/sec.
