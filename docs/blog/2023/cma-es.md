---
date: 2023-11-01 00:00 UK/London
categories: optimisation algorithms cma-es python software
published: true
title: The Covariance Matrix Adaptation Evolution Strategy (CMA-ES)
image: /images/2023/CMAES-1.png
description: 
---

# The Covariance Matrix Adaptation Evolution Strategy (CMA-ES)

Recently I've been working on improved parameterisation and optimisation methods for continuum scale battery models. One of the challenges in predictive modelling is parameter identification from measured data. In the electrochemical field, this data is often time-series in nature, collected from potentiostatic and/or galvanostatic experiments on different time scales.

This challenge becomes even more difficult when the model structure is overly constrained (e.g. multi-particle based continuum models) and there is a lack of information for unique identification. To overcome this, I have been looking for improved optimisation methods to identify the model parameters, and one such method has caught my interest and I thought I would discuss it here.

## What is CMA-ES?
CMA-ES is a stochastic optimisation algorithm that provides a global search for the functional critical point. It is a derivative-free algorithm that uses a population of candidate solutions to iteratively update the search distribution. This method is particularly useful for non-linear, non-convex and multimodal optimisation problems. 

### Step 1 - Sampling & Evaluation
The algorithm starts by sampling candidate solutions from a multivariate normal distribution at step $(g+1)$. The candidates are then evaluated and stored in ascending order of performance, i.e. element zero stores the current best candidate from the optimiser.

$$
    \mathbf{x}_{k}^{(g+1)} \sim \mathbf{m}^{(g)} + \sigma^{(g)} \mathcal{N}\left(0, \mathbf{C}^{(g)}\right), \ \ \ \ \ \ \text{for} \ g = 1,...,\lambda
$$

where, <br>
$\mathbf{x}_{k}^{(g+1)}$ is the $k^\text{th}$ candidate at the $(g+1)$ iteration <br>
$\mathbf{m}^{(g)}$ is the mean vector of the search distribution at $g$<br>
$\sigma^{(g)}$ is the step size at $g$ <br>
$\mathbf{C}^{(g)}$ is the covariance matrix. <br>
$\mathcal{N}\left(0, \mathbf{C}^{(g)}\right)$ is a multivariate normal distribution with corresponding zero mean and covariance matrix $\mathbf{C}^{(g)}$ <br>
$\lambda \geq 2$, is the population size <br>

### Step 2 - Construct the Evolution Paths
Using a weight function $w_i$ and a subset of the population, known as the parent value, the weighted averages as $dy = \sum_{i=1}^{\mu} w_i y_{1:\lambda}$ and $dz = \sum_{i=1}^{\mu} w_i z_{1:\lambda}$ are computed. The evolution path at generation $g$ is then constructed as,

$$
    \mathbf{p}_{\text{c}}^{(g+1)} = (1 - c_{\text{c}}) \mathbf{p}_{\text{c}}^{(g)} + h_{\sigma}^{(g+1)} \sqrt{c_{\text{c}}(2 - c_{\text{c}})\mu_w dy}
$$

where the conjugate evolution path is then constructed as,

$$
    \mathbf{p}_{\sigma}^{(g+1)} = (1 - c_\sigma) \mathbf{p}_{\sigma}^{(g)} + \sqrt{c_\sigma(2 - c_\sigma)\mu_w dz}
$$

where, $\mu_w = 1/\sum_{i=1}^\mu w_i^2$, and $c_{\text{c}}$, $c_{\sigma}$ are the cumulation factors, with $h_{\sigma}^{(g+1)}$ is the Heaviside function, defined as,

$$
h_{\sigma}^{(g+1)} = \begin{cases}
    1, & \text{if } \frac{\left\lVert \mathbf{p}_{\sigma}^{(g+1)} \right\rVert^2}{1-(1-c_\sigma)^{2\cdot(g+1)}} < \left(2+4/(d+1)\right)d, \\
    0, & \text{otherwise}
\end{cases}
$$

### Step 3 - Update the Search Distribution
The algorithm updates the mean search distribution via

$$
    \mathbf{m}^{(g+1)} = \mathbf{m}^{(g)} + c_\text{m}\sum_{i=1}^{\mu} w_{i} \left(\mathbf{x}_{i:\lambda}^{(g+1)} - \mathbf{m}^{(g)}\right)
$$

where, <br>
$w_i$ is a positive weighting vector <br>
$\mu \leq \lambda$ is the number of solutions used to update the mean vector <br>
$c_\text{m}$ is the learning rate <br>

Essentially, the mean from generation $(g)$ is summed with a weighted sum of the geometric difference between the $(g+1)$ samples multiplied by the learning rate. To update the step size, the algorithm uses the following update rule,

$$
    \sigma^{(g+1)} = \sigma^{(g)} \exp\left(\frac{c_\sigma}{d_\sigma}\left(\frac{\left\lVert \mathbf{p}_{\sigma}^{(g+1)} \right\rVert}{\mathbb{E}\left\lVert \mathcal{N}\left(0, \mathbf{I}\right) \right\rVert} - 1\right)\right)
