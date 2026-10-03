# Node-Differentially Private Distance Histograms via Incidence Geometry

Working draft. Scope: Route 1 only. Route 2 is parked as Appendix A.

## Abstract

We study node-differentially private release of distance-collision statistics for planar point datasets. Given a database `P = {p_1, ..., p_n} subset R^2`, the basic statistics count pairs at a prescribed distance, inside a thin annulus, below a distance threshold, or inside bins of a pairwise-distance histogram. Under node-DP, the global sensitivity of these pair counts can be `Theta(n)`, because adding or deleting one point can change all incident distance edges. The central question is whether the error can adapt to the local geometric complexity of the input rather than always paying worst-case `Theta(n/epsilon)` noise.

Our proposed route has three ingredients. First, for a distance graph `G(P)`, define a canonical degree-bounded statistic `f_D(G)` as the maximum number of edges in a subgraph of `G` with maximum degree at most `D`. This avoids order-dependent edge clipping: `f_D` has node sensitivity at most `D`, is computable as a degree-constrained subgraph problem, and satisfies a bias sandwich in terms of the degree tail. Second, use point-circle incidence geometry to prove degree-tail bounds for exact unit-distance graphs:

```text
R_k(P) <= O(n^2/k^3 + n/k),
tail_D(P) <= O(n^2/D^2 + n log(n/D)).
```

The `n/k` term is the star obstruction; under a no-star or bounded-circle-richness condition, the bias improves to `O(n^2/D^2)`, yielding an `~O(n^{2/3} epsilon^{-2/3})` target error. Third, select `D` privately over a doubling grid using the generalized exponential mechanism for score functions with varying sensitivity.

The 2026 OpenAI/Sawin unit-distance breakthrough is used only as an extremal witness and structural reference point. It shows that exact distance collisions can be polynomially superlinear, but those high-collision constructions appear near-regular and are not the hard instances for adaptive mechanisms. The hard instances are skewed-degree configurations such as stars and nested circle families.

## 1. Introduction

Spatial datasets are often released through aggregate distance statistics: how many pairs are exactly at a prescribed distance, how many are within a tolerance band, how many are within a threshold, or how the full pairwise-distance histogram is distributed. These quantities occur in location analytics, epidemiology, co-location analysis, mobility studies, and geometric graph summaries.

Under node-level differential privacy, one individual corresponds to one point. Adding or deleting that point changes every pair involving it. The worst-case sensitivity of a distance edge count is therefore the maximum degree of the corresponding distance graph, and without restrictions this can be `Theta(n)`.

The naive Laplace mechanism gives valid error `O(n/epsilon)`, but this can be unnecessarily pessimistic. Many datasets have low local distance degrees. Other datasets have many distance collisions, but in a near-regular way, so a degree-adaptive mechanism should pay roughly the typical degree rather than `n`.

The 2026 disproof of the Erdos unit-distance conjecture sharpens the motivation but does not supply a privacy mechanism. It proves the existence of planar point sets with more than `n^{1+delta}` unit-distance pairs, with Sawin giving an explicit exponent above `1.014` and later finite-certificate optimization improving the certificate to above `1.0152`. This changes the extremal geometry of exact-distance statistics. However, it does not make relative-error estimation harder on those extremal instances. If the signal is `n^{1+delta}` and the naive noise is `O(n/epsilon)`, the relative error is `O(n^{-delta}/epsilon)`, which is more favorable than on sparse `Theta(n)` instances.

The lesson is different:

```text
High-collision near-regular instances separate naive global-sensitivity noise from adaptive degree-aware mechanisms.
Skewed high-degree instances remain the true worst case.
```

### Contributions in This Draft

1. Formalize three data regimes: continuous exact-distance, quantized exact-distance, and separated annulus graphs.
2. Define the canonical degree-bounded statistic `f_D` via maximum degree-constrained subgraphs.
3. Prove node sensitivity at most `D` for `f_D`.
4. Prove the bias sandwich

