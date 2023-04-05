In data science, you've likely been led through the fundamentals of probability
and it's math formalism in some probability class. In astronomy, you would
rarely take such class, and instead are taught along the way with some
short-hands These short-hands are introduced with observational astronomy on how
to handle uncertainties on data involving the collection of random occuring
things (i.e., photons) [in urns](https://en.wikipedia.org/wiki/Urn_problem)
(e.g., CCD sensors). These short-hands makes the life of a data scientist
(including statisticians) who started with astronomy pretty difficult.

## Photon Events are Poisson Variates

In astronomy, and many fields in physics, a warm body emitting photons are
modeled as stochastic systems. Specifically, the body emits a photon at a
random time and is found to behave as a Poisson random event with an average
number of photons emitted in some time $t$ is $\lambda t$[^1].

$$
  N \sim \text{Poisson}(\lambda t)
$$

[^1]: It's more convenient to use this convention so that $\lambda$ is the rate
of events. Also, I always found this more convenient than implying there is
some unknown time $t$.

The Poisson has very simple cumulant with equal expected value $\text{E}[N]$ and
variance $\text{Var}[N]$ of its parameters $\lambda t$.


## Uncertainty, in units of Magnitude
In astronomy, the count of photons $\lambda t$ is often very large (so much so
we define our units in terms of logarithmic units, the magnitude)

and with large
$\lambda t$, the Poisson leads itself to look very Normal-distributed.

## Systematic Noise Floor
The systematic noise floor is a Poisson