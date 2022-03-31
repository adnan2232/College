/*Without Cut*/

maximum(X,Y,Z):- (X>=Y-> Z=X; Z=Y).

minimum(X,Y,Z):- (X>=Y-> Z=Y; Z=X).

/*With Cut*/

max_cut(X,Y,Max):- X>=Y,!,Max=X; Max=Y.

min_cut(X,Y,Min):- X>=Y,!,Min=Y; Min=X.

