"""
Week 1-2 (線形代数): 内積・コサイン類似度・射影を NumPy で検算する。

実行:
  python3 scripts/linear_algebra_basics.py
"""

from __future__ import annotations

import math

import numpy as np


def dot(v: np.ndarray, u: np.ndarray) -> float:
    v = np.asarray(v, dtype=float)
    u = np.asarray(u, dtype=float)
    if v.shape != u.shape:
        raise ValueError(f"shape mismatch: v{v.shape} vs u{u.shape}")
    return float(np.dot(v, u))


def norm(v: np.ndarray) -> float:
    v = np.asarray(v, dtype=float)
    return float(np.linalg.norm(v))


def cosine_similarity(v: np.ndarray, u: np.ndarray) -> float:
    v = np.asarray(v, dtype=float)
    u = np.asarray(u, dtype=float)
    nv = norm(v)
    nu = norm(u)
    if nv == 0.0 or nu == 0.0:
        raise ValueError("cosine_similarity is undefined for zero vectors")
    return dot(v, u) / (nv * nu)


def projection_onto(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    proj_u(v) = (v·u)/(u·u) * u
    """
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    uu = dot(u, u)
    if uu == 0.0:
        raise ValueError("projection onto the zero vector is undefined")
    return (dot(v, u) / uu) * u


def angle_radians(v: np.ndarray, u: np.ndarray) -> float:
    """
    θ = arccos( (v·u)/(|v||u|) )
    """
    c = cosine_similarity(v, u)
    # 数値誤差で 1.0000000002 のようになることがあるのでクリップする
    c = float(np.clip(c, -1.0, 1.0))
    return float(math.acos(c))


def run_handcalc_example() -> None:
    # docs/notes/week1_linear_algebra_basics.md の手計算例に合わせる
    u = np.array([1.0, 2.0])
    v = np.array([2.0, 1.0])

    print("== 2次元の手計算例 u=(1,2), v=(2,1) ==")
    print(f"dot(v,u) = {dot(v,u):.6f}")
    print(f"||u|| = {norm(u):.6f}, ||v|| = {norm(v):.6f}")
    print(f"cosine_similarity(v,u) = {cosine_similarity(v,u):.6f}")
    print(f"theta(deg) = {math.degrees(angle_radians(v,u)):.6f}")
    print(f"proj_u(v) = {projection_onto(u,v)}")
    print()


def run_random_sanity_checks(seed: int = 0, d: int = 32, trials: int = 5) -> None:
    rng = np.random.default_rng(seed)
    print(f"== ランダム検算 seed={seed}, d={d}, trials={trials} ==")

    for t in range(trials):
        u = rng.normal(size=d)
        v = rng.normal(size=d)

        # 1) 正規化すると dot = cos になる
        u_hat = u / norm(u)
        v_hat = v / norm(v)
        cos1 = cosine_similarity(v, u)
        cos2 = dot(v_hat, u_hat)
        print(f"[{t}] |cos(v,u) - dot(v_hat,u_hat)| = {abs(cos1 - cos2):.3e}")

        # 2) 射影は u 方向ベクトルのスカラー倍になる
        proj = projection_onto(u, v)
        # proj と u の外積は d>3 では定義しにくいので、「直交成分が u と直交」を確認する
        residual = v - proj
        ortho = dot(residual, u)
        print(f"    dot(v - proj_u(v), u) = {ortho:.3e} (≈0)")

    print()


def main() -> None:
    run_handcalc_example()
    run_random_sanity_checks()


if __name__ == "__main__":
    main()

