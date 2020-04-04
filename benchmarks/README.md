# Benchmarking chaoseverywhere

**Chosen functions** : We chose to only run functions that are the root of this module. Indeed, in most of the animations, we create the background once and then only add points or move around the structure. So the main question is not *How long does it take to render the movie?* but rather *How long does it take to produce each part of the movie?*

## Time elapsed

We ran the creation of the Mandelbrot set with a number of iterations of 300 and a precision of 400. Note that in the animations, the parameters used are way lower and the difference between the two functions is almost non-existent. As for the `mandel_branch_points` functions, we used for parameters `(.01, -.5, 1000)` where `1000` is the number of horizontal lines (and also vertical lines) created in the plot. In reality, don't need more than `100` branches.

|      	| mandel_loop 	| mandelbrot 	| mandel_branch_points |
|------	|-------------	|------------	|----------------------|
| time 	| 12.3 s      	| 9.79 s     	|0.002 s    |

The most time consuming functions are the first two : the ones creating the actual Mandelbrot set.
Let's consider the logistic submodule now.

|      	| logi_branch_points(.1,.3,1000) 	| bifurcation 	| logistic_draw(.1,3.4,300,300) |
|------	|-------------	|------------	|----------------------|
| time 	| 0.016 s      	| 26.66 s     	|11.81 s    |

Just like before, the main (and static) pieces of the animations take more time to be generated but the moving parts of the scenes aren't time consuming at all considering that we don't even need that much points).

**Note** : Using numba on the Mandelbrot set function did not make a big difference. It can be a little useful only for the matplotlib animation rendering a zoom on the set.

## Memory use