### Rules of Probability
Pretty much all you need to know will follow from the following rules.

- **Sum Rule**: $P(A) = P(A, B) + P(A, \neg B)$
- **Product Rule**: $P(A, B) = P(B|A)P(A) = P(A|B)P(B)$
- **Law of Total Probability**: $P(X)=\sum^n_{i=1}P(X|A_i)P(A_i)$
- **Bayes' Theorem**: $P(A|B)=\frac{P(A)P(B|A)}{P(B)}$

### The Jargon
- $P(X|D)$ is the posterior for X give D
- $P(X)$ is the prior for X
- $P(D|X)$ is the likelihood of $X$
- $P(D)$ is the evidence for the model
  - $P(D) = \sum_{x\in\chi}P(D|x)P(x)$


### Bayes' Theorem

Let $A_1 + A_2 + … + A_n = E$ and $A_i\cap A_j = \varnothing$ if $i\ne j$. Then, for any $X\in \mathfrak{F}$,
$$
P(A_i|X)=\frac{P(A_i)P(X|A_i)}{\sum^n_{j=1}P(A_j)P(X|A_j)}
$$


### Real World Example

FDA released antibody test for corona virus. 
This was sent to a large number of people to test wether 
they had already had and recovered from the coronavirus. 
The tests have a sensitivity ($P(T|C)$) of 0.938 and a specificity ($P(\neg T|\neg C)$) of 0.96.
Lets say that the general prevelance of Covid-19 ($P(C)$) was <<varc>>.
You take the test and it comes out positive. How do you interperet this result?
How do you update your previous belief? Use Bayes' theorem!

$$
P(T|C)=0.938 \ \ \ \ P(\neg T|\neg C)=0.96\\ \ \ \\ \begin{align} P(C|T) &= \frac{P(T|C)P(C)}{P(T|C)P(C) + P(T|\neg C)P(\neg C)} \\ &= \frac{P(T|C)P(C)}{P(T|C)P(C)+(1-P(\neg T| \neg C))(1-P(C))} \\ &= \frac{0.938 \cdot P(C)}{0.938P(C) + 0.04(1-P(C))}\end{align}\\ \ \\ P(C) = <<varc>> \rightarrow P(C|T)= <<varc|t>>
$$



