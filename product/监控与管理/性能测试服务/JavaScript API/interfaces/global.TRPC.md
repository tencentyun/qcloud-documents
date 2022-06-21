# Interface: TRPC

[global](../modules/global.md).TRPC

## Table of contents

### Properties

- [env](#env)
- [namespace](#namespace)
- [sendOnly](#sendonly)

## Properties

<span id="env"></span>

### env

• **env**: `string`

123 环境名，例如 formal、pre、test

```js
export const option = {
    trpc: {
        env: 'formal'
    }
}
```

#### Defined in

typings/global.d.ts:304

___

<span id="namespace"></span>

### namespace

• **namespace**: `string`

环境类型，例如 Production、Development

```js
export const option = {
    trpc: {
        namespace: 'Development'
    }
}
```

#### Defined in

typings/global.d.ts:316

___

<span id="sendOnly"></span>

### sendOnly

• **sendOnly**: `boolean`

trpc 只发不收选项

```js
export const option = {
    trpc: {
        sendOnly: true
    }
}
```

#### Defined in

typings/global.d.ts:328
