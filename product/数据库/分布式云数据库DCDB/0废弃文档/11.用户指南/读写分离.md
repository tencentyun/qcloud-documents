## 1. 背景说明
云数据库（TDSQL）默认支持读写分离能力，标准版一个数据库节点组（SET）基本配置为一主二从，两从机默认可提供读能力。
为保证不影响集群稳定性，TDSQL的从机读并不需要用户直连从机，而是由网关集群（TProxy）自动分配到低负载从机上。
## 实现方法
在每条需要从机“读”的语句前，增加/*slave*/字段，并且mysql后面要增加-c 参数来解析注释`mysql  -c -e  "/*slave*/sql"`，即可自动将读请求分配到从机，示例如下：

```
//主机读//
select * from emp order by sal，deptno desc；
//从机读//
/*slave*/ select * from emp order by sal，deptno desc；
```


注意事项：
- 	仅支持从机读（select），不支持其他操作，非select语句将失败；
- mysql后面要增加-c 参数来解析注释	
- `/*slave*/`必须为小写，语句前后无空格；
- 	从机出现异常而影响到MAR（强同步）机制时，从机读操作将自动切换回主机。
