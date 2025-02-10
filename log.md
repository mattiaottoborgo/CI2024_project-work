This is my log for what concern my activities during the semester:



## Labs

Delivered lab 0 on 24 Sept 2024
https://github.com/mattiaottoborgo/CI2024_lab0

Delivered lab 1 on 9 Oct 2024
https://github.com/mattiaottoborgo/CI2024_lab1

Delivered lab 2 on 1st November 2024
https://github.com/mattiaottoborgo/CI2024_lab2

Delivered lab 3 on 22nd November 2024
https://github.com/mattiaottoborgo/CI2024_lab3


## Peer Reviews
marioleonardo/CI2024_lab3 Review Lab3
#1 opened on Dec 1, 2024 by mattiaottoborgo
https://github.com/marioleonardo/CI2024_lab3/issues/1
Content:
The choice of implementing A* using Manhattan and Hamming distance is a good start to solving this problem. The code is understandable and clear about the implementation.
Nice the idea of the readme that gives an overview over the project. I would just clean it up a little and add some considerations about the results!.
To further improve the algorithm, I would suggest to improve a different heuristic, even though it is not trivial to find. In general you have done a good work!

Good Job!

AlesCarl/CI2024_lab2 Comment on Lab2
#1 opened on Nov 15, 2024 by mattiaottoborgo
https://github.com/AlesCarl/CI2024_lab2/issues/1
Content:
I liked your implementation fo simulated annealing. I find it very clean and smart. However, I noticed it didn't improve the solution proposed by the greedy algorithm. Here a couple of suggestions you might follow:
-Implementation of Evolutionary algorithm with genetic approach. I think this would help since you would handle multiple individuals, increasing your chances of reaching a good solution.
-Greedy solution as starting point. I think this would significantly improve results of your algorithm. It doesn't take much to retrieve, however it allows the algorithm to start the exploration phase from a much better result than a randomic one, increasing your chances of getting a good result. However I don't suggest to start from a population of just greedy solutions, as you might lack diversity. For this reason, I would suggest to start with a population of random individuals+ some greedy ones+ mechanism to preserve diversity.

MicheleCazzola/CI2024_lab2 Comment on lab 2
#1 opened on Nov 15, 2024 by mattiaottoborgo
https://github.com/MicheleCazzola/CI2024_lab2/issues/1
Content:
First of all, I want to say that your solution is really good! Clean and understandable implementation. The ReadME helped me a lot to understand your implementation.
I would like to make the following observation/suggestions to help to tackle the difficulties you pointed:
You mention that for the italian instance your algorithm seems to get stucked in a good solution and doesn't manage to further improve it. I think the problem might be diversity:
Your initialization technique is really good since it allows the algorithm to start from a solid base, however I think it might lack of diversity. If you think about it, the initial population, which is composed of individuals generated with greedy algorithm, will likely be composed of really similar individuals. I think you could try to implement some mechanism that generates just some individuals based on your greedy algorithm and the rest in a randomic way. I observed you have a similar setup when the initial population is less than the population size. This might be a good start, however it doesn't guarantee that, when the randomic individuals are far less than the greedy ones, they might survive enough to produce interesting results. To solve this, I would also implement some strategy such as "islands" to preserve such diversity.
In conclusion:
-Really good algorithm to start with

Try to add more random individuals and choose the strategy you prefer to preserve diversity!

GiorgioBongiovanni/CI2024_lab1 Review
#2 opened on Oct 22, 2024 by mattiaottoborgo
https://github.com/GiorgioBongiovanni/CI2024_lab1/issues/2
Content:
The code is well structured and divived into section, which helps the review to better examine the code.
I like the implementation of all the methods explained during lectures, which allowed me to understand better the pros and cons of each algorithm. The graphs are well done and help to understand the evolution of the algorithm.
Really good job!

MarilenaDel/CI2024_lab1 Review
#3 opened on Oct 22, 2024 by mattiaottoborgo
https://github.com/MarilenaDel/CI2024_lab1/issues/3
Content:
The code work nicely and is really clean. Some conditions to prune invalid results could be added, as well some prints to understand the evolution of the algorithm, but overall it is solid and accomplish the set goal

reemkhattarr/CI2024_lab0 Comment
#3 opened on Sep 28, 2024 by mattiaottoborgo
https://github.com/reemkhattarr/CI2024_lab0/issues/3
Content:
Probably my computer is smarter than me even when unplugged :)

FedericoPangrazi/CI2024_lab0 Review
#3 opened on Sep 28, 2024 by mattiaottoborgo
https://github.com/FedericoPangrazi/CI2024_lab0/issues/3
Content:
I don't know why but it sounds nice!

## Project

Delivered project work date: 10.02.2025