$$

where $d_\sigma$ is a damping parameter on $\sigma^g$. Next, to estimate the covariance matrix,

$$
    \mathbf{C}^{(g+1)} =  \left(1-c_1-c_\mu \sum w_j\right) \mathbf{C}^{(g)} + c_1 \underbrace{\mathbf{p}_{\text{c}}^{(g+1)} \mathbf{p}_{\text{c}}^{(g+1)^T}}_{\text{rank-one update}} + c_\mu \underbrace{\sum_{i=1}^{\lambda} w_{i} \mathbf{y}_{i:\lambda}^{(g+1)} \left(\mathbf{y}_{i:\lambda}^{(g+1)}\right)^T}_{\text{rank-}\mu \ \text{update}}
$$


where, <br>
$c_1 \approx 2/n^2$, <br>
$c_\mu \approx \text{min}(\mu_{\text{eff}}/n^2, 1-c_1)$ <br>
$y_{i:\lambda}^{(g+1)} = \left(\mathbf{x}_{i:\lambda}^{(g+1)} - \mathbf{m}^{(g)}\right)/\sigma^{(g)}$ <br>

This algorithm is repeated until the termination criteria is met with the best candidate stored on each iteration. The full algorithm is given in [[1,2]](#references).


## Example
Let's look at how CMA-ES deals with the minimisation of a simple two-dimensional parabola function distorted by Gaussian noise. First, the underlying function is given as $f(\mathbf{x}) = \mathbf{x}^2$, where $\mathbf{x} \in \mathbb{R}^2$. A Julia script to construct this function is given below,

```julia
using GLMakie, Distributions, Dierckx

xy = range(-10, stop = 10, length = 100)
z = zeros(length(xy)+1,length(xy)+1)

f(x, y) = x^2 + y^2
z = [f(x, y) for x in xy, y in xy]
```

This gives us the following surface,

<div align="center">
```plotly
{"file_path": "./blog/2023/CMAES/surface-truth.json"}
```
</div>

A nice parabolic function with a global minimum at $(0,0)$. Now let's add some noise to the function, we do this with the [Distributions.jl](https://github.com/JuliaStats/Distributions.jl) package in Julia. Let's sample from a normal distribution with a mean of zero and a standard deviation of 5. The updated function is given by $f(\mathbf{x}) = \mathbf{x}^2 + \varepsilon$, where $\varepsilon \sim \mathcal{N}(0, 5)$. The updated Julia form is then

```julia
using GLMakie, Distributions, Dierckx

sigma = 5
xy = range(-10, stop = 10, length = 100)
z = zeros(length(xy)+1,length(xy)+1)
noise = rand(Normal(0, sigma), length(xy) * length(xy))
μ = Spline2D(xy,xy,reshape(noise,100,100))

f(x, y) = x^2 + y^2 + μ(x,y)
z = [f(x, y) for x in xy, y in xy]
```

Due to the high noise covariance, exploring the functional surface is quite challenging as the gradient information is heavily corrupted by the Gaussian noise. Since the CMA-ES algorithm doesn't need the gradient information, it is a good candidate for this problem. To implement the CMA-ES algorithm, we will use the [Evolutionary.jl](https://github.com/wildart/Evolutionary.jl/tree/master) package. To provide a reference for the performance of CMA-ES on this problem, I've added a gradient descent method using [Optim.jl](https://github.com/JuliaNLSolvers/Optim.jl/). This is implemented with the CMA-ES below.

```julia
using Evolutionary, Distributions, Optim

# Update functional form and optimize
x0 = [-12.4,9.53]
f(x) = x[1]^2 + x[2]^2 + μ(x[1],x[2])
res_cmaes = Evolutionary.optimize(f,x0, CMAES(sigma0=1), Evolutionary.Options(store_trace=true))
res_grad = Optim.optimize(f, x0, GradientDescent(), Optim.Options(store_trace=true, extended_trace=true))
```

The results of each of the optimisation algorithms constructed above are shown on the noisy functional surface given below,

<div align="center">
```plotly
{"file_path": "./blog/2023/CMAES/surface-corrupt.json"}
```
</div>

As expected, the gradient descent method struggles with the large number of local optima created by the Gaussian noise, but the CMA-ES method is able to find the global minimum repeatedly. The code to repeat this example can be found in the [here](https://github.com/BradyPlanden/bradyplanden.github.io/tree/main/docs/blog/2023/CMAES) repository. That's it for this post, I hope you found it useful! Overall, CMA-ES provides a robust method for minimising a difficult cost function, but this robustness is traded off against performance.  If you have any questions or comments, please feel free to contact me.

## References
[1] N. Hansen, ‘The CMA Evolution Strategy: A Tutorial’. arXiv, Mar. 10, 2023. Available: http://arxiv.org/abs/1604.00772 <br>
[2] M. Nomura, Y. Akimoto, and I. Ono, ‘CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?’, in Proceedings of the Genetic and Evolutionary Computation Conference, Jul. 2023, pp. 839–847. doi: [10.1145/3583131.3590358](https://arxiv.org/abs/2304.03473).

