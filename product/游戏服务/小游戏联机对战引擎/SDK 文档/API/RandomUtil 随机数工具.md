>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。


MGOBE SDK 内部实现了一个基于“线性同余算法”的随机数生成方法。RandomUtil 对象方法如下：

### init
#### 接口描述
初始化随机数。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|seed|number|随机数种子|


<dx-alert infotype="explain" title="">
init 方法接受一个 seed 为参数，RandomUtil 在后续生成随机数的过程中将以 seed 为种子。使用相同的 seed 初始化，调用 random 方法生成的随机数序列相同。
</dx-alert>


#### 返回值说明
无

#### 使用示例
```
MGOBE.RandomUtil.init(12345678);
```

### random
#### 接口描述
生成随机数。


#### 参数描述
无



<dx-alert infotype="explain" title="">
如果种子相同、初始化后调用次数相同，生成的随机数将相同。
</dx-alert>


#### 返回值说明
返回值类型为 number，表示随机数，范围为[0,1)。

#### 使用示例
```
const num = MGOBE.RandomUtil.random();
```