```text
U(P) - tail_D(P) <= f_D(G(P)) <= U(P).
```

5. Prove the rich-points lemma and degree-tail corollary for exact unit distances.
6. Prove the adaptive accuracy theorem using the RS16 generalized exponential mechanism.
7. Prove a constant-privacy `Omega(n)` lower obstruction and give an experiment plan.
8. Park the exact unit-circle discrepancy program as Appendix A.

## 2. Model and Problem Definition

### 2.1 Databases and Node-DP

A database is a finite set or ordered list of planar points

```text
P = {p_1, ..., p_n} subset R^2.
```

The primary neighboring relation in this draft is add/remove node adjacency:

```text
P ~ P' iff P' is obtained from P by adding or deleting one point.
```

This choice gives clean sensitivity statements. Replace-one adjacency changes at most two add/remove steps, so all sensitivity bounds below lose at most a factor of 2.

A randomized mechanism `M` is `epsilon`-node-DP if for all neighboring `P ~ P'` and all measurable output events `S`,

```text
Pr[M(P) in S] <= exp(epsilon) Pr[M(P') in S].
```

All main statistics are raw counts, not normalized by `n`. If normalized counts are desired, divide both the released answer and the error guarantees by the appropriate scale.

### 2.2 Distance Graphs and Statistics

For a distance bin `b`, define the distance graph

```text
G_b(P) = (P, E_b(P)),
E_b(P) = { {p_i,p_j} : ||p_i-p_j|| in b }.
```

Important special cases are:

```text
U_r(P)     = #{i<j : ||p_i-p_j|| = r}
A_{r,t}(P) = #{i<j : ||p_i-p_j|| in [r-t, r+t]}
B_r(P)     = #{i<j : ||p_i-p_j|| <= r}
H_b(P)     = #{i<j : ||p_i-p_j|| in bin b}.
```

Each is the edge count of a graph `G_b(P)`.

### 2.3 Primary Regime M1: Continuous Exact-Distance Model

The primary model is:

```text
M1: arbitrary finite P subset R^2, exact distance r, add/remove node-DP, raw count U_r(P).
```

This is the cleanest theoretical regime because degrees are unbounded. A star instance is realizable: put `n-1` points on the circle of radius `r`, and add/delete the center. The statistic changes by `n-1`.

This is the regime where adaptivity is provably necessary. Any mechanism that is accurate on all inputs must confront the `Theta(n)` star sensitivity, but many inputs have much smaller degree tails.

### 2.4 Bonus Regime M2: Quantized Exact-Distance Model

Suppose

```text
P subset (1/q) Z^2
```

and the target distance is `r`, with `qr` an integer. For any point `p`, the number of grid points at exact distance `r` from `p` is at most the number of integer representations

```text
a^2 + b^2 = (qr)^2.
```

Thus the exact-distance degree is bounded by

```text
r_2((qr)^2),
```

where `r_2(N)` is the number of representations of `N` as a sum of two squares. The divisor bound gives

```text
r_2((qr)^2) <= (qr)^{O(1/log log(qr))}.
```

If `q,r = poly(n)`, then the global sensitivity is `n^{o(1)}`. The star obstruction from M1 is no longer realizable at degree `Theta(n)` unless the grid scale or target radius is enormous.

Consequence:

```text
Plain Laplace with scale n^{o(1)}/epsilon essentially resolves quantized exact-distance release up to n^{o(1)} factors.
```

There is also a matching sensitivity example at the lattice-circle degree scale: include a center and all grid points on a radius-`r` lattice circle. Add/delete the center changes the count by `r_2((qr)^2)`.

This observation is useful because number theory enters the privacy sensitivity analysis directly.

### 2.5 Bonus Regime M3: Separated Annulus Model

For annulus statistics

```text
A_{r,t}(P) = #{i<j : ||p_i-p_j|| in [r-t, r+t]},
```

