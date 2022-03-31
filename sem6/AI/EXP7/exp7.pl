mouse(jerry).
cat(tom).
search_for_food(tom).
hungry(X):- search_for_food(X).
will_eat(X,Y):- cat(X),hungry(X),mouse(Y).


play(jack,cricket).
play(billi,cricket).
friends(X,Y):- play(X,Z),play(Y,Z).

eat(kunal,pasta).
loves_to_eat(X,Y):- eat(X,Y).

dances(lili).
happy(X):- dances(X).

is_Closed(school).
free(ryan).

goToPlay(X):- is_Closed(school),free(X).

