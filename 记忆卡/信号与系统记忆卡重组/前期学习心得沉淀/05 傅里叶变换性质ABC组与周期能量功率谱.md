## You

傅里叶变换的性质 A组

①线性性质

②对称性

③尺度变换性质

④时移性质

时移+尺度变换

⑤频移性质


傅里叶变换的性质 B组

①时域微分性质和应用

②频域微分性质

③时域卷积性质（证明）

④频域卷积（证明）

---

## AI Studio

我们严格按照你列出的 **A 组** 和 **B 组** 清单，把每一条性质的**数学表达式、物理含义、推导/证明过程**系统地讲清楚。

统一约定：设 $f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} F(j\omega)$。

---

## 傅里叶变换的性质 · A 组（基本变换与搬移）

### ① 线性性质（Linearity）
* **公式**：若 $f_1(t) \leftrightarrow F_1(j\omega)$，$f_2(t) \leftrightarrow F_2(j\omega)$，则对任意常数 $a, b$：
  $$a f_1(t) + b f_2(t) \stackrel{\mathcal{F}}{\longleftrightarrow} a F_1(j\omega) + b F_2(j\omega)$$
* **由来与含义**：因为傅里叶变换本质上是定积分，而积分满足线性叠加律。信号在时域按比例相加，在频域的频谱密度也按完全相同的比例相加，彼此不会产生新的频率成分。

---

### ② 对称性 / 对偶性（Duality / Symmetry）
* **公式**：若 $f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} F(j\omega)$，则把频域表达式里的自变量 $\omega$ 换成 $t$（保留 $j$）作为新的时域信号，它的变换满足：
  $$F(jt) \stackrel{\mathcal{F}}{\longleftrightarrow} 2\pi f(-\omega)$$
  *(注：若教材习惯简写成 $F(\omega)$，则记为 $F(t) \leftrightarrow 2\pi f(-\omega)$；若 $f(t)$ 是偶函数，则右边就是 $2\pi f(\omega)$。)*
* **2 行由来**：在逆变换公式 $f(t) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} F(j\omega) e^{j\omega t} d\omega$ 中，先将两边乘 $2\pi$ 并令 $t \to -t$，得到 $2\pi f(-t) = \int_{-\infty}^{+\infty} F(j\omega) e^{-j\omega t} d\omega$；然后把积分变量 $\omega$ 与外面的 $t$ 互换名字，即得 $2\pi f(-\omega) = \int_{-\infty}^{+\infty} F(jt) e^{-j\omega t} dt = \mathcal{F}\{F(jt)\}$。
* **意义**：揭示了**时域与频域结构完全对称**。每知道一个变换对，对调一下自变量就能免费得到另一个变换对（例如从 $\delta(t) \leftrightarrow 1$ 直接得 $1 \leftrightarrow 2\pi\delta(\omega)$；从门信号 $\leftrightarrow \text{Sa}$ 直接得 $\text{Sa} \leftrightarrow$ 门信号）。

---

### ③ 尺度变换性质（Time Scaling）
* **公式**（$a$ 为非零实常数）：
  $$f(at) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{|a|} F\left(j\frac{\omega}{a}\right)$$
  * *特例（时间反转）*：当 $a = -1$ 时，$f(-t) \leftrightarrow F(-j\omega)$。
* **由来**：当 $a > 0$ 时，令 $u = at$（$dt = \frac{du}{a}$）：
  $$\int_{-\infty}^{+\infty} f(at) e^{-j\omega t} dt = \frac{1}{a} \int_{-\infty}^{+\infty} f(u) e^{-j\left(\frac{\omega}{a}\right)u} du = \frac{1}{a} F\left(j\frac{\omega}{a}\right)$$
  当 $a < 0$ 时，积分上下限会颠倒，换回来多出一个负号，把 $-\frac{1}{a}$ 合并即得 $\frac{1}{|a|}$。
* **物理含义（时频反比规律）**：
  * 当 $|a| > 1$（比如 $f(2t)$），时域波形**被压缩变窄** $\implies$ 频域 $\frac{\omega}{a}$ 让频谱曲线**横向拉宽**（包含更高频率），同时幅度 $\frac{1}{|a|}$ **纵向压矮**（因为时域面积缩小了，根据零点面积规律，频谱中心高度也等比例缩小）。
  * 一句话：**时域压缩，频域展宽且幅度变矮；时域展宽，频域压缩且幅度变高。**

---

### ④ 时移性质（Time Shifting）& 时移+尺度变换

#### 1. 纯时移性质
* **公式**：
  $$f(t - t_0) \stackrel{\mathcal{F}}{\longleftrightarrow} F(j\omega) e^{-j\omega t_0}$$
* **由来**：令 $u = t - t_0$，则 $\int_{-\infty}^{+\infty} f(u) e^{-j\omega(u+t_0)} du = e^{-j\omega t_0} \int_{-\infty}^{+\infty} f(u) e^{-j\omega u} du = F(j\omega) e^{-j\omega t_0}$。
* **物理含义**：信号在时间上平移 $t_0$，**幅度谱 $|F(j\omega)|$ 完全不变**（因为 $|e^{-j\omega t_0}|=1$），只有**相位谱**整体叠加了一个随频率线性倾斜的相移 $-\omega t_0$。

#### 2. 时移 + 尺度变换（组合变换：$f(at - b)$）
这是最容易出错的组合操作，**核心原则是：所有变换永远只针对自变量 $t$ 本身进行！** 两种等价推法：

