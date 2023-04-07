## JSAPI 接口
```js
getBLEDeviceCharacteristics(param: BLEDeviceCharacteristicsParam): Promise<BLEDeviceCharacteristicsResp>

interface BLEDeviceCharacteristicsParam {
  /**
   * 需要连接的BLE设备id
   */
  deviceId: string;
  /**
   * service的uuid
   */
  serviceId: string;
}

interface BLEDeviceCharacteristicsResp {
  /**
   * 所支持的characteristic列表
   */
  characteristics: BLECharacteristicItem[];
}


/**
 * ble设备提供的characteristic
 */
export interface BLECharacteristicItem {
  /**
   * characteristic的uuid
   */
  characteristicId: string;
  /**
   * 特征支持的属性
   */
  property: BLECharacteristicProperty;
}

/**
 * BLE设备的特征属性
 */
export enum BLECharacteristicProperty {
  /**
   * 广播特征
   */
  PROPERTY_BROADCAST = 1,
  /**
   * 其他特征
   */
  PROPERTY_EXTENDED_PROPS = 128,
  /**
   * 支持indicate的特征
   */
  PROPERTY_INDICATE = 32,
  /**
   * 支持notify的特征
   */
  PROPERTY_NOTIFY = 16,
  /**
   * 支持读的特征
   */
  PROPERTY_READ = 2,
  /**
   * 支持带签名写的特征
   */
  PROPERTY_SIGNED_WRITE = 64,
  /**
   * 支持写的特征
   */
  PROPERTY_WRITE = 8,
  /**
   * 支持无回调写的特征
   */
  PROPERTY_WRITE_NO_RESPONSE = 4,
}

```

## 代码示例
```js
wemeet.bluetooth.getBLEDeviceCharacteristics({
    deviceId: 'xxxxxxxxxx',
    serviceId: 'xxxxxxxxx',
})
    .then((resp) => {
        // 连接的ble设备提供的所有service
        const { characteristics } = resp;
        // 假设目标characteristic 是第一个；
        const targetCharacteristic = services[0];
        // service的uuid
        const {
            characteristicId, // 蓝牙设备特征的 UUID
            property, // 该特征支持的操作类型
        } = targetCharacteristic;
    })
    .catch(error => {
        console.error('getCharacteristics failed', error);
    });

```
