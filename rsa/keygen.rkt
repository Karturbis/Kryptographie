#lang racket
(require "primegen.rkt")


(define (mult-inv a b s1 s2); calculates the multiplicative inverse with a stripped down version of the extended euclidean algorithm
  (if (= b 0)
      (cons a s1); returns a pair, with the gcd of a and b as first element and multiplicative inverse of a modulo b as second element
      (mult-inv; call function gcde recursive
       b; parameter a
       (modulo a b); parameter b
       s2; parameter s1
       (- s1 (* (floor (/ a b)) s2)); parameter s2
      )
  )
)

(define (mult-inv-init a b); initiates the mult-inv function, to calculate the multiplicative inverse of a modulo b
  (mult-inv a b 1 0)
)

(define (gcd a b); calculates the greatest common divisor between a and b with the euclidean algorythm
  (if (= b 0)
      a
   (gcd b (modulo a b))
  )
)

(define (gen-p); function to generate p
  (define prime (gen-prime))
  (if (= (gcd e (- prime 1)) 1); if gcd of e and p-1 ist no 1, restart
      prime
      (gen-p)
  )
)

(define (gen-q); function top generate q
  (define qrime (gen-p)); uses gen-p
  (if (= qrime p); checks if q = p, if yes restart
      (gen-q)
      qrime
  )
)


(define e (random; since rackets random implementation does not accept min and max value to be further apart than 4294967087 this is not entirely safe
           (-
            (expt 2 64); if e > 2^64 the rsa method is vulnerable to chain breaking algorythms, so this is the biggest safe boundrary for e
            4294967087
           )
           (expt 2 64)
          )
)
(define p (gen-p))
(define q (gen-q))
(define N (* p q))
(define phi-N
  (*
   (- p 1)
   (- q 1)
  )
)
(define d (cdr (mult-inv-init e phi-N)))


(define (gen-key modus)
  (if (equal? modus "private")
      (cons d N)
      (cons e N)
  )
)




  