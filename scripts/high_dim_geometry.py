"""
高次元幾何（次元の呪い）を体感する最短実験（写経用）

目的:
- 次元 d を増やすと、次の2つが「集中」していくことを観察する
  1) ランダムな2ベクトルのコサイン類似度 cosθ が 0 付近に集中（ほぼ直交）
  2) ランダムな2ベクトルのユークリッド距離 ||u - v|| が平均の周りに集中（距離の集中）

この実験で見たいこと（直観）:
- 高次元では「距離があまり差にならない」現象が起きやすい
- 一方で、正規化して角度（= コサイン類似度）を見ると「方向の違い」を扱いやすい

実行:
  python3 scripts/high_dim_geometry.py

出力の見方:
- d を上げていくと
  - cos の std が小さくなり、cos が 0 に寄っていく（平均はほぼ0）
  - dist の std も相対的に小さくなり、dist が「だいたい同じ値」に寄っていく

注意:
- このファイルは「写経」前提です。下の TODO 部分を、あなたがコードを書き写して完成させてください。
"""

import numpy as np


def unit(x: np.ndarray) -> np.ndarray:
  """
  正規化する関数
  """
  norms = np.linalg.norm(x, axis=1, keepdims=True) # shape: (n, 1)
  return x / norms


def main():
  rng = np.random.default_rng(0)
  n = 5000
  dims = [2, 8, 32, 128, 512, 2048, 8192]

  for d in dims:
    # (n, d) の乱数行列: n本のd次元ベクトル
    u = rng.normal(size=(n, d))
    v = rng.normal(size=(n, d))

    uh = unit(u)
    vh = unit(v)

    cos = np.sum(uh * vh, axis=1) # shape: (n,)
    dist = np.linalg.norm(u - v, axis=1) # shape: (n,)

    print(
              f"d={d:4d} | "
              f"cos mean={cos.mean(): .4f} std={cos.std(): .4f} | "
              f"dist mean={dist.mean(): .4f} std={dist.std(): .4f}"
          )

if __name__ == "__main__":
  main()

