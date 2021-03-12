% FatosConhecimentos.

gerou(septimus, arthur).
gerou(cedrella, arthur).
gerou(prewett, molly).

gerou(molly, bill).
gerou(molly, percy).
gerou(molly, george).
gerou(molly, ron).
gerou(molly, bill).
gerou(molly, ginny).
gerou(arthur, bill).
gerou(arthur, percy).
gerou(arthur, george).
gerou(arthur, ron).
gerou(arthur, bill).
gerou(arthur, ginny).

gerou(bill, victoire).
gerou(bill, dominique).
gerou(bill, louis).
gerou(fleur, victoire).
gerou(fleur, dominique).
gerou(fleur, louis).
gerou(victoire, teddy).
gerou(percy, lucy).
gerou(percy, molly2).
gerou(audrey, lucy).
gerou(audrey, molly2).
gerou(george, fred2).
gerou(george, roxanne).
gerou(angelina, fred2).
gerou(angelina, roxanne).
gerou(ginny, james).
gerou(ginny, lily).
gerou(ginny, albus).
gerou(harry, james).
gerou(harry, lily).
gerou(harry, albus).
gerou(ron, hugo).
gerou(ron, rose).
gerou(hermione, hugo).
gerou(hermione, rose).

feminino(cedrella).
feminino(molly).
feminino(ginny).
feminino(fleur).
feminino(victoire).
feminino(dominique).
feminino(audrey).
feminino(lucy).
feminino(molly2).
feminino(angelina).
feminino(roxanne).
feminino(lily).
feminino(hermione).
feminino(rose).

masculino(septimus).
masculino(prewett).
masculino(arthur).
masculino(percy).
masculino(george).
masculino(ron).
masculino(bill).
masculino(louis).
masculino(teddy).
masculino(fred2).
masculino(harry).
masculino(james).
masculino(albus).
masculino(hugo).


% Regras.
progenitores(X, Y) :- gerou(X, Y).
pai(X, Y) :- gerou(X, Y), masculino(X).
mae(X, Y) :- gerou(X, Y), feminino(X).

filhos(X, Y) :- gerou(Y, X).
filho(X, Y) :- filhos(X, Y), masculino(X).
filha(X, Y) :- filhos(X, Y), feminino(X).

semelhantes(X, Y) :- gerou(Z, X), gerou(Z, Y), X \== Y.
irmaos(X, Y) :- semelhantes(Y, X), masculino(X).
irmas(X, Y) :- semelhantes(Y, X), feminino(X).

tios(X, Y) :- gerou(Z, X), gerou(Z, B), gerou(B, Y), masculino(X).
sobrinhos(X, Y) :- semelhantes(Z, Y), filhos(X, Z), masculino(X).

avos(X, Y) :- gerou(Z, Y), gerou(X, Z).
avoM(X, Y) :- avos(X, Y), masculino(X).
avoF(X, Y) :- avos(X, Y), feminino(X).
tioAvo(X, Y) :- semelhantes(X, A), avos(A, Y), masculino(X), X \== A.
tiaAvo(X, Y) :- semelhantes(X, A), avos(A, Y), feminino(X), X \== A.

% Testes.
% pai(X, ron). = arthur
% mae(X, ron). = molly
% filho(X, arthur). = bill, percy, george, ron
% filha(X, molly). = ginny
% irmaos(X, ron). = bill, percy, george, ron
% irmas(X, ron). = ginny
% tios(X, teddy). = louis
% sobrinhos(X, bill). = fred2, hugo, james, albus
% avoM(X, teddy). = bill
% avoF(X, teddy). = fleur
% tioAvo(X, teddy). = percy, george, ron
% tiaAvo(X, teddy). = ginny