* **方法 A（先尺度，后时移——推荐，最稳）**：
  先把 $a$ 从括号里提出来，看清到底平移了多少：
  $$f(at - b) = f\left[a\left(t - \frac{b}{a}\right)\right]$$
  1. 先对 $f(t)$ 做尺度变换（$t \to at$）：得到 $\frac{1}{|a|} F\left(j\frac{\omega}{a}\right)$；
  2. 再把上一步的新信号整体平移 $\frac{b}{a}$（即 $t \to t - \frac{b}{a}$）：直接乘上延迟因子 $e^{-j\omega\frac{b}{a}}$。
  $$\boxed{f(at - b) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{|a|} F\left(j\frac{\omega}{a}\right) e^{-j\omega \frac{b}{a}}}$$

* **方法 B（先时移，后尺度——注意 $\omega$ 也要跟着变）**：
  1. 先做时移 $f(t - b) \longleftrightarrow F(j\omega) e^{-j\omega b}$；
  2. 再做尺度变换（$t \to at$）：把**整个频域表达式中所有的 $\omega$** 都替换成 $\frac{\omega}{a}$，并乘以 $\frac{1}{|a|}$：
     $$\frac{1}{|a|} F\left(j\frac{\omega}{a}\right) e^{-j\left(\frac{\omega}{a}\right)b} = \frac{1}{|a|} F\left(j\frac{\omega}{a}\right) e^{-j\omega \frac{b}{a}}$$
  *(常见错误是在第二步只换了 $F$ 里的 $\omega$，忘了把指数上的 $\omega b$ 也换成 $\frac{\omega}{a}b$！)*

---

### ⑤ 频移性质（Frequency Shifting / 调制特性）
* **公式**：
  $$f(t) e^{j\omega_0 t} \stackrel{\mathcal{F}}{\longleftrightarrow} F[j(\omega - \omega_0)]$$
  $$f(t) e^{-j\omega_0 t} \stackrel{\mathcal{F}}{\longleftrightarrow} F[j(\omega + \omega_0)]$$
* **由来**：直接代入定义：$\int_{-\infty}^{+\infty} f(t) e^{j\omega_0 t} e^{-j\omega t} dt = \int_{-\infty}^{+\infty} f(t) e^{-j(\omega - \omega_0)t} dt = F[j(\omega - \omega_0)]$。
* **典型应用（调幅调制）**：给信号乘以余弦波 $\cos(\omega_0 t) = \frac{1}{2}(e^{j\omega_0 t} + e^{-j\omega_0 t})$，则：
  $$f(t)\cos(\omega_0 t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{2}\Big( F[j(\omega - \omega_0)] + F[j(\omega + \omega_0)] \Big)$$
* **物理含义**：在时域乘以一个高频旋转因子/载波，效果就是**把原信号的整张频谱在频率轴上原封不动地向左或向右搬家**（通信里把低频声音搬到高频无线信道发射的原理）。

---

## 傅里叶变换的性质 · B 组（微积分与卷积）

### ① 时域微分性质和应用

* **公式**：
  $$\frac{df(t)}{dt} \stackrel{\mathcal{F}}{\longleftrightarrow} j\omega \, F(j\omega)$$
  推广到 $n$ 阶导数：
  $$\frac{d^n f(t)}{dt^n} \stackrel{\mathcal{F}}{\longleftrightarrow} (j\omega)^n F(j\omega)$$
* **由来**：对逆变换 $f(t) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} F(j\omega) e^{j\omega t} d\omega$ 两边直接对 $t$ 求导，每次求导都会从 $e^{j\omega t}$ 上掉下来一个 $j\omega$ 因子。
  *(注：从正变换做分部积分也可得到，前提是 $t \to \pm\infty$ 时 $f(t) \to 0$。)*

* **两大核心应用**：
  1. **简化分段线性信号的傅里叶变换计算**：
     遇到梯形波、三角形波、锯齿波等分段折线信号，直接做积分需要算多次分部积分。利用微分性质，连续对 $f(t)$ 求导 1 次或 2 次，直到波形变为简单的矩形脉冲或冲激 $\delta(t)$，求出导数的变换后，直接除以 $(j\omega)^n$ 即可得到原变换。
     *(注意：如果原信号在无穷远处不衰减到 $0$——比如阶跃 $u(t)$——求导会丢失直流分量 $\pi\delta(\omega)$，此时不能直接除以 $j\omega$ 了事。)*
  2. **求解线性常系数微分方程（LTI 系统频域法）**：
     对于物理系统方程 $a_2 y''(t) + a_1 y'(t) + a_0 y(t) = b_1 x'(t) + b_0 x(t)$，两边同取傅里叶变换，把 $\frac{d}{dt}$ 全换成 $j\omega$，微分方程瞬间退化为初中代数方程：
     $$[(j\omega)^2 a_2 + j\omega a_1 + a_0] Y(j\omega) = (j\omega b_1 + b_0) X(j\omega)$$
     直接解出系统频率响应 $H(j\omega) = \frac{Y(j\omega)}{X(j\omega)}$。

---

### ② 频域微分性质（Frequency Differentiation）
* **公式**：
  $$(-jt) f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{d F(j\omega)}{d\omega}$$
  两边同乘 $j$ 整理成最常用形式：
  $$t \, f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} j \frac{d F(j\omega)}{d\omega}$$
  推广到 $n$ 次方：
  $$t^n f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} j^n \frac{d^n F(j\omega)}{d\omega^n}$$
* **由来**：直接对正变换定义式两边对 $\omega$ 求导（求导与积分交换顺序）：
  $$\frac{d F(j\omega)}{d\omega} = \frac{d}{d\omega}\int_{-\infty}^{+\infty} f(t) e^{-j\omega t} dt = \int_{-\infty}^{+\infty} [-jt \, f(t)] e^{-j\omega t} dt = \mathcal{F}\{-jt \, f(t)\}$$
  两边同时乘以 $j$（利用 $j \cdot (-j) = 1$），即得 $t f(t) \leftrightarrow j \frac{d F(j\omega)}{d\omega}$。
