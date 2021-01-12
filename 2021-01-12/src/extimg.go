package main

import (
	"fmt"
	"io/ioutil"
	"log"

	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
)

func main() {
	dsn := "isucon:isucon@tcp(localhost:3306)/isubata?charset=utf8mb4&parseTime=true&loc=Local"
	db, err := sqlx.Connect("mysql", dsn)
	if err != nil {
		log.Fatalf("Failed to connect to DB: %s", err.Error())
	}
	defer db.Close()

	rows, err := db.Query("SELECT `name`, `data` FROM image")
	if err != nil {
		log.Fatalf(err.Error())
	}
	defer rows.Close()

	var name string
	var data []byte
	for rows.Next() {
		err2 := roes.Scan(&name, &data)
		if err2 != nil {
			log.Fatalf(err2.Error())
		}
		fmt.Println(name)
		err3 := ioutil.WriteFile(name, data, 0666)
		if err3 != nil {
			log.Fatalf(err3.Error())
		}
	}
}
