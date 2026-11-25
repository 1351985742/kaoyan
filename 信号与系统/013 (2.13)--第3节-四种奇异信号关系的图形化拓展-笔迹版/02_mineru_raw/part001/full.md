## 目录【回顾知识点与题型】

信号

![](images/a283f4c20c3b715d1414251e1f89068892a4bf99205d16737b38aa8fea8ca7c8.jpg)

系统

1 章 连续时间信号与系统.... 1
专题1 连续信号的表示、分类与运算.... 3
考点1：连续信号的表示形式.... a:0 : h>0 ... 3
考点2：连续信号的分类.... 3
考点3：信号运算.... f(t) → f(-at±h) ... 7
专题2 四种奇异信号.... 9
考点1：单位斜变信号.... t(u:t)
考点2：单位阶跃信号.... u(t)
考点3：单位冲激信号.... d(t) ... 流程... 自检 ... 11
考点4：冲激偶信号.... d(t) ... 13
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

# 专题 3 四种奇异信号的图形关系扩展

## 考点1：四种奇异信号关系的图形化表示

1、微积分关系及图形解释

单位斜变信号 $tu(t)$ 单位阶跃信号 $u(t)$ 单位冲激信号 $\delta (t)$ 冲激偶信号 $\delta '(t)$

![](images/6d64918f39e5e11e058152ea302f38c4d961f0ea3ce3f5268f8deffdc3cfc960.jpg)

![](images/2915ead627a0cfae69ad7e68d9271a08ae6ee23ce459bd888fd80af681d74e97.jpg)  
依次求导

2、重点关系解读：

![](images/9e541cec00529a7df49c749db3290c65112cf9e7fb41810e4eca295d18a1b249.jpg)

![](images/b31f500dd3216b7652f14725432181f55ce8548b1f080a6416574210aed4cb6f.jpg)

(1)图形化理解：斜导跳，跳导冲

(2) 斜边求导：斜率值包含了跳跃方向与跳变量 ⇒ 斜边

![](images/bac55b890b6b2321b06fc8a7507373c60ff28361f8906b5b0faed8477761fa78.jpg)

(3)阶跃跳变量求导转化为冲激强度，跳变方向表示了冲激信号的方向和强度的

正负值

![](images/ad872eca23769ba5efeb61c5d9eeb336ab974e83a5a68ae96b4dce6e21564135.jpg)

例 16: 已知 $x(t)=1-|t|$ , $-1 \leq t \leq 1$ , 请画出 $x(t)$ , $x'(t)$ , $x''(t)$ 。

![](images/5472db8e3a134c69328f9f9a5cc801b421be04735962eb2b5f36a84e1c52dfe9.jpg)

例 17: 已知信号 $f(t)$ 的波形如图所示, 试画出 $f'(t)$ 。

![](images/107ca252f11cc020746b2cd5d3a5dcdbf019869e93ce24d86a05fe9236ea776d.jpg)

![](images/653b79c90069f077a0eba7f798f845313097a30ed6e4219e7d091502f7d3ad12.jpg)

![](images/88c7799418a5e8720243acfbfde71cb1a3f52d93c56a0074f1faa35def96bbd0.jpg)

![](images/90ed1267b0c6094c497a2ce57955ec7da21b57ade142e0d13ffb9d5d61c56d74.jpg)

![](images/27e543f2b741f42f11b82b176b163ebaf8df2f996ed8325c83e7ab74d18597bf.jpg)

考点2: 信号微积分运算的应用【由上述内容更方便理解微积分运算】

1、微分运算：使图形的边缘轮廓突出

![](images/024cfde9c15e857aea320a8f1348b016271db65cc72828a72a5e9db284357882.jpg)

![](images/b55fa9065e4f9daa48af26db7f49535201235d3544a19736b69a13bb34be16cd.jpg)

2、积分运算：削弱信号中混入的毛刺(噪声)的影响

![](images/2f82e95c4f6ebc36aef4af5e5bd114705d0f17caada3a1f52370d484c39ad06c.jpg)

![](images/8e237c963aeb3ab620593d6df52f464545cc6693b252375fd5f4bb6b4e725618.jpg)

【例题】重新回看斜变与阶跃的微分关系和例 17

![](images/bb6643778a822df103bbeb910245634d79fdc1b21ea726fff78a6270f7a0d62b.jpg)

官网：tongxi nkaoyan. com

![](images/88dc633dafcd0e602138736a80ac15049525d4376952fea5c385c1ad51422538.jpg)

B站up: 信号与系统\_谷哥

![](images/b9876428e109171309680ef684cbefd29a6672d4f90e7695c2d2b5f7ee27bc57.jpg)

