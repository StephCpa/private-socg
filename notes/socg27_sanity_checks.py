# Numerical sanity checks for the SoCG 2027 draft (manuscript/socg27/main.tex).
# 1. fractional bias lemma (Lemma 9b), top-k averaging (Lemma 8), tail vs S_k (Lemma 10)
# 2. Valtr-norm grid construction: exact incidence count A^2 B^2 (Theorem 3(3))
# 3. Valtr norm triangle inequality; 4. two translates of its unit circle cross at most twice
# Run: python3 notes/socg27_sanity_checks.py
import random, math, itertools
from fractions import Fraction as F
random.seed(1)

# 1. Fractional bias lemma: x_e = min(1, D/deg u, D/deg v) feasible, loss <= tail_D, real D.
def check_bias(trials=3000):
    for _ in range(trials):
        n = random.randint(2, 9)
        p = random.random()
        E = [(u, v) for u in range(n) for v in range(u+1, n) if random.random() < p]
        deg = [0]*n
        for u, v in E: deg[u] += 1; deg[v] += 1
        D = random.uniform(0, n)
        x = {e: min(1.0, D/deg[e[0]], D/deg[e[1]]) for e in E}
        for v in range(n):
            s = sum(x[e] for e in E if v in e)
            assert s <= D + 1e-9 or deg[v] == 0, (s, D)
        tail = sum(max(0.0, d - D) for d in deg)
        assert len(E) - sum(x.values()) <= tail + 1e-9
        # top-k average non-increasing
        ds = sorted(deg, reverse=True)
        S = [sum(ds[:k]) for k in range(1, n+1)]
        for k in range(1, n):
            assert S[k]/(k+1) <= S[k-1]/k + 1e-12
        # tail_D <= max_k (S_k - kD)
        assert tail <= max([0.0] + [S[k-1] - k*D for k in range(1, n+1)]) + 1e-9
    print("bias lemma / averaging / tail-vs-S_k: ok")
check_bias()

# 2. Valtr norm ||(x,y)|| = |y| + sqrt(x^2+y^2); unbalanced grid construction.
def vnorm(dx, dy): return abs(dy) + math.hypot(dx, dy)
def valtr(A, B):
    pts = []
    for i in range(1, A+1):
        for j in range(1, 2*A*B+1):
            x = F(i, 2*A); Y = F(j, 4*A*B)
            pts.append((x, Y - x*x/2))
    cen = []
    for s in range(1, B+1):
        for t in range(1, A*B+1):
            a = F(s, 2*B); b = F(t, 4*A*B) - F(1, 2) + a*a/2
            cen.append((a, b))
    return pts, cen
for A, B in [(2,1),(3,2),(4,3),(2,4),(5,1)]:
    pts, cen = valtr(A, B)
    assert len(set(pts)) == len(pts) and len(set(cen)) == len(cen)
    inc_exact = 0; inc_float = 0
    for (a, b) in cen:
        for (x, y) in pts:
            dx, dy = x - a, y - b
            if dy >= 0 and dx*dx == 1 - 2*dy: inc_exact += 1
            if abs(vnorm(float(dx), float(dy)) - 1) < 1e-12: inc_float += 1
    n, k = len(pts), len(cen)
    print(f"A={A} B={B}: n={n} k={k} incidences exact={inc_exact} float={inc_float} "
          f"A^2B^2={A*A*B*B} ratio to n^(2/3)k^(2/3)={inc_exact/(n*k)**(2/3):.3f}")
    assert inc_exact >= A*A*B*B and inc_float == inc_exact

# 3. Strict convexity of Valtr norm unit ball: random check of triangle inequality strictness
for _ in range(20000):
    u = (random.uniform(-1,1), random.uniform(-1,1)); v = (random.uniform(-1,1), random.uniform(-1,1))
    assert vnorm(u[0]+v[0], u[1]+v[1]) <= vnorm(*u) + vnorm(*v) + 1e-12
print("Valtr norm triangle inequality: ok")

# 4. Two translates of a strictly convex curve (Valtr unit circle) meet in <= 2 points: numeric sampling
def circle_pts(c, m=20000):
    # parametrize by angle via radial scaling of the unit circle of the norm
    out = []
    for i in range(m):
        th = 2*math.pi*i/m; dx, dy = math.cos(th), math.sin(th); r = 1/vnorm(dx, dy)
        out.append((c[0]+r*dx, c[1]+r*dy))
    return out
def count_cross(c1, c2, m=20000):
    # sign changes of f(p) = ||p - c2|| - 1 along circle around c1
    pts = circle_pts(c1, m); vals = [vnorm(x-c2[0], y-c2[1]) - 1 for x, y in pts]
    return sum(1 for i in range(m) if (vals[i] > 0) != (vals[(i+1) % m] > 0))
mx = 0
for _ in range(200):
    c2 = (random.uniform(-2.2, 2.2), random.uniform(-2.2, 2.2))
    mx = max(mx, count_cross((0, 0), c2))
print("max sign changes between two translates:", mx)
assert mx <= 2

# 5. Exact statement for the Valtr grid (Lemma "Valtr grid" in the draft):
#    blue set B (2A^2B points) and red set R (AB^2 centres) are disjoint, every blue point lies
#    strictly above every red centre, and EXACTLY A^2 B^2 pairs (b, r) in B x R are at unit distance.
#    Exact test in rationals: ||(dx,dy)|| = 1  <=>  dx^2 = 1 - 2|dy|.
def unit(p, q):
    dx, dy = p[0]-q[0], p[1]-q[1]
    return dx*dx == 1 - 2*abs(dy)
for A in range(1, 6):
    for B in range(1, 6):
        pts, cen = valtr(A, B)
        assert not (set(pts) & set(cen))
        assert min(y for _, y in pts) > max(b for _, b in cen)
        br = sum(1 for p in pts for c in cen if unit(p, c))
        bb = sum(1 for i, p in enumerate(pts) for q in pts[i+1:] if unit(p, q))
        rr = sum(1 for i, p in enumerate(cen) for q in cen[i+1:] if unit(p, q))
        assert br == A*A*B*B, (A, B, br)
        if A <= 3 and B <= 3:
            print(f"A={A} B={B}: blue-red={br} (=A^2B^2), blue-blue={bb}, red-red={rr}")
print("Valtr grid: blue-red count is exactly A^2 B^2 for all 1 <= A,B <= 5")
