package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

type message struct {
	Message string `json:"message"`
}

var m = message{Message: "Hello World"}

func get(c *gin.Context) {
	fmt.Println(m)
	c.IndentedJSON(200, m)
}

func main() {
	r := gin.Default()
	r.GET("/get", get)
	r.Run(":8080")
}
