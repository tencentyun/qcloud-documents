### 在线扩容原理步骤

1.在 WEB 控制台或者 API 发起扩容操作
2.系统根据需要按新规格创建对应数量的 Secondary 节点
3.依次把新创建的 Secondary 节点加入集群实例内部，同步数据
4.待最后一个 Secondary 节点数据同步完成以后，开始一个一个踢掉原节点，剔除的顺序按先从（Secondary）后主（Primary）
5.当集群内部没有主节点时，会选举出新的主节点
![](https://mc.qcloudimg.com/static/img/c5f2b406c73f6fd9c21b216d1cf0d350/zaixiuankuorong.png)

### 扩容操作
1.在控制台实例列表页单击【扩容】按钮，选择需要扩到的存储容量，单击确认即可
![](https://mc.qcloudimg.com/static/img/3e947304edbd8acadec230ece7b7b9c8/kuoron.png)