no nontrivial bound exists without geometric restrictions. Two clusters of diameter `< t`, placed at distance `r`, create `Theta(n^2)` annulus pairs.

Assume instead a minimum separation condition:

```text
||p_i-p_j|| >= delta for all i != j.
```

Then the degree of any point in the annulus is bounded by a packing estimate:

```text
Delta_annulus <= O(r t / delta^2 + r / delta + 1).
```

Reason: the annulus has area `Theta(r t)` and boundary length `Theta(r)`, and a `delta`-separated set has at most `O(area/delta^2 + perimeter/delta + 1)` points in such a region.

Consequence:

```text
In separated annulus models, global sensitivity is already finite and data-independent.
```

Adaptivity may still be practically useful, but the theoretical need is weaker than in M1.

## 3. Related Work

### Node-Private Graph Statistics

Kasiviswanathan, Nissim, Raskhodnikova, and Smith initiated a systematic study of graph statistics under node differential privacy. Their framework motivates restricting or projecting graphs to bounded-degree families, where node sensitivity becomes controlled.

Raskhodnikova and Smith developed Lipschitz-extension methods for node-private graph statistics and a generalized exponential mechanism that can select among candidates with different sensitivities. Our mechanism layer should be viewed as an application of this machinery to geometric distance graphs. The new contribution is the incidence-geometric control of the clipping bias.

### Distance and Incidence Geometry

The exact unit-distance problem asks for the maximum number of unit-distance pairs among `n` planar points. The best general upper bound remains `O(n^{4/3})`, via Spencer-Szemeredi-Trotter incidence geometry. OpenAI's 2026 model disproved the longstanding `n^{1+o(1)}` conjecture, and Sawin gave an explicit `n^{1.014...}` lower bound. Emmerich later optimized explicit finite certificates, supporting `u(n) > n^{1.0152}` for arbitrarily large `n`.

The present draft uses the unit-distance breakthrough only as extremal context. The technical geometry used in Route 1 is the rich-points incidence bound for congruent circles.

### Discrepancy and Query Release

Muthukrishnan and Nikolov, and Nikolov, Talwar, and Zhang connect private query release to hereditary discrepancy and convex geometry. Hardt and Talwar give a pure-DP packing/volume route. Those tools are relevant to Appendix A, not to the main mechanism in Route 1.

## 4. Degree-Bounded Edge Count

Let `G=(V,E)` be any graph. For an integer `D >= 0`, define

```text
f_D(G) = max { |F| : F subset E, Delta((V,F)) <= D }.
```

That is, `f_D(G)` is the largest number of edges in a subgraph of `G` with maximum degree at most `D`.

This is a canonical replacement for informal edge clipping. It is order-independent and can be computed as a degree-constrained subgraph problem, equivalently a simple `b`-matching instance with uniform vertex capacities `D`.

### Proposition 4.1: Node Sensitivity of `f_D`

Under add/remove node adjacency,

```text
|f_D(G) - f_D(G-v)| <= D.
```

Therefore, for a distance graph `G_b(P)`, the statistic

```text
P -> f_D(G_b(P))
```

has node sensitivity at most `D`.

Proof.

Let `F` be an optimal degree-`D` subgraph of `G`. Since `F` has maximum degree at most `D`, the vertex `v` is incident to at most `D` edges of `F`. Removing `v` and its incident edges leaves a feasible degree-`D` subgraph of `G-v` with at least `f_D(G)-D` edges. Thus

```text
f_D(G-v) >= f_D(G) - D.
```

Conversely, any feasible degree-`D` subgraph of `G-v` is also feasible in `G`, so

```text
f_D(G) >= f_D(G-v).
```

Combining gives the claim.

For replace-one adjacency, apply the add/remove bound twice.

### Proposition 4.2: Bias Sandwich

Let

```text
U(G) = |E|,
deg_G(v) = degree of v in G,
tail_D(G) = sum_{v in V} (deg_G(v)-D)_+.
```