* **用途**：专门用来求时域乘以 $t$ 或 $t^n$ 的信号频谱（例如从 $e^{-at}u(t) \leftrightarrow \frac{1}{a+j\omega}$ 一秒求导得出 $t e^{-at}u(t) \leftrightarrow j \frac{d}{d\omega}\left(\frac{1}{a+j\omega}\right) = \frac{1}{(a+j\omega)^2}$）。

---

### ③ 时域卷积性质（含证明）

* **结论公式**：
  $$f_1(t) * f_2(t) \stackrel{\mathcal{F}}{\longleftrightarrow} F_1(j\omega) \cdot F_2(j\omega)$$
  *(时域卷积，频域直接相乘。)*

* **标准证明过程**：
  1. 根据卷积定义和傅里叶变换定义写出：
     $$\mathcal{F}\{f_1(t) * f_2(t)\} = \int_{-\infty}^{+\infty} \left[ \int_{-\infty}^{+\infty} f_1(\tau) f_2(t - \tau) d\tau \right] e^{-j\omega t} dt$$
  2. 交换双重积分的积分次序（先对 $t$ 积分，再对 $\tau$ 积分）：
     $$= \int_{-\infty}^{+\infty} f_1(\tau) \left[ \int_{-\infty}^{+\infty} f_2(t - \tau) e^{-j\omega t} dt \right] d\tau$$
  3. 对内层关于 $t$ 的积分作变量代换：令 $u = t - \tau$（则 $t = u + \tau$，$dt = du$）：
     $$= \int_{-\infty}^{+\infty} f_1(\tau) \left[ \int_{-\infty}^{+\infty} f_2(u) e^{-j\omega(u + \tau)} du \right] d\tau$$
     把与积分变量 $u$ 无关的 $e^{-j\omega\tau}$ 提出内层积分：
     $$= \int_{-\infty}^{+\infty} f_1(\tau) e^{-j\omega\tau} \left[ \int_{-\infty}^{+\infty} f_2(u) e^{-j\omega u} du \right] d\tau$$
  4. 注意到内层括号里正是 $F_2(j\omega)$（它与 $\tau$ 无关，可提出外层积分）：
     $$= F_2(j\omega) \int_{-\infty}^{+\infty} f_1(\tau) e^{-j\omega\tau} d\tau = F_1(j\omega) \cdot F_2(j\omega)$$
  **证毕。**

---

### ④ 频域卷积性质（含证明）

