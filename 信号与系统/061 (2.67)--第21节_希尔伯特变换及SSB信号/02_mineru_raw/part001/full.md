专题 8 希尔伯特变换及 SSB 信号

考点 1：振幅调制 AM(常规双边带)信号

$$
s _ {A M} (t) = [ A + m (t) ] c o s \omega_ {c} t = A c o s \omega_ {c} t + m (t) c o s \omega_ {c} t
$$

![](images/c68b8f2178dd475ac43a753bcc6d8f7a3ff94ba8097df6b303800b67e85c0ee8.jpg)

![](images/3fa55add56ced42e5fd8b2b933575c64a599d9ca32ccaa38e1045e176638aa5f.jpg)

![](images/e65535480cd7b969db450c223ca762880a3c58000b49c8f0ebea233f4628cfa6.jpg)

![](images/e2f187983f739c68f54d04f7ee74806ce247a9a90b5dd8f91a746e2f45851e7a.jpg)

![](images/ee20103e2afb6e51c0a74baed1cde672000f1cd0ef813092cde4ff56b867398a.jpg)

![](images/83fad6576efd6840ef2c14daa821c62ec5c00447db16c2923327b63dca85c057.jpg)

由 AM 信号频谱图可以看出，AM 信号中携带了载波频率信息，传输 AM 信号的带宽需要 $2\omega_{m}$ 。

考点 2: DSB: 双边带信号

$$
s _ {D S B} (t) = m (t) \cos \omega_ {c} t
$$

DSB 信号的波形和频谱，因为不存在载波分量，调制效率为 100%，比 AM 高，但传输 DSB 信号的带宽也为 $2\omega_{m}$

![](images/e80ba062010fd8a7d35832666a8409946262ab4f19c18854582d8062614c5251.jpg)

![](images/3d385d330964d5a0b3bb4134e32d341ddb52d3aeec28ef44b6fc9c6ed4441781.jpg)

![](images/de6eeefab2f273a72bc23b19a6b7df3fc31f543fa493101f2a56705b56a99916.jpg)

![](images/93a5b301d9c6410b7395b3a670eead58106501a86f2ef2fb6ac70ecc11c0d152.jpg)  
$S_{DSB}(t)$

![](images/b09e71d38486d3a3465b7c2da46725efbf93cfc05759bad501d8256226f67896.jpg)

![](images/81305f6776a286d6afc28bce6444951aada06af361ac00ed1d746cf24b23e56b.jpg)

## 考点 3: SSB: 单边带信号

在 AM 信号频谱中，将频率低于载频的谱线为下边带(LSB)，频率高于载频的谱线为上边带(USB)，在调幅波频谱中的上下两个边带都含有相同的信息，只传送一个边带也就可以完成信息的传送，且传输SSB信号的带宽只需要 $\omega_{m}$ .

## 考点 4: SSB信号的产生——滤波法和移相法

1、滤波法：先产生一个 DSB 信号，然后在通过一个边带滤波器，滤除不需要的边带，即可获得单边带信号。

SSB 滤波法产生结构:

![](images/0f17b54a000aaa6d28fd6cbb7bc65e924a3e3ab7c5b300370d033f7b324552f8.jpg)

![](images/a456ffe31e698a1aae7e5488d722d28ecb48df975354bf9746c557b22281a2bb.jpg)

![](images/909dbc108b9c68b877e7a45c75777886a826df6ed45d1e6c3afafe3e62c2b5f5.jpg)

![](images/d849a18a502990401f8d2fd3e7ced4dec05f8c5cc29f3e2b27f1a8a01efb35d9.jpg)

2、相移法SSB产生：利用相移网络，对载波和调制信号进行适当的相移，以便在合成过程中将其中一个边带抵消，从而获得SSB信号。

例 42: 试证明题图: 所示之系统可以产生单边带信号。图中, 信号 $g(t)$ 的频谱 $G(\omega)$ 受限于 $\sim \omega_{m} \sim +\omega_{m}$ 之间, $\dot{\omega}_{0} \gg \omega_{m}$ ; $H(\omega) = -jsgn\omega$ 。设 $v(t)$ 的频谱为 $V(\omega)$ , 写出 $V(\omega)$ 表示式, 并画出图形。

![](images/a603658af36164a96e8df6d8c4fa788e87d9b3832aafdcbdff23c9b7010167d5.jpg)

![](images/a231c9d7ca8c1fe8a85d9c87ade3893bca724717b99c90cf46168f11824b02f7.jpg)

例 43：下图所示为一个幅度调制系统，该系统由以下两部分组成：先把调制信号与载波之和平方，然后通过带通滤波器获得已调信号，若 $g(t)$ 是带限信号，即 $|\omega| > \omega_{m}$ 时， $G(\omega) = 0$ 。试确定带通滤波器的参数A， $\omega_{1}$ ， $\omega_{h}$ ，使得 $f(t) = g(t)\cos\omega_{c}t$ ，并给出 $\omega_{c}$ 和 $\omega_{m}$ 的约束。

![](images/ea0ac6633e07d4be6438dbd03f38d4af5341ae4a22b0107b048c89dae6337ef4.jpg)

![](images/cabeabb57c8af75ebec8f85f436bc4d9c16fd5cf691fb133eabde783e78852eb.jpg)

## 考点5：希尔伯特变换

一个实值函数 $x(t)$ 的希尔伯特变换是 $x(t)$ 和 $1 / \pi t$ 的卷积。

假设 $x(t)$ 是一个实值函数，求该函数的希尔伯特变换。

$$
\hat {x} (t) = H [ x (t)) ] = x (t) * \frac {1}{\pi t} = \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {x (\tau)}{t - \tau} d \tau
$$

