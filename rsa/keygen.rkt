#lang racket
(require "primegen.rkt")
(provide gen-key)

(define p-min (expt 2 512))
(define p-max (expt 2 513))
(define e-min (expt 2 32))
(define e-max (expt 2 33))

(define (mult-inv b-const a b s1 s2); calculates the multiplicative inverse with a stripped down version of the extended euclidean algorithm
  (if (= b 0)
      (if (< s1 1)
          (cons a (+ b-const s1))
          (cons a s1); returns a pair, with the gcd of a and b as first element and multiplicative inverse of a modulo b as second element
       )
       (mult-inv; call function mult-inv recursive
        b-const
        b; parameter a
        (modulo a b); parameter b
        s2; parameter s1
        (- s1 (* (floor (/ a b)) s2)); parameter s2
       )
  )
)

(define (mult-inv-init a b); initiates the mult-inv function, to calculate the multiplicative inverse of a modulo b
  (mult-inv b a b 1 0)
)

(define (gcd a b); calculates the greatest common divisor between a and b with the euclidean algorythm
  (if (= b 0)
      a
   (gcd b (modulo a b))
  )
)

(define (gen-q p-min p-max); function top generate q
  (define qrime (gen-prime p-min p-max)); uses gen-p
  (define thelogpq
    (abs
     (-
      (log p 2)
      (log qrime 2)
     )
    )
  )
  (if (and (< 0.1 thelogpq)
           (> 30 thelogpq)
      ); avoid p and q being equal or to close
      (gen-q p-min p-max)
      qrime
  )
)

; define the variables that are neede for the key generation:

(define e 
  (gen-prime e-min e-max)
)
(define p (gen-prime p-min p-max))
(define q (gen-q p-min p-max))
(define N (* p q))
; using shortcut to the euclidean phi function
(define phi-N
  (*
   (- p 1)
   (- q 1)
  )
)
(define d (cdr (mult-inv-init e phi-N)))

; method, that is provided to other parts of the package:
(define (gen-key [private #f])
  (if private
      (cons d N)
      (cons e N)
  )
)




  