* **结论公式**：
  $$f_1(t) \cdot f_2(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{2\pi} \Big[ F_1(j\omega) * F_2(j\omega) \Big] = \frac{1}{2\pi} \int_{-\infty}^{+\infty} F_1(j\theta) F_2[j(\omega - \theta)] d\theta$$
  *(时域相乘，频域卷积并乘以 $\frac{1}{2\pi}$。)*

* **标准证明过程**：
  1. 根据傅里叶正变换定义写出乘积信号 $f_1(t)f_2(t)$ 的变换：
     $$\mathcal{F}\{f_1(t) \cdot f_2(t)\} = \int_{-\infty}^{+\infty} f_1(t) f_2(t) e^{-j\omega t} dt$$
  2. 把其中的 $f_1(t)$ 用它的**傅里叶逆变换**展开替换（积分变量改用 $\theta$ 避免与 $\omega$ 混淆）：
     $$f_1(t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} F_1(j\theta) e^{j\theta t} d\theta$$
     代回上式得：
     $$\mathcal{F}\{f_1(t) \cdot f_2(t)\} = \int_{-\infty}^{+\infty} \left[ \frac{1}{2\pi} \int_{-\infty}^{+\infty} F_1(j\theta) e^{j\theta t} d\theta \right] f_2(t) e^{-j\omega t} dt$$
  3. 交换积分次序（先对 $t$ 积分，再对 $\theta$ 积分），并把 $\frac{1}{2\pi}$ 和 $F_1(j\theta)$ 提到外层：
     $$= \frac{1}{2\pi} \int_{-\infty}^{+\infty} F_1(j\theta) \left[ \int_{-\infty}^{+\infty} f_2(t) e^{-j(\omega - \theta)t} dt \right] d\theta$$
  4. 观察内层中括号里的积分，它正好就是 $f_2(t)$ 在频率 $(\omega - \theta)$ 处的傅里叶变换 **$F_2[j(\omega - \theta)]$**！于是得到：
     $$= \frac{1}{2\pi} \int_{-\infty}^{+\infty} F_1(j\theta) F_2[j(\omega - \theta)] d\theta = \frac{1}{2\pi} \Big[ F_1(j\omega) * F_2(j\omega) \Big]$$
  **证毕。**

*(注：这两条卷积性质互为对偶——时域卷积变乘法没有 $\frac{1}{2\pi}$；时域乘法变卷积多了 $\frac{1}{2\pi}$，是因为逆变换带着 $\frac{1}{2\pi}$ 系数。)*

---

## You

对称性这个，能不能给我讲一下怎么用

时移频移这方面好像正负关系和傅里叶级数不一样，傅里叶级数好像都是负对负？

微分性质有点难记

---

## AI Studio

你的这三个问题都抓得非常准，而且刚好都是学到这一章时最容易卡壳的地方。我们一个一个彻底理顺：

---

### 问题一：对称性（对偶性）怎么用？

公式是：若 $f(t) \longleftrightarrow F(j\omega)$，则 $F(jt) \longleftrightarrow 2\pi f(-\omega)$。

实际做题或推导时，根本不用去想抽象的 $F(jt)$ 是啥意思，直接按**“无脑两步互换法”**套就行：

> **核心用法：当你遇到一个长得很像“常见频谱”的时间信号，想求它的傅里叶变换时：**
> 1. 先找一个已知变换对 $f(t) \longleftrightarrow F(j\omega)$，让右边 $F(j\omega)$ 长得跟你要算的信号一模一样；
> 2. **把右边式子里的 $\omega$ 直接改写成 $t$，搬到左边；**
> 3. **把左边式子里的 $t$ 直接改写成 $-\omega$，搬到右边，并在最前面乘个 $2\pi$！**

*(注意：只换字母 $\omega \leftrightarrow t$，原先式子里的虚数单位 $j$ 该留着还得留着！)*

#### 看三个真实使用例子，一看就会：

* **用法 1：求信号 $\frac{1}{a + jt}$ 的傅里叶变换**（直接积分根本积不出来！）
  1. 找已知对：哪个公式的右边长得像 $\frac{1}{a+jt}$？一眼看出是单边指数：
     $$e^{-at} u(t) \longleftrightarrow \frac{1}{a + j\omega}$$
  2. 右边的 $\omega$ 改写成 $t$ 放左边（$j$ 保留）；左边的 $t$ 改写成 $-\omega$ 放右边并乘 $2\pi$：
     $$\frac{1}{a + jt} \longleftrightarrow 2\pi e^{-a(-\omega)} u(-\omega) = \mathbf{2\pi e^{a\omega} u(-\omega)}$$
  *(一秒钟出答案，避开了复变函数留数积分！)*

* **用法 2：求信号 $\frac{2a}{a^2 + t^2}$ 的傅里叶变换**
  1. 找已知对：双边指数 $e^{-a|t|} \longleftrightarrow \frac{2a}{a^2 + \omega^2}$。
  2. 互换字母并乘 $2\pi$：
     $$\frac{2a}{a^2 + t^2} \longleftrightarrow 2\pi e^{-a|-\omega|} = \mathbf{2\pi e^{-a|\omega|}}$$
  *(因为偶函数 $|-\omega| = |\omega|$，负号直接吃掉。)*

* **用法 3：求信号 $\text{Sa}(At)$ 的傅里叶变换**
  1. 找已知对：宽为 $2A$ 的门信号 $G_{2A}(t) \longleftrightarrow 2A \, \text{Sa}(A\omega)$。
  2. 互换字母并乘 $2\pi$：
     $$2A \, \text{Sa}(At) \longleftrightarrow 2\pi G_{2A}(-\omega) = 2\pi G_{2A}(\omega)$$
  3. 两边同时除以 $2A$，即得 $\text{Sa}(At) \longleftrightarrow \frac{\pi}{A} G_{2A}(\omega)$。

---

### 问题二：时移、频移的正负关系，和傅里叶级数一样吗？

先直接给结论：**一模一样，没有任何变化！**
你之所以感觉“级数好像都是负对负”，可能是记混了级数里的频移公式。我们把它们摆在一起对比一下：

| 性质 | 傅里叶级数（FS） | 傅里叶变换（FT） | 规律 |
| :--- | :--- | :--- | :--- |
| **时移** | $x(t - t_0) \longleftrightarrow a_k e^{\mathbf{-}jk\omega_0 t_0}$ | $f(t - t_0) \longleftrightarrow F(j\omega) e^{\mathbf{-}j\omega t_0}$ | **同号**（负对负，正对正） |
| **频移** | $e^{\mathbf{+}jM\omega_0 t} x(t) \longleftrightarrow a_{k \mathbf{-} M}$ | $e^{\mathbf{+}j\omega_0 t} f(t) \longleftrightarrow F[j(\omega \mathbf{-} \omega_0)]$ | **反号**（正对负，负对正） |

你看，**不管是级数还是变换：**
* **时移永远是“同号”**：左边 $t - t_0$（负），右边指数就是 $-j\omega t_0$（负）。
* **频移永远是“反号”**：左边乘 $e^{+j\omega_0 t}$（正），右边频谱就是 $\omega - \omega_0$（负）；左边乘 $e^{-j\omega_0 t}$（负），右边频谱就是 $\omega + \omega_0$（正）。

#### 怎么理解并记住这个“一时同号、一时反号”，永远不混淆？
用图形平移的常识一句话就能看穿：
1. **看“频移”为什么是反号**：
   你想把一张频谱图**向右（往正高频方向）平移 $+\omega_0$**。
   * 在函数画图里，“图像往右移 $\omega_0$”的数学写法就是把 $\omega$ 变成 **$\omega - \omega_0$**（即所谓的“左加右减”）。
   * 而物理上要让一个信号的频率**升高 $+\omega_0$**，时域里必须乘一个**正方向旋转**的载波 **$e^{+j\omega_0 t}$**！
   * 所以：“正旋转波 $e^{+j\omega_0 t}$” $\longleftrightarrow$ “频谱右移 $F[j(\omega - \omega_0)]$”，一个写着 $+$，一个写着 $-$。
2. **看“时移”为什么是同号**：
   你想把时域波形**向右（延迟）平移 $t_0$**，数学上写成 $f(t - t_0)$；而时间延迟在相位上意味着**相位滞后（角度减小）**，所以右边乘的是负角度 $e^{-j\omega t_0}$。两边刚好都是负号！

---

### 问题三：微分性质有点难记，怎么记？

很多人记混，是因为有的书在频域微分上写 $(-jt)f(t) \leftrightarrow \frac{dF}{d\omega}$，有的写 $tf(t) \leftrightarrow j\frac{dF}{d\omega}$，正负号和 $j$ 到底在哪边非常容易乱。

这里给你一个**惊人对称、极其好记的统一写法**——把两边的式子都整理成**“左边只干纯实数的活，把所有的 $j$ 全扔到右边”**：

$$\text{时域微分：} \quad \frac{d^n f(t)}{dt^n} \longleftrightarrow \mathbf{j^n} \omega^n F(j\omega)$$
$$\text{频域微分：} \quad t^n f(t) \longleftrightarrow \mathbf{j^n} \frac{d^n F(j\omega)}{d\omega^n}$$

你看它们在一阶（$n=1$）时的样子：
1. **$\frac{df(t)}{dt} \longleftrightarrow \mathbf{+j} \, \omega F(j\omega)$**
2. **$t \, f(t) \longleftrightarrow \mathbf{+j} \, \frac{d F(j\omega)}{d\omega}$**

**只需要死记一句话：**
> **只要左边不带任何负号和 $j$（纯粹求导 $f'(t)$，或者纯粹乘 $t$），右边最前面永远都是乘一个【正的 $+j$】（$n$ 阶就乘 $j^n$）！**

#### 万一考场上还是不确定是 $+j$ 还是 $-j$，教你 2 秒钟现场验算：
只要记住：**正变换里指数是 $e^{-j\omega t}$，逆变换里指数是 $e^{+j\omega t}$**。
1. **验算时域微分**（对 $t$ 求导 $\to$ 找左边是 $f(t)$ 的**逆变换** $e^{+j\omega t}$）：
   对 $e^{+j\omega t}$ 求一次 $t$ 的导数，指数上掉下来的是 **$+j\omega$** $\implies$ 所以是 $+j\omega F(j\omega)$。
2. **验算频域微分**（对 $\omega$ 求导 $\to$ 找左边是 $F(j\omega)$ 的**正变换** $e^{-j\omega t}$）：
   对 $e^{-j\omega t}$ 求一次 $\omega$ 的导数，掉下来的是 **$-jt$**，所以 $(-jt)f(t) \leftrightarrow \frac{dF}{d\omega}$；为了把左边变成纯粹的 $t f(t)$，两边同乘以 $+j$（因为 $j \cdot (-j) = 1$），于是右边就多出了 **$+j$** $\implies$ $t f(t) \leftrightarrow +j \frac{dF}{d\omega}$。

---

## You

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

[Attachment: image]

傅里叶变换性质 C组

①频域微分

②时域积分

③频域积分性质

④共轭

⑤奇偶虚实



能量谱相关

1.能量谱密度定义

2.帕萨瓦尔能量定理

3.维纳xinqing

功率谱相关综合
卷积和互相关函数关系

互相关、自相关的傅里叶变换

能量谱密度def


互相关函数、自相关函数前提和def
功率谱相关综合
能量谱相关

1.能量谱密度定义

2.帕萨瓦尔能量定理

3.维纳xinqing

---

## AI Studio

你上传的这些图片笔记非常有条理，把**周期信号的频域桥梁**、**相关函数**、**能量谱**和**功率谱**的逻辑链条全都串联起来了。

我把你的**文字大纲**和**图片里的笔记**合并整理成**四大块**，按逻辑顺序给你彻底讲透、串成一张完整的知识网：

---

## 第一块：傅里叶变换性质 · C 组

### ① 频域微分性质
$$(-jt) f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{d F(j\omega)}{d\omega} \quad \Longleftrightarrow \quad t \, f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} j \frac{d F(j\omega)}{d\omega}$$
*(n 阶：$t^n f(t) \longleftrightarrow j^n \frac{d^n F(j\omega)}{d\omega^n}$。原理：对正变换 $\int f(t)e^{-j\omega t}dt$ 两边对 $\omega$ 求导，指数掉出 $-jt$。)*