Then

```text
U(G) - tail_D(G) <= f_D(G) <= U(G).
```

Proof.

The upper bound is immediate since `f_D(G)` counts a subset of edges.

For the lower bound, start with `G` and repeatedly delete an edge incident to any vertex whose current degree exceeds `D`. Each deleted edge reduces

```text
sum_v (deg(v)-D)_+
```

by at least 1. The initial value is `tail_D(G)`, so after at most `tail_D(G)` edge deletions all degrees are at most `D`. The remaining subgraph has at least `U(G)-tail_D(G)` edges and is feasible for `f_D(G)`.

### Fixed-`D` Mechanism

For fixed `D`, release

```text
M_D(P) = f_D(G_b(P)) + Laplace(D/epsilon).
```

By Proposition 4.1, this is `epsilon`-node-DP under add/remove adjacency. Its error relative to the true edge count `U_b(P)=|E_b(P)|` is

```text
|M_D(P) - U_b(P)| <= noise + bias
                 ~= O(D/epsilon) + tail_D(G_b(P)).
```

This gives the oracle target:

```text
min_D { D/epsilon + tail_D(G_b(P)) }.
```

### Private Selection of `D`

Let the candidate set be a doubling grid

```text
D_grid = {1,2,4,...,2^ceil(log_2 n)}.
```

The selector is the generalized exponential mechanism of Raskhodnikova-Smith, applied to candidate-specific sensitivity `D`.

For each `D`, define the underestimate

```text
f_D(G_b(P)) <= U_b(P).
```

Fix a target failure probability `beta`. Let

```text
a = log(2/beta).
```

The high-probability oracle error proxy is

```text
err(D;P) = U_b(P) - f_D(G_b(P)) + a D/epsilon_rel,
```

where `epsilon_rel` is the privacy budget reserved for the final noisy release. Since `U_b(P)` is common to all `D`, minimizing `err(D;P)` is equivalent to minimizing the computable score

```text
q_D(P) = -f_D(G_b(P)) + a D/epsilon_rel.
```

The score `q_D` has sensitivity at most `D`, because `f_D` has sensitivity at most `D` and the second term is public. This is exactly the varying-sensitivity setting of RS16. The generalized exponential mechanism selects `D_hat` with excess score controlled by the sensitivity of the near-optimal threshold rather than by the maximum candidate sensitivity.

Split the privacy budget as `epsilon = epsilon_sel + epsilon_rel`, and use failure probabilities `beta/2` for selection and `beta/2` for release. RS16's generalized exponential mechanism gives, with probability at least `1-beta/2`,

```text
q_{D_hat}(P)
  <= min_D { q_D(P) + 4D log(2|D_grid|/beta)/epsilon_sel }.
```

After releasing

```text
f_{D_hat}(G_b(P)) + Laplace(D_hat/epsilon_rel),
```

the final error is controlled by the selected threshold's approximation error plus Laplace noise. This gives the formal theorem in Section 6.3.

## 5. Incidence Geometry for Exact Unit Distances

This section is specific to exact-distance graphs. It does not apply to fat annuli without additional separation or density assumptions.

By scaling, take the target distance to be 1.

For a point set `P` with `|P|=n`, define the unit-distance degree

```text
deg(p) = #{q in P : ||p-q|| = 1}
```

and the rich-point count

```text
R_k(P) = #{p in P : deg(p) >= k}.
```

### Lemma 5.1: Rich-Points Bound

For every `k >= 1`,

```text
R_k(P) <= O(n^2/k^3 + n/k).
```

Proof.

Let `Q subset P` be the set of `k`-rich points, so `|Q|=R_k(P)=m`. For each `q in Q`, consider the unit circle centered at `q`. Let `Gamma` be this family of `m` congruent circles.

Each `q in Q` has at least `k` points of `P` on its unit circle, so the number of point-circle incidences between `P` and `Gamma` satisfies