公众号：通信考研小马哥

考点3：四种奇异信号关系的图形化推广

3、三角形信号的微分

4、梯形的微分与分解

![](images/d4f5af7d70f400bfbd6d4845618243f7f23b04509a35402deca0bde032a1ef33.jpg)

![](images/687b63e4b12596b00a2332c3fcb1853b0d5e272423df78342723b80dfe3e15bd.jpg)

考点4: 信号综合运算的拓展

(1) 信号运算+微积分运算

![](images/61c7f7056c1ac5fda872d0241f95111d5176b70ec009d5a34a4d7cec1e24d4a4.jpg)

① $f(t) \rightarrow \int_{-b}^{t} f(\pi) d\tau$

② 求 $f'(-at \pm b)$

$$
[ f (- a t \pm b) ] ^ {\prime} = \frac {d f (- a t \pm b)}{d t} = f ^ {\prime} (- a t \pm b) (- a).
$$

涉及数学问题: $\frac{df(-2t+1)}{dt}$ 和 $f'(-2t+1)$ 的关系

$x \rightarrow  f\left( n\right)$

$$
f (x) = \frac {d f (x)}{d x}
$$

$$
[ f (u) ] ^ {\prime} = \frac {d f (u)}{d u} \cdot \frac {d u}{a x}
$$

$$
\xrightarrow {f (t)} f (2 t + 1) \xrightarrow {\mathrm{导}} [ f (2 t + 1) ] ^ {\prime} = f ^ {\prime} (2 t + 1) \cdot 2
$$

例 18: 已知信号 $f\left( {2 - t}\right)$ 的波形如图所示,绘出 ${f}^{\prime }\left( {{2t} + 1}\right)$ 的波形。

![](images/1dadffef7b0a804d4732cd680b1b0754fff837b3546fbdb995b6d0a9652b1ad4.jpg)

(2) 信号运算+图形含有冲激信号

涉及知识点：

1) 信号综合运算的基本知识

①原则：一切变换只针对于自变量

②结论：运算次序不同，不影响最终结果

③疑惑：运算次序如何选择？

$f(t) \rightarrow f(t-1)$ $f(\Delta t) \stackrel{\text{整位}}{\longrightarrow}$

先积分 ① $f(u) \stackrel{\text{逆}}{\rightarrow} f(t)$

![](images/7bd16d5d40c14b44b36290c0be47e359b839f5296dba4e6e7cd7dac00ea81187.jpg)

在信号综合运算中, 若信号中包括冲激信号, 则尺度变换性质会影响冲激信号的强度, 建议尺度运算放最后, 其他运算规律一律不变。

B站up: 信号与系统\_谷哥

例 19: 已知 $f(t)$ 波形如图所示，试画出 $f\left(-\frac{1}{2}t-2\right)$ 的波形。

![](images/b2979feae547437c4fef6aa94f8b2fe32ebee68f98674ea6ed16a62334348d6b.jpg)

B站up: 信号与系统\_谷哥

例 20: 已知 $f(5 - 2t)$ 的波形如图所示，求 $f(t)$ 的波形。

![](images/493fb42629275842d603ae120f61860b033cdbec25643c6f44e82a13736df664.jpg)

## 信号知识自检表（前三节）

<table><tr><td>知识点名称</td><td>考试点内容</td></tr><tr><td>四种奇异信号</td><td>□阶跃信号的应用→取单边、加窗(取段)fuu□冲激(偶)信号的性质→流程、自检思路←性质公式□四种奇异信号的关系及图形化拓展与FT综合重大</td></tr><tr><td>信号运算</td><td>□信号基本运算原则与结论□信号微积分运算□信号含有冲激信号时的综合运□题型1°f(h)→f(-αt±h)<img src="images/ef22888c3b3eb687b65823f9af47e386ef340fb5dee622a1854717ccc618b062.jpg"/></td></tr><tr><td>信号分解(理解第一,记忆第二)</td><td>□周期与非周期→周期判断□能量与功率信号→判断与常见□奇信号与偶信号□直流与交流(不会独立考试,在傅里叶级数中超重要)</td></tr></table>

$f(-at+b)$ $\times$ $\frac{10}{at}d[f(-at+b)]$ $\downarrow$ $f(-at+b)\Rightarrow\|$ 直接求导 $\downarrow20[f(-at+b)]$ $\uparrow$ $\downarrow$ $f'(-at+b)$

免费讲义Q群：1095841878

![](images/6e429f6b7694200cdd64de939249fe5d6c939ff6c709a2e90d4e4a446e144187.jpg)