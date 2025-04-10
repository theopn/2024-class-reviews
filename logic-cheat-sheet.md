# Logic Cheat Sheet

## Propositional Logic

|     |     | Negation | Conjunction | Disjunction | XOR          | Implication       | Biconditional         |
|-    | -   |----------|-------------|-------------|--------------|-------------------|-----------------------|
| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$  | $p \oplus q$ | $p \rightarrow q$ | $p \leftrightarrow q$ |
| T   | T   | F        | T           | T           | F            | T                 | T                     |
| T   | F   | F        | F           | T           | T            | F                 | F                     |
| F   | T   | T        | F           | T           | T            | T                 | F                     |
| F   | F   | T        | F           | F           | F            | T                 | T                     |


Precedence:

1. $\neg$
2. $\land$, $\lor$
3. $\rightarrow$, $\leftrightarrow$

Important equivalences:

| Eqivalence                                                                                                               | Name                |
| -                                                                                                                        | -                   |
| $p \land T \equiv p$ <br /> $p \lor F \equiv p$                                                                          | Identity Laws       |
| $p \lor T \equiv T$ <br /> $p \land F \equiv F$                                                                          | Domination Laws     |
| $p \lor p \equiv p$ <br /> $p \land p \equiv p$                                                                         | Idempotent Laws     |
| $\neg ( \neg p ) \equiv p$                                                                                               | Double negation law |
| $p \lor q \equiv q \lor p$ <br /> $p \land q \equiv q \land p$                                                           | Commutative laws    |
| $p \lor (q \lor r) \equiv (p \lor q) \lor r$ <br /> $p \land (q \land r) \equiv (p \land q) \land r$                     | Associative laws    |
| $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ <br /> $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$  | Distributive laws   |
| $\neg (p \land q) \equiv \neg p \lor \neg q$ <br /> $\neg (p \lor q) \equiv \neg p \land \neg q$                         | De Morgan’s laws    |
| $p \lor (p \land q) \equiv p$ <br /> $p \land (p \lor q) \equiv p$                                                       | Absorption laws     |
| $p \lor \neg p \equiv T$ <br /> $p \land \neg p \equiv F$                                                                | Negation laws       |


- Logical equivalences involving $\rightarrow$
    - $p \rightarrow q \equiv \neg p \lor q$
    - $p \rightarrow q \equiv \neg q \rightarrow \neg p$
    - $p \lor q \equiv \neg p \rightarrow q$
    - $p \land q \equiv \neg (p \rightarrow \neg q)$
    - $\neg (p \rightarrow q) \equiv p \land \neg q$
    - $(p \rightarrow q) \land (p \rightarrow r) \equiv p \rightarrow (q \land r)$
    - $(p \rightarrow r) \land (q \rightarrow r) \equiv (p \lor q) \rightarrow r$
    - $(p \rightarrow q) \lor (p \rightarrow r) \equiv p \rightarrow (q \lor r)$
    - $(p \rightarrow q) \lor (q \rightarrow r) \equiv (p \land q) \rightarrow r$

- Logical equivalences involving $\leftrightarrow$
    - $p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$
    - $p \leftrightarrow q \equiv \neg p \leftrightarrow \neg q$
    - $p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)$
    - $\neg (p \leftrightarrow q) \equiv p \leftrightarrow \neg q$

Extended De Morgan's Law

$\neg (p_1 \lor p_2 \lor \dots \lor p_n) \equiv (\neg p_1 \land \neg p_2 \land \dots \land \neg p_n)$

or

$\neg (\bigvee_{j = 1}^{n} p_j) \equiv \bigwedge_{j = 1}^{n} \neg p_j$

Similarly,
$\neg (\bigwedge_{j = 1}^{n} p_j) \equiv \bigvee_{j = 1}^{n} \neg p_j$

## Predicates and Quantifiers

| Statement       | When T?                               | When F?                               |
| -               | -                                     | -                                     |
| $\forall P(x)$  | Trivial                               | There is an $x$ where $P(x) \equiv F$ |
| $\exists  P(x)$ | There is an $x$ where $P(x) \equiv F$ | Trivial                               |

Distribution:

- $\forall (P(x) \land Q(x)) \equiv \forall P(x) \land \forall Q(x)$
- $\exists (P(x) \lor Q(x)) \equiv \exists P(x) \lor \exists Q(x)$
- We cannot distribute $\forall$ over $\lor$ nor can we distribute $\exists$ over $\land$

De Morgan's Laws for quantifiers:


| Statement                                    | When T?                               | When F?                               |
| -                                            | -                                     | -                                     |
| $\neg \exists P(x) \equiv \forall \neg P(x)$ | Trivial                               | There is an $x$ where $P(x) \equiv T$ |
| $\neg \forall P(x) \equiv \exists \neg P(x)$ | There is an $x$ where $P(x) \equiv F$ | Trivial                               |

Nested qualtifiers:


| Statement                                                          | When T?                                                     | When F?                                                    |
| -                                                                  | -                                                           | -                                                          |
| $\forall_x \forall_y P(x, y)$ <br /> $\forall_y \forall_x P(x, y)$ | Trivial                                                     | There is a pair $(x, y)$ where $P(x, y) \equiv F$          |
| $\forall_x \exists_y P(x, y)$                                      | For every $x$, there is a $y$ where $P(x, y)  \equiv T$     | There is an $x$ such that $P(x, y) \equiv F$ for every $y$ |
| $\exists_x \forall_y P(x,y)$                                       | There is an $x$ for which $P(x, y) \ equiv T$ for every $y$ | For every $x$, there is a $y$ for which $P(x, y) \equiv F$ |
| $\exists_x \exists_y P(x, y)$ <br /> $\exists_y \exists_x P(x, y)$ | There is a pair $(x,y)$ where $P(x, y) \equiv T$            | Trivial                                                    |

## Rules of inference

| Rules of Inference (in the form of tautology)                               | Name                   |
| -                                                                           | -                      |
| $(p \land (p \rightarrow q)) \rightarrow q$                                 | Modus Ponens           |
| $(\neg q \land (p \rightarrow q)) \rightarrow \neg p$                       | Podus Tollens          |
| $((p \rightarrow q) \land (q \rightarrow r)) \rightarrow (p \rightarrow r)$ | Hypothetical Syllogism |
| $((p \lor q) \land \neg p) \rightarrow q$                                   | Disjunctive Syllogism  |
| $p \rightarrow (p \lor q)$                                                  | Addition               |
| $(p \land q) \rightarrow p$                                                 | Simplification         |
| $((p) \land (q)) \rightarrow (p \land q)$                                   | Conjunction            |
| $((p \lor q) \land (\neg p \lor r)) \rightarrow (q \lor r)$                 | Resolution             |


For quantifiers

| Rules of Inference (in the form of tautology)                  | Name                       |
| -                                                              | -                          |
| $\forall_x P(x)$ <br /> $\therefore P(x)$                      | Universal instantiation    |
| $P(c)$ for an arbitrary $c$ <br /> $\therefore \forall_x P(x)$ | Universal generalization   |
| $\exists_x P(x)$ <br /> $P(c)$ for an arbitrary $c$            | Existential instantiation  |
| $P(c)$ for some element $c$ <br /> $\therefore \exists_x P(x)$ | Existential generalization |

