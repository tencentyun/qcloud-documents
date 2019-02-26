## Application Scenarios
Local disk is used by following ways:
- Specified source path (HostPath): Mount the file directory of the host where the container resides to the specified mount point of the container. For example, if the container needs to access` / etc / hosts`, `HostPath` can be used to map `/etc/hosts`.
- Empty source path (EmptyDir): Used for the temporary storage of data for containers, such as disk-based sorting.

## Operation Steps
1. In the service creation page, click [Add Volume] under "**Volume**" option.
  ![][createVolume]
2. Configure volume.
 - **Type**: Click "∨", and select a type in the drop-down box. Here, we choose local disk.
 - **Name**: Volume name, which consists of lowercase letters, numbers and en dash ("-"). It must start with a lowercase letter and cannot exceed 20 characters.
 - **Source Path**: Enter the host's source path as needed or leave it empty.

 ![][setVolumeConfig]
3. Set a mount path: Enter the mount point in "**Containers in Pod**".
 - **Volume name**: Select the volume configured above.
 - **Destination path**: Set the path where the data volume is mounted to the container.
 - **Permission**: Set the read/write permission for the path.

 ![][setVolumeMountPath]

4. After the setting is completed, log in to verify the container.
![][verification]


[createVolume]:https://mc.qcloudimg.com/static/img/0286498ec3ada210c6c01f9ef8ca7b52/image.png
[setVolumeConfig]:https://mc.qcloudimg.com/static/img/062d9b093b006627f6186a5b59cbe2ff/%7BAD62E0D6-78E7-4BB2-93D8-CC0D29ADDB57%7D.png
[setVolumeMountPath]:https://mc.qcloudimg.com/static/img/1367d8a35e215c7c22450a5cc9c1fda6/%7B0BE30571-DB5E-43A4-AFEC-656A47647EEB%7D.png
[verification]:https://mc.qcloudimg.com/static/img/d84e7b3246ef627889c67e0ed38f95aa/%7B4768A55C-CEB7-46AF-A3A2-0A49D3AC7063%7D.png

