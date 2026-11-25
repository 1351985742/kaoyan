e: $f(t) \rightarrow$ A + $f(t)$ [A + $f(t)$ ]coswct $\leftrightarrow$ -wc

(每元)

发点

接收

含有载射

到波信息

典型两种调幅

AM
善画双边带调幅

≤3.3%

DTB
抑到载波双边带调幅

(及熵双半高)

相同:

常宽2Wm

f(t) → x →

单边带调幅信号 SSB

$1^{0}$ 浪泻法

![](images/94fc8c7cd0d97c8da4d19193c68fb99abdd3566cefd086d3f45a24b7053b3d87.jpg)

登陆中用漏洞队，得不到SSB → VSB 弹也带

![](images/e658f12d4cdef946151ee30bce71eef0b382b060e932c64c4b160fd0e952f4c2.jpg)

$S_{DSB}(t)$

B站up: 信号与系统\_谷哥

专题 8 希尔伯特变换及 SSB 信号

考点 1：振幅调制 AM(常规双边带)信号

$$
s _ {A M} (t) = [ A + m (t) ] c o s \omega_ {c} t = A c o s \omega_ {c} t + m (t) c o s \omega_ {c} t
$$

![](images/289b4c1f24ad69201e79ab86d3031c8910b69cf00011ef77c3b1f8fe95dd38c3.jpg)

由 AM 信号频谱图可以看出，AM 信号中携带了载波频率信息，传输 AM 信号的带宽需要 $2 \omega_{m}$ 。

考点 2: DSB: 双边带信号

$$
s _ {D S B} (t) = m (t) \cos \omega_ {c} t
$$

DSB 信号的波形和频谱，因为不存在载波分量，调制效率为 $100\%$ ，比 AM 高，但传输 DSB 信号的带宽也为 $2 \omega_{m}$

![](images/c45b03e3b86c6cd8fb6dc9bab459286a4d596e169210a846a0956cc81b3cdb55.jpg)

![](images/991ae7b5dca901d17f8373ed35d7bb60e548fe79f08d8a8915df2cfb69aea4ef.jpg)

![](images/e0ea12c858a416643840e766eb68076d1feb6b620226d5778aa4949d9fb903d7.jpg)

![](images/fb39fee382393ba5fe3f97b79fcf1d2097627e996c91731f8d17e00c3b1b8e0a.jpg)

![](images/82d768339b78626260af5c2b2f2adfddc5c45a3df6d09dc132e5ca635866a9cd.jpg)

![](images/cba6029658b1a0b095650e28e34002c8b51cb27a842c889bc633ab2efaac4bc6.jpg)

## 考点 3: SSB: 单边带信号

在 AM 信号频谱中，将频率低于载频的谱线为下边带(LSB)，频率高于载频的谱线为上边带(USB)，在调幅波频谱中的上下两个边带都含有相同的信息，只传送一个边带也就可以完成信息的传送，且传输SSB信号的带宽只需要 $\omega_{m}$ .

## 考点 4: SSB信号的产生——滤波法和移相法

1、滤波法：先产生一个 DSB 信号，然后在通过一个边带滤波器，滤除不需要的边带，即可获得单边带信号。

SSB 滤波法产生结构:

![](images/a6baa8801ce53b314ad78edab218f2c47828643703af804792b860df79c9c475.jpg)

![](images/0adb1db7a35832f800a2a6503f4f305a5b6954c6199d092be88b475efab4b5a3.jpg)

![](images/2c3e66d845b13b9748f589c441ce922f82365d03a68a1d5218c377690c951007.jpg)

![](images/7fe1393a59717b643485d622490498c2f72a3327f92ab74c3f6a0a086a6e0642.jpg)

![](images/e770d7ac9a04888acb72cd9f7edf14b19e9b4881adc0f1cb4b2ee01b5e3119d4.jpg)

