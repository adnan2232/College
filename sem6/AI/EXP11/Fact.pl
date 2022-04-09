factorial(1,X):- X is 1.
factorial(N,X) :- N1 is N-1, factorial(N1,X1),X is N*X1.
