在线扩容原理步骤
1.在WEB控制台或者API发起扩容操作
2.系统根据需要按新规格创建对应数量的Secondary节点
3.依次把新创建的Secondary节点加入集群实例内部，同步数据
4.待最后一个Secondary节点数据同步完成以后，开始一个一个踢掉原节点，剔除的顺序按先从（Secondary）后主（Primary）
5.当集群内部没有主节点时，会选举出新的主节点
![](https://mc.qcloudimg.com/static/img/c5f2b406c73f6fd9c21b216d1cf0d350/zaixiuankuorong.png)
