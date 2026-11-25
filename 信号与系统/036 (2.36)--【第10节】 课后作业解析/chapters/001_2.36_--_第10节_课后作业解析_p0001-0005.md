## 【第10节】课后作业

1、【2024 重庆邮电大学 3】某系统的全响应 $y(t)$ 与激励 $f(t)$ 以及初始状态 $x(0)$ 的关系表达式为

$$
y (t) = e ^ {- t} \cdot x (0) + \int_ {- \infty} ^ {t} \sin (\tau) f (\tau) d \tau
$$

判断该系统是否为线性系统？

解：完全向应 $y(t)$ 具有可分解性， $y_{i}(t)=e^{-t}x(0)$ ， $y_{s}(t)=\int_{-\infty}^{t}\sin(\tau)f(\tau)d\tau$ (1) $y_{i}(t)$ 线化判断：让初始状态乘 $e^{-t}$

$$
[ a _ {1} x _ {1 0}) + a _ {2} x _ {2 0}) ] = e ^ {- t} [ a _ {1} x _ {1 0}) + a _ {2} x _ {2 0}) ]\tag{①}
$$

$$
a _ {1} y _ {2 i _ {1}} (t) + a _ {2} y _ {2 i _ {2}} (t) = a _ {1} e ^ {- t} x _ {1} (0) + a _ {2} e ^ {- t} x _ {2} (0)\tag{2}
$$

①=② 故y比对初始状态呈线性关系

(2) $y_{x}(t)$ 线性判断：让激励 t→t，求 $\sin(\tau)$ 后填加 $\int_{-\infty}^{t} d\tau$ 和 $H[a_{1}f_{1}(t)+a_{2}f_{2}(t)]=\int_{-\infty}^{t}\sin(\tau)\left[a_{1}f_{1}(t)+a_{2}f_{2}(t)\right]d\tau$ ③ $a_{1}y_{x_{1}}(t)+a_{2}y_{x_{2}}(t)=a_{1}\int_{-\infty}^{t}\sin(\tau)f_{1}(t)d\tau+a_{2}\int_{-\infty}^{t}\sin(\tau)f_{2}(t)d\tau$ ④

③ = ④ 故 $y_{x}(t)$ 与激励呈线性关系

综上所述，该系统为线性系统。

2、【2024 华侨大学 3.1】设系统的初始状态为 $x(0)$ , 输入为 $f(t)$ , 完全响应为 $y(t)$ , 试判断下系统的性质（线性/非线性, 时变/时不变, 因果/非因果, 稳定/不稳定）;

$$
y (t) = 5 x (0) + f (2 t) + f (t + 3)
$$

(1) $y_{i1}$ 具有可分辨性, 其中 $y_{21}|t|=5x(10)$ , $y_{25}|t=f(2t)+f(1t+3)$ $H[a_1x_1(10)+a_2x_2(10)]=5[a_1x_1(10)+a_2x_2(10)] ①$ $a_1y_{2i1}(t)+a_2y_{2i2}(t)=a_15x_1(10)+a_25x_2(10) ②$ $H[a_1f(1t)+a_2f_2(1t)]=\left[a_1f_1(2t)+a_2f_2(2t)\right]+\left[a_1f_1(1t+3)+a_2f_2(1t+3)\right] ③$ $a_1y_{2s1}(t)+a_2y_{2s2}(t)=a_1[f_1(2t)+f_1(1t+3)]+a_2[f_2(2t)+f_2(1t+3)] ④$ ①=②, ③=④ 故系统为线性系统:

12) $H[f(t-t_{0})] = f(2t-t_{0}) + f(t+3-t_{0})$ ⑤ $y[t-t_{0}] = f(2(t-t_{0}) + f(t-t_{0}+3))$ ⑥

⑧ ⑨ ⑩ 系元为时度系统.

