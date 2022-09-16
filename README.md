# genetic_algorithm
Implemented the genetic algorithm on python

INPUT:

![image](https://user-images.githubusercontent.com/80597420/190743338-12d6426e-8ba1-4e66-9a66-7951ce8b3667.png)


OUTPUT: 

![image](https://user-images.githubusercontent.com/80597420/190744536-407756f3-1f19-49f8-b06f-dc0a645c1671.png)


It took about 12847 generations for the algorithm to converge to the output. The threshold probability for mutation was set to 0.9. This means that 10 percent chances are there for the children to mutate which might be higher for this length of string. I have used random variables wherever necessary and higher the randomness, longer it takes to converge.


However, if we take a smaller sentence, the convergence happens a lot quicker!

INPUT:

![image](https://user-images.githubusercontent.com/80597420/190748602-7e8220db-eef3-48e9-994c-d3b32a39ed99.png)

OUTPUT:

![image](https://user-images.githubusercontent.com/80597420/190748906-9ea6a974-ef35-4fac-8dad-f6ea3a35361f.png)

An exponential rise in time is observed with change in length of string which can be controlled using the rate of mutation.
