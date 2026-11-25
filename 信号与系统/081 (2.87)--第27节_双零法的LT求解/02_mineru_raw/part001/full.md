## 专题5 双零法的LT求解

## 考点1：零输入响应的s域求解

1、原理：

$$
f ^ {\prime} (t) \leftrightarrow s F (s) - f (0 _ {-})
$$

$$
f ^ {\prime \prime} (t) \leftrightarrow s ^ {2} F (s) - s f (0 _ {-}) - f ^ {\prime} (0 _ {-})
$$

2、步骤：零输入响应满足齐次，方程两边同时进行拉氏变换，然后写出 $R_{zi}(s)$ 表达式，最后逆变换。

例 26: $r''(t)+3r'(t)+2r(t)=e'(t)+3e(t), r(0_{-})=1, r'(0_{-})=2$ ，求 $r_{zi}(t)$ 。

解析：

考点2：零状态响应的s域求解

$$
R _ {z s} (s) = H (s) \cdot E (s) \xrightarrow {\text {逆变换}} r _ {z s} (t)
$$

考点 3：系统完全响应的求解流程

零状态一律用LT，零输入尽量用时域(除非题目要求s域)

$$
\text {微分方程} \rightarrow \left\{\begin{array}{l l}\text {已知} r ^ {(k)} (0 _ {-})&\left[\begin{array}{l}\text {时域} r _ {z i} (t)\\\text {LT} r _ {z s} (t)\end{array}\right]\rightarrow r (t) = r _ {z i} (t) + r _ {z s} (t)\\\text {已知} r ^ {(k)} (0 _ {+})&\left[\begin{array}{l}\text {LT求} r _ {z s} (t) \xrightarrow [ \text {特解} ]{\text {解形式}} \text {时域} r (t) \xrightarrow [ (\text {含系数}) ]{r ^ {(k)} (0 _ {+})} r (t) \xrightarrow [ r _ {z i} (t) = r (t) - r _ {z s} (t) ]{\text {时域}:}\\\text {设} r _ {z i} (t) \text {解(含系数)} \rightarrow r (t) \text {完全(含系数)} \xrightarrow {r ^ {(k)} (0 _ {+})} r _ {z i} (t) \text {和} r (t)\end{array}\right.\end{array}\right.
$$

例27：描述某LTI系统的微分方程为

$$
y ^ {\prime \prime} (t) + 3 y ^ {\prime} (t) + 2 y (t) = f ^ {\prime} (t) + 4 f (t)
$$

求在下列条件下的零输入响应和零状态响应。

$$
(1) f (t) = e ^ {- 2 t} u (t), y (0 _ {-}) = 1, y ^ {\prime} (0 _ {-}) = 1 。
$$

(2) $f(t)=e^{-2t}u(t)$ , $y(0_{+})=1$ , $y'(0_{+})=2$ 。

例 28: 已知初始状态为 $y(0_{-})$ ，单位冲激响应为 $h(t) = e^{-2t} u(t)$ 的连续 LTI 系统在信号 $x_{1}(t)$ 的作用下输出的全响应信号为 $y_{1}(t) = (2e^{-2t} - e^{-3t}) u(t)$ ，若初始状态不变，输入为 $x_{2}(t) = \frac{d}{dt} x_{1}(t)$ 时全响应信号为 $y_{2}(t) = (3e^{-3t} - e^{-2t}) u(t)$ ，求 $x_{1}(t)$ 和初始状态 $y(0_{-})$ 。

![](images/6cc5de6d9bd8b7e6647ad020ed4c10dd8752a9edc94b8473c84be7742e75682e.jpg)

考点4：系统函数可约性对系统分析的影响

【引例】

1、微分方程的隐含信息

(1)阶数(特征根的个数、极点的个数): 看方程的左边, 与右边无关

(2)零输入响应的解形式

(3)零状态响应的解形式: 左边方程+激励 $\Rightarrow y_{zs}(t)$ 解形式一般性

(4) 完全响应的解形式

(5) 系统函数 $\leftrightarrow$ 微分方程

以 $y''(t)+3y'(t)+2y(t)=f'(t)+4f(t)$ 为例：

$$
\begin{array}{r l} & {\text {①} f (t) = e ^ {- 3 t} u (t)} \\ & {\qquad \Rightarrow y _ {z i} (t) = A _ {1} e ^ {- t} + A _ {2} e ^ {- 2 t} \Rightarrow y _ {z s} (t) = A _ {3} e ^ {- t} + A _ {4} e ^ {- 2 t} + B e ^ {- 3 t}} \end{array}
$$

$$
\begin{array}{r l} & {\text {②} f (t) = e ^ {- 2 t} u (t)} \\ & {\qquad \Rightarrow y _ {z i} (t) = A _ {1} e ^ {- t} + A _ {2} e ^ {- 2 t} \Rightarrow y _ {z s} (t) = A _ {3} e ^ {- t} + A _ {4} e ^ {- 2 t} + B t e ^ {- 2 t}} \end{array}
$$

## 2、系统函数的可约性

$$
\text {以} y ^ {\prime \prime} (t) + 3 y ^ {\prime} (t) + 2 y (t) = f ^ {\prime} (t) + f (t), f (t) = e ^ {- 3 t} u (t), y (0 _ {-}) = 1, y ^ {\prime} (0 _ {-}) = 1
$$

为例：

(1)由方程可列 $y_{zi}(t)$ 的形式为：

$$
y _ {z i} (t) = A _ {1} e ^ {- t} + A _ {2} e ^ {- 2 t}
$$

代入 $y^{(k)}(0_{-})$ 值后可得:

$$
y _ {z i} (t) = (e ^ {- t} - 2 e ^ {- 2 t}) u (t)
$$

(2)由方程和激励可列 $y_{zs}(t)$ 的形式为:

$$
y _ {z s} (t) = A _ {3} e ^ {- 3 t} + A _ {4} e ^ {- 2 t} + B e ^ {- 3 t}
$$

$$
\begin{array}{r l} & {H (s) = \frac {\text {右边}}{\text {左边}} = \frac {s + 1}{s ^ {2} + 3 s + 2} = \frac {s + 1}{(s + 1) (s + 2)} = \frac {1}{(s + 2)}} \\ & {\qquad \Rightarrow Y _ {z s} (s) = H (s) \cdot F (s) = \frac {1}{(s + 2)} \cdot \frac {1}{(s + 3)}} \\ & {\qquad \Rightarrow y _ {z s} (t) = (e ^ {- 2 t} - e ^ {- 3 t}) u (t)} \end{array}
$$

由上例可见，系统函数可约性对系统分析的影响，具体如下：

(1) 对零输入响应的计算和解形式均无影响;

(2) 可以简化零状态响应的计算，解形式中会缺少某些极点 (特征根) 信息；

(3)零极点分布: 不影响零极点个数和求解, 但有部分零点和极点相同, 零极点图对应位置可以不画 (提前说明已约分) 或同时画零极点符号;

(4) 系统函数与微分方程

①(直接、间接)已知系统函数表达式，求方程时，该系统函数直接转换；

②(直接、间接)已知系统函数表达式，若有(阶数、零输入或其他隐含信息)，需要额外考虑方程阶数。