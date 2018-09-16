package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Path[1:]
	log.Println(fmt.Sprintf("Got path of '%s'", path))
	sleep, err := strconv.Atoi(path)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(fmt.Sprintf("Invalid delay: %s", path)))
		return
	}
	time.Sleep(time.Millisecond * time.Duration(sleep))

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Here is some data"))
}

func main() {
	http.HandleFunc("/", handler)
	log.Println("Running server..")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
