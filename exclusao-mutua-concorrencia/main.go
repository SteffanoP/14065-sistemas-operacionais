package main

import (
	"fmt"
	"strconv"
	"time"
)

type Buffer struct {
	acumulador_critico     int
	acumulador_nao_critico int
	buffer                 string
	tamanho, capacidade    int
}

const TAMANHO_INICIAL = 0
const CAPACIDADE = 100

var lock chan int = make(chan int, 1)

func threadInserir(buf *Buffer, c string) {
	for i := 0; i < 500; i++ {
		inserir(buf, c)
		time.Sleep(50 * time.Millisecond)
	}
}

func inserir(buf *Buffer, c string) {
	acumulador_nao_critico, _ := strconv.Atoi(c)
	buf.acumulador_nao_critico += acumulador_nao_critico
	lock <- 0
	if buf.tamanho < buf.capacidade {
		buf.buffer = buf.buffer + c
		acumulador_critico, _ := strconv.Atoi(c)
		buf.acumulador_critico = buf.acumulador_critico + acumulador_critico
		buf.tamanho++
		<-lock
	} else {
		<-lock
		pausa()
	}
}

func esvaziar(buf *Buffer) (string, int, int) {
	for buf.tamanho < buf.capacidade {
		pausa()
	}
	lock <- 1
	buf.tamanho = 0
	resultado := buf.buffer
	acumulador_critico := buf.acumulador_critico
	acumulador_nao_critico := buf.acumulador_nao_critico
	buf.buffer = ""
	buf.acumulador_critico = 0
	buf.acumulador_nao_critico = 0
	<-lock
	return resultado, acumulador_critico, acumulador_nao_critico
}

func pausa() {
	time.Sleep(100 * time.Millisecond)
}

func main() {
	var buffer = Buffer{0, 0, "", TAMANHO_INICIAL, CAPACIDADE}
	go threadInserir(&buffer, "1")
	go threadInserir(&buffer, "2")
	go threadInserir(&buffer, "3")
	go threadInserir(&buffer, "4")
	go threadInserir(&buffer, "5")

	for i := 0; i < 10; i++ {
		resultado, acumulador_critico, acumulador_nao_critico := esvaziar(&buffer)

		fmt.Printf("\n\nImpressao # %v:\n Buffer = %s -> Tamanho: %v\n Acumulador crítico = %v\n Acumulador não crítico = %v", (i + 1), resultado, len(resultado), acumulador_critico, acumulador_nao_critico)
	}

	fmt.Println("\n\nMain terminou.")
}
