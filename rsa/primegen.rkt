#lang racket
(require math); imports the math library, which includes random-prime generation
(provide gen-prime); provides the method gen-prime to other modules

;#####################################################################################
;##### Input Section #################################################################
(define min (expt 2 512)); change this, to change the minimum of the prime number. ##
(define max (expt 2 616)); change this, to change the maximum of the prime number. ##
;#####################################################################################
;#####################################################################################

(define (gen-prime); generates a random prime between min and max
  (define randomprime (random-prime max)); generates a random prime smaller than max
  (if (< randomprime min); checks if prime is smaller than min
      (gen-prime); if yes, start the process over again
      randomprime; if no, returns the prime
  )
)

