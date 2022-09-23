## 配置和模板管理多环境
### 第一步：创建配置项
1. 进入控制台，创建配置项，填写`配置项名称`、`版本号`、`版本描述`
2. 支持按YAML语法编辑， 支持按可视化编辑

- YAML语法编辑，格式为`key：value`格式， value可以是字符串，也可以是文本。若Value是文本， 则用`“|”` 表示。YAML已缩进作为分割。
- 支持可视化编辑， 可视化的value支持字符串和文本。
如下图：
![Alt text](https://mc.qcloudimg.com/static/img/c3bc8b5c36986fa59493cce525430df4/%7B70371D71-F78F-4523-92EB-55C1218F4EAC%7D.png)
创建完成后，创建服务即可使用该配置项。

### 第二步：创建或更新应用模板使用配置项进行变量替换
1. 进入创建或更新应用模板页面
2. 将常变的参数修改成变量的形式
3. 选择已有配置项为变量赋值

![Alt text][1]
![Alt text][2]

[1]:https://main.qcloudimg.com/raw/c2df22bd3c91e735fa306da88178fb3b.png
[2]:https://main.qcloudimg.com/raw/c4c04b186ce8e9e9c978e8a6870f2c36.png
