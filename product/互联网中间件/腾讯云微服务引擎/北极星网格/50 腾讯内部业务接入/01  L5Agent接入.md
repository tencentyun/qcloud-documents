## 操作场景
 
本文针对腾讯内部自研上云用户接入微服务引擎托管的 PolarisMesh 治理中心。

### L5agent 使用北极星

#### L5 的SID在北极星中如何创建
 
由于 l5api 仅支持访问 L5 SID，因此访问非 L5 SID 格式的服务名，需要创建 CL5 SID 格式的服务别名指向该服务，这里请直接从内部北极星将服务对应的L5别名SID信息直接复制，然后在公有云北极星中创建响应的服务别名。

- 复制 SID 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/81d75a94d0f82138bd91de6c19c34057.png)
- 如果对应的环境类型（即命名空间）在公有云北极星引擎中不存在，则先进行手动创建。
![](https://qcloudimg.tencent-cloud.cn/raw/c97b1a669c8912e1cd1b04fb67766c89.png)
- 在公有云北极星引擎实例中创建L5格式的服务别名。
![](https://qcloudimg.tencent-cloud.cn/raw/c71c1b754b02120262a2551dc7bebe48.png)


#### SID 和命名空间的对应关系

L5 SDI 的格式：ModID:CmdID

>!**强烈建议用户命名空间选择 default 或者 Production，ModID 取值范围为： [2, 192,000,000]**

如果用户确实有需要使用其他命名空间，请按照以下方式进行其他命名空间的换算：
ModID 数值右移6位，如果结果 >= 3000001，则需要计算 ModID & 63 的结果值，根据结果值对应的命名空间信息如下，否则会出现L5寻址失败的问题：

```json
{
	1: "Production",
	2: "Development",
	3: "Pre-release",
	4: "Test",
	5: "Polaris",
	6: "default",
}
```

## 微服务引擎操作场景
本文主要面向腾讯内部自研上云用户如何迁移至微服务引擎托管的 PolarisMesh 治理中心。

## 前提条件
已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。


### 引擎实例未开启客户端公网访问

#### L5Agent 接入

1. 查看引擎的接入地址，在实例的基本信息页面中，记住访问地址中的每个VPC内网IP地址以及访问端口
![](https://qcloudimg.tencent-cloud.cn/raw/fb9e4d3a42c3795682cf030409feedf0.png)
2. 修改L5Agent的配置文件 l5_config.ini
```toml
[L5CONFIG]
ServerIp={对应 vpc 的内网接入地址}
ServerPort=7779
```
4. 重启 L5agent，启动前要把/data/L5Backup/l5server_list.backup删掉

### 引擎实例开启客户端公网访问

#### L5Agent 接入

1. 查看引擎的接入地址，在实例的基本信息页面中，记住访问地址中的公网IP地址以及访问端口
![](https://qcloudimg.tencent-cloud.cn/raw/2e7e813be530b1d4f5fc6fe501452b03.png)
2. 修改L5Agent的配置文件 l5_config.ini
```toml
[L5CONFIG]
ServerIp={对应公网接入地址}
ServerPort=7779
```
4. 重启L5agent，启动前要把/data/L5Backup/l5server_list.backup删掉

## 常见问题排查

### 使用 ./L5GetRoute1 查询失败

**现象**

./L5GetRoute1 xxx xxx 10
ApiGetRoute failed, ret: -9998, usec=181283,avg_usec=181283,err: FILE[static_route.cpp] LINE[153][GetRoute],NOT FOUND,invalid mod[xxx] cmd[xxx]

**排除方向**

- 检查 l5config.ini 中对于 ServerIp 的信息是否填写正确
- 确保对应的服务下有健康的服务实例
- L5 的 SID 所对应的命名空间是否正确
- 是否已经在北极星中创建了格式为 SID 的服务别名
