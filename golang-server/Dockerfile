FROM golang:latest 
RUN mkdir /cmd
ADD . /cmd
WORKDIR /cmd/cmd/main
RUN go build -o main . 
CMD ["/cmd/cmd/main/main"]