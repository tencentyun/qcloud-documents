HAVIP 不是从控制台绑定，而是由后端云服务器根据心跳检测，协商和声明绑定 HAVIP 的设备，此处与传统模式一致。您也可以通过更改 HA 应用的配置文件来更改绑定关系。
如，在 keepalived 方案下，在 keepalived.conf 中指定 virtual_address。如果是其他方案，在对应的配置文件中指定 virtual IP 为 HAVIP 即可。
详细操作步骤（以 keepalived 为例），请参见最佳实践 [VPC 内通过 keepalived 搭建高可用主备集群](https://cloud.tencent.com/document/product/215/20186)。
