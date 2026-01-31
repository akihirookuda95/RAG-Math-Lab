# 明日の学習 TODO（Week 1-2: 線形代数）

想定所要時間：**2〜3 時間**

## 1) 読む（30 分）

- [ ] `docs/week1_linear_algebra_basics.md` の **「2. 内積」→「3. コサイン類似度」** を通読
- [ ] 各式を **日本語で 1 行**に言い換える（自分の言葉で）
  - [ ] $v\cdot u = \|v\|\,\|u\|\,\cos\theta$
  - [ ] $\cos\theta = \dfrac{v\cdot u}{\|v\|\,\|u\|}$
  - [ ] $\hat{v} = \dfrac{v}{\|v\|}$（正規化）

## 2) 手計算（45 分）

- [ ] `docs/week1_linear_algebra_basics.md` の **「4. 手計算で確認」** を、途中式込みで自力で計算
  - [ ] $u=(1,2),\ v=(2,1)$
  - [ ] 内積 $v\cdot u$
  - [ ] ノルム $\|u\|,\ \|v\|$
  - [ ] コサイン類似度 $\cos\theta$
  - [ ] 角度 $\theta=\arccos(\cos\theta)$（度数も）

## 3) 射影（30 分）

- [ ] `docs/week1_linear_algebra_basics.md` の **「5. 射影」** を、途中式込みで手計算
  - [ ] $\operatorname{proj}_u(v) = \dfrac{v\cdot u}{u\cdot u}\,u$
- [ ] 射影が「$u$ 方向成分」だと言える理由を **自分の言葉で 1 段落**書く

## 4) 検算（15 分）

- [ ] `scripts/linear_algebra_basics.py` を実行して、手計算と一致することを確認
  - [ ] `dot(v,u)`
  - [ ] `cosine_similarity(v,u)`
  - [ ] `theta(deg)`
  - [ ] `proj_u(v)`

## 明日終わったら、ここに貼るもの（次回の質問素材）

- [ ] 「内積の式」「コサイン類似度の式」「正規化の式」の **1 行言い換え**
- [ ] 射影の **1 段落説明**
