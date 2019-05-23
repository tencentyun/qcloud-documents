LogListener is a log collection agent provided by Tencent Cloud's Cloud Log Service (CLS). You can install and deploy it on the destination server to collect logs in real time.

## Supported Environment
LogListener supports the following Linux 64-bit operating systems:

- CentOS
- Debian
- SUSE
- OpenSUSE
- Ubuntu


## Installation Procedure

### 1. Download LogListener
Download URL of the latest LogListener:
[Download LogListener](https://main.qcloudimg.com/raw/6fe6877508ad86943d623799c2c68185/loglistener.2.1.6.tar.gz)

### 2. Install LogListener
Decompress the downloaded installer package and save it to a directory, enter `/loglistener/tools` under the directory to execute the following command with the root permission:
```
./install.sh $(SecretId) $(SecretKey) $(region)
```

| Parameter Name | Type Description |
|-----|:-----|
|SecretId| Part of the [Cloud API Key](https://console.cloud.tencent.com/cam/capi), which is used to identify the API caller |
|SecretKey| Part of the [Cloud API Key](https://console.cloud.tencent.com/cam/capi), which is used for signature string encryption, and signature string verification by server |
|region| Region of CLS |

> **Notes:**
>
> - It is recommended to use a collaborator key, and the collaborator should be granted the read-write permission of CLS by the primary account.
> - "region" is the region where CLS is available instead of the region in which your business server resides.
> - The installation script uses `rc.local` to ensure that the client starts normally upon server restart.


## Working with LogListener

### 1. Start LogListener
You can start the LogListener with the following script:
```
cd loglistener/tools; ./start.sh
```
### 2. Stop LogListener
You can stop the LogListener with the following script:
```
cd loglistener/tools; ./stop.sh
```

### 3. Check processes
You can check the processes of LogListener using the following command:
```
cd loglistener/tools; ./p.sh
```

Generally, there are three processes:
```
bin/loglistenerm -d                                # Daemon
bin/loglistener --conf=etc/loglistener.conf        # Main process    
bin/loglisteneru -u --conf=etc/loglistener.conf    # Update process
```


### 4. Uninstall LogListener
You can uninstall the LogListener using the following command:
```
cd loglistener/tools;
./uninstall
```

>**Note:**
>Uninstalling LogListener will delete the auto-restart tool from `rc.local`.

## Updating LogListener

We recommend that you update LogListener to the latest version. **Log structuring is not supported for versions below LogListener 2.1.1.** You can check the LogListener version in `loglistener/version.txt`.
- If your LogListener version is higher than 2.0.0 but lower than the latest version, update it by following the procedure below:
 1. Download a new installer package.
 2. Decompress the new package to the installation directory (the same level as LogListener directory).
 3. After the decompression, restart LogListener to complete the update process.

- If your LogListener version is lower than 2.0.0, update it manually by following the procedure below:
 1. Stop the lower version of LogListener.
 2. Back up the lower version of LogListener.
 3. Download and install the latest LogListener.

> Auto update of LogListener 2.0.0 or above will be available soon. [User guide on LogListener lower than 2.0.0](https://cloud.tencent.com/document/product/614/13550).

