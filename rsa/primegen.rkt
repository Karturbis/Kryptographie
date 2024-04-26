#lang racket
(require math); imports the math library, which includes random-prime generation
(provide gen-prime); provides the method gen-prime to other modules

(define (gen-prime min max); generates a random prime between min and max
  (define randomprime (random-prime max)); generates a random prime smaller than max
  (if (< randomprime min); checks if prime is smaller than min
      (gen-prime min max); if yes, start the process over again
      randomprime; if no, returns the prime
  )
)

