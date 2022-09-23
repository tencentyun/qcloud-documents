**语法如下：**
```
TRUNCATE [TABLE] tbl_name
```

>!
- 需要有drop权限
- 截断操作会导致隐式提交，因此无法回滚
- 第一次执行truncate若失败，则进行第二次truncate

**示例：**

```
truncate table t1;
```
