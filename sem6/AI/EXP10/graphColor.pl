color(1,red,a).
color(2,blue,a).
color(3,green,a).
color(4,yellow,a).
color(5,blue,a).
color(1,red,b).
color(2,blue,b).
color(3,green,b).
color(4,yellow,b).
color(5,blue,b).

adj(1,2).
adj(1,3).
adj(1,4).
adj(1,5).
adj(2,3).
adj(2,4).
adj(3,5).
adj(4,5).


adjacent(X,Y) :- adj(X,Y);adj(Y,X).

conflict(Z):- adjacent(X,Y),color(X,K,Z),color(Y,K,Z), write(X),write('->'),write(Y),writeln(' conflict').