(3) $y_{x}(t) = f(2t) + f(t+3)$ 令 t=1 即 $y_{x}(1) = f(2) + f(4)$ 可见存在响应超前波动. 故非因果系统

(6) $\frac{1}{0}|f(t)|\leq M$ 则 $|y_{x}(t)|=|f(x)+f(t+3)|\leq|f(x)|+(|f(t+3)|\leq M+M=2M$ 说明系统为稳定系统.

梦马班作业

3、【2024 电子科技大学 3】某二阶连续因果线性时不变系统，初始条件为 $y(0^{-}), y'(0^{-})$ ，已知：

(a) 当 $y(0^{-}) = 2, y' (0^{-}) = 0, y_{zi1}(t) = (4e^{-t} - 2e^{-2t})u(t)$

(b) 当 $y(0^{-}) = 0, y' (0^{-}) = 1, y_{zi2}(t) = (e^{-t} - e^{-2t})u(t)$

(c) 当输入 $x_{1}(t), y(0^{-}) = 1, y^{\prime}(0^{-}) = -1$ , 全响应 $y(t) = (1 + e^{-2t})u(t)$

求: $x_{2}(t) = 3x_{1}(t)$ 时, $y(0^{-}) = 2, y^{\prime}(0^{-}) = -2$ , 全响应 $y_{2}(t)$ 在 $t > 0$ 时的表达式

$\frac{1}{2}(a)-(b) \Rightarrow y_{1}(a^{-})=1, y_{1}(a^{-})=-1, \text{对} \frac{1}{2}y_{2i1}(a- y_{2i2}(a))=e^{-t}u(t)$

由(0)可知： $x_{1}(t)$ 对应要状态响应为 $y(t)-e^{-t}u(t)=\left(1+e^{-2t}-e^{-t}\right)(u(t))$

故 $x_{2}(t)=3x_{1}(t)$ 时 $y(0-2)=2$ ， $y'(0-2)=-2$ 时

$$
\begin{array}{r l} {y _ {2 | t |}} & {= 3 (1 + e ^ {- x t} - e ^ {- t}) u (t) + 2 e ^ {- t} u (t)} \\ & {= (3 + 3 e ^ {- x t} - e ^ {- t}) u (t)} \end{array}
$$

B站up: 信号与系统\_谷哥

5、【2024 天津工业大学 27】某LTI系统, 系统起始状态为 $y(0_{-})$ , 已知: 当 $y(0_{-}) = 1$ , 激励为因果信号 $f(t)$ 时, 全响应 $y_{1}(t) = (e^{-t} + \cos \pi t) z(t)$ ; 当 $y(0_{-}) = 2$ , 激励为因果信号 $3f(t)$ 时, 全响应 $y_{2}(t) = 2\cos \pi t z(t)$ , 利用时域分析方法求 $y(0_{-}) = -2$ ,

激励为因果信号 $3f'(t) + f(t-1)$ 时，全响应 $y_{3}(t)$ 。

解：令 $y_{(0,-1)} = 1$ ，鼓励 f(t) 分别对应的差输入和差状态为 $y_{2i}(t)$ 和 $y_{2k}(t)$

$$
\mathrm{则} y _ {1} (t) = y _ {x} (t) + y _ {x} (t). = [ e ^ {- t} + \cos (\pi t) ] u (t) ①
$$

故 ${y}_{2}\left( t\right)  = 2{y}_{2} : \left( t\right)  + 3{y}_{x}\left( t\right)  = {20\cos \pi } + \operatorname{arct}$

① ②联立可知: $y_{x|t|} = -2e^{-t}u(t)$ $y_{2i|t|} = (3e^{-t} + \cos\pi t)u(t)$

$$
\begin{array}{r l} {\mathrm{故} y _ {3} (t)} & {= - 2 y _ {1} (t) + 3 y _ {2} (t) + y _ {2} (t - 1)} \\ & {= (- 6 e ^ {- t} - 2 \cos \pi t) u (t) - 6 [ - e ^ {- t} u (t) + d (t) ] - 2 e ^ {- (t - 1)} u (t - 1)} \\ & {= - 2 \cos \pi t (u (t)) - 6 d (t) - 2 e ^ {- (t - 1)} u (t - 1)} \end{array}
$$

【2024 广东工业大学 3.3】描述某 LTI 系统的微分方程为 $y''(t) + 4y'(t) + 4y(t) = f'(t) + 3f(t)$ ，已知 $x(t) = e^{-t}u(t)$ ， $y(0_{+}) = 1$ ， $y'(0_{+}) = 3$ ，系统的零输入响应 $y_{zi}(t)$ 和零状态响应 $y_{zs}(t)$ 。

$$
\alpha^ {2} + 4 \alpha + 4 = (\alpha + 2) ^ {2} = 0
$$

$$
\mathrm{故} y _ {x} (t) = (A _ {1} t + A _ {2}) e ^ {- 2 t} + 2 e ^ {- t}
$$

$$
\alpha_ {1, 2} = - 2 (= \mathrm{重根})
$$

$$
y _ {3} ^ {\prime \prime} (t) = a 0 (t + 1) + b \Delta (u t) \Rightarrow a = 1
$$

$$
\begin{array}{r l} {f (t) + 3 f (t)} & {= [ e ^ {- t} u (t) ] ^ {\prime} + 3 e ^ {- t} u (t)} \\ & {= - e ^ {- t} u (t) + \sqrt {(t)} + 3 e ^ {- t} u (t)} \\ & {= 2 e ^ {- t} u (t) + \sqrt {(t)} \mathrm{触项}} \end{array}
$$

$$
y _ {x} ^ {\prime} (t) = a \Delta (1 + t) \Rightarrow y _ {x} ^ {\prime} (a +) = a = 1
$$

$$
y _ {x} (t) = a t \Delta u (t) \Rightarrow y _ {x} (a t) = 0
$$

$t > 0$ 自由项 $= 2{e}^{-t}$ ,故 ${y}_{p}\left( t\right)  = B{e}^{-t}$

$$
\left\{ \begin{array}{l l} y _ {x 1} (x +) = A _ {2} + 2 = 0 \\ y _ {x 1} ^ {\prime} (x +) = A _ {1} - 2 A _ {2} - 2 = 1 \end{array} \right.
$$

$$
\begin{array}{r l} {B e ^ {- t} - 4 B e ^ {- t} + 4 B e ^ {- t}} & {= 2 e ^ {- t}} \\ {B} & {= 2} \\ {g _ {p} (t)} & {= 2 e ^ {- t} (u (t))} \end{array}
$$

$$
\Rightarrow A _ {2} = - 2, A _ {1} = - 1
$$

$$
\Rightarrow y _ {x} | t | = [ (- t - 2) e ^ {- x t} + 2 e ^ {- t} ] u (t)
$$

$$
\sum y _ {2 i} (t) = (C t + D) e ^ {- x t}
$$

$$
\Rightarrow y (t) = \left[ (c - 1) t + (D - 2) \right] e ^ {- 2 t} + 2 e ^ {- t}
$$

$$
y (V _ {+}) = D - 2 + 2 = 1 \Rightarrow D = 1
$$

$$
y ^ {\prime} (t) = \left[ C - 1 \right] e ^ {- t} + \left[ (C - 1) t + (D - 2) \right] - 2 e ^ {- t}   \text {   由   } - 2 e ^ {- t} / t = 0
$$

$$
y ^ {\prime} (0 + 1) = c - 1 - 2 (0 - 2) - 2 = 3
$$

$$
\Rightarrow c = 4
$$

$$
\Rightarrow y _ {2 i} (t) = (4 t + 1) e ^ {- 2 t} (u t)
$$

官网：www.tongxinkaoyan.com

梦马班作业