![](images/7f105bd46fcdbba3bbe35bde269b7a187121ffbf45cff58d7751abd55a3e717f.jpg)

2、相移法SSB产生：利用相移网络，对载波和调制信号进行适当的相移，以便在合成过程中将其中一个边带抵消，从而获得SSB信号。

相因
1° V(W)
2° 说明系统作用

例42: 试证明题图: 所示之系统可以产生单边带信号。图中, 信号 $g(t)$ 的频谱 $G(\omega)$ 受限于 $\sim \omega_{m} \sim +\omega_{m}$ 之间, $\dot{\omega}_{0} \gg \omega_{m}$ ; $H(\omega) = -jsgn\omega$ 。设 $v(t)$ 的频谱为 $V(\omega)$ , 写出 $V(\omega)$ 表示式, 并画出图形。

$$
V (w) = G _ {1} (w) + G _ {3} (w)
$$

![](images/7963317393047f3286bcab3c986ab535886d7a8f13e48e01bb655301b78d799a.jpg)

![](images/049bb901b6e51d877161a9f066d5bc1a40ea97c0971d2aa440ab56fa87ba3460.jpg)

$$
\begin{array}{r l} {g _ {3} (t)} & {= g _ {2} (t) \cdot [ - \sin w o t ]} \\ & {= \frac {j}{2} [ - G _ {2} (w + w _ {0}) + G _ {2} (w - w _ {0}) ]} \end{array}
$$

![](images/7b44a88f972463837130e5282bdabf2891c7d9b5a7ab67e3057bddc1a74b0aad.jpg)

![](images/60e46112219fb4e6183cfc43a0dfdf2d9bde21598192022f1bfc8a97570335d7.jpg)

例43: 下图所示为一个幅度调制系统, 该系统由以下两部分组成: 先把调制信号与载波之和平方, 然后通过带通滤波器获得已调信号, 若 $g(t)$ 是带限信号, 即 $|\omega| > \omega_{m}$ 时, $G(\omega) = 0$ 。试确定带通滤波器的参数 $A, \omega_{1}, \omega_{h}$ , 使得 $f(t) = g(t)\cos \omega_{c} t$ , 并给出 $\omega_{c}$ 和 $\omega_{m}$ 的约束。

![](images/dc34a52c9c2534e33948e33cd2e6dc173fa9030ed4a0797f8c650de3709b95f8.jpg)

FT
大题
级数
结果+频数
同频FT
①用掉
②用掉的调 $F_n = \frac{1}{T_1} F_0(w)/w = nW_1$ >“心动的频谱”
恢复：无温度
无恢复： $W_c > W_m$

![](images/8e7a35055a549e6ab72a597de47bac6d936088146df1b0e1f650cd48105bb0e6.jpg)

考点 5: 希尔伯特变换

$= \int \limits_{-{b0}}^{b0} f_{1}(t) f_{2}(t \cdot 2)b$

一个实值函数 $x(t)$ 的希尔伯特变换是 $x(t)$ 和 $1/\pi t$ 的卷积。

$$
= \frac {1}{\pi} \int_ {- \infty} ^ {\infty} x | \tau | \cdot \frac {1}{t - \tau} d \tau
$$

假设 $x(t)$ 是一个实值函数，求该函数的希尔伯特变换。

$$
\hat {x} (t) = H [ x (t)) ] = x (t) * \frac {1}{\pi t} = \left(\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {x (\tau)}{t - \tau} d \tau\right)
$$

$\rightarrow  \left\lbrack  {h + 1}\right\rbrack   = {3}^{y + 1}$

因此 $\hat{x}(t)$ 可以被解读为 $x(t)$ 的线性时不变系统的输出，该线性时不变系统的脉冲

