B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

## 目录

第1章 连续时间信号与系统.... 1  
专题1 连续信号的表示、分类与运算.... 3  
考点1：连续信号的表示形式.... 3  
考点2：连续信号的分类.... 3  
考点3：信号运算.... 7  
专题2 四种奇异信号.... 9  
考点1：单位斜变信号.... 9  
考点2：单位阶跃信号.... 9  
考点3：单位冲激信号.... 11  
考点4：冲激偶信号.... 13  
专题3 四种奇异信号的图形关系扩展.... 15  
考点1：四种奇异信号关系的图形化表示.... 15  
考点2：四种奇异信号关系的图形化推广.... 15  
考点3：信号微积分运算的应用.... 16  
考点4：包含冲激信号的信号运算.... 17  
专题4 连续系统的时域形式及其转换.... 21  
考点1：连续系统的微分方程.... 21  
考点2：连续系统的模拟框图.... 21  
专题5 连续系统分类与判断.... 24  
考点1：系统表示及作用分析.... 24  
考点2：线性系统的判断.... 24  
考点3：时不变系统的判断.... 25  
考点4：因果系统.... 26  
考点5：记忆系统和无记忆系统.... 26  
考点6：稳定系统和不稳定系统.... 27  
考点7：可逆系统和不可逆系统.... 27  
专题6 线性时不变系统的判断与应用.... 29  
考点1：简易表达式形式下LTIS的判断.... 29  
考点2：微分方程形式下LTIS的判断.... 29  
考点3：线性时不变系统的特性与应用.... 30

本2节学习目标:

(1) 基础:

(2) 理解:

(3) 拓展:

附：【四种奇异信号关系及性质证明】 【详见一点通P15-18】

