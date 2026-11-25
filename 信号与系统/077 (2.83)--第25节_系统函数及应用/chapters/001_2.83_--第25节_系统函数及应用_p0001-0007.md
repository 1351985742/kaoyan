## 专题3 系统函数及应用

## 考点1：系统函数的定义及意义

1、定义：

$$
H (s) = \frac {R (s)}{E (s)}
$$

零状态响应的拉氏变换与激励的拉氏变换之比。

## 2、物理意义：

系统函数的逆拉氏变换即为系统的冲激响应，即 $h(t) = \mathcal{L}^{-1}[H(s)]$ 。

$h(t)$ 为冲激响应，取决于系统本身的结构，描述了系统的固有性质； $H(s)$ 也仅仅决定于系统结构， $H(s)$ 是表征系统特性的重要参数。冲激响应 $h(t)$ 与系统函数 $H(s)$ 从时域和变换域两方面表征了同一系统的特性。

对给定的激励 $e(t)$ ，其零状态响应为 $r_{zs}(t)=\mathcal{L}^{-1}[H(s)E(s)]$ 。

## 考点2：系统函数的求解

1、定义法：给定系统的输入和零状态响应，严格按照两者拉氏变换结果之比求解；

2、直接由冲激响应求，即 $H(s)=\mathcal{L}[h(t)]$ ;

3、从零状态系统的微分方程出发，两端取拉氏变换求 $H(s)$ ，即 $H(s)=\frac{R(s)}{E(s)}=\frac{\text{右边形式}}{\text{左边形式}};$

4、从零状态s域电路模型出发，按基本定义式求响应的拉氏变换与激励的拉氏变换的比，即 $H(s)=\frac{R(s)}{E(s)}$ ;【后续学习】

5、从系统的框图/流图出发，通过梅森公式直接写出系统函数。【后续学习】例 16：已知激励信号为 $e(t)=e^{-t}u(t)$ ，零状态响应为 $r(t)=\left(\frac{1}{2}e^{-t}-e^{-2t}+2e^{3t}\right)u(t)$ ，求系统函数。

例 17: 已知系统微分方程 $r''(t) + 3r'(t) + 2r(t) = e'(t) + 3e(t)$ ，求系统函数。

夢馬考研

## 考点3：系统函数的应用

1、求解系统方程 $H(s)=\frac{R_{zs}(s)}{E(s)}=\frac{右边形式}{左边形式}$

2、求解系统的冲激响应： $H(s)\xrightarrow{\text{逆变换}}h(t)$

3、求解系统的阶跃响应： $G(s)=\frac{H(s)}{s}\xrightarrow{\text{逆变换}}g(t)$

4、求解系统的零状态响应： $R_{zs}(s)=H(s)\cdot E(s)\xrightarrow{\text{逆变换}}r_{zs}(t)$

例 18: 已知微分方程 $r''(t) + 3r'(t) + 2r(t) = e'(t) + 3e(t)$ ， $e(t) = e^{-4t}u(t)$ ，求 $h(t)$ 、 $g(t)$ 、 $r_{zs}(t)$ 。

5、求解系统某一特征值的复频域响应

若输入为 $e^{s_0t}$ ，则对应输出为 $H(s_0)e^{s_0t}$ 【要求 $s_0$ 在ROC内， $s_0$ 为复常数】，当 $s_0 = 0$ 时，输入为直流信号 $E = E \cdot e^{0 \cdot t}$ (E看为系数)，则对应的输出 $E \cdot H(0) \cdot e^{0 \cdot t} = E \cdot H(0)$

6、系统零极点分布判断系统内在特性【详见下一节内容】

【新增引例与分析】

(1) 系统响应分解: 自由+强迫, 零输入+零状态, 稳态+暂态;

(2) 稳态存在的条件:

(3) 如果稳态存在，一定存在于。。。。。。。响应中。

例 20: 已知 $H(s)=\frac{s+2}{s^{2}+5s+4}$ ，激励为 $e(t)=5\cos(2t)u(t)$ ，求输出信号。

## 7、求稳态响应

(1)稳态响应存在的条件：当输入为阶跃信号或者有始周期信号时，稳定系统的完全响应分解为稳态+暂态，其中稳态通常由阶跃信号或有始周期信号组成；如果输入非阶跃信号或非有始周期信号或系统为不稳定系统，则完全响应不能按此分解，在输入为阶跃或有始周期信号时，稳定系统的强迫响应也称稳态响应。

(2)在完全响应中，当 $t\to\infty$ 时，等于0的部分称之为瞬(暂)态响应，剩余部分称之为稳态响应。

(3)激励为三角信号时的稳态响应

若激励为 $e(t)=E_{m}\sin(\omega_{0}t)$ 或 $e(t)=E_{m}\cos(\omega_{0}t)$

则系统稳态响应结果： $r_{ss}(t)=E_{m}H_{0}\sin(\omega_{0}t+\varphi_{0})$ 或 $r_{ss}(t)=E_{m}H_{0}\cos(\omega_{0}t+\varphi_{0})$

(4)稳态响应的求解步骤:

①根据 $e(t)$ 明确 $E_{m}$ 和 $\omega_{0}$ 的大小

② $H(j\omega_{0})=H(s)/s=j\omega_{0}$ ，将 $H(j\omega_{0})$ 化成一个复数 $z=a+bj$ （明确实部和虚部）

③ $H_{0} = \left|H(j\omega_{0})\right|$ ， $\varphi_{0}$ 为相角【 $z = a + bj$ $\quad |z| = \sqrt{(a^2 + b^2)}$ $\quad \varphi = \arctan{\frac{b}{a}}$ 】

④将 $E_{m},\omega_{0},H_{0},\varphi_{0}$ 带入结论。

例 19: 已知 $H(s)=\frac{s+2}{s^{2}+5s+4}$ ，激励为 $e(t)=5\cos(2t)u(t)$ ，求稳态响应。

(5) 激励为三角信号时的响应 (严格不能称之为稳态响应)

若激励为 $e(t)=E_{m}\sin\left(\omega_{0}t\right)$ 或 $e(t)=E_{m}\cos\left(\omega_{0}t\right)$

则系统稳态响应结果:

$$
r _ {s s} (t) = E _ {m} H _ {0} \sin (\omega_ {0} t + \varphi_ {0}) \text {或} r _ {s s} (t) = E _ {m} H _ {0} \cos (\omega_ {0} t + \varphi_ {0})
$$

## 【梦马班点拨】对稳态的总结：

$$
\begin{array}{r l} & H (s) \quad \left\{ \begin{array}{l l} s = j \omega \\ H (j \omega) \end{array} \right. \left\{ \begin{array}{l l} \cos (\omega_ {0} t) & \longrightarrow \text {输出:} | H (j \omega_ {0}) | \cos [ \omega_ {0} t + \varphi (\omega_ {0}) ] (\text {不加} u (t)) \\ \cos (\omega_ {0} t) u (t) & \longrightarrow \left\{ \begin{array}{l l} \text {稳态:} | H (j \omega_ {0}) | \cos [ \omega_ {0} t + \varphi (\omega_ {0}) ] u (t) \\ \text {输出:} [ \sum_ {i} A _ {i} e ^ {\alpha_ {i} t} + | H (j \omega_ {0}) | \cos [ \omega_ {0} t + \varphi (\omega_ {0}) ] ] u (t) \end{array} \right. \end{array} \right. \end{array}
$$