---

### ② 时域积分性质
$$\int_{-\infty}^{t} f(\tau) d\tau \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{F(j\omega)}{j\omega} + \pi F(j0)\delta(\omega)$$
* **为什么后面多了一个 $\pi F(j0)\delta(\omega)$？**
  因为积分相当于把 $f(t)$ 与阶跃信号 $u(t)$ 做卷积：$\int_{-\infty}^{t} f(\tau)d\tau = f(t) * u(t)$。
  套用时域卷积性质，乘以 $u(t)$ 的变换 $\left(\frac{1}{j\omega} + \pi\delta(\omega)\right)$：
  $$F(j\omega) \cdot \left(\frac{1}{j\omega} + \pi\delta(\omega)\right) = \frac{F(j\omega)}{j\omega} + \pi F(j0)\delta(\omega)$$
* **物理含义**：如果原信号总面积不为零（即 $F(j0) \neq 0$），从 $-\infty$ 积分到 $t$ 会在正半轴留下一个永久的直流台阶，从而在 $\omega=0$ 处产生冲激 $\pi F(j0)\delta(\omega)$；只有当信号总面积 $F(j0) = 0$ 时，积分才简化为纯粹的 $\frac{F(j\omega)}{j\omega}$。

---

### ③ 频域积分性质（与时域积分完全对偶）
$$\frac{f(t)}{-jt} + \pi f(0)\delta(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \int_{-\infty}^{\omega} F(j\xi) d\xi$$
*(注：$\frac{1}{-j} = j$，所以左边也可写成 $j\frac{f(t)}{t} + \pi f(0)\delta(t)$。)*
* **推导由来**：$\int_{-\infty}^{\omega} F(j\xi)d\xi = F(j\omega) * u(\omega)$，由频域卷积性质（乘积 $\leftrightarrow \frac{1}{2\pi}$ 卷积）即可反推出左边。
* **记忆对比**：时域微/积分除以/乘以 **$+j\omega$**，频域微/积分除以/乘以 **$-jt$**（或把 $j$ 移到对面变符号）。

---

### ④ 共轭性质
$$f^*(t) \stackrel{\mathcal{F}}{\longleftrightarrow} F^*(-j\omega)$$
*(推论：$f^*(-t) \stackrel{\mathcal{F}}{\longleftrightarrow} F^*(j\omega)$ —— 这条推论马上在“相关函数”里会直接用到！)*
* **由来**：$\int f^*(t)e^{-j\omega t}dt = \left[\int f(t)e^{+j\omega t}dt\right]^* = F^*(-j\omega)$。

---

### ⑤ 奇偶虚实性质
把 $f(t)$ 拆成实部/虚部、偶部/奇部，代入正变换展开式：
$$F(j\omega) = \int_{-\infty}^{+\infty} f(t) (\cos\omega t - j\sin\omega t) dt$$
记住一个**2 秒口诀**就能推出全部 4 种情况：**偶部配实余弦（$\cos$），奇部配虚正弦（$-j\sin$）**：
1. **$f(t)$ 为实偶** $\implies$ 与 $\cos$ 积分 $\implies$ **$F(j\omega)$ 为实偶**
2. **$f(t)$ 为实奇** $\implies$ 与 $-j\sin$ 积分 $\implies$ **$F(j\omega)$ 为纯虚奇**
3. **$f(t)$ 为纯虚偶** $\implies$ $j \times \cos$ $\implies$ **$F(j\omega)$ 为纯虚偶**
4. **$f(t)$ 为纯虚奇** $\implies$ $j \times (-j\sin) = +\sin$ $\implies$ **$F(j\omega)$ 为实奇**

*(对于一般实信号：$f(t)$ 可拆为实偶+实奇 $\implies$ $F(j\omega)$ 实部偶、虚部奇，即共轭对称 $F(-j\omega) = F^*(j\omega)$。)*

---

## 第二块：周期信号的傅里叶变换与理想冲激串（对应你第 1~5 张图）

你这几张图的核心主线，是在回答一个大问题：**怎么用“非周期信号的傅里叶变换”，直接反杀出“周期信号的傅里叶级数系数”？**

### 1. 先辨析：理想冲激串 $\delta_T(t)$ 的两种变换形式（图 2、图 4）
设理想冲激串为 $\delta_T(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT)$。
* **形式一（整体作为周期信号展开后的 FT，最常用）**：
  先算它的傅里叶级数系数（图 4）：在一个周期 $[-T/2, T/2]$ 里只框住原点一根冲激 $\delta(t)$，所以
  $$F_n = \frac{1}{T} \int_{-T/2}^{T/2} \delta(t) e^{-jn\omega_0 t} dt = \frac{1}{T}$$
  于是 $\delta_T(t) = \sum_{n=-\infty}^{\infty} \frac{1}{T} e^{jn\omega_0 t}$，逐项取 FT（$e^{jn\omega_0 t} \leftrightarrow 2\pi\delta(\omega - n\omega_0)$）得：
  $$\sum_{n=-\infty}^{\infty} \delta(t - nT) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{2\pi}{T} \sum_{n=-\infty}^{\infty} \delta\left(\omega - n\frac{2\pi}{T}\right) = \omega_0 \sum_{n=-\infty}^{\infty} \delta(\omega - n\omega_0)$$
* **形式二（逐个单根冲激直接用时移性质）**：
  因为单根冲激 $\delta(t - nT) \stackrel{\mathcal{F}}{\longleftrightarrow} e^{-jnT\omega}$，直接相加得：
  $$\sum_{n=-\infty}^{\infty} \delta(t - nT) \stackrel{\mathcal{F}}{\longleftrightarrow} \sum_{n=-\infty}^{\infty} e^{-jnT\omega}$$
* **关系**：这两种写法在数学上**完全相等**（泊松求和公式）。形式一直观画出了频域的等距冲激串；形式二把它们表示成了无数个复指数在频域干涉叠加的结果。

### 2. 两条路径“会师”，直接推出周期信号级数系数（图 1、3、5）
设周期信号 $x(t)$ 周期为 $T$，$\omega_0 = \frac{2\pi}{T}$，单周期脉冲为 $g(t)$（其傅里叶变换为 $G(j\omega)$）。

* **路径 ①（从级数直接做 FT —— 图 3）**：
  把 $x(t) = \sum_{n=-\infty}^{\infty} F_n e^{jn\omega_0 t}$ 逐项取傅里叶变换：
  $$X(j\omega) = \mathbf{2\pi \sum_{n=-\infty}^{\infty} F_n \delta(\omega - n\omega_0)} \quad \text{（①式）}$$

* **路径 ②（先化成卷积再做 FT —— 图 1、图 5）**：
  任何周期信号 $x(t)$ 都可以看成**单周期波形 $g(t)$ 与理想冲激串做卷积**（卷积把 $g(t)$ 复制粘贴到每个 $nT$ 处）：
  $$x(t) = g(t) * \sum_{n=-\infty}^{\infty} \delta(t - nT)$$
  两边取 FT（时域卷积 $\to$ 频域相乘），再乘上冲激串的变换：
  $$X(j\omega) = G(j\omega) \cdot \frac{2\pi}{T} \sum_{n=-\infty}^{\infty} \delta(\omega - n\omega_0)$$
  利用冲激的**乘法抽样性**（$G(j\omega)\delta(\omega - n\omega_0) = G(jn\omega_0)\delta(\omega - n\omega_0)$）：
  $$X(j\omega) = \mathbf{\frac{2\pi}{T} \sum_{n=-\infty}^{\infty} G(jn\omega_0) \delta(\omega - n\omega_0)} \quad \text{（②式）}$$

* **会师结论（对比 ① 式和 ② 式 —— 图 5）**：
  对应项系数相等：$2\pi F_n = \frac{2\pi}{T} G(jn\omega_0)$ $\implies$
  $$\boxed{F_n = \frac{1}{T} G(j\omega)\Big|_{\omega = n\omega_0}}$$
  **核心意义**：求任何周期信号的傅里叶级数系数 $F_n$，只需要先求它**单个周期 $g(t)$ 的傅里叶变换 $G(j\omega)$**，然后在 $n\omega_0$ 处抽样并除以 $T$ 即可（$\frac{G(j\omega)}{T}$ 就是离散级数频谱的**连续包络线**）。

---

## 第三块：相关函数与能量谱密度（对应你第 6~8 张、11~13 张图）

### 1. 互相关函数、自相关函数的前提和定义（图 8）
* **前提**：针对**实能量信号** $f_1(t), f_2(t)$（能量有限：$\int_{-\infty}^{+\infty} |f(t)|^2 dt < \infty$；若为复信号，移位项需加共轭 $*$）。
* **互相关函数**（把 $f_2$ 平移 $\tau$ 后与 $f_1$ 相乘积分，衡量错位 $\tau$ 时的相似程度）：
  $$R_{12}(\tau) = \int_{-\infty}^{+\infty} f_1(t) f_2(t - \tau) dt = \int_{-\infty}^{+\infty} f_1(t + \tau) f_2(t) dt$$
  $$R_{21}(\tau) = \int_{-\infty}^{+\infty} f_1(t - \tau) f_2(t) dt = \int_{-\infty}^{+\infty} f_1(t) f_2(t + \tau) dt$$
  * **两者关系**：把 $\tau$ 换成 $-\tau$ 即互化，$R_{12}(\tau) = R_{21}(-\tau)$。
* **自相关函数**（信号自己和延迟后的自己做相关）：
  $$R(\tau) = \int_{-\infty}^{+\infty} f(t) f(t - \tau) dt = \int_{-\infty}^{+\infty} f(t + \tau) f(t) dt$$
  * **核心性质**：① **偶函数**（$R(\tau) = R(-\tau)$）；② **零点取最大值且等于信号总能量**（$R(0) = \int_{-\infty}^{+\infty} f^2(t) dt = E$）。

### 2. 卷积与互相关函数的关系（图 7）
* **卷积**是“反折 + 平移”：$f_1(t) * f_2(t) = \int_{-\infty}^{+\infty} f_1(\tau) f_2(t - \tau) d\tau$
* **相关**是“**不反折**，直接平移”：$R_{12}(t) = \int_{-\infty}^{+\infty} f_1(\tau) f_2(\tau - t) d\tau$
* 强行把 $(\tau - t)$ 改写成 $-(t - \tau)$，就看出了它和卷积的血缘关系（图 7）：
  $$R_{12}(t) = \int_{-\infty}^{+\infty} f_1(\tau) f_2\big(-(t - \tau)\big) d\tau = \mathbf{f_1(t) * f_2(-t)}$$
  同理：$R_{21}(t) = f_1(-t) * f_2(t)$，自相关 $R(t) = f(t) * f(-t)$。（复信号则写为 $f_1(t) * f_2^*(-t)$）。

### 3. 互相关与自相关的傅里叶变换（图 6）
利用刚得到的 $R_{12}(t) = f_1(t) * f_2(-t)$，两边做 FT（时域卷积 $\to$ 频域相乘；且对实信号 $f_2(-t) \leftrightarrow F_2(-j\omega) = F_2^*(j\omega)$）：
$$R_{12}(\tau) \stackrel{\mathcal{F}}{\longleftrightarrow} F_1(j\omega) F_2^*(j\omega)$$
$$R_{21}(\tau) \stackrel{\mathcal{F}}{\longleftrightarrow} F_1^*(j\omega) F_2(j\omega)$$
令 $f_1 = f_2 = f$，立刻得到**自相关的傅里叶变换**：
$$R(\tau) \stackrel{\mathcal{F}}{\longleftrightarrow} F(j\omega) F^*(j\omega) = |F(j\omega)|^2$$

### 4. 能量谱相关三大核心（图 11、12、13）
1. **能量谱密度定义（ESD）**：
   $$E(\omega) \triangleq |F(j\omega)|^2$$
   * 表示信号能量在单位频率上的密集程度（实数、非负 $E(\omega)\ge 0$、对实信号为偶函数）。它**丢掉了相位信息**（所以信号在时域平移后，能量谱密度完全不变）。
2. **帕萨瓦尔能量定理（Parseval's Theorem）**：
   $$E_{\text{total}} = \int_{-\infty}^{+\infty} |f(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{+\infty} |F(j\omega)|^2 d\omega = \frac{1}{2\pi} \int_{-\infty}^{+\infty} E(\omega) d\omega$$
   * 时域求总能量 $=$ 频域对能量谱密度积分（除以 $2\pi$），体现能量守恒。
3. **维纳-辛钦定理（能量信号形式）**：
   $$R_{ff}(\tau) \stackrel{\mathcal{F}}{\longleftrightarrow} E(\omega) = |F(j\omega)|^2$$
   * 即：**信号自相关函数与能量谱密度互为傅里叶变换对**。
   * 当 $\tau = 0$ 时，由逆变换得 $R_{ff}(0) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} E(\omega)d\omega$，完美统一了自相关零点能量与帕萨瓦尔定理。

---

## 第四块：功率谱相关综合（对应你第 9、10 张图）

对于周期信号或随机信号，总能量无穷大，能量谱失去意义，必须改用衡量“平均每秒能量”的**功率谱密度（PSD，记为 $S(\omega)$）**。

### 1. 根本定义：适用所有功率信号的维纳-辛钦定理（图 10）
* 首先定义功率信号的**自相关函数**（核心区别：多了一个**求时间平均** $\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}$）：
  $$R_{ff}(\tau) = \lim_{T\to\infty} \frac{1}{T} \int_{-T/2}^{T/2} f(t) f^*(t - \tau) dt$$
  *(同样有 $R_{ff}(0) = P_{\text{平均总功率}}$)*