因此 $\hat{x}(t)$ 可以被解读为 $x(t)$ 的线性时不变系统的输出，该线性时不变系统的脉冲响应为：

$$
h (t) = \frac {1}{\pi t}
$$

该脉冲响应的傅里叶变换为:

$$
H (\omega) = - j s g n (\omega) = \left\{ \begin{array}{l l} - j, & \omega > 0 \\ j, & \omega \leq 0 \end{array} \right.
$$

## 考点 6: 希尔伯特变换—90°移相器

信号经过希尔伯特变换之后，频域内各频率成分的幅值不变，但相位出现 $90^{\circ}$ 相移。即正频率滞后 $\pi/2$ ，负频率导前 $\pi/2$ ，因此希尔伯特变换器又称 $90^{\circ}$ 移相器。希尔伯特变换器又称 $90^{\circ}$ 移相器，如下图。两次希尔伯特变换之后，原信号相位翻转了 $180^{\circ}$ ，四次希尔伯特变换之后又变回本身。

![](images/48eb84eb2a3950458105e9f65ac0d1ed2ce306c33e90989a3d4ac1df6e4bd0ad.jpg)

例 44: 如图所示, 理想 $-\pi/2rad$ 全通相移器的频响特性定义为

$$
H (\omega) = \left\{ \begin{array}{l l} - j & \omega > 0 \\ j & \omega <   0 \end{array} \right.
$$

(1)求该相移器的单位冲激响应 $h(t)$ 。

(2)对于任意输入 $e(t)$ ，求该相移器的输出 $r(t)$ 。

(3)当 $e(t)=\cos\omega_{0}t$ 时，求该相移器的输出 $r(t)$ 。

![](images/91cec6fda037c7ce7082a8ae12637d3b772eafa8c369f4111403161d66c2a184.jpg)

![](images/e49c99824dd5cf9ce91ad99ee560e01b7dd00efcde6ab5bd9a4edebd33df089f.jpg)

## 考点7：系统可实现的(因果)的约束条件—希尔伯特变换变换对

系统可实现性的实质是具有因果性。本节将要证明，由于因果性的限制，系统函数的实部与虚部或模与辐角之间将具备某种相互制约的特性，这种特性以希尔伯特(Hilbert)变换的形式表现出来。

对于因果系统，其冲激响应 $h(t)$ 在t<0时等于0，仅在t>0时存在，因此

$$
h (t) = h (t) u (t) ①
$$

设 $h(t)$ 的傅里叶变换即系统函数 $H(\mathrm{j}\omega)$ 可分解为实部 $R(\omega)$ 和虚部 $jX(\omega)$ 之和

$$
H (j \omega) = \mathcal {F} [ h (t) ] = R (\omega) + j X (\omega)
$$

对式①运用傅里叶变换的频域卷积定理得到

$$
\mathcal {F} [ h (t) ] = \frac {1}{2 \pi} \{\mathcal {F} [ h (t) ] * \mathcal {F} [ u (t) ] \}
$$

于是有

$$
\begin{array}{r} R (\omega) + j X (\omega) = \frac {1}{2 \pi} \bigg \{[ R (\omega) + j X (\omega) ] * \bigg [ \pi \delta (\omega) + \frac {1}{j \omega} \bigg ] \bigg \} \\ = \frac {1}{2 \pi} \bigg \{R (\omega) * \pi \delta (\omega) + X (\omega) * \frac {1}{\omega} \bigg \} + \frac {j}{2 \pi} \bigg \{X (\omega) * \pi \delta (\omega) - R (\omega) * \frac {1}{\omega} \bigg \} \\ = \left\{\frac {R (\omega)}{2} + \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {X (\lambda)}{\omega - \lambda} d \lambda \right\} + j \left\{\frac {X (\omega)}{2} - \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {R (\lambda)}{\omega - \lambda} d \lambda \right\} \end{array}
$$

解得

$$
R (\omega) = \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {X (\lambda)}{\omega - \lambda} d \lambda ②
$$

$$
X (\omega) = - \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {R (\lambda)}{\omega - \lambda} d \lambda ③
$$

式②与式③称为希尔伯特变换对。它说明了具有因果性的系统函数 $H(\omega)$ 的一个重要特性：实部 $R(\omega)$ 被已知的虚部 $X(\omega)$ 唯一地确定，反过来也一样。

从以上推证过程可以看出，傅氏变换实部与虚部构成希尔伯特变换对的特性，不只限于具有因果性的系统函数，对于任意因果函数，其傅氏变换的这种特性都是成立的。也即，若函数 $f(t)$ 满足

$$
f (t) = f (t) u (t)
$$

且 $f(t)$ 的傅里叶变换为

$$
F (\omega) = R (\omega) + \mathrm{j} X (\omega)
$$

则 $R(\omega)$ 与 $X(\omega)$ 之间构成希尔伯特变换对[满足式②与式③的互换关系]。

例 45：已知因果LTI系统频响特性 $H(\omega)$ 的实部为 $\pi\delta(\omega)$ ，求该系统的频响特性 $H(\omega)$ 和单位冲激响应 $h(t)$ 。

![](images/3767b134237ce6e0e0cd200090d2ab01d5d9a471835b316cfba9422934bebaa7.jpg)

## 考点8：希尔伯特变换在通信系统中应用—SSB信号产生

希尔伯特变换在通信系统中的应用体现在单边带信号的产生，具体框图如下，其分析过程可详见 P162。

![](images/caf137f04a49eb64e4b83983c178c4792c57495b8c230cffddcd81986c699a1e.jpg)

![](images/019917bf3164bf4aebffb5384686f16bf2e9bc9ee403924bc893434b13c3cae0.jpg)