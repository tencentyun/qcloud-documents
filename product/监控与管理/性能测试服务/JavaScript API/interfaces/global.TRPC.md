## Properties（属性）
[](id:env)
### env
**env**: `string`

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
**namespace**: `string`

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
**sendOnly**: `boolean`

trpc 只发不收选项
```js
export const option = {
    trpc: {
        sendOnly: true
    }
}
```
