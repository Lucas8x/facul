% Exercicio 03 - Regras e Fatos.
% Lucas Emanuel

% Parte 1
cursa(lucas, algoritmos).
cursa(flavio, web).
cursa(tarcisio, sia).
ensina(pedro, sia).
ensina(carlos, algoritmos).
ensina(sandney, web).

% Regras.
e_professor(X, ALUNO) :- cursa(ALUNO, MATERIA),ensina(X, MATERIA).
esta_cursando(ALUNO, MATERIA) :- cursa(ALUNO, MATERIA).

% Testes.
% e_professor(X, lucas).
% esta_cursando(lucas, algoritmos).


% Parte 2
a_direita_de(flavio, lucas).
a_direita_de(tarcisio, flavio).
a_direita_de(gabriel , tarcisio).
a_direita_de(fabiano , gabriel).
a_direita_de(bryan, fabiano).

% Regras.
a_esquerda_de(X, Y) :- a_direita_de(Y,X).
sao_vizinhos_de(ESQ, DIR, MEIO) :- a_esquerda_de(ESQ, MEIO),a_direita_de(DIR, MEIO).
adjacente(X, Y) :- a_direita_de(X, Y);a_esquerda_de(X, Y).

% Testes.
% a_esquerda_de(lucas, flavio).
% sao_vizinhos_de(lucas, tarcisio, flavio).
% adjacente(flavio, tarcisio).
% adjacente(tarcisio, flavio).
