## 专题9 连续系统的频域分析

## 考点 1：连续系统的频域表示

1、结构框图与网络函数

已知连续LTI系统的冲激响应为 $h(t)$ ，设输入信号为 $e(t)$ ，输出为 $r(t)$ 。若

$h(t)\leftrightarrow H(\omega)$ $e(t)\leftrightarrow E(\omega)$ $r(t)\leftrightarrow R(\omega)$

则

$$
r (t) = e (t) * h (t)
$$

根据卷积定理

$$
R (\omega) = E (\omega) H (\omega)
$$

则

$$
H (\omega) = \frac {R (\omega)}{E (\omega)}
$$

$H(\omega)$ 称为系统函数，也称作系统的频率响应特性。

$$
\text { 时域 } f (t) \longrightarrow \boxed {h (t)} \longrightarrow y (t) \Rightarrow y (t) = f (t) * h (t)
$$

$$
\text {频域} F (\omega) \longrightarrow \boxed {H (\omega)} \longrightarrow Y (\omega) \Rightarrow Y (\omega) = F (\omega) \cdot H (\omega)
$$

例 46: 求下列微分方程所描述系统的频率响应 $H(\omega)$ 。

(1) $y''(t) + 3y'(t) + 2y(t) = f'(t);$

$$
(2) y ^ {\prime \prime} (t) + 5 y ^ {\prime} (t) + 6 y (t) = f ^ {\prime} (t) + 4 f (t) 。
$$

## 考点2：网络函数的应用

(1)求零状态

$$
Y _ {z s} (\omega) = F (\omega) \cdot H (\omega) \stackrel {\text {逆变换}} {\rightarrow} y _ {z s} (t)
$$

(2)与直流卷积

(3)与 $e$ 指数卷积

(4)与 $cos\omega_0t$ 卷积

夢馬考研

## 考点3：无失真系统频谱特点

所谓无失真是指响应信号与激励信号相比，只是大小与出现的时间不同，而无波形上的变化。设激励信号为 $e(t)$ ，响应信号为 $r(t)$ ，无失真传输的条件是时域表示：

$$
r (t) = k e (t - t _ {0})
$$

系统的冲激响应：

$$
h (t) = k \delta (t - t _ {0})
$$

系统的频率响应：

$$
H (\omega) = k e ^ {- j \omega t _ {0}}
$$

无失真传输系统的幅度和相位特性如所示。

![](images/693e9bdba1810fc963ffbce3a95ad82bdbbed535b2be5d2b867ae11614cd0a0b.jpg)

也就是说， $H(\omega)$ 的幅频特性必须是一个与频率无关的常数，相位必须是频率的线性函数。

例 47: 在以下由冲激响应或频率响应函数描述的系统中, 能够无失真传输信号的是( )。
A、 $h(t)=3\delta(t-3)$ B、 $h(t)=\sin2t$ C、 $H(j\omega)=\frac{2-j\omega}{2+j\omega}$ D、 $H(j\omega)=2e^{-j\omega}, |\omega|<1$

考点4：全通系统频谱特点

全通系统的幅频特性为常数， $|H(\omega)| = k$ ，相位特性不受任何约束，一般用来相位均衡器或移相器。

## 考点 5：理想低通滤波器

1、理想低通滤波器的频谱特性:

系统函数:

