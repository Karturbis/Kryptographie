#lang racket
;(require "keygen.rkt"); import the keys from keygen.txt

(define (encrypt e N message)
  (modulo
   (expt message e)
   N
  )
)

(define (decrypt d N chiffre)
  (modulo
   (expt chiffre d)
   N
  )
)