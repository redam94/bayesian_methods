### Rules of Probability
Pretty much all you need to know will follow from the following rules.

- **Sum Rule**: $P(A) = P(A, B) + P(A, \neg B)$
- **Product Rule**: $P(A, B) = P(B|A)P(A) = P(A|B)P(B)$
- **Law of Total Probability**: $P(X)=\sum^n_{i=1}P(X|A_i)P(A_i)$
- **Bayes' Theorem**: $P(A|B)=\frac{P(A)P(B|A)}{P(B)}$

### Bayes' Theorem

Let $A_1 + A_2 + … + A_n = E$ and $A_i\cap A_j = \varnothing$ if $i\ne j$. Then, for any $X\in \mathfrak{F}$,
$$
P(A_i|X)=\frac{P(A_i)P(X|A_i)}{\sum^n_{j=1}P(A_j)P(X|A_j)}
$$

