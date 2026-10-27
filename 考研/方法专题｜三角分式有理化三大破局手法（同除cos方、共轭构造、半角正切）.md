# 方法专题｜三角分式有理化三大破局手法（同除cos方、共轭构造、半角正切）

- **专题归属**：考研数学一 · 三角函数积分与分式有理化底座
- **核心定位**：解决“三角函数长在分母上，无法直接用初等公式求积，盲目万能换元导致计算发散”的痛点。

---

## 一、核心思想：为什么要“有理化”？

当正弦 $\sin x$、余弦 $\cos x$ 出现在**分母**上，且分子没有现成的导数因子时，任何多项式积分法都会失效。
此时唯一的解题大方向是：
> **想办法将三角分式，全盘翻译为关于正切变量 $t = \tan x$（或半角 $t = \tan\frac{x}{2}$）的【纯代数有理分式】！**

翻译的手法共有以下三种标准动作：

---

## 二、三大破局手法详解

### 手法 1：【同除 $\cos^2 x$ 法】（专治分母二次齐次式 · 考研最高频）

#### 1. 触发信号
- 分母由 $\sin^2 x$、$\cos^2 x$、$\sin x \cos x$（或 $\sin 2x = 2\sin x\cos x$）组成，**各项总次数均为 2（或偶数次）**。
- 代表形态：$\int \frac{dx}{a^2\sin^2 x + b^2\cos^2 x}$、$\int \frac{dx}{\sin 2x}$、$\int \frac{dx}{\sin^2 x \cos^4 x}$。

#### 2. 破局机理
分子分母**同时除以 $\cos^2 x$**，产生两重自动化简：
1. **分子**：$\frac{1}{\cos^2 x} dx = \sec^2 x dx = \mathbf{d(\tan x)}$（自动生成新变量的微分 $dt$）；
2. **分母**：
   $$\frac{\sin^2 x}{\cos^2 x} = \tan^2 x = t^2, \quad \frac{\cos^2 x}{\cos^2 x} = 1, \quad \frac{\sin x \cos x}{\cos^2 x} = \tan x = t$$
3. **落地点**：三角式瞬间消失，直接化为关于 $t$ 的标准代数有理分式 $\int \frac{dt}{P(t)}$，套反正切或对数公式秒杀！

#### 3. 经典母题实战
求 $\int \frac{dx}{a^2\sin^2 x + b^2\cos^2 x}$：
$$\int \frac{dx}{a^2\sin^2 x + b^2\cos^2 x} = \int \frac{\frac{1}{\cos^2 x}}{\frac{a^2\sin^2 x + b^2\cos^2 x}{\cos^2 x}} dx = \int \frac{d(\tan x)}{a^2\tan^2 x + b^2}$$
令 $t = \tan x$，直接命中标准反正切积分：
$$= \int \frac{dt}{a^2 t^2 + b^2} = \frac{1}{ab} \arctan\left(\frac{a}{b}t\right) + C = \mathbf{\frac{1}{ab}\arctan\left(\frac{a\tan x}{b}\right) + C}$$

---

### 手法 2：【共轭有理化】（专治分母带 $1 \pm \sin x$ 或 $1 \pm \cos x$）

#### 1. 触发信号
- 分母不是二次齐次式，而是出现**常数与正弦/余弦的一次和差**：$1 \pm \sin x$ 或 $1 \pm \cos x$。
- 代表形态：$\int \frac{dx}{1+\sin x}$、$\int \frac{dx}{1-\cos x}$。

#### 2. 破局机理
看到 $1+\sin x$，绝对不要套万能公式！直接利用初中平方差共轭因式：
**分子分母同时乘以共轭式 $(1 - \sin x)$**：
- **分母**：$(1+\sin x)(1-\sin x) = 1 - \sin^2 x = \mathbf{\cos^2 x}$！
- **效果**：分母从难搞的“两项相加”，变成了单一的“单项余弦平方”！

#### 3. 经典母题实战
求 $\int \frac{dx}{1+\sin x}$：
$$\int \frac{1 - \sin x}{(1+\sin x)(1-\sin x)} dx = \int \frac{1 - \sin x}{\cos^2 x} dx$$
拆为两项基础积分：
$$= \int \left( \frac{1}{\cos^2 x} - \frac{\sin x}{\cos^2 x} \right) dx = \int \sec^2 x \, dx - \int \sec x \tan x \, dx$$
两行写完答案：
$$= \mathbf{\tan x - \sec x + C}$$

---

### 手法 3：【倍角与半角切线转化】（专治混合一次与倍角三角）

#### 1. 触发信号
- 分母同时包含不同频率的正弦余弦，如 $\sin 2x + 2\sin x$。
- 无法直接同除 $\cos^2 x$，也无法一眼共轭。

#### 2. 破局机理
1. **因式分解**：利用 $\sin 2x = 2\sin x \cos x$ 提取公因式：
   $$\sin 2x + 2\sin x = 2\sin x(\cos x + 1)$$
2. **利用倍角降为半角**：
   $$\cos x + 1 = 2\cos^2\frac{x}{2}, \quad \sin x = 2\sin\frac{x}{2}\cos\frac{x}{2}$$
   整个分母改写为关于半角 $\frac{x}{2}$ 的齐次式：
   $$2\sin x(\cos x+1) = 2 \left(2\sin\frac{x}{2}\cos\frac{x}{2}\right) \left(2\cos^2\frac{x}{2}\right) = 8\sin\frac{x}{2}\cos^3\frac{x}{2}$$
3. **回到手法 1**：此时分母是半角的 4 次齐次式，分子分母同除以 $\cos^4\frac{x}{2}$，令 $t = \tan\frac{x}{2}$，彻底转化为代数有理分式。

---

## 三、做题决策快速对照卡

| 题面特征 | 第一识别 | 首选动作 |
| :--- | :--- | :--- |
| 分母为 $\sin^2 x, \cos^2 x, \sin 2x$ 组合 | 二次齐次型 | **分子分母同除以 $\cos^2 x$**，令 $t=\tan x$ |
| 分母为 $1 \pm \sin x$ 或 $1 \pm \cos x$ | 共轭平方型 | **分子分母同乘共轭式 $1 \mp \sin x$**，化分母为 $\cos^2 x$ |
| 分母为 $\sin 2x + k\sin x$ | 半角因子型 | **因式分解提取公因式**，用倍角降为半角齐次式 |
| 分子分母为 $\sin x, \cos x$ 纯一次比值 | 待定系数型（P4） | **设分子 $= A(\text{分母}) + B(\text{分母})'$** |
