#lang racket
(require "keygen.rkt")
(provide verschluesseln entschluesseln)

(define N (cdr (gen-key)))
(define e (car (gen-key)))
(define d (car (gen-key #t)))



(define (verschluesseln m e N)
  (mod-exp m (base2 e) N))

(define (entschluesseln c d N)
  (mod-exp c (base2 d) N))


(define (base2 n)
  (if (< n 2)
      (list n)
      (append (base2 (floor (/ n 2)))
              (list (remainder n 2)))))

(define (mod-exp b e m) ; Berechnet b^e modulo m
  (mod-exp-inner 1 b (reverse e) m 0))


(define (mod-exp-inner R x e m a)
  (if (<= (length e) a)
  R   
  (mod-exp-inner (modulo
                  (* R
                     (expt x
                           (list-ref e a)
                     )
                  )
                 m)
                 (modulo (expt x 2) m) e m (+ a 1)
  )
   
  )
)
  
  