```text
I(P,Gamma) >= k m.
```

Congruent circles form a pseudo-circle family: any two distinct unit circles intersect in at most two points. The Szemeredi-Trotter-type incidence bound for points and pseudo-circles gives

```text
I(P,Gamma) <= C( n^{2/3} m^{2/3} + n + m )
```

for an absolute constant `C`.

Thus

```text
k m <= C( n^{2/3} m^{2/3} + n + m ).
```

For small constant `k`, the bound is trivial after adjusting constants. For larger `k`, absorb the `Cm` term into the left side. Then either

```text
k m <= O(n^{2/3} m^{2/3})
```

which implies

```text
m <= O(n^2/k^3),
```

or

```text
k m <= O(n),
```

which implies

```text
m <= O(n/k).
```

Combining yields the stated bound.

### Corollary 5.2: Degree-Tail Bound

For the exact unit-distance graph,

```text
tail_D(P) = sum_{p in P} (deg(p)-D)_+
```

satisfies

```text
tail_D(P) <= O(n^2/D^2 + n log(n/D)).
```

Proof.

Use the identity

```text
sum_p (deg(p)-D)_+ <= sum_{k>D} R_k(P),
```

with `k` ranging up to `n`. By Lemma 5.1,

```text
sum_{k>D} R_k(P)
 <= O( sum_{k>D} n^2/k^3 + sum_{k>D} n/k )
 <= O(n^2/D^2 + n log(n/D)).
```

### Scoping Notes

1. Exact distances only. The lemma uses point-circle incidences. Fat annuli are regions, not curves, and can contain `Theta(n^2)` pairs without separation.
2. The `n/k` term is tight because of the star construction.
3. The `n^2/k^3` term is tied in spirit to the `O(n^{4/3})` unit-distance upper bound. Improvements in incidence or unit-distance upper bounds could improve this tail estimate.
4. A parameterized alternative is possible. If one assumes a unit-distance upper bound `u(N) <= O(N^alpha)`, then from `k R_k <= u(n+R_k) <= O(n^alpha)` one gets

```text
R_k <= O(n^alpha/k)
```

for `R_k <= n`. This is not always stronger than the incidence rich-points bound, but it makes the dependence on future progress in the unit-distance problem explicit.

## 6. Accuracy Theorems

### Theorem 6.1: Fixed-`D` Accuracy

For fixed `D`, the mechanism

```text
M_D(P) = f_D(G_1(P)) + Laplace(D/epsilon)
```

is `epsilon`-node-DP under add/remove adjacency and, with constant probability,

```text
|M_D(P)-U_1(P)| <= O(D/epsilon + tail_D(P)).
```

For high probability `1-beta`, replace `D/epsilon` by `(D/epsilon) log(1/beta)`.

Proof.

Privacy follows from Proposition 4.1 and the Laplace mechanism. Accuracy follows from Proposition 4.2 and the standard Laplace tail bound.

### Theorem 6.2: Incidence-Controlled Accuracy

For exact unit-distance release in M1, fixed-`D` release satisfies

```text
|M_D(P)-U_1(P)| <= O(D/epsilon + n^2/D^2 + n log(n/D))
```

with constant probability.

Under a no-star or bounded-circle-richness condition eliminating the `n/k` rich-point term, the error becomes

```text
O(D/epsilon + n^2/D^2).
```

Choosing

```text
D ~= (epsilon n^2)^{1/3}
```

gives

```text
~O(n^{2/3} epsilon^{-2/3})
```

error, ignoring logarithmic and calibration factors.

### Theorem 6.3: Adaptive Accuracy via Varying-Sensitivity Selection

Let

```text
D_grid={1,2,4,...,2^ceil(log_2 n)},     K=|D_grid|.
```

Split `epsilon=epsilon_sel+epsilon_rel` and fix failure probability `beta`. Set

```text
a = log(2/beta).
```

Run the generalized exponential mechanism on scores

