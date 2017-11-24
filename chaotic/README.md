This article is part of my [Python Playground Plus](https://github.com/electronut/ppp) project. 

<hr/>

## Strange Attractors and Turtle Graphics

An [attractor][1] is a set of numerical values to which a mathematical system converges, and 
a *strange attractor* is one which in these values have a fractal structure. Though the mathematics 
of these constructs are quite scary, you don't need to be a genius to appreciate their beauty, or 
to write some Python code to plot them.

In this project, we're looking at two attactors - *Lorenz* and *Thomas*.

## The Lorenz Attractor

The [Lorenz equations][3] are given as:

![](lorenz.png)

In the code, the equations are solved using a simple time discretisation. To see it in action, run the code as follows:

```
python chaotic.py --axes zx --attr lorenz
```

Here's the output:

![](lorenz-attr.png)


## Thomas' cyclically symmetric attractor

The equations for this [attractor][4] are given as:

![](thomas.png)

Run it as:

```
python chaotic.py --axes xy --attr thomas
```

Here's the output:

![](thomas-attr.png)

[1]: https://en.wikipedia.org/wiki/Attractor
[2]: https://en.wikipedia.org/wiki/Fractal
[3]: https://en.wikipedia.org/wiki/Lorenz_system
[4]: https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor
