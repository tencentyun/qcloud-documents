``` html
@JsPlugin(secondary = true)
public class CustomPlugin extends BaseJsPlugin {
    @JsEvent("custom_event")
    public void custom(final RequestEvent req) {        
    //获取参数        
    //req.jsonParams        
    //异步返回数据        
    //req.fail();        
    //req.ok();        
    req.ok(new JSONObject());    
}    
    @JsEvent({"getSystemInfo", "getSystemInfoSync"})    
    public String custom1(final RequestEvent req) {        
    //获取参数        
    //req.jsonParams        
    //同步返回数据(必须返回json数据)        
    return new JSONObject().toString();    
    }
}
```
- 继承 BaseJsPlugin 并用注解进行定义 @JsPlugin(secondary = true)。

- 定义一个方法，方法只能有一个参数且参数必须是 RequestEvent 类型。

- 然后在方法上定义注解 @JsEvent("事件名")，当小程序 js 调用“事件名”时就会调用到 @JsEvent 修饰的对应方法。

- @JsEvent 支持定义多个事件名。

- 支持同步或异步返回数据（同一事件只能选择一种方式）。