```text
q_D(P) = -f_D(G_1(P)) + a D/epsilon_rel
```

with sensitivity bound `D`, obtaining `D_hat`. Then release

```text
f_{D_hat}(G_1(P)) + Laplace(D_hat/epsilon_rel).
```

This mechanism is `epsilon`-node-DP by adaptive composition. With probability at least `1-beta`, its error satisfies

```text
error(P)
  <= min_{D in D_grid} {
        tail_D(P)
        + D log(2/beta)/epsilon_rel
        + 4D log(2K/beta)/epsilon_sel
      }.
```

Taking a constant privacy split gives the simpler bound

```text
error(P) <= O( min_{D in D_grid} {
  tail_D(P) + D log(K/beta)/epsilon
} ).
```

Proof.

Privacy: for each `D`, the score `q_D` has node sensitivity at most `D`. The generalized exponential mechanism run with privacy budget `epsilon_sel` is `epsilon_sel`-node-DP. Conditional on the selected `D_hat`, the statistic `f_{D_hat}` has node sensitivity at most `D_hat`, so the Laplace release with scale `D_hat/epsilon_rel` is `epsilon_rel`-node-DP. Adaptive composition gives `epsilon`-node-DP.

Utility: by the RS16 utility guarantee for varying-sensitivity scores, with probability at least `1-beta/2`,

```text
q_{D_hat}(P)
  <= min_{D in D_grid} {
       q_D(P) + 4D log(2K/beta)/epsilon_sel
     }.
```

With probability at least `1-beta/2`, the Laplace noise `Z` in the final release satisfies

```text
|Z| <= D_hat log(2/beta)/epsilon_rel = a D_hat/epsilon_rel.
```

On the intersection of these events,

```text
|f_{D_hat}(G_1(P)) + Z - U_1(P)|
  <= U_1(P) - f_{D_hat}(G_1(P)) + |Z|
  <= U_1(P) - f_{D_hat}(G_1(P)) + a D_hat/epsilon_rel
  = U_1(P) + q_{D_hat}(P).
```

Applying the selection guarantee and using `U_1(P)-f_D(G_1(P)) <= tail_D(P)` proves the displayed bound. A union bound gives probability at least `1-beta`.

## 7. Lower Obstructions

### Star Obstruction

Let `P` consist of one center point and `m=n-1` points on the unit circle around it. Deleting the center changes `U_1(P)` by `m`. Therefore the local sensitivity at this instance is `Theta(n)`.

This proves that no mechanism accurate on all inputs can avoid confronting `Theta(n)` local changes.

### Proposition 7.1: Constant-Privacy `Omega(n)` Lower Obstruction

For add/remove node-DP on databases of size at most `n`, any `epsilon`-node-DP mechanism estimating `U_1` has worst-case expected absolute error at least

```text
Omega( n / (1+exp(epsilon)) ).
```

In particular, for constant `epsilon`, the worst-case expected error is `Omega(n)`.

Proof.

Let `P_0` consist of `m=n-1` points on the unit circle centered at the origin, and let

```text
P_1 = P_0 union {0}.
```

Then `P_0` and `P_1` are add/remove neighbors, and

```text
U_1(P_1) = U_1(P_0) + m,
```

because the added center creates exactly `m` new unit-distance pairs. Let `L=U_1(P_0)`, and define the interval

```text
T = [L + 2m/3, L + 4m/3].
```

If a mechanism has error less than `m/3` on `P_1`, its output lies in `T`. If it has error less than `m/3` on `P_0`, its output lies outside `T`. Write

```text
p_1 = Pr[M(P_1) in T],     p_0 = Pr[M(P_0) in T].
```

Differential privacy gives

```text
p_1 <= exp(epsilon) p_0.
```

If the probability of error at least `m/3` were less than `rho` on both `P_0` and `P_1`, then `p_1 > 1-rho` and `p_0 < rho`, implying