* **功率谱密度 $S(\omega)$（维纳-辛钦定理）**：
  $$S(\omega) \triangleq \mathcal{F}\{R_{ff}(\tau)\}$$
  即**功率信号的功率谱密度，定义为该信号自相关函数的傅里叶变换**。同样满足功率守恒：$P = R_{ff}(0) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} S(\omega) d\omega$。

### 2. 针对周期信号的特殊形式（离散谱 —— 图 9）
当功率信号恰好是周期为 $T_0$（$\omega_0 = \frac{2\pi}{T_0}$）的确定性周期信号 $f(t) = \sum_{n=-\infty}^{\infty} C_n e^{jn\omega_0 t}$ 时：
1. 代入功率信号自相关定义算出 $R_{ff}(\tau)$（因为不同频率分量正交，交叉项积分全为 0，只剩同频项）：
   $$R_{ff}(\tau) = \sum_{n=-\infty}^{\infty} |C_n|^2 e^{j n \omega_0 \tau}$$
2. 对它直接取傅里叶变换（$e^{jn\omega_0 \tau} \leftrightarrow 2\pi\delta(\omega - n\omega_0)$），即得周期信号的功率谱密度：
   $$S(\omega) = \sum_{n=-\infty}^{\infty} 2\pi |C_n|^2 \delta(\omega - n\omega_0)$$
