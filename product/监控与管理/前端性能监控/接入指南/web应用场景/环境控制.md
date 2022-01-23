
aegis 默认把数据所在环境当作 `production` 进行上报，如果需自行修改，可以使用 env 参数进行修改。

```javascript
new Aegis({
  id: '',
  env: Aegis.environment.gray
})
```


Aegis.environment 枚举值如下：

```javascript
export enum Environment {
  production = 'production', // 生产环境
  gray = 'gray', // 灰度环境
  pre = 'pre', // 预发布环境
  daily = 'daily', // 日发布环境
  local = 'local', // 本地环境
  test = 'test', // 测试环境
  others = 'others' // 其他环境
}
```

修改 env 参数后，aegis 上报的数据都会带上该参数，方便开发者区分不同环境的数据，但是只有 production 环境的数据会参与项目得分的计算。
