using Distributions, Dierckx, LinearAlgebra
using Optim, Evolutionary, DataFrames, CSV

# Generate surface
sigma = 5
xy = range(-10, stop = 10, length = 100)
z = zeros(length(xy) + 1, length(xy) + 1)
noise = rand(Normal(0, sigma), length(xy) * length(xy))
μ = Spline2D(xy, xy, reshape(noise, 100, 100))

f(x, y) = x^2 + y^2 + μ(x, y)
z[2:end, 2:end] = [f(x, y) for x in xy, y in xy]

# Export Data
z[1, 2:end] = xy
z[2:end, 1] = xy
df1 = DataFrame(z, :auto)
CSV.write("surface.csv", df1, header = false)

# Update CMAES trace
function Evolutionary.trace!(record::Dict{String, Any},
        objfun,
        state,
        population,
        method::CMAES,
        options)
    record["σ"] = state.σ
    record["s"] = state.s
    record["fitpop"] = state.fitpop
    record["parent"] = state.parent
    record["fittest"] = state.fittest
end

# Update functional form and optimize
x0 = [-12.4, 9.53]
f(x) = x[1]^2 + x[2]^2 + μ(x[1], x[2])
hist = Vector{Float64}[]

# Store function calls
function kj(x)
    push!(hist, x)
    return f(x)
end

# Run optimisation
res_CMAES = Evolutionary.optimize(kj,
    x0,
    CMAES(sigma0 = 1),
    Evolutionary.Options(store_trace = true))
res_Grad = Optim.optimize(kj,
    x0,
    GradientDescent(),
    Optim.Options(store_trace = true, extended_trace = true))

# Store trace
k = zeros(length(res_CMAES.trace), 3)
for i in 1:length(res_CMAES.trace)
    k[i, 1:2] = res_CMAES.trace[i].metadata["fittest"]
    k[i, 3] = res_CMAES.trace[i].value
end

# Export Data
df = DataFrame(k, :auto)
CSV.write("CMAES.csv", df, header = false)

# Store trace
k = zeros(length(res_Grad.trace), 3)
for i in 1:length(res_Grad.trace)
    k[i, 1:2] = res_Grad.trace[i].metadata["x"]
    k[i, 3] = res_Grad.trace[i].value
end

# Export Data
df = DataFrame(k, :auto)
CSV.write("GradientDescent.csv", df, header = false)