```text
1-rho < exp(epsilon) rho.
```

Thus for at least one of `P_0,P_1`, the probability of error at least `m/3` is at least `1/(1+exp(epsilon))`. The expected-error bound follows.

For fixed-size databases under replace-one adjacency, add a dummy point far away from all other points and replace it by the center; constants change by at most a factor of two.

### Lower-Bound Target and a Geometry Caveat

For arbitrary node-private graph edge count, standard packing/geometric-mechanism arguments give `Omega(n/epsilon)` error in the appropriate parameter range. For exact unit-distance graphs, the situation is subtler. The star construction realizes a one-step `Theta(n)` sensitivity gap, which yields a robust `Omega(n)` obstruction for constant `epsilon`. Getting an additional `1/epsilon` factor would require a long packing path whose count increases by `Theta(n)` at each neighboring step.

Such a path is easy in unrestricted graph families, and may be possible in fat-annulus or threshold models with clustering, but it is not immediate for exact unit-distance graphs because the geometry prevents many high-degree centers from sharing the same leaves. Thus, in M1 the clean lower-bound statement supported by the star construction is Proposition 7.1:

```text
worst-case error >= Omega(n)     for constant epsilon.
```

The stronger `Omega(n/epsilon)` exact-distance lower bound should be treated as an open proof target.

Proof target to formalize:

1. Build a family of datasets whose unit-distance counts differ by multiples of `m=Theta(n)` over a path in node distance.
2. Apply group privacy to relate output distributions along the path.
3. Use a packing argument to show that too-small error would distinguish too many neighboring groups.

This stronger target does not contradict adaptive guarantees, which improve on inputs with small degree tails.

## 8. Role of the Unit-Distance Breakthrough

The OpenAI/Sawin construction should not be used as the first practical benchmark. At realistic sizes, `n^{0.014}` is barely above constant; for `n=10^6`, it is about `1.2`. Classical scaled integer grids are likely more visible finite benchmarks.

The correct roles are:

1. Extremal witness: exact-distance collisions can be polynomially superlinear.
2. Naive-vs-adaptive separation: if the construction is near-regular with degree about `n^{alpha_UD-1}`, adaptive mechanisms pay roughly that degree rather than `n`.
3. Route 2 object: the lattice construction induces a near-Cayley graph whose spectrum may be analyzable.

For a near-regular unit-distance graph with

```text
U_1(P) ~= n^{alpha_UD},
Delta ~= n^{alpha_UD-1},
```

choosing `D ~= Delta` gives noise

```text
O(n^{alpha_UD-1}/epsilon)
```

and relative error

```text
O(1/(epsilon n)).
```

Thus the construction is not hard for a degree-adaptive mechanism. It is hard mainly for the naive global-sensitivity baseline.

## 9. Experiments

The experimental goal is to show that the oracle and private degree selection adapt across sparse, near-regular high-collision, and skewed high-sensitivity inputs.

### Synthetic Datasets

1. Scaled integer grids.
2. Random-rounded points in a bounded region.
3. Star configurations.
4. Nested circle families.
5. Two-cluster annulus examples showing `Theta(n^2)` blowup without separation.
6. Separated annulus instances with controlled `delta`.

### Real Datasets

Use at least one coordinate-rounded location dataset:

1. Gowalla check-ins.
2. Brightkite check-ins.
3. Optional: Foursquare or SafeGraph-like public aggregate substitutes, if licensing permits.

Preprocessing should include coordinate rounding, deduplication policy, and bin definitions.

### Metrics

1. Raw additive error.
2. Relative error when the true count is nonzero and sufficiently large.
3. Selected private `D_hat` versus oracle `D*`.
4. Tail curve `tail_D(P)` as a function of `D`.
5. Runtime of computing `f_D` exactly versus flow relaxation / greedy proxy.
6. Privacy parameters and composition across distance bins.

### Baselines

