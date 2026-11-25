## 专题 5 冲激响应与阶跃响应

## 考点1: 冲激响应的求解

## 1、定义

以单位冲激信号 $\delta(t)$ 作激励，系统产生的零状态响应称为“单位冲激响应”或简称“冲激响应”，以 $h(t)$ 表示。

例 27: 已知某一LTI系统对激励 $e(t)$ 的零状态响应

$$
r _ {z s} (t) = \int_ {t - 2} ^ {\infty} e ^ {t - \tau} e (\tau - 1) d \tau
$$

求该系统的单位冲激响应。

2、经典法求解——微分方程表示系统

例 28: 若激励为 $e(t)$ , 响应 $r(t)$ 的系统的微分方程由下式描述, 求系统的冲激响应 $h(t)$ 。

$$
\frac {d r (t)}{d t} + 2 r (t) = 3 e (t)
$$

官网：tongxinkaoyan.com

梦马班讲义

## 考点2：特殊情况下冲激函数匹配法的应用

例 29: 设 $h(t)$ 方程中, $h(t)$ 最高阶系数为 $n$ 阶, 激励 $\delta(t)$ 最高阶系数项为 $m$ 。

(1) $n > m$

$$
h ^ {\prime \prime} (t) + 3 h ^ {\prime} (t) + 2 h (t) = \delta^ {\prime} (t) + 3 \delta (t)
$$

(2) $n = m$

$$
h ^ {\prime \prime} (t) + 3 h ^ {\prime} (t) + 2 h (t) = \delta^ {\prime \prime} (t) + 2 \delta (t)
$$

$$
(3) n <   m
$$

$$
h ^ {\prime \prime} (t) + 3 h ^ {\prime} (t) + 2 h (t) = \delta^ {\prime \prime \prime} (t) + 2 \delta (t)
$$

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

例 30: 已知某 LTI 系统, 若激励为 $e(t)$ , 响应 $r(t)$ 的系统的微分方程由下式描述, 求系统的冲激响应 $h(t)$ 。

$$
\frac {d r (t)}{d t} + 2 r (t) = \frac {d ^ {2} e (t)}{d t ^ {2}} + 3 \frac {d e (t)}{d t} + 3 e (t)
$$

![](images/094a1b08beec5ba4423a2d00e463e0dfa996bf30f252081e64ab61578ea02017.jpg)

【梦马班点拨】冲激函数匹配法与齐次法方法比较：

冲激函数匹配法：计算简单，解题的体系结构一致，但对于有默认冲激项时易忽视

齐次法：右边可始终保持 $\delta (t)$ 原型计算，不用考虑默认项，但线性时，需要计算各种微分。

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

## 考点 3: 阶跃响应的求解

## 1、定义

以单位阶跃信号 $u(t)$ 作激励，系统产生的零状态响应称为“单位阶跃响应”或简称“阶跃响应”，以 $g(t)$ 表示。

2、阶跃响应的经典法求解

例 31: 描述某LTI系统的微分方程为

$$
\frac {d ^ {2} r (t)}{d t ^ {2}} + 5 \frac {d r (t)}{d t} + 6 r (t) = 3 \frac {d e (t)}{d t} + 2 e (t)
$$

试求其阶跃响应 $g(t)$ 。

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

例 32: 若激励为 $e(t)$ , 响应 $r(t)$ 的 LTI 系统的微分方程由下式描述, 求系统的阶跃响应 $g(t)$ 。

$$
\frac {d r (t)}{d t} + 2 r (t) = \frac {d ^ {2} e (t)}{d t ^ {2}} + 3 \frac {d e (t)}{d t} + 3 e (t)
$$

## 3、LTIS下微积分求解法

由于单位阶跃函数 $u(t)$ 与单位冲激函数 $\delta(t)$ 的关系为

$$
\delta (t) = \frac {d u (t)}{d t}, u (t) = \int_ {- \infty} ^ {t} \delta (x) d x
$$

根据LTI系统的微(积)分特性,同一系统的阶跃响应与冲激响应的关系为

$$
h (t) = \frac {d g (t)}{d t}, g (t) = \int_ {- \infty} ^ {t} h (x) d x
$$

例：若已知 $h(t)=(-4e^{-2t}+7e^{-3t})u(t)$

$$
\begin{array}{c} \therefore g (t) = \int_ {- \infty} ^ {t} h (\tau) d \tau = \int_ {- \infty} ^ {t} [ - 4 e ^ {- 2 \tau} + 7 e ^ {- 3 \tau} ] u (\tau) d \tau \\ = \left[ - 4 \int_ {0} ^ {t} e ^ {- 2 \tau} d \tau + 7 \int_ {0} ^ {t} e ^ {- 3 \tau} d \tau \right] u (t) = \left[ - 4 \cdot \frac {e ^ {- 2 \tau}}{- 2} \Bigg | _ {0} ^ {t} + 7 \cdot \frac {e ^ {- 3 \tau}}{- 3} \Bigg | _ {0} ^ {t} \right] u (t) \\ = \left[ 2 (e ^ {- 2 t} - 1) - \frac {7}{3} (e ^ {- 3 t} - 1) \right] u (t) = \left(2 e ^ {- 2 t} - \frac {7}{3} e ^ {- 3 t} + \frac {1}{3}\right) u (t) \end{array}
$$

官网：tongxinkaoyan.com

梦马班讲义

考点4: $h(t)$ 与 $g(t)$ 求解总结

$$
\begin{array}{r l} & {h (t) \left\{ \begin{array}{l l} {\text {非常规方程：定义法}} \\ {\text {线性常系数微分方程} \left\{ \begin{array}{l l} {\text {经典法}} \\ {L T \text {法}} \end{array} \right.} \end{array} \right.} \\ & {\quad g (t) =  \int_ {- \infty} ^ {t} h (\tau) d \tau   [ \text {注意默认项} ]} \end{array}
$$

例 33: 一因果性的LTI系统, 其输入、输出用下列微分一积分方程表示:

$$
\frac {d}{d t} r (t) + 5 r (t) = \int_ {- \infty} ^ {\infty} e (\tau) f (t - \tau) d \tau - e (t)
$$

其中 $f(t)=e^{-t}u(t)+3\delta(t)$ ，求该系统的单位冲激响应 $h(t)$ 。

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

## 考点 5: $h(t)$ 系统表示与应用

1、 $h(t)$ 可以表征系统

2、 $h(t)$ 判断系统特性

(1)因果: $t < 0$ 时, $h(t) = 0$

(2) 稳定： $\int_{-\infty}^{\infty}|h(t)|dt < \infty$

例 34: 一LTI系统零状态响应 $y_{zs}(t)$ 与输入 $f(t)$ 关系为 $y_{zs}(t)=\int_{t-1}^{\infty}e^{2(t-\tau)}f(2-\tau)d\tau$ 。

(1)求 $h(t)$ ，判别是否为因果系统；

(2)该系统是否稳定?写出判别过程。

免费讲义Q群：1095841878

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

官网：tongxinkaoyan.com

梦马班讲义