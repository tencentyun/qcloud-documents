## Policy Syntax Instruction

### 1. Overview
A policy in CAM is essentially a JSON document, which is mainly used to grant permissions to specified users. A basic policy syntax demo is shown below

     {	
           "version":"1.0",
            "statement":
                  {
                       "effect":"allow",   
                       "action":"name/cos:*",
                       "resource":"qcs::cos:uin/123:*"
                  }
     }


### 2. Syntax Structure