f(n \* h(eg)

响应为：

$$
\varphi = \frac {\pi}{2}
$$

![](images/e0ecad750d4143bef24effbc68b4d176e951543ccd33559799a5fb0b35cf5960.jpg)

该脉冲响应的傅里叶变换为:

![](images/33eae77874c081d21c256cc47b407de3add1dbe7c4559ea6d9fc132385216eb6.jpg)

$$
\begin{array}{r l} {H (w)} & {= \left| H (w) \right| \cdot e ^ {j (\varphi w)} = e ^ {j}} \\ & {= \left\{ \begin{array}{l l} {- j, w > 0} & {\varphi (w) =} \\ {j, w <   0} & \end{array} \right.} \\ & {\mathrm{考点6:希尔伯华}} \end{array}
$$

$$
H (\omega) = \boxed {- j s g n (\omega)} = \left\{ \begin{array}{l l} - j, & \omega > 0 \\ j, & \omega \leq 0 \end{array} \right.
$$

考点6：希尔伯特变换—90°移相器

![](images/35f09e878b2d0738ab842faec1ebd30234c6c1b93d4454512f04e28046ec7ea4.jpg)

$$
\begin{array}{l} {H (w) = | H (w) | \cdot e ^ {j (q w)}} \\ {\mathrm{问} | H (w) | = 1} \end{array}
$$

信号经过希尔伯特变换之后，频域内各频率成分的幅值不变，但相位出现 $90^{\circ}$ 相移。即正频率滞后 $\pi/2$ ，负频率导前 $\pi/2$ ，因此希尔伯特变换器又称 $90^{\circ}$ 移相器。希尔伯特变换器又称 $90^{\circ}$ 移相器，如下图。两次希尔伯特变换之后，原信号相位翻转了 $180^{\circ}$ ，四次希尔伯特变换之后又变回本身。

![](images/1964dfade8037eaa7940156599de91419927562dc3455c88fdfbf581fb662c75.jpg)

![](images/d6b619b07ff812002075aecdfd6010c4d6c3f4a1cd3cc1856b9d6281facf631b.jpg)

例 44: 如图所示, 理想 $-\pi / 2 \mathrm{rad}$ 全通相移器的频响特性定义为

$$
H (\omega) = \left\{ \begin{array}{l l} - j & \omega > 0 \\ j & \omega <   0 \end{array} \right.
$$

(1)求该相移器的单位冲激响应 $h(t)$ 。 $=\frac{1}{\pi t}$ (2)对于任意输入 $e(t)$ ，求该相移器的输出 $r(t)$ 。 $=e(t)\times\frac{1}{\pi t}$ = $\frac{1}{\pi}\int_{-\infty}^{+\infty}\frac{e(\tau)}{t-\pi}d\tau$

(3)当 $e(t)=\cos\omega_{0}t$ 时求该相移器的输出 $r(t)$ 。

$$
e (t) \xrightarrow {\text {相位器}} \boxed {- \frac {\pi}{2} r a d} \xrightarrow {r (t) = \hat {e} (t)}
$$

张

$\hat{3}k = 2$

李良作用$r(t)=e(t-\frac{2}{2})$ $=cos(wot-\frac{\pi}{2})$ $=sinwot\sin wot$

![](images/5c8b50ea25bc40daeecc351cf7de89690682b9e918f83428ba4d7946ef102b47.jpg)

![](images/de2dfe58c0d5ce8d46fc2680182661946460df3c49e04151e9f157528fe44ee2.jpg)

![](images/7bc0fa9bb8e01b07bf0c707a79d3052f4c5a47eba88f0b898f62d0fa1d0a648b.jpg)

考点7：系统可实现的(因果)的约束条件—希尔伯特变换变换对

系统可实现性的实质是具有因果性。本节将要证明，由于因果性的限制，系统函数的实部与虚部或模与辐角之间将具备某种相互制约的特性，这种特性以希尔伯特(Hilbert)变换的形式表现出来。
对于因果系统，其冲激响应 $h(t)$ 在t<0时等于0，仅在t>0时存在，因此
设 $h(t)$ 的傅里叶变换即系统函数 $H(j\omega)$ 可分解为实部 $R(\omega)$ 和虚部 $jX(\omega)$ 之和
对式①运用傅里叶变换的频域卷积定理得到

于是有

$$
\mathcal {F} [ h (t) ] = \frac {1}{2 \pi} \{\mathcal {F} [ h (t) ] * \mathcal {F} [ u (t) ] \}
$$

$$
\begin{array}{r l} & {R (\omega) + j X (\omega) = \frac {1}{2 \pi} \Bigl \{\left[ R (\omega) + j X (\omega) \right] * \left[ \pi \delta (\omega) + \frac {1}{j \omega} \right] \Bigr \}} \\ & {= \frac {1}{2 \pi} \Bigl \{R (\omega) * \pi \delta (\omega) + X (\omega) * \frac {1}{\omega} \Bigr \} + \frac {j}{2 \pi} \Bigl \{X (\omega) * \pi \delta (\omega) - R (\omega) * \frac {1}{\omega} \Bigr \}} \\ & {= \left\{\frac {R (\omega)}{2} + \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {X (\lambda)}{\omega - \lambda} d \lambda \right\} + j \left\{\frac {X (\omega)}{2} - \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {R (\lambda)}{\omega - \lambda} d \lambda \right\}} \end{array}
$$

$$
R (\omega) = \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {X (\lambda)}{\omega - \lambda} d \lambda ②
$$

$$
X (\omega) = - \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {R (\lambda)}{\omega - \lambda} d \lambda ③
$$

$$
R (w) - \frac {R (w)}{\frac {2}{R (w)}} = \frac {1}{2 \pi} \int d \lambda .
$$

式②与式③称为希尔伯特变换对。它说明了具有因果性的系统函数 $H(\omega)$ 的一个重要特性：实部 $R(\omega)$ 被已知的虚部 $X(\omega)$ 唯一地确定，反过来也一样。

从以上推证过程可以看出, 傅氏变换实部与虚部构成希尔伯特变换对的特性, 不只限于具有因果性的系统函数, 对于任意因果函数, 其傅氏变换的这种特性都是成立的。也即, 若函数 $f(t)$ 满足

$$
f (t) = f (t) u (t)
$$

且 $f(t)$ 的傅里叶变换为

$$
F (\omega) = R (\omega) + \mathrm{j} X (\omega)
$$

则 $R(\omega)$ 与 $X(\omega)$ 之间构成希尔伯特变换对[满足式②与式③的互换关系]。

例 45: 已知因果LTI系统频响特性 $H(\omega)$ 的实部为 $\pi\delta(\omega)$ ，求该系统的频响特性 $H(\omega)$ 和单位冲激响应 $h(t)$ 。

$$
\begin{array}{r l} & {\mathrm{if:}} \\ & {\mathrm{and}} \\ & {\frac {H (w) = R (w) + j \lambda (w)}{R (w) = \frac {1}{\pi} \int_ {- \infty} ^ {w} \frac {\lambda (\lambda)}{w - \lambda} d \lambda}} \\ & {\frac {x (w) = - \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {2 (\lambda)}{w - \lambda} d \lambda}{= - \frac {1}{\pi} \int_ {- w} ^ {\infty} \frac {\pi d (\lambda)}{w - \lambda} d \lambda}} \\ & {\quad = - \frac {1}{w}} \\ & {H (w) = \lambda d (w) - j \frac {1}{w} = \lambda d (w) + \frac {1}{j w}} \\ & {\Rightarrow h (t) = u (t)} \end{array}
$$

考点8：希尔伯特变换在通信系统中应用—SSB信号产生

希尔伯特变换在通信系统中的应用体现在单边带信号的产生，具体框图如下，其分析过程可详见 P162。

夢馬考研  
![](images/7847b0663d173d4cbfe6f017e6fd43b490b93cdc9422501e49be973281ce9c84.jpg)