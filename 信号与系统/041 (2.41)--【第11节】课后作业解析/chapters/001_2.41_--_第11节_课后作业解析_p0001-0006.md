## 【第11节】课后作业

1、【2024 长春理工大学 2】某系统微分方程为 $y''(t) + 3y'(t) + 2y(t) = f''(t) +$

$2f(t)$ ，当 $f(t) = u(t)$ 时，全响应 $y(t) = (1 - e^{-t} + 2e^{-2t})u(t)$

(1) 求冲激响应 $h(t)$ ;

(2) 求 $y_{zi}(t), y_{zs}(t)$ 。

解：(1) $h^{\prime}|t| + 3h^{\prime}|t| + 2h(t) = \delta^{\prime}|t| + 2\delta(t)$

$$
h (t) = A e ^ {- t} + B e ^ {- 2 t}
$$

$$
h ^ {\prime \prime} (t) = a d ^ {\prime \prime} (t) + b d ^ {\prime} (t) + c d (t) + d \Delta (u (t)) \Rightarrow a = 1
$$

$$
h ^ {\prime} (t) = a \delta^ {\prime} (t) + b \delta (t) + C \Delta u (t) \Rightarrow b + 3 a = 0 \Rightarrow b = - 3 \Rightarrow h (v + 1) = h (v - 1) + c = 9
$$

$$
h (t) = a \delta (t) + b \Delta u (t) \Rightarrow c + 3 b + 2 a = 2 \Rightarrow c = 9 \Rightarrow h (0 +) = h (0 -) + b = - 3
$$

