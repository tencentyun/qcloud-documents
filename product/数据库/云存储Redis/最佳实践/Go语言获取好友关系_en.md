 
```
package main

import (
	"fmt"
	"github.com/garyburd/redigo/redis"
)

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	redisServer := "localhost:6379"
	client, err := redis.Dial("tcp", redisServer)
	checkErr(err)
	defer client.Close()
	//my friends
	client.Do("SADD", "myfriends", "John")
	client.Do("SADD", "myfriends", "Emily")
	client.Do("SADD", "myfriends", "Ben")
	client.Do("SADD", "myfriends", "Steven")
	fmt.Println("my friends are: ")
	myList, err := redis.Strings(client.Do("SMEMBERS", "myfriends"))
	checkErr(err)
	for _, item := range myList {
		fmt.Print(item + " ")
	}
	fmt.Println()
	//your friends
	client.Do("SADD", "yourfriends", "Mark")
	client.Do("SADD", "yourfriends", "Tim")
	client.Do("SADD", "yourfriends", "Willim")
	client.Do("SADD", "yourfriends", "Ben")
	client.Do("SADD", "yourfriends", "Steven")
	fmt.Println("your friends are: ")
	youList, err := redis.Strings(client.Do("SMEMBERS", "yourfriends"))
	checkErr(err)
	for _, item := range youList {
		fmt.Print(item + " ")
	}
	fmt.Println()
	fmt.Println("our common friends are: ")
	commonList, err := redis.Strings(client.Do("SINTER", "myfriends", "yourfriends"))
	checkErr(err)
	for _, item := range commonList {
		fmt.Print(item + " ")
	}
	fmt.Println()
}
```
The result is as follows:
![](https://mc.qcloudimg.com/static/img/6119908db94734b6b398075da64ef2d4/image.png)
