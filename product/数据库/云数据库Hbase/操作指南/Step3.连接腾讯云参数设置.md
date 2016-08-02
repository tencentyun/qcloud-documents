##  连接腾讯云参数设置

1).连接腾讯云Hbase服务时必须设置以下参数为true（完整代码请参考示例代码），方能正常使用：
config.setBoolean("chbase.tencent.enable", true);

2).如需要使用yarn，还需要额外设置实例ID（管理页面可以查到，完整代码请参考示例代码），如：
config.set("yarn.chbase.tencent.instanceid", "chb-lpvsvdlr");

提示：
除增加以上代码，其余使用方式和社区版本Hbase一致；可以参考https://hbase.apache.org/ 的API文档；
如您未设置以上参数，也可以正常连接社区版的Hbase。
