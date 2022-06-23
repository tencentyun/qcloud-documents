## Properties（属性）
[](id:env)
### env
- **env**: `string`

```
 Defined in typings/global.d.ts:304
```
123 环境名，例如 formal、pre、test
```js
export const option = {
    trpc: {
        env: 'formal'
    }
}
```


[](id:namespace)
### namespace
- **namespace**: `string`

```
Defined in ypings/global.d.ts:316
```
环境类型，例如 Production、Development
```js
export const option = {
    trpc: {
        namespace: 'Development'
    }
}
```

[](id:sendOnly)
### sendOnly
- **sendOnly**: `boolean`

```
Defined in typings/global.d.ts:328
```
trpc 只发不收选项
```js
export const option = {
    trpc: {
        sendOnly: true
    }
}
```
