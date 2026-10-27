# 方法专题｜反常积分审敛全景心法（p判据颠倒律、原函数1-p指数法与对数临界凑微分）

- **所属模块**：高等数学 / 一元函数积分学 / 反常积分
- **核心痛点**：为什么无穷远是 $p>1$，瑕点却是 $p<1$？两者为何颠倒？对数临界项 $x(\ln x)^q$ 的敛散性如何用最本质的方式秒判？
- **沉淀日期**：2026-10-21

---

## 一、破局总纲：核心全在原函数的指数 $1-p$

无论是无穷积分还是瑕积分，被积函数的核心骨架都是幂函数 $\frac{1}{x^p} = x^{-p}$。  
当 $p \neq 1$ 时，其原函数统一形式为：
$$F(x) = \frac{x^{1-p}}{1-p}$$

**收敛还是发散，完全由指数 $1-p$ 的正负（即 $x$ 最终留在分子还是分母）说了算！**

```
                       ┌── 指数 1-p < 0 (即 p > 1) ── x在分母 ── 代入+∞趋于0 ──【无穷积分收敛】
原函数 x^(1-p) ───────┤
                       └── 指数 1-p > 0 (即 p < 1) ── x在分子 ── 代入0得到0 ───【瑕积分收敛】
```

---

## 二、两大基本模型的底层推导

### 1. 无穷积分（横向无限长走廊）：$\int_1^{+\infty} \frac{1}{x^p} dx$
- **目标**：代入上限 $+\infty$ 时，结果必须是有限常数：
  $$\lim_{x \to +\infty} x^{1-p} < +\infty$$
- **机理**：$x$ 必须被压在**分母**上，才能在 $x \to +\infty$ 时衰减为 $0$。
- **条件**：指数 $1-p < 0 \implies \mathbf{p > 1}$。
  - 例：$p = 2 \implies F(x) = -\frac{1}{x} \xrightarrow{x\to+\infty} 0$（**收敛**）。
  - 例：$p = \frac{1}{2} \implies F(x) = 2\sqrt{x} \xrightarrow{x\to+\infty} +\infty$（**发散**）。

---

### 2. 瑕积分（纵向无限高柱子）：$\int_0^1 \frac{1}{x^p} dx$（$x=0$ 为瑕点）
- **目标**：代入下限 $0$ 时，结果不能爆成无穷大：
  $$\lim_{x \to 0^+} x^{1-p} \neq \infty$$
- **机理**：$x$ 必须留在**分子**上，代入 $0$ 才能得到 $0$（不能被除以 $0$ 爆掉）。
- **条件**：指数 $1-p > 0 \implies \mathbf{p < 1}$。
  - 例：$p = \frac{1}{2} \implies F(x) = 2\sqrt{x} \xrightarrow{x\to 0^+} 0$（**收敛**）。
  - 例：$p = 2 \implies F(x) = -\frac{1}{x} \xrightarrow{x\to 0^+} -\infty$（**发散**）。

---

### 3. 分水岭死穴：$p = 1$ 两头皆发散
当 $p = 1$ 时，原函数是 $\ln x$：
- 无穷远：$\ln(+\infty) = +\infty$ $\implies$ **发散**；
- 瑕点 $0$：$\ln(0^+) = -\infty$ $\implies$ **发散**。
- **结论**：$\frac{1}{x}$ 是无穷与瑕点的公共临界发散线。

---

## 三、对数临界项秒杀：凑微分化归律

当分母卡在 $p=1$ 发散边缘时，常乘入对数项 $\ln x$：
$$\int \frac{1}{x (\ln x)^q} dx$$

### 破局动作：凑微分把 $\ln x$ 视为整体 $u$
利用 $(\ln x)' = \frac{1}{x}$，直接凑微分：
$$\frac{1}{x} dx = d(\ln x)$$
原式直接化为：
$$\int \frac{1}{(\ln x)^q} d(\ln x) \xrightarrow{u = \ln x} \int \frac{1}{u^q} du$$

### 无论在无穷远还是瑕点，统一归结为 $u \to +\infty$：
1. **无穷远**（$x \to +\infty$）：$u = \ln(+\infty) \to +\infty$；
2. **瑕点**（$x \to 0^+$）：令 $u = -\ln x \implies u \to -\ln(0^+) = +\infty$。

在 $u \to +\infty$ 处，本质就是标准的无穷积分 $\int \frac{1}{u^q} du$：
$$\mathbf{q > 1 \iff 收敛，\quad q \le 1 \iff 发散}$$

- **验算**：
  - $q = 1 \implies$ 原函数 $\ln(\ln x) \xrightarrow{x\to+\infty} +\infty$（救不活，发散）；
  - $q = 2 \implies$ 原函数 $-\frac{1}{\ln x} \xrightarrow{x\to+\infty} 0$（成功收敛）。

---

## 四、审敛红线：独立截断 vs 柯西主值陷阱

1. **反常积分的定义是一票否决制**：
   $$\int_{-\infty}^{+\infty} f(x)dx \stackrel{\text{def}}{=} \lim_{A\to-\infty}\int_A^c f(x)dx + \lim_{B\to+\infty}\int_c^B f(x)dx$$
   左右两侧极限**必须各自独立存在**。只要有一端发散，全盘发散！

2. **柯西主值绝对不能代替普通反常积分收敛**：
   $$\lim_{R\to+\infty} \int_{-R}^R f(x)dx \quad \text{（柯西主值，捆绑对称变化率）}$$
   - **杀手反例**：$f(x) = \sin x$ 或 $f(x) = x$（奇函数）。
   - 对称主值恒为 $0$，但其实际反常积分 $\int_{-\infty}^{+\infty} \sin x dx$ 彻底发散！