$H(\omega) = \left\{ \begin{array}{ll}e^{-j\omega t_0} & |\omega | <   \omega_c\\ 0 & \omega \text{为其他值} \end{array} ,t_0\right.$ 为常数

![](images/5629e53470b7069fc5cd18cb8ce0664df446e0ba00140abb14f30c8751f0b5f2.jpg)  
理想低通滤波器的幅频与相频特性

## 考点6：相关：比较某信号与另一个延时 $\tau$ 的信号之间的相似程度

## 应用背景：(1)雷达回波识别(2)通信同步信号识别

1、自相关与互相关

(1)设 $f_{1}(t)$ 与 $f_{2}(t)$ 为能量有限信号，则

互相关

$$
R _ {1 2} (\tau) = \int_ {- \infty} ^ {\infty} f _ {1} (t) f _ {2} (t - \tau) d t = \int_ {- \infty} ^ {\infty} f _ {1} (t + \tau) f _ {2} (t) d t
$$

自相关

$$
R (\tau) = \int_ {- \infty} ^ {\infty} f (t) f (t - \tau) d t = \int_ {- \infty} ^ {\infty} f (t + \tau) f (t) d t
$$

具有性质

$$
R _ {1 2} (\tau) = R _ {2 1} (- \tau), R (\tau) = R ^ {*} (- \tau)
$$

(2)设 $f_{1}(t)$ 与 $f_{2}(t)$ 为功率有限信号，则

互相关

$$
R _ {1 2} (\tau) = \lim _ {T \rightarrow \infty} \left[ \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {1} (t) f _ {2} (t - \tau) d t \right]
$$

自相关

$$
R (\tau) = \lim _ {T \to \infty} \left[ \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f (t) f (t - \tau) d t \right]
$$

2、相关与卷积的关系

$$
R _ {1 2} (t) = f _ {1} (t) * f _ {2} (- t)
$$

3、相关定理

维纳—欣钦关系

$$
\left\{ \begin{array}{l} R (\tau) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \phi (\omega) e ^ {j \omega \tau} d \omega \\ \phi (\omega) = \int_ {- \infty} ^ {\infty} R (\tau) e ^ {- j \omega \tau} d \tau \end{array} \right.
$$

即功率有限信号的功率谱函数与自相关函数是一对傅里叶变换。在实际中，有些信号无法求它的傅里叶变换，但可用求自相关函数的方法，达到求功率谱的目的。

## 【梦马班点拨】总结——自相关和互相关函数的求解

(1) 定义法 $\leftrightarrow$ 表达式法

(2) 图解法 (类似于卷积)

(3) 频域逆变换法: 已知 $f(t) \leftrightarrow F(\omega)$ ，求 $f(t)$ 的自相关 $R(\tau)$ .

例 48: 已知 $f(t) = u(t) - u(t - 2)$ ，求信号 $f(t)$ 的自相关函数 $R(\tau)$

例 49: 求 $f(t) = e^{-\alpha t} u(t)$ 的自相关函数.

例 50: $x(t)$ 的自相关函数 $R_{x}(\tau)$ 的傅里叶变换 $P_{x}(\omega)$ 如图所示，信号 $x(t)$ 的同相分量 $x_{c}(t)$ 的自相关函数可表示为

$$
R _ {x c} (\tau) = R _ {x} (\tau) \cos (\omega_ {c} \tau) + \widehat {R} _ {x} (\tau) \sin (\omega_ {c} \tau)
$$

其中 $\widehat{R}_x(\tau)$ 为 $R_{x}(\tau)$ 的希尔伯特变换。求 $R_{xc}(\tau)$ 的傅里叶变换 $P_{xc}(\omega)$ ，并画出 $P_{xc}(\omega)$ 的图形。

![](images/a7e81568d967535ebb333972c07f68ba6dfdb80610ef7bfa442edf9423040944.jpg)

## 考点 7：功率谱与能量谱

## 1、能量信号和能量谱

## (1)能量信号

信号在时间区间 $(- \infty, \infty)$ 内的能量为有限值，而在时间区间 $(- \infty, \infty)$ 内的平均功率 $P = 0$ ，这样的信号称为能量信号。大多数时限信号为能量信号。有些信号既不属于能量信号也不属于功率信号，例如 $f(t) = e^{t}; \delta(t)$ 为无定义的非功率非能量信号。

## (2)能量信号能量E的计算公式:

时域公式:

$$
E = \int_ {- \infty} ^ {\infty} | f (t) | ^ {2} d t
$$

频域公式:

$$
E = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | F (\omega) | ^ {2} d \omega
$$

## (3)能量谱

令 $G(\omega) = |F(\omega)|^2$ ， $G(\omega)$ 的单位为 $J / rad$ ，则

$$
E = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} G (\omega) d \omega
$$

$G(\omega)$ 称为能量信号的能量频谱密度，简称能量谱。它描述了单位频带内信号的能量随 $\omega$ 分布的规律。

例 51: 令 $f(t) = e^{-\alpha t} u(t)$ ，如果频带 $(- \omega_B, \omega_B)$ 将包含信号总能量的 50%，求 $\omega_B$ 。

## 2、功率信号和功率谱

## (1)功率信号

信号在时间区间 $(- \infty, \infty)$ 内的能量为 $\infty$ ，但平均功率为有限值，这样的信号称为功率信号。周期信号、阶跃信号、符号函数等为功率信号。

(2)功率信号平均功率P的计算公式

时域公式:

$$
P = \lim _ {T \to \infty} \frac {1}{T} \int_ {T} | f (t) | ^ {2} d t
$$

频域公式(对于周期信号):

$$
P = c _ {0} ^ {2} + \sum_ {n = 1} ^ {\infty} \left(\frac {c _ {n}}{\sqrt {2}}\right) ^ {2} = \sum_ {n = - \infty} ^ {\infty} | F _ {n} | ^ {2}
$$

即平均功率 $P$ 等于频域中直流分量与各次谐波分量平均功率之和。

(3)功率谱密度

$$
\phi (\omega) = \lim _ {T \to \infty} \frac {| F _ {T} (\omega) | ^ {2}}{T} = 2 \pi \sum_ {n = - \infty} ^ {\infty} | F _ {n} | ^ {2} \delta (\omega - n \omega_ {1})
$$

其中 $F_{T}(\omega)$ 为功率信号 $f(t)$ 的截断函数 $f_{T}(t)$ 的傅里叶变换。

(4)功率有限信号的功率谱与自相关函数是一对傅里叶变换对维纳辛钦关系

$$
\left\{ \begin{array}{l} R (\tau) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \phi (\omega) e ^ {j \omega t} d \omega \\ \phi (\omega) = \int_ {- \infty} ^ {\infty} R (\tau) e ^ {- j \omega \tau} d \tau \end{array} \right.
$$

即功率有限信号的功率谱函数与自相关函数是一对傅里叶变换。在实际中，有些信号无法求它的傅里叶变换，但可用求自相关函数的方法，达到求功率谱的目的。

$$
R (\tau) = \lim _ {T \to \infty} [ \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f (t) f (t - \tau) d t ]
$$

对其取傅里叶变换可得:

$$
\begin{array}{r} F T [ R (\tau) ] = F T \left[ \lim _ {T \to \infty} \frac {1}{T} \int_ {- \infty} ^ {\infty} f _ {T} (t) \cdot f _ {T} (t - \tau) d t \right] = F T \left[ \lim _ {T \to \infty} \frac {1}{T} [ f _ {T} (\tau) * f _ {T} (- \tau) ] \right] \\ = \lim _ {T \to \infty} \frac {1}{T} F _ {T} (\omega) \cdot F _ {T} ^ {*} (\omega) = \lim _ {T \to \infty} \frac {1}{T} | F _ {T} (\omega) | ^ {2} \end{array}
$$

例 52: $f(t) = U_{m} \cos \omega_{0} t$ 的自相关函数和功率谱.

例53： $f(t) = U_{1}\cos \omega_{1}t + U_{2}\cos \omega_{2}t$ 的自相关函数和功率谱.

## 考点 8：能量谱和功率谱的求解推荐

1、功率信号→功率谱

(1)周期信号是功率信号→考察多三角信号之和

(2)傅里叶级数 $F_{n}$

(3)平均功率： $P = \sum_{n = -\infty}^{\infty}|F_n|^2$

(4)功率谱： $\phi (\omega) = 2\pi \sum_{-\infty}^{\infty}|F_n|^2\delta (\omega -n\omega_0)$

(5)自相关： $\phi(\omega)$ 逆变换得 $R(\tau)$

## 2、能量信号→能量谱

(1)持续时间有限信号和 $t\to\infty$ 时， $f(t)\to0$ 的信号

(2)能量： $E = \int_{-\infty}^{\infty}|f(t)|^{2}dt = \frac{1}{2\pi}\int_{-\infty}^{\infty}|F(\omega)|^{2}d\omega$

(3)能量谱： $G(\omega) = |F(\omega)|^2$

(4)自相关： $G(\omega)$ 逆变换得 $R(\tau)$

例 54: 已知信号 $x(t) = 16 \cos \left(20\pi t + \frac{\pi}{4}\right) + 6 \cos \left(30\pi t + \frac{\pi}{6}\right) + 4 \cos \left(40\pi t + \frac{\pi}{3}\right)$ .

(1) 计算并画出信号的功率谱

(2) 计算包含在频率区间 12\~22Hz 范围内的功率是多少?

![](images/6644c842da00cf2cba473275a86de8a82897434e6f03cc6c261a561de4718ba5.jpg)

例 55: 若信号 $f(t) = A \cos(100\pi t) \cdot \cos(1000\pi t)$ ，求：

(1)判断该信号为能量信号还是功率信号;

(2)计算自相关函数；

(3)求功率谱密度或是能量谱密度;

(4)求信号平均功率或是归一化能量。