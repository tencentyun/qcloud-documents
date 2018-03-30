
开发商的 web 服务器不需要做任何改造，wns 透传开发商自己的 http 数据包。为了开发商便于获取终端的信息，wns 在 http 头上，会添加部分信息。具体内容如下
X-Wns-Qua : Wns Sdk 的版本信息，开发商可以记录 sdk 版本信息，定位问题时可以便于确认具体的版本号。
X-Forwarded-For : 移动终端的 IP 地址，开发商可以根据终端 IP 做精确营销等服务。
X-Wns-DeviceInfo : 移动终端的设备信息，开发商可以根据设备信息做图片适配、差异化服务等。
X-Wns-Wid : 移动终端的唯一标识，可以根据 wid 做详细的问题定位，开发商也可以使用 wid 做 push 消息调用。
QVIA : 移动终端的 IP，内容和 X-Forwarded-For 相同。