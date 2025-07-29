:- discontiguous pai/2.
:- discontiguous mae/2.

% Base de dados
pai(joao, pedro).
pai(pedro, ana).
mae(maria, pedro).
mae(ana_clara, ana).

homem(joao).
homem(pedro).
mulher(maria).
mulher(ana_clara).
mulher(ana).

% Regras do problema

filho(X, Y) :- pai(Y, X).
filho(X, Y) :- mae(Y, X).

avo(X, Z) :- pai(X, Y), pai(Y, Z).
avo(X, Z) :- pai(X, Y), mae(Y, Z).

irmao(X, Y) :- pai(P, X), pai(P, Y), mae(M, X), mae(M, Y), X \= Y.