## 配置导入到环境变量
### 第一步：创建配置项
1. 进入控制台，创建配置项，填写`配置项名称`、`版本号`、`版本描述`
2. 支持按YAML语法编辑， 支持按可视化编辑

- YAML语法编辑，格式为`key：value`格式， value可以是字符串，也可以是文本。若Value是文本， 则用`“|”` 表示。YAML已缩进作为分割。
- 支持可视化编辑， 可视化的value支持字符串和文本。
如下图：
![Alt text](https://mc.qcloudimg.com/static/img/c3bc8b5c36986fa59493cce525430df4/%7B70371D71-F78F-4523-92EB-55C1218F4EAC%7D.png)
创建完成后，创建服务即可使用该配置项。

### 第二步：创建服务通过配置项导入环境变量
1.进入控制台，单击创建/更新服务
2.环境变量参数选择导入环境变量
![Alt text][1]
![Alt text][2]

3.完成创建

[1]:https://main.qcloudimg.com/raw/ac724731c0482e1fba590f119b7039b9.png
[2]:https://main.qcloudimg.com/raw/55fa4732a4b17100b7b8e2e07a4aa68d.png
