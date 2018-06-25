## Application Scenario of Cloud Disk Volume
A Kubernetes block storage plug-in extended based on Tencent Cloud CBS. You can specify a Tencent Cloud CBS to be mounted to a container path, and it is migrated along with the container.
The cloud disk volume is used for the persistent storage of data, and is suitable for stateful services such as MySQL.
If the cloud disk volume is configured, the maximum number of pods is 1.



## How to Use Cloud Disk volume
1. In the service creation page, click [Add Volume] under "**Volume**" option.
![][createVolume]
2. Configure volume.
 - **Type**: Click "∨", and select a type in the drop-down box. Here, we choose cloud disk.
 - **Name**: Volume name, which consist of lowercase letters, numbers and en dash ("-"). It must start with a lowercase letter and cannot exceed 20 characters.
 - **Cloud disk**: Select the CBS in the same region as the cluster.

 ![][setVolumeConfig]
3. Set a mount path: Enter the mount point in "**Containers in Pod**".
 - **Volume name**: Select the volume configured above.
 - **Destination path**: Set the path where the data volume is mounted to the container.
 - **Permission**: Set the read/write permission for the path.

 ![][setVolumeMountPath]

4. After the setting is completed, log in to verify the container.

  ![][verification]

[createVolume]:https://mc.qcloudimg.com/static/img/0286498ec3ada210c6c01f9ef8ca7b52/image.png
[setVolumeConfig]:https://mc.qcloudimg.com/static/img/a066bec7342ef64ece17f3cee685b476/%7B915B0650-0AB4-441B-94A0-40F4CA948173%7D.png
[setVolumeMountPath]:https://mc.qcloudimg.com/static/img/5be0d9f420a6e5e3faaedaa28d232817/%7B59ED8246-75CE-4DCE-B03F-937A3F9B14B9%7D.png
[verification]:https://mc.qcloudimg.com/static/img/df8085760b2ffeb6100b24ecb07ac91b/%7B4DC33FE1-22B6-4E7A-A898-B482C39D102B%7D.png

