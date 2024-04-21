# Bayesian Methods

## Modeling Considerations

When we model we often have a priori knowledge, or beliefs, about the system we are modeling.
These beliefs place reasonable contraints on what we would consider plausible 
without significant evidence to the contrary.

<img src="https://imgs.xkcd.com/comics/frequentists_vs_bayesians_2x.png" alt="Did the sun just explode?" width="300"/>

In our modeling experience, for example, we might have the belief that
the effects of marketing are positive or at worst zero but not negative. 
How would we encode this belief in a statistical model? 
How should we update our beliefs after we gather more data?

Notes from Lecture 1 Probabilistic ML class of 
Prof. Dr. Philipp Hennig in the Summer Term 2020 at the University of Tübingen 
https://youtu.be/M2fUmhGTNrQ
## Measurable Space
$E \in \mathfrak{F}$ where $E$ is a space of elementary events. We consider the
power set $2^E$, and let $\mathfrak{F}\subset 2^E$ be a set of subsets of $\Omega$. 
If $\mathfrak{F}$ satisfies the following properties, it is called a $\sigma$-algebra:
1. $A, B \in \mathfrak{F} \implies A-B \in \mathfrak{F}$
2. $A_1, A_2, ... \in \mathfrak{F} \implies (\bigcup^\infty_{i=1}A_i \in \mathfrak{F} \ \ \wedge \ \ \bigcap^\infty_{i=1} A_i \in \mathfrak{F})$
 (allow a countable but unbounded field of sets)
 
(Implies $\emptyset \in \mathfrak{F}$. If $E$ is countable then $2^E$ is a $\sigma$-algebra). 
If $\mathfrak{F}$ is a $\sigma$-algebra, then $(E, \mathfrak{F})$ is a measurable space (**Borel space**).

In plain english, a $\sigma$-algebra is a set of sets that is closed under 
countable unions and intersections. If we have a set of events, say for a coin flip. $E=\{H, T\}$ 
the $\sigma$-algebra $2^E$ would be $\{\emptyset, \{H\}, \{T\}, \{H, T\}\}$.
Lets check a few of the properties:
1. $\{H, T\}-\{T\} = \{H\} \in 2^E$
2. $\{H\}, \{T\} \in 2^E \implies \{H\} \cup \{T\} = \{H, T\} \in 2^E$
 
Note: No mention of probability yet. This is just a set of sets.

## Measures and Probability
Let ($\Omega$, $\mathfrak{F}$) be a measurable space. A nonnegative real function 
$P: \mathfrak{F} \rightarrow \mathbb{R}_{0,+}$ is called a **measure** if it satifies:
1. $P(\emptyset) = 0$
2. For any countable sequence $\{A_i\in\mathfrak{F}\}_{i=1,…}$ of pairwise disjoint sets 
($A_i\cap A_j = \varnothing$ if $i \neq j$), P satisfies countable additivity (aka. $\sigma$-additivity):
$$
P(\bigcup^\infty_{i=1}A_i) = \sum^\infty_{i=1}P(A_i)
$$

The measure $P$ is called a **probability measure** if $P(\Omega) = 1$. 
Then $(\Omega, \mathfrak{F}, P)$ is called a **probability space**.

In plain english, a measure is a function that assigns a non-negative real number 
to a set of events. From the previous example take $\Omega = \{H, T\}$ and $\mathfrak{F} = 2^\Omega$ and $P(\{H\}) = a$ and $P(\{T\}) = 1-a$ where $a\in[0, 1]$.
From 2. we have $P(\Omega) = P(\{H, T\}) = P(\{H\}\bigcup\{T\}) = P(\{H\}) + P(\{T\}) = a + 1 - a = 1$. Then $(\Omega, \mathfrak{F}, P)$ is a probability space!
### Theorem: Sum Rule
From $A+\neg A = E$ (binary outcomes)
$$
\begin{align}
P(A) + P(\neg A) &= P(E) = 1 
\\ P(A) &= 1-P(\neg A) 
\end{align}
$$
From $A = A \cap (B + \neg B)$, using the notation $P(A, B)$ for $P(A \cap B)$ for the 
**joint probability** of A and B we get the sum rule:
$$
P(A) = P(A, B) + P(A, \neg B)
$$
The sum rule allows for the elimination of variables that are summed over.
### Definition: Conditional Probability
If $P(A) > 0$ then the **conditional probability** of B given A is defined as:
$$
P(B|A) = \frac{P(A, B)}{P(A)}
$$
From the definition of conditional probability we can immediately see that:
$$
P(A, B) = P(B|A)P(A) = P(A|B)P(B)
$$
It is then easy to show that $P(B|A)\ge 0$, $P(E|A) = 1$, and that for
$B\cap C = \emptyset$ $P(B+C|A) = P(B|A) + P(C|A)$. Thus, for a fixed $A$, 
$(E, \mathfrak{F}, P(\bullet|A))$ is a probability space.
### Theorem: Law of Total Probability
Let $A_1 + A_2 + … + A_n = E$ and 
$A_i\cap A_j = \varnothing$ if $i\ne j$. Then, for any $X\in \mathfrak{F}$, 
$$
P(X)=\sum^n_{i=1}P(X|A_i)P(A_i)
$$

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

