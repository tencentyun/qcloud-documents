## NFS数据卷应用场景
使用NFS数据卷适用于多读多写的持久化存储，适用于大数据分析、媒体处理、内容管理等场景，可以选择使用腾讯云的[文件存储CFS](https://cloud.tencent.com/document/product/582/9127), 也可使用自建的文件存储NFS。

## 使用NFS数据卷操作流程
1. 在创建服务页面 **数据卷** 选项下单击**添加数据卷**。
![][createVolume]
2. 配置数据卷。
 - **类型**：单击**∨**，在下拉框中选择数据卷的类型，选择使用NFS盘。
 - **名称**：数据卷的名称，由小写字母和数字和连接符 “-” 组成，必须是小写字母开头，且在 20 个字符以内。
 - **NFS路径**：填写CFS或自建NFS地址, 如需创建CFS详情查看[CFS使用指引](https://cloud.tencent.com/document/product/457/10910), 创建完成后可在CFS控制台查看挂载点信息获取NFS的IP地址和目录。
 
 ![][setVolumeConfig]
3. 设置挂载路径：在 **实例内容器**填写挂载点。
 - **数据卷名称**：选择上述设置的数据卷
 - **目标路径**：设置数据卷挂载到容器内的路径
 - **权限**：设置该路径的读写权限。

 ![][setVolumeMountPath]

4. 设置完成，登录容器验证。

  ![][verification]

[createVolume]:https://mc.qcloudimg.com/static/img/0286498ec3ada210c6c01f9ef8ca7b52/image.png
[setVolumeConfig]:https://mc.qcloudimg.com/static/img/366d4f7229e12327308f36cfa88cf537/%7B3CDF6473-D03E-4AF7-BEE6-C87CDD70FACD%7D.png
[setVolumeMountPath]:https://mc.qcloudimg.com/static/img/3547f641ae9b6882c4bc9cead42f2b05/%7B8F01ACF0-6408-4EFB-A2B3-D1EE8A56EA6C%7D.png
[verification]:https://mc.qcloudimg.com/static/img/1770f6809fd201f1bcf1ec85dddd3c2b/%7BDF572259-79C1-4879-9121-F33A66F002BD%7D.png
