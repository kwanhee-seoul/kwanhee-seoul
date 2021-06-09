package main

import "fmt"

func main() {
	names := [3]string{"kwanhee", "sujin", "sangwoo"}
	names[1] = "juhye"
	fmt.Println(names)
}
