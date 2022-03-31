male(james).
male(charles).
male(george).
male(james).

female(catherine).
female(elizabeth).
female(sophia).

mother(catherine,charles).
mother(catherine,george).
mother(catherine,elizabeth).

sister(catherine,sophia).

partner(james,catherine).


is_father(X,Y):- male(X),partner(X,Z),mother(Z,Y).

is_mother(X,Y):- mother(X,Y).

is_sister(X,Y):- sister(X,Y); (female(X), mother(Z,X),mother(Z,Y)).

is_brother(X,Y):- male(X), mother(Z,X), mother(Z,Y).

is_aunty(X,Y):- female(X), sister(Z,X), mother(Z,Y).


