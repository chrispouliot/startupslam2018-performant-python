package main

import (
	"log"
	"net/http"
	"strconv"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	sleep, err := strconv.Atoi(r.URL.Path[1:])
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
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
