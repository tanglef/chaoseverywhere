"""
An animation of the logistic function
=============================================
"""

####################################
# The logistic map and... rabbits?
# ----------------------------------
# A commun example to understand the logistic map is to think of a pattern to simulate a population of rabbits
# with the most simple conditions in a multiplicativ model.
# Let's consider a group made of :math:`x_n` rabbits, where :math:`x_n` is a percentage of the maximum number of rabbits we can have.
# Let's observe them every six months (time they need to be able to produce offsprings).
# Then at the next observation, if we note :math:`r` the growth rate of the population, there will be :math:`rx_n` rabbits.
# However, this modelisation is wrong because it assumes that none of the rabbits died or escaped its cage to go back to the wilderness.
# So, a way to control this pattern is to multiply :math:`rx_n` by :math:`(1-x_n)`, a factor that, when :math:`x_n` approaches it's maximum, tends to :math:`0`.
#
#
# Thus the equation of the logistic map is :
#
# .. math::
#
#       x_{n+1}=rx_n(1-x_n),\ \forall\, (x_0,r)\in [0,1]\times [0,4].
#
# Let's see how the population evolves over time depending on the growth ratio. Let's begin with a growth ratio of :math:`2.5`.


import chaoseverywhere as chaos
import matplotlib.pyplot as plt

plt.style.use('ggplot')
chaos.logistic_draw(0.01, 2.5, 100, 100)
hline = plt.axhline(y=1.5/2.5, color='black', ls=':', label=r'$y=\dfrac{2.5-1}{2.5}=0.6$')
plt.legend(handles=[hline])
plt.show()


################################
# Evolution in term of r values
# --------------------------------
# * For :math:`r\leq 1`, our bunnies die. The sequence tends to :math:`0`.
# * For :math:`r\in [1,3]`, the population oscillates and then stabilizes to the value :math:`\frac{r-1}{r}`.
# * For :math:`r\in [3,3.57]` the population oscillates between several values, there is no longer one attractor.
# * For :math:`r\geq 3.57` there is almost surely a chaotic design.
#
#
# .. raw:: html
#
#     <iframe width="356" height="200" src="https://www.youtube.com/embed/YiqpSf13kzI" frameborder="0" allowfullscreen></iframe>
#
