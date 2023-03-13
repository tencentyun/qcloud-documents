MapContext 实例，可通过 wx.createMapContext 获取。

MapContext 通过 id 跟一个 `<map>` 组件绑定，操作对应的 `<map>` 组件。

方法
MapContext.addMarkers
添加 marker。

MapContext.fromScreenLocation
获取屏幕上的点对应的经纬度，坐标原点为地图左上角。

MapContext.getCenterLocation
获取当前地图中心的经纬度。返回的是 gcj02 坐标系，可以用于 wx.openLocation()

MapContext.getRotate
获取当前地图的旋转角

支持度：仅Android

MapContext.getRegion()
获取当前地图的视野范围

MapContext.getScale()
获取当前地图的缩放级别

MapContext.getSkew()
获取当前地图的倾斜角

MapContext.includePoints(Object object)
缩放视野展示所有经纬度

MapContext.moveAlong
沿指定路径移动 marker，用于轨迹回放等场景。动画完成时触发回调事件，若动画进行中，对同一 marker 再次调用 moveAlong 方法，前一次的动画将被打断。

支持度：仅iOS

MapContext.moveToLocation
将地图中心移置当前定位点，此时需设置地图组件 show-location 为true。

MapContext.openMapApp
拉起地图 APP 选择导航。

MapContext.removeMarkers
移除 marker。

MapContext.translateMarker
平移marker，带动画。

示例代码
```
<!-- map.wxml -->
<map id="myMap" show-location />

<button type="primary" bindtap="getCenterLocation">获取位置</button>
<button type="primary" bindtap="moveToLocation">移动位置</button>
<button type="primary" bindtap="translateMarker">移动标注</button>
<button type="primary" bindtap="includePoints">缩放视野展示所有经纬度</button>
```

```

// map.js
Page({
  onReady: function (e) {
    // 使用 wx.createMapContext 获取 map 上下文
    this.mapCtx = wx.createMapContext('myMap')
  },
  getCenterLocation: function () {
    this.mapCtx.getCenterLocation({
      success: function(res){
        console.log(res.longitude)
        console.log(res.latitude)
      }
    })
  },
  moveToLocation: function () {
    this.mapCtx.moveToLocation()
  },
  translateMarker: function() {
    this.mapCtx.translateMarker({
      markerId: 0,
      autoRotate: true,
      duration: 1000,
      destination: {
        latitude:23.10229,
        longitude:113.3345211,
      },
      animationEnd() {
        console.log('animation end')
      }
    })
  },
  includePoints: function() {
    this.mapCtx.includePoints({
      padding: [10],
      points: [{
        latitude:23.10229,
        longitude:113.3345211,
      }, {
        latitude:23.00229,
        longitude:113.3345211,
      }]
    })
  }
})
```