① $u(t)$ 与 $\delta(t)$ 微积分关系 $\left\{\begin{aligned}\frac{du(t)}{dt}&=\delta(t)\\u(t)&=\int_{-\infty}^{t}\delta(\tau)d\tau\end{aligned}\right.$

证明：

已知 $u(t)=\left\{\begin{aligned}1,&t>0\\ 0,&t<0\end{aligned}\right.$

而 \(\delta (t)\) 的积分为 \(\int\_{-\infty}^{t}\delta (\tau)d\tau = \left\{ \begin{array}{ll}1, & t > 0[t > 0\) 时上下限内包含 \(\tau = 0\) 的点]\\ 0, & t < 0[t < 0\) 时上下限不包含 \(\tau = 0\) 的点] \end{array} \right.\)

综上所述

$$
u (t) = \int_ {- \infty} ^ {t} \delta (\tau) d \tau
$$

扩展: $u^{\prime}(t - 1) = \delta (t - 1)$ , 即

$$
\int_ {- \infty} ^ {t} \delta (\tau - 1) d t = u (t - 1)
$$

② $\delta(t)$ 尺度性质 $\delta(at)=\frac{1}{|a|}\delta(t)$

证明：

$$
\int_ {- \infty} ^ {\infty} \delta (a t) d t
$$

当a>0时，令m=at，

$$
\mathrm{原式} = \int_ {- \infty} ^ {\infty} \delta (m) d \frac {m}{a} = \int_ {- \infty} ^ {\infty} \frac {1}{a} \delta (t) d t \Longrightarrow \delta (a t) = \frac {1}{a} \delta (t)
$$

当 $a < 0$ 时，令 $m = at$

$$
\text {原式} = \int_ {- \infty} ^ {- \infty} \delta (m) d \frac {m}{a} = \int_ {- \infty} ^ {\infty} - \frac {1}{a} \delta (t) d t \Longrightarrow \delta (a t) = - \frac {1}{a} \delta (t)
$$

综上所述， $\delta(at)=\frac{1}{|a|}\delta(t)$ 。

③ $\delta'(at)=\frac{1}{|a|}\cdot\frac{1}{a}\delta'(t)$

证明：

$$
\int_ {- \infty} ^ {\infty} \delta^ {\prime} (a t) f (t) d t = \frac {1}{| a |} \int_ {- \infty} ^ {\infty} \delta^ {\prime} (x) f \left(\frac {x}{a}\right) d x = \frac {1}{| a |} \int_ {- \infty} ^ {\infty} \delta^ {\prime} (x) f \left(\frac {x}{a}\right) d x
$$

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

$$
\begin{array}{c} = \frac {1}{| a |} \int_ {- \infty} ^ {\infty} f \left(\frac {t}{a}\right) d \delta (t) = \frac {1}{| a |} \left[ f \left(\frac {t}{a}\right) \delta (t) \Bigg | _ {- \infty} ^ {\infty} - \int_ {- \infty} ^ {\infty} \delta (t) d f \left(\frac {t}{a}\right) \right] \\ = \frac {1}{| a |} \left[ 0 - \int_ {- \infty} ^ {\infty} \delta (t) f ^ {\prime} \left(\frac {t}{a}\right) \cdot \frac {1}{a} d t \right] = - \frac {1}{| a |} \cdot \frac {1}{a} f ^ {\prime} (0) = \frac {1}{| a |} \cdot \frac {1}{a} \cdot \int_ {- \infty} ^ {\infty} \delta^ {\prime} (t) f (t) d t \\ \Rightarrow \delta^ {\prime} (a t) = \frac {1}{| a |} \cdot \frac {1}{a} \cdot \delta^ {\prime} (t) \end{array}
$$

解释 $\frac{1}{|a|}$ ，令 $at = x$ ， $dt = \frac{1}{a} dx$

当 $a > 0$ 时， $\int_{-\infty}^{\infty}\delta '(at)f(t)dt = \frac{1}{a}\int_{-\infty}^{\infty}\delta '(x)f\left(\frac{x}{a}\right)dx$

当 $a < 0$ 时， $\int_{-\infty}^{\infty}\delta '(at)f(t)dt = \frac{1}{a}\int_{\infty}^{-\infty}\delta '(x)f\left(\frac{x}{a}\right)dx = -\frac{1}{a}\int_{-\infty}^{\infty}\delta '(x)f\left(\frac{x}{a}\right)dx$

综上所述， $\int_{-\infty}^{\infty}\delta^{'}(at)f(t)dt = \frac{1}{|a|}\int_{-\infty}^{\infty}\delta^{'}(x)f\left(\frac{x}{a}\right)dx$

④ $\delta^{(n)}(at) = \frac{1}{|a|} \cdot \frac{1}{a^n} \delta^{(n)}(t)$ （为③式的高阶性质推导）

⑤ $\delta^{\prime}(at\pm b) = \frac{1}{|a|}\cdot \frac{1}{a}\cdot \delta^{\prime}\left(t\pm \frac{b}{a}\right)$

证明：

$$
\int_ {- \infty} ^ {\infty} \delta^ {\prime} (a t \pm b) f (t) d t
$$

令 $at \pm b = x$ ，则 $dt = \frac{1}{a} dx$

$a > 0$ 时， $\int_{-\infty}^{\infty}\delta '(at\pm b)f(t)dt = \frac{1}{a}\int_{-\infty}^{\infty}\delta '(x)f\left(\frac{x\mp b}{a}\right)dx$

$a < 0$ 时， $\int_{-\infty}^{\infty}\delta'(at\pm b)f(t)dt = \frac{1}{a}\int_{-\infty}^{\infty}\delta'(x)f\left(\frac{x\mp b}{a}\right)dx = -\frac{1}{a}\int_{-\infty}^{\infty}\delta'(x)f\left(\frac{x\mp b}{a}\right)dx$

则

$$
\begin{array}{r l} \int_ {- \infty} ^ {\infty} \delta^ {\prime} (a t \pm b) f (t) d t & = \frac {1}{| a |} \int_ {+ \infty} ^ {- \infty} \delta^ {\prime} (x) f \left(\frac {x \mp b}{a}\right) d x = \frac {1}{| a |} \int_ {- \infty} ^ {\infty} f \left(\frac {x \mp b}{a}\right) d \delta (x) \\ & = \frac {1}{| a |} \left[ f \left(\frac {t \mp b}{a}\right) \delta (t) \Bigg | _ {- \infty} ^ {\infty} - \int_ {- \infty} ^ {\infty} \delta (t) d f \left(\frac {t \mp b}{a}\right) \right] \\ & = \frac {1}{| a |} \left[ 0 - \frac {1}{a} \int_ {- \infty} ^ {\infty} \delta (t) \cdot f ^ {\prime} \left(\frac {t \mp b}{a}\right) d t \right] \\ & = - \frac {1}{| a |} \cdot \frac {1}{a} \cdot f ^ {\prime} \left(\frac {\mp b}{a}\right) = \frac {1}{| a |} \cdot \frac {1}{a} \cdot \int_ {- \infty} ^ {\infty} \delta^ {\prime} \left(t \pm \frac {b}{a}\right) f (t) d t \\ & \Rightarrow \delta^ {\prime} (a t \pm b) = \frac {1}{| a |} \cdot \frac {1}{a} \delta^ {\prime} \left(t \pm \frac {b}{a}\right) \end{array}
$$

推广 $\Rightarrow \delta^{(n)}(at\pm b) = \frac{1}{|a|}\cdot \frac{1}{a^n}\delta^{(n)}\left(t\pm \frac{b}{a}\right)$

3

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

⑥ $\delta(t)$ 的万能公式

$$
\delta [ \boldsymbol {f} (\boldsymbol {t}) ] = \sum_ {i} \frac {\mathbf {1}}{\left| \boldsymbol {f} ^ {\prime} (\boldsymbol {t} _ {i}) \right|} \delta (\boldsymbol {t} - \boldsymbol {t} _ {i})
$$

证明：

设 $f(t)$ 有n个互不相等的实根 $t_{i}$ ， $(i=1,2,3,\ldots,n)$ ，则在任一单根 $t_{i}$ 附近足够小的邻域内， $f(t)$ 可展开为泰勒级数

$$
f (t) = f (t _ {i}) + f ^ {\prime} (t _ {i}) (t - t _ {i}) + \frac {1}{2} f ^ {\prime \prime} (t _ {i}) (t - t _ {i}) ^ {2} + \dots
$$

$$
\delta [ f (t) ] = \delta \big [ f ^ {\prime} (t _ {i}) (t - t _ {i}) \big ] = \frac {1}{\left| f ^ {\prime} (t _ {i}) \right|} \delta (t - t _ {i})
$$

$\approx f^{\prime}(t_{i})(t - t_{i})[\text{考虑到} f(t_{i}) = 0$ 和忽略高次项]

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

## 专题 2 四种奇异信号

信号本身或其微、积分信号存在不连续点，则称该信号为奇异信号。常见四种奇异信号有单位斜变信号、单位阶跃信号、单位冲激信号和冲激偶信号，其中单位冲激信号和单位阶跃信号贯穿整本教材，尤为重要。

## 考点1: 单位斜变信号

1、定义

$$
f (t) = \left\{ \begin{array}{l l} t, & t \geq 0 \\ 0, & t <   0 \end{array} \right.
$$

2、图形

![](images/c4752b1194af3540ecd2c92ef0932e6d2fad617f706e593ef543c85441e3ecf5.jpg)

3、应用——图形斜边的表示

![](images/5f913456fdbecbc979ed4b9059c230a6d5e8439d2c632a498845b71cb5a9285c.jpg)

0\~1范围内：2t

1\~2范围内： $-2t + 4$

## 考点 2: 单位阶跃信号

1、基本定义

$$
u (t) = \left\{ \begin{array}{l l} 1, & t > 0 \\ 0, & t <   0 \end{array} \right.
$$

![](images/c659008069920323fd20865b151e455522fd7240c9a68b679823516325755287.jpg)

B站up: 信号与系统\_谷哥

2、性质及应用

公众号：通信考研小马哥

2）反转

某点之前或之后

1）尺度 $u(t)\xrightarrow{a > 0}u(at)\Rightarrow u(at) = u(t)$

3）移位

![](images/5aa1796b6f8bf773934c03e6c157e0977ce8deb66348192d9a06c5593ebfa0a4.jpg)

存在范围

4）综合 $u(-at \pm b), a > 0, b > 0$

解：令 $-at \pm b > 0$ ，解出 $t$ 的范围，即该范围是 $u(-at \pm b)$ 不为0的范围

范围段

5）信号相减：相同 $t$ 值对应的函数值相减

矩形(rectangle)信号

$$
R _ {T} (t) = u (t) - u (t - T)
$$

门(gate)信号：左右对称的矩形信号

![](images/eee6fe376761331f3053586f21f7f4adccd915b3217fb5b6ae6c3d0177726818.jpg)

$$
G _ {T} (t) = u (t + \frac {T}{2}) - u (t - \frac {T}{2})
$$

![](images/e4a74e59798d4ef0ea459927bbeec9085f24adc4f59f725089597936450d37a9.jpg)

应用：确定范围 $\rightarrow$ 范围内画 $f(t)$ 的图

(1)

(2)

例 11: 画出以下信号的图形。

(1) $x_{1}(t) = u(2 - t)$ ;

(2) $x_{2}(t) = tu(t - 2) - 2u(t)$ ;

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

(3) $x_{3}(t)=(t-2)u(t)-u(t-2)$ 。

例 12: 已知信号 $f_{1}(t)$ 的波形如图所示, 求 $y_{1}(t) = f_{1}(t + 1) u(-t)$ 的波形。

![](images/bdf59fef4e910978c22f55a1162a0b05c90a6745fb98165932bcade10399707e.jpg)

例 13: 已知信号 $f(t)$ 的波形如图所示, 试画出 $f(t+1)[u(t)-u(t-1)]$ 的波形。

![](images/e428a396cf5b70d36817884eca09a3d33fbae9f6df4986075f9c52c702aed317.jpg)

官网：tongxinkaoyan.com

梦马班讲义

B站up: 信号与系统\_谷哥

## 考点 3: 单位冲激信号

1、基本定义与演变

(1)定义：

①极限定义：

$$
\delta (t) = \lim _ {\tau \rightarrow 0} \frac {1}{\tau} \left[ u \left(t + \frac {\tau}{2}\right) - u \left(t - \frac {\tau}{2}\right)\right]
$$

$$
\delta (t) = \lim _ {\tau \rightarrow 0} \left\{\frac {1}{\tau} \left(1 - \frac {| t |}{\tau}\right) [ u (t + \tau) - u (t - \tau) ] \right\}
$$

![](images/bfe63f875bfc511ac1034d680cd50bc10099f3d5a06ec10317a8db9457acb067.jpg)

②狄拉克定义：

$$
\left\{ \begin{array}{l} \int_ {- \infty} ^ {\infty} \delta (t) d t = 1 \\ \delta (t) = \left\{ \begin{array}{l l} \infty , & t = 0 \\ 0, & t \neq 0 \end{array} \right. \end{array} \right.
$$

(2)图形：

![](images/82cfc3615262c1784287e128568fe206164f802d715bc6d7e324517cfacd4261.jpg)

2、性质

(1)抽样性

$$
f (t) \delta (t) = f (0) \delta (t)
$$

$$
f (t) \delta (t - t _ {0}) = f (t _ {0}) \delta (t - t _ {0})
$$

$$
\int_ {- \infty} ^ {\infty} f (t) \delta (t) d t = f (0)
$$

$$
\int_ {- \infty} ^ {\infty} f (t) \delta (t - t _ {0}) d t = f (t _ {0})
$$

【梦马班点拨】注意上下限必须包含 $\delta$ 项括号内整体等于0的点，不然积分为0

例如： $\int_{-\infty}^{\infty}\left[t^{2} + \sin \left(\frac{\pi t}{4}\right)\right]\delta (t + 2)dt$

$$
\int_ {1} ^ {\infty} \left[ t ^ {2} + \sin \left(\frac {\pi t}{4}\right) \right] \delta (t + 2) d t
$$

8

官网：tongxinkaoyan.com

梦马班讲义

(2)对称性—偶函数

$$
\delta (t) = \delta (- t)
$$

(3)尺度性质

$\delta (at) = \frac{1}{|a|}\delta (t)$ —涉及尺度性质的，先用尺度再抽样性

例如： $\int_{-\infty}^{\infty}\left(t^{2} + 2\right)\delta \left(\frac{t}{2}\right)dt$

(4)万能公式

$\delta [f(t)] = \sum_{i}\frac{1}{|f'(t_i)|}\delta (t - t_i)$ 其中 $t_i$ 表示 $f(t) = 0$ 的 $i$ 个根

例如： $\delta (-2t + 4)$

$$
\delta (t ^ {2} - 9)
$$

例 14: 求下列积分:

(1) $\int_0^\infty 4t^2\delta (t + 1)dt$

(2) $\int_{-4}^{2}\cos(2\pi t)\delta(2t+1)dt$

(3) $\int_{-\infty}^{\infty} 2t\delta(t - 2)dt$

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

(4) $\int_{-\infty}^{\infty}\left(4 - t^{2}\right)\delta (t + 3)dt$

(5) $\int_{-3}^{6}(4-t^{2})\delta(t+4)dt$

(6) $\int_{-\infty}^{\infty}\delta(t-2)\delta(x-t)dt$

(7) $\int_{-3}^{6}\left(6 - t^2\right)\left[\delta (t + 4) + 2\delta (2t + 4)\right]dt$

性质（5）——与 u(t) 的关系

(8) $\int_{-\infty}^{t}\delta (2t - 1)dt$

(9) $\int_{-\infty}^{t}\left[\delta (t + 2) - \delta (t - 2)\right]dt$

## 【梦马班点拨】含冲激信号的计算解题技巧：

万能公式→抽样性 $\left\{\begin{array}{l}\text { 相乘形式: 注意结果含有冲激项 } \\ \text { 积分形式 }\left\{\begin{array}{l}\text { 积分上下限均为数(包含无穷): 结果为数 } \\ \text { 积分限存在t项: 结果为函数 }\end{array}\right.\end{array}\right.$

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

考点4：冲激偶信号

1、冲激偶信号的图形

![](images/80d6c7b50cb8c4ab6c55b79375400fae78bbfd6684291b308d938ceed2f0ad08.jpg)

![](images/8d1705d712165e310815818c1eff8519a7c6b3692eab4c9825ca2ed125908c00.jpg)

2、冲激偶信号的性质

(1)抽样性

$$
f (t) \delta^ {\prime} (t) = f (0) \delta^ {\prime} (t) - f ^ {\prime} (0) \delta (t)
$$

$$
f (t) \delta^ {\prime} (t - t _ {1}) = f (t _ {1}) \delta^ {\prime} (t - t _ {1}) - f ^ {\prime} (t _ {1}) \delta (t - t _ {1})
$$

$$
\int_ {- \infty} ^ {\infty} f (t) \delta^ {\prime} (t) d t = - f ^ {\prime} (0) \quad \int_ {- \infty} ^ {\infty} f (t) \delta^ {\prime} (t - t _ {0}) d t = - f ^ {\prime} (t _ {0})
$$

可扩展为

$$
\int_ {- \infty} ^ {\infty} f (t) \delta^ {(n)} (t) d t = (- 1) ^ {n} f ^ {(n)} (0)
$$

【梦马班点拨】注意上下限必须包含δ项括号内整体等于0的点,不然积分为0。

例：

$$
\int_ {- \infty} ^ {\infty} (t ^ {3} + 2 t ^ {2} - 2 t + 1) \delta^ {\prime} (t - 1) d t =
$$

(2)对称性—奇函数

$$
\delta^ {\prime} (t) = - \delta^ {\prime} (- t)
$$

(3)尺度变换

$$
\delta^ {(n)} (a t) = \frac {1}{| a |} \frac {1}{a ^ {n}} \delta^ {(n)} (t)
$$

例 15: 求积分 $\int_{-2}^{2}\left[(t-3)\delta(2t+2)+8\cos(\pi t)\delta'(t-0.5)\right]dt$

(4) 综合运算

$$
\boldsymbol {\delta} ^ {\prime} (\boldsymbol {a t} \pm \boldsymbol {b}) = \frac {1}{| a |} \cdot \frac {1}{a} \cdot \boldsymbol {\delta} ^ {\prime} \left(\boldsymbol {t} \pm \frac {\boldsymbol {b}}{a}\right)
$$

(5)积分性质

$$
\left\{ \begin{array}{l} \int_ {- \infty} ^ {\infty} \delta^ {\prime} (t) d t = \delta (\infty) - \delta (- \infty) = 0 \\ \int_ {- \infty} ^ {t} \delta^ {\prime} (\tau) d \tau = \delta (t) \end{array} \right.
$$

![](images/a400508e6cf702dc00c85c6bfb2d6bbd6735b8cdc4df9f37bf84602ae414b69e.jpg)

B站up: 信号与系统\_谷哥

公众号：通信考研小马哥

考点 5 四种奇异信号的关系

B站up: 信号与系统\_谷哥

第 2 节 四种奇异信号（表达式视角）自检表

<table><tr><td>知识点名称</td><td>具体考察点</td></tr><tr><td>单位斜边信号</td><td>☐定义及图形</td></tr><tr><td>★单位阶跃信号</td><td>☐定义、变形及对应图形☐应用:取单边 取段突破口:</td></tr><tr><td>★单位冲激信号</td><td>☐定义、变形及对应图形☐万能公式☐解题流程及注意事项</td></tr><tr><td>冲激偶信号</td><td>☐定义、变形及对应图形☐万能公式☐解题流程及注意事项</td></tr><tr><td>四种奇异信号的关系</td><td>☐表达式及图形关系表示</td></tr></table>