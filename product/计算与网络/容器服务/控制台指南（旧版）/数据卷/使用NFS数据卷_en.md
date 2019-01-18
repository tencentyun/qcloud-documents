## Application Scenario of NFS Volume
NFS volume is used for the persistent storage of data that can be read and written many times, and is suitable for scenarios such as big data analysis, media processing and content management. You can use Tencent Cloud [CFS](https://cloud.tencent.com/document/product/582/9127) or self-built NFS.

## How to Use NFS Volume
1. In the service creation page, click [Add Volume] under "**Volume**" option.
![][createVolume]
2. Configure volume.
 - **Type**: Click "∨", and select a type in the drop-down box. Here, we choose NFS disk.
 - **Name**: Volume name, which consists of lowercase letters, numbers and en dash ("-"). It must start with a lowercase letter and cannot exceed 20 characters.
 - **NFS path**: Enter CFS or self-built NFS address. For more information on CFS creation, please see [How to Use CFS](https://cloud.tencent.com/document/product/457/10910). After creation, check the mount point information on the CFS console for the NFS IP address and directory.
 
 ![][setVolumeConfig]
3. Set a mount path: Enter the mount point in "**Containers in Pod**".
 - **Volume name**: Select the volume configured above.
 - **Destination path**: Set the path where the data volume is mounted to the container.
 - **Permission**: Set the read/write permission for the path.

 ![][setVolumeMountPath]

4. After the setting is completed, log in to verify the container.

  ![][verification]

[createVolume]:https://mc.qcloudimg.com/static/img/0286498ec3ada210c6c01f9ef8ca7b52/image.png
[setVolumeConfig]:https://mc.qcloudimg.com/static/img/366d4f7229e12327308f36cfa88cf537/%7B3CDF6473-D03E-4AF7-BEE6-C87CDD70FACD%7D.png
[setVolumeMountPath]:https://mc.qcloudimg.com/static/img/3547f641ae9b6882c4bc9cead42f2b05/%7B8F01ACF0-6408-4EFB-A2B3-D1EE8A56EA6C%7D.png
[verification]:https://mc.qcloudimg.com/static/img/1770f6809fd201f1bcf1ec85dddd3c2b/%7BDF572259-79C1-4879-9121-F33A66F002BD%7D.png

