#lang racket
(require "keygen.rkt"); import the keys from keygen.txt

(define (encrypt e N message)
  (mod-exp message e N)
)

(define (decrypt d N chiffre)
  (mod-exp chiffre d N)
)


(define (integer->bitlist a)
   (string->list
    (number->string a 2)
   )
)

(define (mod-exp b e m)
  (mod-exp-inner 1 b (reverse (integer->bitlist e)) m 0)
)

(define (mod-exp-inner r x e m i)
  (if (>= i (length e))
      r
      (mod-exp-inner
       (modulo
        (* r (expt
              x
              (- (char->integer (list-ref e i)) 48); to convert from ascii number to real number
             )
         )
        m; the modulus
        ); this is the r parameter of recursive call
       (modulo
        (expt x 2)
        m
       )
       e
       m
       (+ i 1)
      )
   )
)