$$
\begin{array}{l} {h (0 + 1) = A + B = - 3} \\ {h (u + 1) = - A - 2 B = 9} \end{array} \Rightarrow \left\{ \begin{array}{l l} {A = 3} \\ {B = - 6} \end{array} \right.
$$

$$
h (t) = (3 e ^ {- t} - 6 e ^ {- 2 t}) u (t) + \sqrt [ 3 ]{(t)}
$$

(2) 当 $f(t)=u(t)$ 时的空状态 $y_{2s}(t)=9(t)=\int_{-10}^{10}h(\tau)d\tau$ 故 $y_{2s}(t)=\int_{-10}^{t}(3e^{-\tau}-6e^{-2\tau})u(\tau)d\tau+\int_{-10}^{t}\sqrt{(\tau)}d\tau$ $=\int_{0}^{t}(3e^{-\tau}-6e^{-2\tau})d\tau\cdot u(t)+u(t)$ $=\left[-3e^{-\tau}+3e^{-2\tau}\right]_{0}^{t}\cdot u(t)+u(t)$ $=\left[-3e^{-t}+3e^{-2t}+3-3\right]u(t)+u(t)$ $=(-3e^{-t}+3e^{-2t}+1)u(t)$ $y_{2i}(t)=y(t)-y_{x}(t)=(2e^{-t}-e^{-2t})u(t)$

官网：www.tongxinkaoyan.com

2、【2024 大连理工大学四改编】某系统微分方程为

$$
r ^ {\prime \prime} (t) + 3 r ^ {\prime} (t) + 2 r (t) = - e ^ {\prime} (t) - 6 e (t)
$$

(1) 求单位冲激响应 $h(t)$ ;

(2) 判断系统的稳定性;

(3)已知 ${r}_{zi}\left( 0\right)  = 2,{r}_{zi}^{^{\prime }}\left( 0\right)  =  - 1$ ,以及 $e\left( t\right)  = 4{e}^{-{u}}\left( t\right)$ ,求系统的零输入响应、零状态响应和全响应,并判断自然、强迫,瞬态和稳态响应分量。

$$
\begin{array}{l} {h ^ {\prime} (t) + 3 h ^ {\prime} (t) + 2 h (t) = - \delta^ {\prime} (t) - 6 \delta^ {\prime} (t)} \\ {h (t) = A e ^ {- t} + B e ^ {- 2 t}} \\ {\left\{ \begin{array}{l l} {h ^ {\prime} (t) = a \delta^ {\prime} (t) + b \delta (t) + c \Delta u (t)} & {\Rightarrow a = - 1} \\ {h ^ {\prime} (t) = a \delta (t) + b \Delta u (t)} & {\Rightarrow b + 3 a = - 6 \Rightarrow b = - 3 \Rightarrow h (v +)} \\ {h (t) = a \Delta u (t)} & {\Rightarrow h (v +) = h (v -) + a = - 1} \end{array} \right.} \\ {h (v +) = A + B = - 1 \quad \Rightarrow \quad \left\{ \begin{array}{l l} {A = - 5} \\ {B = 4} \end{array} \right.} \\ {h ^ {\prime} (v +) = - A - 2 B = - 3 \quad \Rightarrow \quad B = 4} \\ {h (t) = (- 5 e ^ {- t} + 4 e ^ {- 2 t}) u (t)} \end{array}
$$

(2)

$$
\begin{array}{r l} {\int_ {- \infty} ^ {\infty} | h (t) | d t} & {= \int_ {- \infty} ^ {\infty} | - 5 e ^ {- t} + 4 e ^ {- x t} | u (t) d t = \int_ {0} ^ {\infty} | - 5 e ^ {- t} + 4 e ^ {- x t} | d t} \\ & {\leq \int_ {0} ^ {\infty} | - 5 e ^ {- t} | d t + \int_ {0} ^ {\infty} | 4 e ^ {- 2 t} | d t} \\ & {= 5 \int_ {0} ^ {\infty} e ^ {- t} d t + 4 \int_ {0} ^ {\infty} e ^ {- x t} d t} \\ & {= 5 [ - e ^ {- t} ] _ {0} ^ {\infty} + 4 [ - \frac {1}{2} e ^ {- 2 t} ] _ {0} ^ {\infty}} \\ & {= 5 [ 0 + 1 ] - 2 [ 0 - 1 ]} \\ & {= 7 <   \infty \quad \mathrm{故系统稳定}} \end{array}
$$

$$
\begin{array}{r l} {(3)} & {r _ {2 i} | t | = C e ^ {- t} + D e ^ {- 2 t}} \\ & {r _ {2 i} (0) = C + D = 2} \\ & {r _ {2 i} ^ {\prime} (0) = - C - 2 D = - 1} \\ & {\Rightarrow C = 3, D = - 1} \\ & {\therefore r _ {2 i} | t | = (3 e ^ {- t} - e ^ {- x}) u (t)} \end{array}
$$

$$
- e ^ {i t} - 6 e (t) = - [ 4 e ^ {- 3 t} u (t) ] ^ {\prime} - 2 4 e ^ {- 3 t} u (t) = - 1 2 e ^ {- 3 t} u (t) - 4 d (t)
$$

$$
\begin{array}{r l} {9 E e ^ {- 3 t} - 9 E e ^ {- 3 t} + 2 E e ^ {- 3 t}} & {= - 1 2 P ^ {- 3 t}} \\ {E} & {= - 6} \end{array}
$$

$$
\therefore r _ {x} | t | = M e ^ {- t} + N e ^ {- 2 t} - 6 e ^ {- 3 t}
$$

官网：www.tongxinkaoyan.com

$$
\left\{ \begin{array}{l} {r _ {2} ^ {\prime \prime} | t | = a (| t |) + b (\Delta u | t) \Rightarrow a = - 4} \\ {r _ {2} ^ {\prime} | t | = a (\Delta u | t) \Rightarrow r _ {2} ^ {\prime} | u + 1 = - 4} \\ {r _ {2} ^ {\prime} | t | = a (\Delta u | t) \Rightarrow r _ {2} ^ {\prime} | u + 1 = r _ {2} ^ {\prime} | u - 1 > 0} \end{array} \right. \mathrm{梦马班作业}
$$

免费讲义Q群：1095841878

B站up：信号与系统\_谷哥 $n_{t+1}$ 为瞬，无状态

自由响应为 $(-7e^{-t}+15e^{-2t}-6e^{-3t})$ (uH)

强迫响应为 $-6e^{-3t}$ (uH) $r_{2s}(u_{t+1}) = M + N - 6 = 0 \Rightarrow M = -10, N = 16$ 公众号：通信考研小马哥 $r_{2s}'(u_{t+1}) = -M - 2N + 18 = -4 \Rightarrow r_{2s}'(t) = \left( -10e^{-t} + 16e^{-2t} - 6e^{-3t} \right)$ (uH)

3、【2024天津师范大学7】已知一系统，对激励为 $e_{1}(t)=u(t)$ 时完全响应为 $r_{1}(t)=2e^{-t}u(t)$ 对激励为 $e_{2}(t)=\delta(t)$ 完全响应为 $r_{2}(t)=\delta(t)$ ，求零输入响应

$$
r _ {z i} (t),
$$

解：由题意可知：

$$
\begin{array}{r l} {r _ {2 i} (t)} & {+ g (t) = r _ {1} (t) = 2 e ^ {- t} v (t)} \\ {r _ {2 i} (t)} & {+ h (t) = r _ {2} (t) = \sqrt [ 3 ]{(t)}} \end{array}
$$

②-①3年

$$
h (t) - g (t) = g ^ {\prime} (t) - g (t) = \delta (t) - 2 e ^ {- t} u (t)
$$

$$
g _ {h} (t) = B e ^ {t}
$$

$$
\begin{array}{r l} & {g (t) = B e} \\ & {t > 0 \mathrm{时身体项} = - 2 e ^ {- t} \Rightarrow g _ {p} (t) = A e ^ {- t}} \\ & {- A e ^ {- t} - A e ^ {- t} = - 2 e ^ {- t} \Rightarrow A = 1} \\ & {\Rightarrow g (t) = B e ^ {t} + e ^ {- t}} \\ & {\left\{ \begin{array}{l l} {g (t)} & {a d (t) + b (\Delta u (t)) \Rightarrow a = 1} \\ {g (t)} & {a \Delta u (t) \Rightarrow g (u +) = g (u -) + a = 1} \end{array} \right.} \\ & {\Rightarrow g (0 +) = B + 1 = 1 \Rightarrow B = 0} \\ & {\Rightarrow g (t) = e ^ {- t} u (t)} \end{array}
$$

特殊方程

代入①得 $b_{i}|t|=e^{-t}u(t)$

官网：www.tongxinkaoyan.com

4、【2024 内蒙古大学 2.1】已知 LTI 因果系统的输入输出关系由下列方程给出：

$$
\frac {d y (t)}{d t} + 1 0 y (t) = - x (t) + \int_ {- \infty} ^ {\infty} x (\tau) z (t - \tau) d t
$$

解：

$$
z (t) = e ^ {- t} u (t) + 3 \delta (t), \text {   求:   系统函数   } H (s) \text {   和单位冲激相应   } h (t) 。   h (t) + 1 0 h (t) = - \delta (t) + \int_ {- \infty} ^ {\infty} \delta (\tau) z (t - \tau) d t = - \delta (t) + z (t) = e ^ {- t} u (t) + 2 \delta (t)
$$

$h(t) = Ae^{-10t}$ (齐次部分)

$$
\begin{array}{r l} & {h (t) = A e ^ {- t} + (\mathrm{而对}) ^ {2}} \\ & {t > 0 \mathrm{时自由项为} e ^ {- t} \mathrm{则} h _ {p} (t) = B e ^ {- t}} \\ & {- B e ^ {- t} + 1 0 B e ^ {- t} = e ^ {- t} \Rightarrow B = \frac {1}{9} \Rightarrow h _ {p} (t) = \frac {1}{9} e ^ {- t}} \\ & {\therefore h (t) = A e ^ {- 1 0 t} + \frac {1}{9} e ^ {- t}} \\ & {\left\{ \begin{array}{l l} {h ^ {\prime} (t) = a d (t) + b \Delta u (t)} & {\Rightarrow a = 2} \\ {h (t) = a \Delta u (t)} & {\Rightarrow h (0 + 1) = h (0 - 1) = 2} \\ {h (0 + 1) = A + \frac {1}{9} = 2} & {\Rightarrow A = \frac {1 7}{9}} \end{array} \right.} \\ & {\Rightarrow h (t) = (\frac {1 7}{9} e ^ {- 1 0 t} + \frac {1}{9} e ^ {- t}) u (t)} \end{array}
$$

梦马班作业

5、【2024厦门大学2】某一线性时不变系统，初始状态恒定，其微分方程如下：

$$
y ^ {\prime \prime} (t) + a _ {0} y ^ {\prime} (t) + a _ {1} y (t) = b _ {0} x ^ {\prime} (t) + b _ {1} x (t)
$$

已知当输入为 $f_{1}(t)=e^{-2t}u(t)$ 时，系统的全响应为 $(e^{-t}+2e^{-2t}-e^{-4t})u(t)$

当输入为 $f_{2}(t)=\delta(t)-2e^{-2t}u(t)$ 时，系统的全响应为 $(3e^{-t}-4e^{-2t}+4e^{-4t})u(t)$

(1) 求系数 $a_{0}$ 和 $a_{1}$ 的值;

(2) 求系统的零输入响应 $y_{zi}(t)$ 和冲激响应 $h(t)$ ;

(3) 求 $b_{0}$ 和 $b_{1}$ 的值。

(3) 求 $b_0$ 和 $b_1$ 的值。
解 (1) 由 $f_1(t) = e^{-\alpha} u(t)$ 对应完全响应的形式可知。
-1 和 -4 为余分特征根
即 $(\alpha + 1)(\alpha + 4) = \alpha^2 + 5\alpha + 4$ 故 $a_0 = 5, a_1 = 4$ 设系统恒定初始状态下零输入响应为 $\beta_{1}$

$f(t)=e^{-2t}$ (1) 对应更状态为 $y_{2}(t)$

$$
f _ {1} (t) = [ e ^ {- 2 t} u + t ] = - 2 e ^ {- 2 t} u (t) + \delta (t) = f _ {2} (t)
$$

$$
y _ {x} ^ {\prime} (t)
$$

$$
y _ {i} (t) + y _ {2 s} (t) = \left(e ^ {- t} + 2 e ^ {- 2 t} - e ^ {- 4 t}\right) (u t)
$$

$$
y _ {2 i} (t) + y _ {x i} (t) = (3 e ^ {- t} - 4 e ^ {- x t} + 4 e ^ {- (t)} u (t))
$$

②-①得 $y_{x}(t)-y_{x}(t)=(2e^{-t}-6e^{-2t}+5e^{-4t})u(t)$

$$
y _ {2 s h} (t) = A e ^ {t}
$$

$$
y _ {x p} (t)
$$

$$
2 e ^ {- t}
$$

$$
- 6 e ^ {- 2 t} \cdot 5 e ^ {- 4 t}
$$

$$
B _ {2} e ^ {- x}
$$

$$
\begin{array}{r l} & {\Rightarrow B _ {1} e ^ {- t} - B _ {2} e ^ {- t}} \\ & {- B _ {1} e ^ {- t} - B _ {1} e ^ {- t} = 2 e ^ {- t} \Rightarrow B _ {1} = - 1} \\ & {- 2 B _ {2} e ^ {- 2 t} - B _ {2} e ^ {- 2 t} = - 6 e ^ {- 2 t} \Rightarrow B _ {2} = 2} \\ & {- 4 B _ {3} e ^ {- 4 t} - B _ {3} e ^ {- 4 t} = 5 e ^ {- 4 t} \Rightarrow B _ {3} = - 1} \\ & {\Rightarrow y _ {x, t} (t) = A e ^ {t} - e ^ {- t} + 2 e ^ {- x} - e ^ {- 4 t}} \end{array}
$$

无烟度 $y_{x}(14) = A - 1 + 2 - 1 = 0 \Rightarrow A = 0$

官网：www.tongxinkaoyan.com

$$
\Rightarrow y _ {2 1} | t | = \left(- e ^ {5 t} + 2 e ^ {- x} - e ^ {- 4 t}\right) (u | t)
$$

梦马班作业

$$
\begin{array}{r l} {1 0 9 5 8 4 1 8 7 8} & {\Rightarrow y _ {2 i} (t) = 2 e ^ {- t} u (t)} \\ & {\quad f _ {2 i} (t) \mathrm{对应的要状态响应} = h (t) - 2 y _ {x} (t) = y _ {2 s} ^ {\prime} (t)} \\ & {\Rightarrow h (t) = y _ {x s} ^ {\prime} (t) + 2 y _ {2 s} (t)} \\ & {\qquad = [ e ^ {- t} - 4 e ^ {- 2 t} + 4 e ^ {- 4 t} ] u (t) + 2 [ - e ^ {- t} + 2 e ^ {- 2 t} - e ^ {- 4 t} ] u (t)} \\ & {\qquad = (- e ^ {- t} + 2 e ^ {- 4 t}) u (t)} \end{array}
$$

(3)

$$
\begin{array}{r l} {b _ {0} x ^ {\prime} (t) + b _ {1} x (t)} & {= b _ {0} \left[ - 2 e ^ {- 2 t} (u (t) + d ^ {\prime} (t)) + b _ {1} \cdot e ^ {- 2 t} (u (t) \right.} \\ & {= (- 2 b _ {0} + b _ {1}) e ^ {- 2 t} (u (t) + b _ {0} d ^ {\prime} (t))} \end{array}
$$

$$
\begin{array}{r l} {t > 0 \mathrm{时}} & {(- 2 b _ {0} + b _ {1}) e ^ {- 2 t} \Rightarrow y _ {2 \mathrm{sp}} (t) = C e ^ {- 2 t}} \\ & {4 C e ^ {- 2 t} - 1 0 C e ^ {- 2 t} + 4 C e ^ {- 2 t} = (- 2 b _ {0} + b _ {1}) e ^ {- 2 t}} \\ & {\Rightarrow - 2 c = - 2 b _ {0} + b _ {1}} \\ & {\mathrm{其中} c = 2 \Rightarrow \sqrt {- 2 b _ {0} + b _ {1}} = - 4} \end{array}
$$

$$
\left\{ \begin{array}{l} y _ {2 s} ^ {\prime \prime} (t) = a d (t) + b \Delta u (t) \Rightarrow a = b _ {0} \\ y _ {2 s} ^ {\prime} (t) = a \Delta u (t) \Rightarrow y _ {2 s} ^ {\prime} (u + 1) = b _ {0} \\ y _ {2 s} (t) = a t \Delta u (t) \\ y _ {2 s} ^ {\prime} (u + 1) = 1 = b _ {0} \\ \therefore b _ {1} = - 4 + 2 = - 2 \end{array} \right.
$$