# CI2024_project-work
The project has been developed in collaboration with Federico Fortunati and Yuri Pettorossi.
### Introduction

The goal of the project has been the development of a symbolic regression to extract a formula that best represents the distribution of 8 datasets. This project has been done in collaboration with Federico Fortunati and Yuri Pettorossi.

### Methodology
In order to accomplish this task, we have implemented a genetic programming algorithm which returns a formula as a combination of different operators and constants . The formula is obtained through a series of Permutations and Crossovers. The algorithm is interrupted when a target number of generations is reached. The best candidate is obtained as the candidate with the lowest MSE. Each candidate is represented as a tree data structure. Each node can represent either an operator or a constant.

### Operators

The following is the list of operators implemented 
1. Addition
2. Subtraction
3. Arctangent
4. Multiplication
5. Division
6. Power
7. Square Root
8. Cube Root
9. Logarithm
10. Sine
11. Hyperbolic Cosine
12. Hyperbolic Sine
13. Hyperbolic Tangent
14. Cosine
15. Exponential
16. Absolute Value

### Initialization

The algorithm is initialized through the ramped half-and-half method, which consists in generating initial candidate trees through two modalities:
Full method, where each branch has dept = Dmax. Nodes at depth d< Dmax are randomly chosen from the function set F. Nodes at depth d= Dmax are randomly chosen from the terminal set T.
Grow method, where each branch has dept <= Dmax. Nodes at depth d< Dmax are randomly chosen from F U T. Nodes at depth d= Dmax are randomly chosen from the terminal set T.
Each candidate has a fixed probability of 50% of being generated either by the Full method or Grow Method.

### Mutations

Mutations are applied with a low probability . The following is the list of possible mutations:
- Ephemeral Random Constants: mutation applied to constants. It substitutes the current value with a random one within a fixed range.
- Point Mutations: Mutation applied to operators and variables. The node is substituted respectively with a randomly chosen operator and variable.
- Mutate all tree: mutation applied on the candidate level. It substitutes a candidate with a newly generated one.

### Crossover

- Swap trees with random height
- Swap trees with similar height 
  
### Evolution strategy

The genetic programming algorithm is developed as follow:
1. Initialize the Population The algorithm begins by creating an initial population of candidate solutions (functions).
Each candidate is generated using generate_candidate(MAX_DEPTH, features).
Only valid candidates are added to the population. A candidate is valid if:
- It produces a valid output when evaluated (evaluate_function(candidate, data) is not None).
- It contains all required variables (features).
2. Evolution over generations. This step is articulated as follow:
   1. Parent selection through tournament selection.
   2. Offspring generation through Crossover or Mutation
   3. Merge Offspring with parents
   4. Select top candidates with lowest MSE through fitness proportional method.
In order to stay consistent with the traditional implementation of genetic programming, we have implemented mutation with a low probability. This means that the algorithm needs a consistent amount of candidates to ensure diversity among the candidates, which is vital to minimize the risk of converging to local optima due to lack of genotype diversity.