* **物理画面**：周期信号的功率不是连续散开的，而是**离散地集中**在各个谐波点 $n\omega_0$ 上；每根冲激的强度（面积除以 $2\pi$）直接等于该次谐波的平均功率 $|C_n|^2$（把所有项加起来 $\sum |C_n|^2$ 正好等于总平均功率）。

---

### 能量谱 vs 功率谱 一眼对照收尾：
| 对比 | 能量信号（脉冲/衰减信号） | 功率信号（周期信号/平稳随机信号） |
| :--- | :--- | :--- |
| **自相关 $R(\tau)$** | 直接全时间积分 $\int_{-\infty}^{\infty} f(t)f^*(t-\tau)dt$ | 取时间平均 $\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2} f(t)f^*(t-\tau)dt$ |
| **零点 $R(0)$** | 信号**总能量** | 信号**平均总功率** |
| **谱密度定义** | **能量谱** $E(\omega) = \mathcal{F}\{R(\tau)\} = |F(j\omega)|^2$ | **功率谱** $S(\omega) = \mathcal{F}\{R(\tau)\}$ |
| **周期信号特例** | 无 | 离散冲激串：$S(\omega) = \sum 2\pi|C_n|^2\delta(\omega - n\omega_0)$ |

---

## You

共轭和奇偶虚实没看懂