1. Naive Laplace using global sensitivity `n`.
2. Quantized-model Laplace using lattice-circle degree bound where applicable.
3. Fixed-`D` release for hand-tuned `D`.
4. Oracle `D*` release, non-private, as an upper-performance reference.
5. Private selector `D_hat`, the actual proposed mechanism.

## 10. Paper Structure

Suggested submission structure:

```text
1. Introduction
2. Model and Problem Definition
3. Related Work
4. Degree-Bounded Edge Counts
5. Incidence Bounds for Degree Tails
6. Private Mechanism and Accuracy Theorems
7. Lower Obstructions
8. Experiments
9. Discussion: Unit-Distance Breakthrough as Extremal Witness
Appendix A. Exact Unit-Circle Workloads and Discrepancy
Appendix B. Quantized and Separated Annulus Models
```

## Appendix A. Route 2: Exact Unit-Circle Workloads

Let `P` be a finite universe of candidate points and `C` a set of query centers. Define

```text
A_{c,p} = 1[ ||p-c|| = 1 ].
```

Rows are queries; columns are universe points. For a histogram database `x in N^P`, the query answers are `Ax`.

The discrepancy program asks for

```text
disc(A) = min_{chi in {+-1}^P} ||A chi||_infty,
herdisc(A) = max_{S subset P} disc(A restricted to columns S).
```

High incidence does not imply high discrepancy. The unit-distance breakthrough gives many ones in `A(P,P)`, but one must prove a determinant, spectral, gamma_2, or expander-type obstruction to obtain DP lower bounds.

For exact unit-circle workloads, Beck-Fiala gives

```text
herdisc(A) <= O(Delta),
```

where `Delta` is the maximum number of unit circles containing a point, equivalently the maximum degree in the corresponding unit-distance graph when `C=P`.

For the Sawin/OpenAI near-Cayley construction, the idealized adjacency operator has the form

```text
(Af)(x) = sum_{s in S} f(x+s),
```

with eigenvalues

```text
lambda_chi = sum_{s in S} chi(s).
```

The concrete Route 2 problem is to estimate these character sums and determine whether they imply a hereditary-discrepancy lower bound or instead a high-incidence / low-discrepancy separation.

This appendix should remain an open-problems section until the spectral estimates are actually proved.

## References

- OpenAI, "An OpenAI model has disproved a central conjecture in discrete geometry", 2026. <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- Noga Alon, Thomas F. Bloom, W. T. Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, Melanie Matchett Wood, "Remarks on the disproof of the unit distance conjecture", arXiv:2605.20695, 2026. <https://arxiv.org/abs/2605.20695>
- Will Sawin, "An explicit lower bound for the unit distance problem", arXiv:2605.20579, 2026. <https://arxiv.org/abs/2605.20579>
- Michael T. M. Emmerich, "Optimizing Explicit Unit-Distance Lower-Bound Certificates", arXiv:2606.03419, 2026. <https://arxiv.org/abs/2606.03419>
- Shiva P. Kasiviswanathan, Kobbi Nissim, Sofya Raskhodnikova, Adam Smith, "Analyzing Graphs with Node Differential Privacy", TCC 2013. <https://link.springer.com/chapter/10.1007/978-3-642-36594-2_26>
- Sofya Raskhodnikova, Adam Smith, "Lipschitz Extensions for Node-Private Graph Statistics and the Generalized Exponential Mechanism", FOCS 2016. <https://arxiv.org/abs/1504.07912>
- S. Muthukrishnan, Aleksandar Nikolov, "Optimal Private Halfspace Counting via Discrepancy", 2012. <https://arxiv.org/abs/1203.5453>
- Aleksandar Nikolov, Kunal Talwar, Li Zhang, "The Geometry of Differential Privacy", 2012. <https://arxiv.org/abs/1212.0297>
- Moritz Hardt, Kunal Talwar, "On the Geometry of Differential Privacy", STOC 2010. <https://arxiv.org/abs/0907.3754>
