#lang racket
(provide string-encode string-decode)

(define (string-decode input)
  (string-decode-inner (number->string input) "" 0)
)


(define (string-decode-inner input output i)
  (if (>= i (string-length input))
          output
          (string-decode-inner input; the input parameter
                               (string-append; begin of the output parameter
                               output
                                (string
                                 (integer->char
                                  (string->number
                                   (substring
                                    input
                                    (add1 i)
                                    (+ i 1
                                       (string->number
                                        (string
                                         (string-ref input i)
                                        )
                                       )
                                    )
                                   )
                                  )
                                 )
                                )
                               ); end of the output parameter
                               (+ i 1
                                  (string->number
                                   (string
                                    (string-ref input i)
                                   )
                                  )
                               )
           )
  )
)
  



(define (string-encode input)
  (string-encode-inner (string->list input) "" 0)
)

(define (string-encode-inner input output i)
  (if (>= i (length input))
  (string->number output)
  (string-encode-inner input; the input parameter
     (string-append output
                    (string-append
                     (number->string
                      (string-length
                       (number->string
                        (char->integer
                         (list-ref input i)
                        )
                       )
                      )
                     )
                     (number->string
                       (char->integer
                        (list-ref input i)
                       )
                     )
                    )
     ); the output parameter
     (+ i 1); the iterator (i) parameter
   )
  )
)