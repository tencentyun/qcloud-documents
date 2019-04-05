## Application Scenario of Configuration Item Volume
Map the specified key in the configuration file to the container (key is the file name and Value is the file content). Configuration item volume is mainly used for mounting the business configuration file and can be applied to mount the configuration file to the specified container directory.

## How to Use Configuration Item Volume
1. Step 1: [Create Configuration Item](https://cloud.tencent.com/document/product/457/10173#.E9.85.8D.E7.BD.AE.E6.96.87.E4.BB.B6.E7.9A.84.E5.88.9B.E5.BB.BA) (You can skip this step if you already have a configuration item)
2. Step 2: In the service creation page, click [Add Volume] under "**Volume**" option.
![][createVolume]
3. Step 3: Configure volume.
 - **Type**: Click "∨", and select a type in the drop-down box. Here, we choose configuration item.
 - **Name**: Volume name, which consists of lowercase letters, numbers and en dash ("-"). It must start with a lowercase letter and cannot exceed 20 characters.
 - **Configuration**: Select the key of the required configuration item. Multiple keys can be selected.

 ![][setVolumeConfig]
4. Step 4: Set a mount path: Enter the mount point in "**Containers in Pod**".
 - **Volume name**: Select the volume configured above.
 - **Destination path**: Set the path where the data volume is mounted to the container.
 - **Permission**: Set the read/write permission for the path.

 ![][setVolumeMountPath]

5. After the setting is completed, log in to verify the container. Finally, the `configuration item-version number` is used as the name of configMap. Import the content of the configuration item into the cluster. "key" is the file name, and "Value" is the file content to be mounted to the specified path of the container.
  - Log in to the container to verify the status of mounting:

    ![][verification1]

  - Check the generation of configMap through kubectl:

    ![][verification2]

[createVolume]:https://mc.qcloudimg.com/static/img/0286498ec3ada210c6c01f9ef8ca7b52/image.png
[setVolumeConfig]:https://mc.qcloudimg.com/static/img/eeded2a4004698e1d80d7aefa2c8ec89/%7B93E0B701-53FC-4A2D-8F2D-3BEC63D74B6C%7D.png
[setVolumeMountPath]:https://mc.qcloudimg.com/static/img/e01549058b6a3d247b1984dc9e7b7ae6/%7B3EDDC270-1C72-45FB-80B9-0E48C9F2EBA9%7D.png
[verification1]:https://mc.qcloudimg.com/static/img/f7c1d19ddbaf27c8f02dd26812131d02/%7BBFC5C7DC-67B0-4845-A29B-4A2DB5F2F527%7D.png
[verification2]:https://mc.qcloudimg.com/static/img/0511cf8b32247d3d86cd2a1b8041f74a/%7BAB51D5B6-6CB4-4613-B49F-4E33BD174564%7D.png