---

## AI Studio

刚才那段为了把所有块串起来，确实压缩得太厉害了。我们现在放慢节奏，只讲**④ 共轭性质**和**⑤ 奇偶虚实**这两个点，用最直观的拆解和具体例子把它讲透。

---

## 第一部分：彻底搞懂“④ 共轭性质”

### 1. 公式长什么样？
如果 $f(t) \stackrel{\mathcal{F}}{\longleftrightarrow} F(j\omega)$，那么把时域信号取复共轭 $f^*(t)$，它的傅里叶变换是：
$$f^*(t) \stackrel{\mathcal{F}}{\longleftrightarrow} F^*(-j\omega)$$

*(注：如果教材习惯写成 $F(\omega)$，这里右边就写成 $F^*(-\omega)$，意思一模一样：不仅要取共轭 $*$，括号里的 $\omega$ 还要变成 $-\omega$。)*

### 2. 疑问：为什么右边既有共轭 $*$，里面又多了一个负号 $-\omega$？
只要看 3 行推导，你就一眼看穿那个负号是从哪钻出来的：

1. 写出 $f^*(t)$ 的傅里叶变换定义：
   $$\mathcal{F}\{f^*(t)\} = \int_{-\infty}^{+\infty} f^*(t) e^{-j\omega t} dt$$
2. 我们想把共轭星号 $*$ 整个提到积分外边去。注意：**星号提出来，里面的 $j$ 必须变号！** 所以原本的 $e^{-j\omega t}$，塞进共轭括号里就必须变成 $e^{+j\omega t}$：
   $$= \left[ \int_{-\infty}^{+\infty} f(t) e^{+j\omega t} dt \right]^*$$
3. 把 $+j\omega t$ 凑回标准正变换形式 $-j(-\omega)t$：
   $$= \left[ \int_{-\infty}^{+\infty} f(t) e^{-j(-\omega)t} dt \right]^* = F^*(-j\omega)$$

**一目了然：** 那个 $-\omega$ 的负号，纯粹是因为 $e^{-j\omega t}$ 里的 $j$ 在提共轭时翻了个号！

### 3. 它的两个重要用途
1. **推论（反折 + 共轭）：$f^*(-t) \stackrel{\mathcal{F}}{\longleftrightarrow} F^*(j\omega)$**
   * 既然单纯共轭会让 $\omega$ 变一次负号（$-\omega$），而单纯时间反折 $t \to -t$ 也会让 $\omega$ 变一次负号，**负负得正**！
   * 所以时间既反折又取共轭，频域里的 $-\omega$ 负号刚好抵消，就只剩干净的 $F^*(j\omega)$（这就是你前面截图里求互相关函数 $R_{12}(t) = f_1(t) * f_2^*(-t) \leftrightarrow F_1(j\omega)F_2^*(j\omega)$ 的由来
<truncated 20274 bytes>
