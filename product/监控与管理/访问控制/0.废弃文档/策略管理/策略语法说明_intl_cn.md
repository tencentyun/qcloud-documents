##策略语法说明文档

### 1.概述
CAM中的策略本质上是一个json文档，主要用于给指定用户授权，一条基本的策略语法demo如下所示

     {	
           "version":"1.0",
            "statement":
                  {
                       "effect":"allow“,   
                       "action":"cos:*",
                       "resource":"qcs::cos:uin/123:*"
                  }
     }


### 2.语法结构
