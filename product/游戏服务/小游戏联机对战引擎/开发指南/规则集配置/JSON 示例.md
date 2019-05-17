本文档主要介绍三种游戏场景的 JSON 示例 demo。
 
### 斗地主 1V1V1
- 组队条件：按用户所拥有的积分值区间进行组队。
- 积分区间分别为：0 - 100积分、201 - 1000积分、1001 - 5000积分、5001 - 10000积分。

示例代码如下：

    {
    	"version": "V1.0",
    	"teams": [
    		{
    			"name": "1v1v1",
    			"maxPlayers": 3,
    			"minPlayers": 3,
    			"number": 1
    		}
    	],
    	"playerAttributes": [
    		{
    			"name": "score",
    			"type": "number"
    		}
    	],
    	"rules": [
    		{
    			"type": "segment",
    			"expression": "teams[i].players.score",
    			"value": [
    				[
    					0,
    					100
    				],
    				[
    					101,
    					1000
    				],
    				[
    					1001,
    					5000
    				],
    				[
    					5001,
    					10000
    				]
    			]
    		}
    	]
    }

### 实时对战 5V5
- 组队条件：1级匹配，2 - 3级匹配，4 - 6级匹配，7 - 9级匹配。
- 队与队匹配：每个队伍 ELT 属性值平均值的误差不超过2。

示例代码如下：
    
    {
    	"version": "V1.0",
    	"teams": [
    		{
    			"name": "5v5",
    			"maxPlayers": 5,
    			"minPlayers": 5,
    			"number": 2
    		}
    	],
    	"playerAttributes": [
    		{
    			"name": "grade",
    			"type": "number"
    		},
    		{
    			"name": "elt",
    			"type": "number"
    		}
    	],
    	"rules": [
    		{
    			"type": "segment",
    			"expression": "teams[i].players.grade",
    			"value": [
    				[
    					1,
    					1
    				],
    				[
    					2,
    					3
    				],
    				[
    					4,
    					6
    				],
    				[
    					7,
    					9
    				]
    			]
    		},
    		{
    			"type": "deviation",
    			"expression": "avg(teams[*].players.elt)",
    			"value": 2
    		}
    	]
    }

### 答题游戏 3V3
- 组队条件：1 - 5级匹配、6 - 10级匹配、11 - 20级匹配、21 - 100级匹配。
- 对与对匹配：每个队伍积分属性平均误差值不得超过10。

示例代码如下：

    {
    	"version": "V1.0",
    	"teams": [
    		{
    			"name": "3v3",
    			"maxPlayers": 3,
    			"minPlayers": 3,
    			"number": 2
    		}
    	],
    	"playerAttributes": [
    		{
    			"name": "garde",
    			"type": "number",
    			"default": 0
    		},
    		{
    			"name": "score",
    			"type": "number",
    			"default": 0
    		}
    	],
    	"rules": [
    		{
    			"type": "segment",
    			"expression": "teams[i].players.garde",
    			"value": [
    				[
    					1,
    					5
    				],
    				[
    					6,
    					10
    				],
    				[
    					11,
    					20
    				],
    				[
    					21,
    					100
    				]
    			]
    		},
    		{
    			"type": "deviation",
    			"expression": "avg(teams[*].players.score)",
    			"value": 10
    		}
    	]
    }
