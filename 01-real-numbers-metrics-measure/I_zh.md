# 实数、距离与测度

## 引言

我们在高中微积分中已经接触过极限、连续、微分和积分，而实分析所做的事情是进一步理解它们背后的数学结构。例如，我们为什么可以相信一个不断逼近某个位置的数列真的存在极限？为什么实数轴不会在某个地方突然出现一个无法定义的“空缺”？当我们把积分从区间推广到更加复杂的集合时，又应该怎样严格地定义一个集合的“大小”？

这些问题看起来分散，但实际上彼此之间存在非常紧密的联系。

实数的完备性保证很多极限过程不会脱离我们正在研究的空间；度量把“距离”和“趋近”推广到更加一般的集合；测度论则从另一个方向出发，尝试给集合赋予大小，并最终为 Lebesgue 积分建立基础。

这里更希望做的是把一些以后会反复出现的概念放到同一条逻辑线上，让第一次接触这些对象的读者知道它们为什么会出现，以及不同定义之间究竟是什么关系。

### 实分析与实变函数

“实分析”和“实变函数论”在不同教材和课程体系中的用法并不完全统一。

有些课程直接把 Real Analysis 翻译为实变函数，有些课程则把实变函数理解为实分析中以 Lebesgue 测度和 Lebesgue 积分为中心的一部分，再把度量空间、一般测度空间和泛函空间等内容放到更广义的分析框架中。

本文不试图规定一种唯一的术语用法。

为了方便后文，我们大致把

$$
(\mathbb{R}^{n},\mathcal{L},m)
$$

上的 Lebesgue 测度、可测函数、Lebesgue 积分等问题视为经典实变函数论的主要内容，而把一般测度空间

$$
(X,\mathcal{F},\mu)
$$

以及更抽象的度量空间、函数空间等内容放在更广义的实分析框架中。

这种区分只是为了组织文章，并不影响任何数学定义。

从这个角度来看，本篇其实同时承担两个任务。

一方面，我们要为后面的 Lebesgue 积分建立测度论基础；另一方面，也会提前引入度量空间等更加抽象的语言。这样以后讨论 $L^{p}$ 空间、Banach 空间乃至更加一般的分析问题时，就不需要重新建立这些概念。

本文默认读者已经熟悉基本集合符号，并且对极限、导数和积分有初步认识。除此之外，大部分概念都会从定义开始。

## 实数与分析基础

### 实数的代数结构

为了讨论分析中的极限和完备性，我们首先需要明确正在使用的实数结构。

记实数集合为

$$
\mathbb{R}.
$$

在 $\mathbb{R}$ 上定义加法和乘法

$$
+:\mathbb{R}\times\mathbb{R}\rightarrow\mathbb{R},
$$

$$
\cdot:\mathbb{R}\times\mathbb{R}\rightarrow\mathbb{R}.
$$

也就是说，对于任意 $x,y\in\mathbb{R}$，都有

$$
x+y\in\mathbb{R},\qquad xy\in\mathbb{R}.
$$

实数上的加法和乘法满足我们熟悉的一系列性质。对任意 $x,y,z\in\mathbb{R}$，

$$
x+(y+z)=(x+y)+z,
$$

$$
x(yz)=(xy)z,
$$

$$
x+y=y+x,
$$

$$
xy=yx,
$$

以及

$$
x(y+z)=xy+xz.
$$

此外存在加法单位元 $0$ 和乘法单位元 $1\ne0$，使得

$$
x+0=x,
$$

$$
x\cdot1=x.
$$

每个 $x\in\mathbb{R}$ 都存在加法逆元 $-x$，满足

$$
x+(-x)=0,
$$

而每个非零实数 $x$ 都存在乘法逆元 $x^{-1}$，满足

$$
xx^{-1}=1.
$$

满足这些性质的代数结构称为一个**域（Field）**。

因此

$$
(\mathbb{R},+,\cdot)
$$

是一个域。

但是只靠这些条件还不足以刻画实数，因为有理数

$$
\mathbb{Q}
$$

同样构成一个域。

实数还拥有顺序结构。

在 $\mathbb{R}$ 上考虑关系 $\leq$。它满足

$$
x\leq x,
$$

若

$$
x\leq y,\qquad y\leq x,
$$

则

$$
x=y,
$$

若

$$
x\leq y,\qquad y\leq z,
$$

则

$$
x\leq z,
$$

并且任意两个实数都可以比较：

$$
x\leq y \quad\text{或}\quad y\leq x.
$$

除此之外，顺序还必须与域运算相容。

若

$$
x\leq y,
$$

则对任意 $z\in\mathbb{R}$，

$$
x+z\leq y+z.
$$

若

$$
0\leq x,\qquad0\leq y,
$$

则

$$
0\leq xy.
$$

具有这些性质的域称为**有序域（Ordered Field）**。

所以 $\mathbb{R}$ 是有序域。

但 $\mathbb{Q}$ 仍然也是有序域。

真正把 $\mathbb{R}$ 和 $\mathbb{Q}$ 区分开的，是完备性。

### 上确界与完备性

设

$$
E\subseteq\mathbb{R}.
$$

如果存在 $M\in\mathbb{R}$，使得

$$
x\leq M,\qquad\forall x\in E,
$$

则称 $M$ 是 $E$ 的一个**上界（Upper Bound）**。

例如集合

$$
E=(0,1)
$$

存在无数个上界：

$$
1,\ 2,\ 10,\ldots
$$

都是它的上界。

我们更关心这些上界中最小的那个。

若 $\alpha$ 满足

$$
x\leq\alpha,\qquad\forall x\in E,
$$

并且对于 $E$ 的任意上界 $M$ 都有

$$
\alpha\leq M,
$$

则称 $\alpha$ 是 $E$ 的**上确界（Supremum）**，记作

$$
\alpha=\sup E.
$$

类似地可以定义下界与下确界

$$
\inf E.
$$

这里需要区分上确界和最大值。

例如

$$
E=(0,1)
$$

满足

$$
\sup E=1,
$$

但是

$$
1\notin E.
$$

所以 $E$ 没有最大值。

实数最重要的性质之一是：

**上确界性质**

每一个非空且有上界的集合

$$
E\subseteq\mathbb{R}
$$

都存在上确界

$$
\sup E\in\mathbb{R}.
$$

这就是实数完备性的一种基本表达。

有理数并不满足这个性质。

例如考虑

$$
E=\{q\in\mathbb{Q}:q>0,\ q^{2}<2\}.
$$

这个集合在 $\mathbb{Q}$ 中显然有上界，例如 $2$ 就是一个上界。

但如果它在 $\mathbb{Q}$ 中存在上确界 $\alpha$，那么这个上确界应该对应

$$
\alpha^{2}=2.
$$

也就是

$$
\alpha=\sqrt{2}.
$$

然而

$$
\sqrt{2}\notin\mathbb{Q}.
$$

所以 $E$ 在 $\mathbb{Q}$ 中没有上确界。

从数轴的角度看，可以把这种情况理解为 $\mathbb{Q}$ 中存在一个“缺口”，而 $\mathbb{R}$ 的完备性保证这样的缺口不存在。

因此，在适当的意义下，实数可以被刻画为一个**完备有序域**。

完备性看起来只是关于上确界的一条性质，但它实际上支撑了大量分析中的基本结论。

例如可以从中推出 Archimedean 性质。

**Archimedean 性质**

对任意 $x\in\mathbb{R}$，存在 $n\in\mathbb{N}$，使得

$$
n>x.
$$

证明并不复杂。

假设 $\mathbb{N}$ 在 $\mathbb{R}$ 中有上界。由完备性，

$$
\alpha=\sup\mathbb{N}
$$

存在。

那么

$$
\alpha-1<\alpha.
$$

由于 $\alpha$ 是最小上界，$\alpha-1$ 不可能仍然是 $\mathbb{N}$ 的上界，所以存在 $n\in\mathbb{N}$ 满足

$$
n>\alpha-1.
$$

于是

$$
n+1>\alpha.
$$

但 $n+1\in\mathbb{N}$，这与 $\alpha$ 是 $\mathbb{N}$ 的上界矛盾。

因此 $\mathbb{N}$ 在 $\mathbb{R}$ 中没有上界。

由此可以立即得到一个以后极限证明中非常常用的事实：

对于任意 $\varepsilon>0$，都存在 $n\in\mathbb{N}$ 使

$$
\frac{1}{n}<\varepsilon.
$$

只需要选择

$$
n>\frac{1}{\varepsilon}
$$

即可。

完备性还可以进一步导出闭区间套定理、Bolzano-Weierstrass 定理、单调有界数列收敛定理等结果。它们在形式上看起来互不相同，但背后的核心都是实数没有缺口。

### Dedekind 切割

前面我们把完备性作为实数已经拥有的一种性质。

另一种思路则是从有理数出发，直接构造实数。

Dedekind 切割（Dedekind Cut）就是一种经典构造。

设

$$
A\subsetneq\mathbb{Q}.
$$

如果 $A$ 满足：

1. $A\ne\varnothing$；

1. 若 $x\in A$ 且 $y<x$，则 $y\in A$；

1. $A$ 不存在最大元；

则可以把 $A$ 看作一个 Dedekind 切割的左半部分。

对于有理数 $r$，可以定义

$$
A_{r}=\{q\in\mathbb{Q}:q<r\}.
$$

这个集合对应的就是有理数 $r$。

真正有趣的是，即使一个位置并不对应任何有理数，我们仍然可以得到一个合法的切割。

例如定义

$$
A=\{q\in\mathbb{Q}:q<0\ \text{或}\ q^{2}<2\}.
$$

这个集合描述的正是数轴上 $\sqrt{2}$ 左侧的所有有理数。

虽然

$$
\sqrt{2}\notin\mathbb{Q},
$$

但是集合 $A$ 本身完全可以只利用有理数定义。

于是我们可以把这个切割本身看作一个新的数。

沿着这种思路，可以把所有 Dedekind 切割组成的集合定义为实数集合，再在它上面定义加法、乘法和顺序，并最终证明得到的结构是一个完备有序域。

这里更值得注意的是 Dedekind 切割和上确界性质之间的区别。

Dedekind 切割是一种**构造实数的方法**，而上确界性质是实数的一种**完备性性质**。

在已经建立好 $\mathbb{R}$ 以后，实分析通常不会每次都回到 Dedekind 切割，而会直接使用实数完备性。

同样地，也可以通过 Cauchy 序列的等价类构造实数。不同构造得到的实数系统在有序域意义下是同构的，因此后面的分析只需要关心它们共有的结构性质。

### 度量空间

在实数轴上，我们使用

$$
|x-y|
$$

表示两个实数之间的距离。

在二维或三维欧氏空间中，我们则使用熟悉的勾股定理。

但分析中的对象并不一定是普通的几何点。我们还可能研究函数、序列、矩阵以及各种更加抽象的对象。

所以有必要把“距离”真正需要满足的性质单独抽取出来。

设 $X$ 是一个非空集合。

函数

$$
d:X\times X\rightarrow[0,\infty)
$$

如果满足，对任意 $x,y,z\in X$，

$$
d(x,y)\geq0,
$$

且

$$
d(x,y)=0\Longleftrightarrow x=y,
$$

同时

$$
d(x,y)=d(y,x),
$$

以及

$$
d(x,z)\leq d(x,y)+d(y,z),
$$

则称 $d$ 是 $X$ 上的一个**度量（Metric）**。

此时

$$
(X,d)
$$

称为一个**度量空间（Metric Space）**。

最熟悉的例子就是

$$
X=\mathbb{R}^{n}.
$$

若

$$
x=(x_{1},\ldots,x_{n}),\qquad y=(y_{1},\ldots,y_{n}),
$$

则通常的欧氏距离为

$$
d_{2}(x,y)=\left(\sum_{i=1}^{n}|x_{i}-y_{i}|^{2}\right)^{1/2}.
$$

但这并不是 $\mathbb{R}^{n}$ 上唯一可能的度量。

例如还可以定义

$$
d_{1}(x,y)=\sum_{i=1}^{n}|x_{i}-y_{i}|
$$

以及

$$
d_{\infty}(x,y)=\max_{1\leq i\leq n}|x_{i}-y_{i}|.
$$

它们都满足度量公理。

甚至在任意集合 $X$ 上，我们都可以定义离散度量

$$
d(x,y)=\begin{cases}0, & x=y,\\ 1, & x\ne y.\end{cases}
$$

所以度量空间并不一定具有我们熟悉的几何图形。

它真正提供的是“两个点有多接近”这一概念。

给定 $x\in X$ 与 $r>0$，定义开球

$$
B_{r}(x)=\{y\in X:d(x,y)<r\}.
$$

如果集合 $U\subseteq X$ 满足，对每个 $x\in U$，都存在 $r>0$ 使得

$$
B_{r}(x)\subseteq U,
$$

则称 $U$ 是开集。

由一个度量产生的所有开集构成一个拓扑。

于是度量不仅能够定义距离，也自动给出了空间中的开集、闭集、邻域、连续性以及收敛等结构。

### 极限与收敛

一个 $X$ 中的序列本质上是一个映射

$$
x:\mathbb{N}\rightarrow X.
$$

通常记作

$$
(x_{n})^{\infty}_{n=1}.
$$

在实数中，我们习惯把数列的收敛理解为它的项越来越靠近某个数。

度量空间可以把这个定义完整地推广。

设 $(X,d)$ 是度量空间。

如果存在 $x\in X$，使得对于任意 $\varepsilon>0$，都存在 $N\in\mathbb{N}$，使得

$$
n\geq N\Longrightarrow d(x_{n},x)<\varepsilon,
$$

则称 $(x_{n})$ 收敛于 $x$，记为

$$
x_{n}\rightarrow x.
$$

形式上可以写成

$$
\forall\varepsilon>0,\ \exists N\in\mathbb{N},\ \forall n\geq N,\ d(x_{n},x)<\varepsilon.
$$

理解这个定义时，最重要的不是把 $\varepsilon$ 想成一个“很小的数”，而是注意量词的顺序。

我们要求的是：

无论别人给出多么严格的误差 $\varepsilon$，总能找到一个位置 $N$，使得从这一项以后所有序列项都永久落在 $x$ 的 $\varepsilon$ 邻域中。

这个定义首先带来一个基本结论。

**极限唯一性**

度量空间中，一个收敛序列至多存在一个极限。

假设

$$
x_{n}\rightarrow x
$$

并且

$$
x_{n}\rightarrow y.
$$

若 $x\ne y$，则

$$
d(x,y)>0.
$$

取

$$
\varepsilon=\frac{1}{3}d(x,y).
$$

当 $n$ 足够大时，可以同时满足

$$
d(x_{n},x)<\varepsilon
$$

和

$$
d(x_{n},y)<\varepsilon.
$$

于是由三角不等式，

$$
d(x,y)\leq d(x,x_{n})+d(x_{n},y)<2\varepsilon=\frac{2}{3}d(x,y),
$$

矛盾。

所以

$$
x=y.
$$

### Cauchy 列与完备空间

有时我们并不知道序列究竟应该收敛到哪里。

于是可以不直接与候选极限比较，而观察序列后面的项是否彼此越来越接近。

如果对于任意 $\varepsilon>0$，存在 $N\in\mathbb{N}$，使得

$$
m,n\geq N\Longrightarrow d(x_{m},x_{n})<\varepsilon,
$$

则称 $(x_{n})$ 为一个 **Cauchy 序列**。

任何收敛序列都是 Cauchy 序列。

事实上，若

$$
x_{n}\rightarrow x,
$$

则给定 $\varepsilon>0$，可以选择 $N$ 使得

$$
n\geq N\Longrightarrow d(x_{n},x)<\frac{\varepsilon}{2}.
$$

因此对任意 $m,n\geq N$，

$$
d(x_{m},x_{n})\leq d(x_{m},x)+d(x,x_{n})<\varepsilon.
$$

但是反过来并不一定成立。

如果一个度量空间中的任何 Cauchy 序列都收敛到空间中的某个点，则称这个度量空间是**完备的（Complete）**。

实数空间

$$
(\mathbb{R},|\cdot|)
$$

是完备的。

而

$$
(\mathbb{Q},|\cdot|)
$$

不是。

例如可以构造一列有理数 $(q_{n})$，使得

$$
q_{n}\rightarrow\sqrt{2}
$$

在 $\mathbb{R}$ 中成立。

$(q_{n})$ 是 Cauchy 序列，但它在 $\mathbb{Q}$ 中找不到极限，因为

$$
\sqrt{2}\notin\mathbb{Q}.
$$

这与前面通过上确界讨论的完备性其实反映的是同一件事情。

在实数中，上确界性质、Cauchy 完备性、单调有界数列收敛性、闭区间套性质等多种形式的完备性可以彼此推出。

这也是实分析中非常典型的现象：同一个结构性质可能拥有很多表面完全不同的等价描述。

还有一个以后经常使用的简单结论。

**Cauchy 序列有界性**

任意 Cauchy 序列都是有界的。

设 $(x_{n})$ 是 Cauchy 序列。

取

$$
\varepsilon=1.
$$

存在 $N$，使得

$$
m,n\geq N\Longrightarrow d(x_{m},x_{n})<1.
$$

固定 $m=N$，则

$$
n\geq N\Longrightarrow d(x_{n},x_{N})<1.
$$

所以序列尾部全部落在开球

$$
B_{1}(x_{N})
$$

中。

剩下只有有限多个点

$$
x_{1},\ldots,x_{N-1}.
$$

取

$$
R=1+\max_{1\leq k<N}d(x_{k},x_{N}),
$$

就得到

$$
x_{n}\in B_{R}(x_{N}),\qquad\forall n\in\mathbb{N}.
$$

因此整个序列有界。

### 紧致性

与完备性关系非常密切的另一个概念是紧致性（Compactness）。

设 $K\subseteq X$。

如果一族开集

$$
\{U_{\alpha}\}_{\alpha\in I}
$$

满足

$$
K\subseteq\bigcup_{\alpha\in I}U_{\alpha},
$$

则称它是 $K$ 的一个开覆盖。

如果 $K$ 的任意开覆盖都可以从中取出有限多个开集

$$
U_{\alpha_{1}},\ldots,U_{\alpha_{m}}
$$

仍然覆盖 $K$，则称 $K$ 是紧的。

在度量空间中，紧致性等价于序列紧致性：

任意 $K$ 中的序列都存在一个收敛子列，并且这个子列的极限仍然属于 $K$。

在有限维欧氏空间中还有著名的 Heine-Borel 定理：

$$
K\subseteq\mathbb{R}^{n}
$$

紧，当且仅当 $K$ 闭且有界。

也就是

$$
K\text{ compact}\Longleftrightarrow K\text{ closed and bounded}.
$$

不过需要强调，“闭且有界等价于紧”是有限维欧氏空间中的特殊性质，并不能直接推广到任意度量空间。

例如无限维赋范空间中的闭单位球通常并不紧。

任意紧度量空间都是完备的，但完备空间未必紧。

这两个概念以后在函数空间中会逐渐表现出非常明显的区别。

### 代数结构

到这里稍微插入一些后面会不断遇到的代数语言。

它们并不是本篇测度论的核心，但分析中的很多空间都会同时携带代数结构和拓扑结构，因此提前明确这些词的意义会方便不少。

设 $G$ 是非空集合，并定义二元运算

$$
\cdot:G\times G\rightarrow G.
$$

如果满足：

1. 结合律

   $$
   (xy)z=x(yz);
   $$

1. 存在单位元 $e\in G$

   $$
   ex=xe=x;
   $$

1. 每个 $x\in G$ 都存在逆元 $x^{-1}$，使

   $$
   xx^{-1}=x^{-1}x=e;
   $$

则称

$$
(G,\cdot)
$$

是一个**群（Group）**。

如果还满足

$$
xy=yx,
$$

则称为 Abel 群或交换群。

如果只要求封闭性和结合律，则得到半群（Semigroup）；如果半群还存在单位元，则得到幺半群（Monoid）。

在一个集合 $R$ 上考虑两种运算 $+$ 和 $\cdot$。

如果

$$
(R,+)
$$

是 Abel 群，同时乘法满足结合律，并且乘法对加法满足左右分配律

$$
x(y+z)=xy+xz,
$$

$$
(x+y)z=xz+yz,
$$

则称

$$
(R,+,\cdot)
$$

为一个**环（Ring）**。

如果乘法交换，则称为交换环。

如果还存在乘法单位元 $1$，则称为含幺环。

域则是在这个基础上进一步要求所有非零元素对于乘法构成 Abel 群。

因此一个域 $K$ 可以简洁地写成

$$
(K,+)\text{ 是 Abel 群},
$$

$$
(K\setminus\{0\},\cdot)\text{ 是 Abel 群},
$$

并且乘法对加法满足分配律。

常见例子包括

$$
\mathbb{Q},\qquad\mathbb{R},\qquad\mathbb{C}.
$$

这些代数结构本身属于抽象代数，但分析中会不断把它们与极限、拓扑和测度结合起来。

例如拓扑群、Banach 代数以及局部紧群上的 Haar 测度都建立在这种“代数结构 + 分析结构”的组合上。

## 测度空间

### 测度与基数

如果要描述一个集合的大小，最先想到的往往是集合中元素的个数，也就是基数（Cardinality）。

对于有限集合，这当然十分自然。

例如

$$
A=\{1,2,3\}
$$

的大小可以写成

$$
|A|=3.
$$

但是一旦进入连续空间，基数就无法表达我们真正关心的几何大小。

例如

$$
[0,1]
$$

和

$$
[0,100]
$$

具有相同的基数。

事实上二者都与整个实数集合 $\mathbb{R}$ 等势。

然而从长度来看，

$$
[0,100]
$$

显然应该比

$$
[0,1]
$$

大一百倍。

因此我们需要另一种“大小”。

在一维空间中，这种大小对应长度；在二维中对应面积；在三维中对应体积。

测度论所做的事情，就是把这些概念统一推广到更加一般的集合和空间。

这也是 Lebesgue 积分出现的基础。

Riemann 积分主要从定义域的区间分割出发，而 Lebesgue 理论首先需要知道哪些集合能够被测量，以及这些集合具有多大的测度。

于是第一个问题并不是“测度是多少”，而是：

我们究竟允许测量哪些集合？

### $\sigma$-代数

设 $X$ 是一个非空集合。

记它的幂集为

$$
\mathcal{P}(X)=\{A:A\subseteq X\}.
$$

一个集合族

$$
\mathcal{F}\subseteq\mathcal{P}(X)
$$

如果满足：

1. $$
   X\in\mathcal{F};
   $$

1. 若

   $$
   A\in\mathcal{F},
   $$

   则

   $$
   A^{c}=X\setminus A\in\mathcal{F};
   $$

1. 若

   $$
   A_{1},A_{2},\ldots\in\mathcal{F},
   $$

   则

   $$
   \bigcup_{n=1}^{\infty}A_{n}\in\mathcal{F};
   $$

则称 $\mathcal{F}$ 是 $X$ 上的一个 **$\sigma$-代数（$\sigma$-algebra）**。

从第一、第二条立即可以得到

$$
\varnothing\in\mathcal{F},
$$

因为

$$
\varnothing=X^{c}.
$$

再利用 De Morgan 律，

$$
\left(\bigcup_{n=1}^{\infty}A_{n}\right)^{c}=\bigcap_{n=1}^{\infty}A_{n}^{c},
$$

可以得到 $\mathcal{F}$ 对可数交同样封闭：

$$
A_{1},A_{2},\ldots\in\mathcal{F}\Longrightarrow\bigcap_{n=1}^{\infty}A_{n}\in\mathcal{F}.
$$

有限并和有限交当然也是可数并、可数交的特殊情况。

最简单的 $\sigma$-代数是

$$
\{\varnothing,X\},
$$

称为平凡 $\sigma$-代数。

最大的则是

$$
\mathcal{P}(X).
$$

为什么定义中要求的是**可数**并，而不是任意并？

一个重要原因是分析中的极限本身天然由数列索引。

例如如果

$$
A_{1}\subseteq A_{2}\subseteq\cdots,
$$

我们经常需要研究

$$
\bigcup_{n=1}^{\infty}A_{n}.
$$

这种可数结构恰好与极限、级数以及积分理论相匹配。

另一方面，如果要求 $\sigma$-代数对任意并封闭，很多自然的可测结构会变得过强，最终甚至可能强迫我们包含不希望包含的集合。

如果给定一个集合族

$$
\mathcal{C}\subseteq\mathcal{P}(X),
$$

则所有包含 $\mathcal{C}$ 的 $\sigma$-代数的交仍然是一个 $\sigma$-代数。

因此存在包含 $\mathcal{C}$ 的最小 $\sigma$-代数，记为

$$
\sigma(\mathcal{C}).
$$

称为由 $\mathcal{C}$**生成的 $\sigma$-代数**。

这在后面定义 Borel 集时非常重要。

### 可测空间与测度

如果 $X$ 配备了一个 $\sigma$-代数 $\mathcal{F}$，则二元组

$$
(X,\mathcal{F})
$$

称为一个**可测空间（Measurable Space）**。

$\mathcal{F}$ 中的集合称为可测集。

注意这里“可测”只意味着这个集合被纳入了我们允许测量的集合系统。

此时还没有真正赋予它大小。

为此需要定义测度。

函数

$$
\mu:\mathcal{F}\rightarrow[0,\infty]
$$

如果满足

$$
\mu(\varnothing)=0
$$

以及可数可加性：

若

$$
A_{i}\cap A_{j}=\varnothing\qquad(i\ne j),
$$

则

$$
\mu\left(\bigcup_{n=1}^{\infty}A_{n}\right)=\sum_{n=1}^{\infty}\mu(A_{n}),
$$

则称 $\mu$ 是 $\mathcal{F}$ 上的一个**测度（Measure）**。

三元组

$$
(X,\mathcal{F},\mu)
$$

称为一个**测度空间（Measure Space）**。

测度允许取值 $+\infty$。

这是必要的。例如整个实数轴的 Lebesgue 测度就是

$$
m(\mathbb{R})=+\infty.
$$

从可数可加性可以推出很多基本性质。

首先是有限可加性。

如果

$$
A\cap B=\varnothing,
$$

则

$$
\mu(A\cup B)=\mu(A)+\mu(B).
$$

其次是单调性。

若

$$
A\subseteq B,
$$

则可以写成

$$
B=A\cup(B\setminus A),
$$

且这两个集合不交，于是

$$
\mu(B)=\mu(A)+\mu(B\setminus A)\geq\mu(A).
$$

所以

$$
A\subseteq B\Longrightarrow\mu(A)\leq\mu(B).
$$

如果

$$
A_{1}\subseteq A_{2}\subseteq\cdots,
$$

并令

$$
A=\bigcup_{n=1}^{\infty}A_{n},
$$

那么还有**从下连续性**

$$
\mu(A)=\lim_{n\to\infty}\mu(A_{n}).
$$

证明可以把集合序列拆成互不相交的部分：

$$
B_{1}=A_{1},
$$

$$
B_{n}=A_{n}\setminus A_{n-1},\qquad n\geq2.
$$

则

$$
A_{n}=\bigcup_{k=1}^{n}B_{k}
$$

以及

$$
A=\bigcup_{k=1}^{\infty}B_{k}.
$$

由可数可加性，

$$
\mu(A_{n})=\sum_{k=1}^{n}\mu(B_{k}),
$$

而

$$
\mu(A)=\sum_{k=1}^{\infty}\mu(B_{k}).
$$

因此

$$
\mu(A_{n})\rightarrow\mu(A).
$$

同样，如果

$$
A_{1}\supseteq A_{2}\supseteq\cdots
$$

且

$$
\mu(A_{1})<\infty,
$$

则

$$
\mu\left(\bigcap_{n=1}^{\infty}A_{n}\right)=\lim_{n\to\infty}\mu(A_{n}).
$$

这称为**从上连续性**。

这些结论以后在积分和极限定理中都会反复出现。

### 零测集与完备性

如果

$$
N\in\mathcal{F}
$$

满足

$$
\mu(N)=0,
$$

则称 $N$ 为一个零测集。

一个很自然的问题是：

如果

$$
A\subseteq N,
$$

那么 $A$ 是否一定可测？

答案是未必。

虽然从“大小”的角度来看，我们当然希望

$$
\mu(A)=0,
$$

但 $A$ 首先必须属于 $\mathcal{F}$，测度 $\mu(A)$ 才有定义。

如果一个测度空间满足：

只要

$$
N\in\mathcal{F},\qquad\mu(N)=0,
$$

则任意

$$
A\subseteq N
$$

都属于 $\mathcal{F}$，

那么称这个测度空间是**完备的（Complete Measure Space）**。

注意这里的完备性和度量空间中的 Cauchy 完备性不是同一个概念。

虽然使用了同一个词，但二者讨论的是完全不同的结构。

### Borel 集

如果 $X$ 是一个拓扑空间，记其拓扑为 $\tau$。

由于 $\tau$ 就是 $X$ 上所有开集组成的集合族，我们可以考虑由这些开集生成的 $\sigma$-代数：

$$
\mathcal{B}(X)=\sigma(\tau).
$$

这称为 $X$ 上的 **Borel $\sigma$-代数**。

其中的元素称为 **Borel 集**。

所以 Borel 集可以理解为：

从所有开集出发，通过可数次取并、取交和取补能够产生的集合。

所有闭集当然也是 Borel 集，因为闭集是开集的补集。

在实数轴上，

$$
\mathcal{B}(\mathbb{R})
$$

也可以由所有开区间生成：

$$
\mathcal{B}(\mathbb{R})=\sigma\big(\{(a,b):a<b\}\big).
$$

事实上还可以进一步减少生成元，例如

$$
\mathcal{B}(\mathbb{R})=\sigma\big(\{(-\infty,a):a\in\mathbb{R}\}\big).
$$

定义在 Borel $\sigma$-代数上的测度称为 Borel 测度。

需要注意，Borel $\sigma$-代数本身一般不是完备的。

也就是说，一个 Borel 零测集的某些子集可能不再是 Borel 集。

这一点稍后会成为区分 Borel 可测集与 Lebesgue 可测集的关键。

## 外测度与 Carathéodory 构造

### 外测度

到这里，测度的定义似乎已经完成。

但是还存在一个很实际的问题：

假如我们希望从最基本的区间长度开始构造 Lebesgue 测度，一开始根本还不知道哪些集合应该可测。

因此不能直接先写

$$
\mu:\mathcal{F}\rightarrow[0,\infty]
$$

然后假定合适的 $\mathcal{F}$ 已经存在。

更自然的做法是反过来。

先尝试对 $X$ 的**所有子集**给出一种外部意义下的大小，然后再从中挑出真正行为良好的集合。

这就是外测度。

设 $X$ 是一个集合。

函数

$$
\mu^{*}:\mathcal{P}(X)\rightarrow[0,\infty]
$$

如果满足：

1. $$
   \mu^{*}(\varnothing)=0;
   $$

1. 若

   $$
   A\subseteq B,
   $$

   则

   $$
   \mu^{*}(A)\leq\mu^{*}(B);
   $$

1. 对任意集合序列 $(A_{n})$，

   $$
   \mu^{*}\left(\bigcup_{n=1}^{\infty}A_{n}\right)\leq\sum_{n=1}^{\infty}\mu^{*}(A_{n});
   $$

则称 $\mu^{*}$ 为 $X$ 上的一个**外测度（Outer Measure）**。

与测度相比，最明显的区别是：

测度在互不相交集合上要求可数**可加性**，

$$
\mu\left(\bigcup_{n}A_{n}\right)=\sum_{n}\mu(A_{n}),
$$

而外测度只要求可数**次可加性**

$$
\mu^{*}\left(\bigcup_{n}A_{n}\right)\leq\sum_{n}\mu^{*}(A_{n}).
$$

这正是把定义域扩大到所有子集所付出的代价。

### 覆盖构造

外测度最自然的来源之一是覆盖。

假设我们已经知道怎样给一族比较简单的集合

$$
\mathcal{C}
$$

赋予大小。

记这个大小函数为

$$
\rho:\mathcal{C}\rightarrow[0,\infty].
$$

对于一个任意集合 $E\subseteq X$，我们可能还不知道怎样直接测量 $E$。

于是考虑用可数个简单集合覆盖它：

$$
E\subseteq\bigcup_{k=1}^{\infty}C_{k},\qquad C_{k}\in\mathcal{C}.
$$

每一个覆盖都有一个总大小

$$
\sum_{k=1}^{\infty}\rho(C_{k}).
$$

不同覆盖可能非常浪费。

所以我们在所有可能的覆盖中取下确界：

$$
\mu^{*}(E)=\inf\left\{\sum_{k=1}^{\infty}\rho(C_{k}):E\subseteq\bigcup_{k=1}^{\infty}C_{k},\ C_{k}\in\mathcal{C}\right\}.
$$

直观来看，我们先从外面用一些已知大小的集合把 $E$ 包住，再不断寻找更加紧的覆盖。

这也是“外测度”这个名称非常自然的一层理解。

因为是下确界，对于任意 $\varepsilon>0$，只要 $\mu^{*}(E)<\infty$，就能够找到一个覆盖满足

$$
\sum_{k=1}^{\infty}\rho(C_{k})<\mu^{*}(E)+\varepsilon.
$$

这里一般不能保证真的存在一个覆盖恰好达到下确界。

所以 $\varepsilon$ 在测度论里经常用来表示“任意接近最优，但不要求最优真的取得”。

这种覆盖定义确实会产生外测度。

空集显然可以由空覆盖得到测度 $0$。

如果

$$
A\subseteq B,
$$

那么任何覆盖 $B$ 的集合族也会覆盖 $A$，因此

$$
\mu^{*}(A)\leq\mu^{*}(B).
$$

而对于

$$
E=\bigcup_{n=1}^{\infty}E_{n},
$$

给每个 $E_{n}$ 选择一个几乎达到其外测度的覆盖，再把这些覆盖全部合在一起，就得到 $E$ 的一个覆盖。

让每个误差取为

$$
\frac{\varepsilon}{2^{n}},
$$

便可得到

$$
\mu^{*}(E)\leq\sum_{n=1}^{\infty}\mu^{*}(E_{n})+\varepsilon.
$$

再令 $\varepsilon\rightarrow0$，得到

$$
\mu^{*}(E)\leq\sum_{n=1}^{\infty}\mu^{*}(E_{n}).
$$

因此确实满足次可加性。

### Carathéodory 可测性

现在有了一个定义在

$$
\mathcal{P}(X)
$$

上的外测度。

接下来要解决的问题就是：

哪些集合能够让外测度真正恢复为可数可加的测度？

Carathéodory 给出了一个非常漂亮的判据。

设 $E\subseteq X$。

如果对于任意 $A\subseteq X$ 都有

$$
\mu^{*}(A)=\mu^{*}(A\cap E)+\mu^{*}(A\cap E^{c}),
$$

则称 $E$ 是 **Carathéodory 可测的**。

这个条件值得慢一点理解。

集合 $E$ 把任意集合 $A$ 分成两个互不相交的部分：

$$
A\cap E
$$

和

$$
A\cap E^{c}.
$$

因为

$$
A=(A\cap E)\cup(A\cap E^{c}),
$$

外测度的次可加性总能给出

$$
\mu^{*}(A)\leq\mu^{*}(A\cap E)+\mu^{*}(A\cap E^{c}).
$$

所以 Carathéodory 条件真正要求的是反方向：

$$
\mu^{*}(A)\geq\mu^{*}(A\cap E)+\mu^{*}(A\cap E^{c}).
$$

也就是说，用 $E$ 把一个集合切开以后，不会凭空增加总外测度。

从这个角度看，可测集就是那些能够“干净地切割”所有集合的集合。

记所有 Carathéodory 可测集为

$$
\mathcal{M}_{\mu^{*}}.
$$

一个基本定理是：

**Carathéodory 可测性定理**

$\mathcal{M}_{\mu^{*}}$ 构成一个 $\sigma$-代数，并且

$$
\mu=\mu^{*}|_{\mathcal{M}_{\mu^{*}}}
$$

是一个完备测度。

这个定理正是从外测度走向真正测度的核心。

下面把其中的主要逻辑写出来。

首先，

$$
X\in\mathcal{M}_{\mu^{*}},
$$

因为对任意 $A\subseteq X$，

$$
A\cap X=A,\qquad A\cap X^{c}=\varnothing,
$$

所以

$$
\mu^{*}(A)=\mu^{*}(A)+0.
$$

其次，可测性条件对于 $E$ 与 $E^{c}$ 是完全对称的。

因此

$$
E\in\mathcal{M}_{\mu^{*}}\Longrightarrow E^{c}\in\mathcal{M}_{\mu^{*}}.
$$

接下来考虑有限并。

若

$$
E,F\in\mathcal{M}_{\mu^{*}},
$$

则利用 $E$ 的可测性先把任意 $A$ 分成

$$
A\cap E
$$

和

$$
A\cap E^{c}.
$$

再利用 $F$ 的可测性分割第二部分：

$$
A\cap E^{c}=(A\cap E^{c}\cap F)\cup(A\cap E^{c}\cap F^{c}).
$$

因此

$$
\mu^{*}(A)=\mu^{*}(A\cap E)+\mu^{*}(A\cap E^{c}\cap F)+\mu^{*}(A\cap E^{c}\cap F^{c}).
$$

注意

$$
(A\cap E)\cup(A\cap E^{c}\cap F)=A\cap(E\cup F),
$$

而

$$
A\cap E^{c}\cap F^{c}=A\cap(E\cup F)^{c}.
$$

配合外测度的次可加性可以得到

$$
\mu^{*}(A)=\mu^{*}(A\cap(E\cup F))+\mu^{*}(A\cap(E\cup F)^{c}).
$$

所以

$$
E\cup F\in\mathcal{M}_{\mu^{*}}.
$$

对于可数并，可以先把集合序列不交化。

给定

$$
E_{1},E_{2},\ldots\in\mathcal{M}_{\mu^{*}},
$$

定义

$$
F_{1}=E_{1},
$$

以及

$$
F_{n}=E_{n}\setminus\bigcup_{k=1}^{n-1}E_{k},\qquad n\geq2.
$$

则每个 $F_{n}$ 可测，而且两两不交，并且

$$
\bigcup_{n=1}^{\infty}F_{n}=\bigcup_{n=1}^{\infty}E_{n}.
$$

对于任意 $A\subseteq X$，反复利用 $F_{n}$ 的可测性，可以得到对任意 $N$，

$$
\mu^{*}(A)\geq\sum_{n=1}^{N}\mu^{*}(A\cap F_{n})+\mu^{*}\left(A\cap\left(\bigcup_{n=1}^{N}F_{n}\right)^{c}\right).
$$

令

$$
F=\bigcup_{n=1}^{\infty}F_{n}.
$$

因为

$$
A\cap F^{c}\subseteq A\cap\left(\bigcup_{n=1}^{N}F_{n}\right)^{c},
$$

由单调性，

$$
\mu^{*}(A)\geq\sum_{n=1}^{N}\mu^{*}(A\cap F_{n})+\mu^{*}(A\cap F^{c}).
$$

令 $N\rightarrow\infty$，

$$
\mu^{*}(A)\geq\sum_{n=1}^{\infty}\mu^{*}(A\cap F_{n})+\mu^{*}(A\cap F^{c}).
$$

另一方面，由次可加性，

$$
\mu^{*}(A\cap F)\leq\sum_{n=1}^{\infty}\mu^{*}(A\cap F_{n}).
$$

于是

$$
\mu^{*}(A)\geq\mu^{*}(A\cap F)+\mu^{*}(A\cap F^{c}).
$$

再与次可加性给出的反向不等式结合，得到等号。

所以 $F$ 可测。

因此 $\mathcal{M}_{\mu^{*}}$ 是一个 $\sigma$-代数。

在这个 $\sigma$-代数上，把外测度限制为

$$
\mu(E)=\mu^{*}(E)
$$

以后，可以证明 $\mu$ 满足可数可加性，所以它是真正的测度。

而且这个测度自动完备。

如果

$$
N\in\mathcal{M}_{\mu^{*}},\qquad\mu(N)=0,
$$

且

$$
A\subseteq N,
$$

那么

$$
\mu^{*}(A)=0.
$$

对于任意 $T\subseteq X$，

$$
\mu^{*}(T\cap A)=0.
$$

由次可加性，

$$
\mu^{*}(T)\leq\mu^{*}(T\cap A)+\mu^{*}(T\cap A^{c})=\mu^{*}(T\cap A^{c}).
$$

另一方面，

$$
T\cap A^{c}\subseteq T,
$$

因此

$$
\mu^{*}(T\cap A^{c})\leq\mu^{*}(T).
$$

所以

$$
\mu^{*}(T)=\mu^{*}(T\cap A)+\mu^{*}(T\cap A^{c}).
$$

于是 $A$ 也是 Carathéodory 可测的。

这说明由外测度得到的 Carathéodory 测度天然是完备的。

### Carathéodory 延拓

Carathéodory 可测性定理和 Carathéodory 延拓定理经常出现在同一个构造过程中，因此很容易混在一起。

但它们强调的是两个不同的问题。

Carathéodory 可测性定理从一个已经存在的外测度

$$
\mu^{*}
$$

出发，找出一族可测集。

而 Carathéodory 延拓定理则讨论：

如果我们只在一族简单集合上知道测度，能不能把它扩张到由这些集合生成的 $\sigma$-代数？

设 $\mathcal{A}$ 是 $X$ 上的一个集合代数。

也就是说，$\mathcal{A}$ 对有限并和补集封闭。

设

$$
\mu_{0}:\mathcal{A}\rightarrow[0,\infty]
$$

是一个预测度（Premeasure）。

预测度要求，当

$$
A_{n}\in\mathcal{A}
$$

两两不交，并且

$$
\bigcup_{n=1}^{\infty}A_{n}\in\mathcal{A},
$$

则

$$
\mu_{0}\left(\bigcup_{n=1}^{\infty}A_{n}\right)=\sum_{n=1}^{\infty}\mu_{0}(A_{n}).
$$

利用 $\mu_{0}$ 可以在所有子集上定义外测度

$$
\mu^{*}(E)=\inf\left\{\sum_{n=1}^{\infty}\mu_{0}(A_{n}):E\subseteq\bigcup_{n=1}^{\infty}A_{n},\ A_{n}\in\mathcal{A}\right\}.
$$

然后使用 Carathéodory 判据得到可测集合。

Carathéodory 延拓定理告诉我们：

$\mu_{0}$ 可以延拓成

$$
\sigma(\mathcal{A})
$$

上的一个测度。

如果 $\mu_{0}$ 是 $\sigma$-有限的，也就是存在

$$
X=\bigcup_{n=1}^{\infty}A_{n},\qquad A_{n}\in\mathcal{A},
$$

并且

$$
\mu_{0}(A_{n})<\infty,
$$

那么这个延拓在

$$
\sigma(\mathcal{A})
$$

上还是唯一的。

这就是从区间长度构造 Lebesgue 测度的理论基础之一。

### 度量外测度

如果 $X$ 本身还是一个度量空间 $(X,d)$，那么外测度可以进一步与空间中的距离发生联系。

对于两个非空集合

$$
A,B\subseteq X,
$$

定义集合之间的距离

$$
d(A,B)=\inf\{d(a,b):a\in A,\ b\in B\}.
$$

如果

$$
d(A,B)>0,
$$

则称 $A$ 与 $B$ 是正分离的（Positively Separated）。

设 $\mu^{*}$ 是 $X$ 上的外测度。

如果对于任意正分离集合 $A,B$ 都满足

$$
\mu^{*}(A\cup B)=\mu^{*}(A)+\mu^{*}(B),
$$

则称 $\mu^{*}$ 是一个**度量外测度（Metric Outer Measure）**。

这里需要特别注意：

“度量外测度”并不是指“只要在度量空间上定义的外测度”。

真正额外的条件是正分离集合上的可加性。

一个重要定理是：

度量空间上的任意度量外测度，其所有 Borel 集都是 Carathéodory 可测的。

因此，如果一个外测度与空间的度量足够协调，那么拓扑产生的 Borel $\sigma$-代数会自然包含在它的可测集合系统中。

这正是拓扑和测度之间一个非常漂亮的连接。

旧式的另一个自然想法是用集合直径来构造大小。

对于

$$
E\subseteq X,
$$

定义直径

$$
\operatorname{diam}(E)=\sup\{d(x,y):x,y\in E\}.
$$

然后尝试用一族小集合 $U_{k}$ 覆盖 $E$，并计算

$$
\sum_{k}\operatorname{diam}(U_{k}).
$$

不过严格来说，如果只直接取

$$
\inf\sum_{k}\operatorname{diam}(U_{k}),
$$

得到的对象更接近 Hausdorff content，而不是“度量外测度”这个名词本身的定义。

真正的 Hausdorff 测度还要限制覆盖集合的直径。

对于 $s\geq0$ 和 $\delta>0$，定义

$$
\mathcal{H}^{s}_{\delta}(E)=\inf\left\{\sum_{k=1}^{\infty}(\operatorname{diam}U_{k})^{s}:E\subseteq\bigcup_{k=1}^{\infty}U_{k},\ \operatorname{diam}U_{k}<\delta\right\}.
$$

当 $\delta$ 下降时，允许使用的覆盖越来越严格，因此

$$
\mathcal{H}^{s}_{\delta}(E)
$$

单调增加。

定义

$$
\mathcal{H}^{s}(E)=\lim_{\delta\downarrow0}\mathcal{H}^{s}_{\delta}(E).
$$

这就是 $s$ 维 Hausdorff 测度。

当 $s=1$ 时，它与长度有关；$s=2$ 时与面积有关；对于分形集合，甚至可以选择非整数 $s$。

所以从“用小球或小集合的直径覆盖”的直觉出发，实际上可以自然地走向分形几何和 Hausdorff 维数。

## Lebesgue 测度

### 矩形与体积

现在把讨论重新放回欧氏空间

$$
\mathbb{R}^{n}.
$$

我们的目标是构造一种测度，使它在一维时给出长度，在二维时给出面积，在三维时给出体积，并且对更复杂的集合仍然有意义。

首先考虑矩形。

设

$$
R=\prod_{i=1}^{n}(a_{i},b_{i}).
$$

定义它的体积为

$$
\lambda(R)=\prod_{i=1}^{n}(b_{i}-a_{i}).
$$

当 $n=1$ 时，

$$
R=(a,b)
$$

且

$$
\lambda(R)=b-a.
$$

当 $n=2$ 时，

$$
\lambda(R)=(b_{1}-a_{1})(b_{2}-a_{2}),
$$

就是普通矩形面积。

这个公式当然符合直觉。

真正的问题是：

如果

$$
E\subseteq\mathbb{R}^{n}
$$

是一个非常不规则的集合，怎样定义它的体积？

### Lebesgue 外测度

考虑所有可数个开矩形组成的覆盖

$$
E\subseteq\bigcup_{k=1}^{\infty}R_{k}.
$$

每个覆盖都有总容积

$$
\sum_{k=1}^{\infty}\lambda(R_{k}).
$$

定义

$$
m^{*}(E)=\inf\left\{\sum_{k=1}^{\infty}\lambda(R_{k}):E\subseteq\bigcup_{k=1}^{\infty}R_{k}\right\}.
$$

这称为 $E$ 的 **Lebesgue 外测度**。

从构造可以直接看出，Lebesgue 外测度就是前面一般覆盖构造的一个具体例子。

例如对于区间

$$
I=(a,b),
$$

显然有

$$
m^{*}(I)\leq b-a,
$$

因为 $I$ 自己就是一个合法覆盖。

真正需要证明的是反方向

$$
m^{*}(I)\geq b-a.
$$

也就是说，无论怎样使用可数个开区间覆盖 $(a,b)$，这些区间长度之和都不可能小于 $b-a$。

证明可以利用紧致性。

固定

$$
\varepsilon>0
$$

并考虑紧区间

$$
[a+\varepsilon,b-\varepsilon].
$$

任意覆盖 $(a,b)$ 的开区间族当然也覆盖这个紧区间。

由 Heine-Borel 性质，可以取出有限子覆盖。

对于有限个开区间，可以通过整理端点证明覆盖一个区间所需的总长度至少是该区间长度，因此

$$
\sum_{k}|I_{k}|\geq b-a-2\varepsilon.
$$

令

$$
\varepsilon\downarrow0
$$

得到

$$
\sum_{k}|I_{k}|\geq b-a.
$$

再对所有覆盖取下确界，

$$
m^{*}((a,b))=b-a.
$$

于是外测度确实与我们原来熟悉的长度概念相容。

### Lebesgue 可测集

有了 Lebesgue 外测度 $m^{*}$，便可以使用 Carathéodory 判据。

若

$$
E\subseteq\mathbb{R}^{n}
$$

满足对任意

$$
A\subseteq\mathbb{R}^{n}
$$

都有

$$
m^{*}(A)=m^{*}(A\cap E)+m^{*}(A\cap E^{c}),
$$

则称 $E$ 是 **Lebesgue 可测的**。

所有 Lebesgue 可测集合组成一个 $\sigma$-代数，通常记作

$$
\mathcal{L}(\mathbb{R}^{n})
$$

或简写为 $\mathcal{L}$。

在这个 $\sigma$-代数上定义

$$
m(E)=m^{*}(E).
$$

于是得到测度空间

$$
(\mathbb{R}^{n},\mathcal{L},m).
$$

这里的 $m$ 就是 Lebesgue 测度。

由于它来自 Carathéodory 构造，

$$
(\mathbb{R}^{n},\mathcal{L},m)
$$

是一个完备测度空间。

所以如果

$$
N\in\mathcal{L},\qquad m(N)=0,
$$

那么任意

$$
A\subseteq N
$$

也属于 $\mathcal{L}$，并且

$$
m(A)=0.
$$

### 平移与缩放

Lebesgue 测度应当符合我们对于几何体积的基本直觉。

最重要的性质之一是平移不变性。

设

$$
E\in\mathcal{L}(\mathbb{R}^{n})
$$

以及

$$
a\in\mathbb{R}^{n}.
$$

定义

$$
E+a=\{x+a:x\in E\}.
$$

则

$$
E+a
$$

仍然 Lebesgue 可测，并且

$$
m(E+a)=m(E).
$$

也就是说，一个图形在空间中移动以后，其体积不应发生改变。

对于缩放，若

$$
c>0,
$$

定义

$$
cE=\{cx:x\in E\}.
$$

则

$$
m(cE)=c^{n}m(E).
$$

这里的指数 $n$ 来自空间维数。

在二维中，所有边长放大 $c$ 倍，面积放大

$$
c^{2}
$$

倍。

在三维中则是

$$
c^{3}.
$$

这进一步推广到一般的可逆线性变换。

设

$$
T:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}
$$

是可逆线性映射。

如果 $E$ Lebesgue 可测，则 $T(E)$ 也 Lebesgue 可测，并满足

$$
m(T(E))=|\det T|\,m(E).
$$

所以

$$
|\det T|
$$

可以理解为线性变换的体积缩放因子。

从这个角度看，线性代数中行列式的几何意义在测度论中得到了非常自然的表达。

### Borel 集与 Lebesgue 可测集

Lebesgue 外测度是一个度量外测度。

因此所有 Borel 集都是 Lebesgue 可测的：

$$
\mathcal{B}(\mathbb{R}^{n})\subseteq\mathcal{L}(\mathbb{R}^{n}).
$$

但是这个包含关系实际上是严格的。

Lebesgue $\sigma$-代数可以理解为 Borel $\sigma$-代数关于 Lebesgue 测度的完备化。

更准确地说，如果 $E$ Lebesgue 可测，那么存在一个 Borel 集 $B$，使得

$$
m(E\triangle B)=0,
$$

其中

$$
E\triangle B=(E\setminus B)\cup(B\setminus E)
$$

表示对称差。

也就是说，任何 Lebesgue 可测集在忽略一个零测集以后，都可以用某个 Borel 集表示。

反过来，如果 $B$ 是 Borel 集，$N$ 是某个 Borel 零测集的任意子集，那么

$$
B\cup N
$$

仍然是 Lebesgue 可测的。

所以从结构上可以把 Lebesgue 可测集理解为：

Borel 集再加上所有应该由完备性补进去的零测集子集。

Cantor 集给出了一个非常典型的例子。

记经典 Cantor 集为

$$
C\subseteq[0,1].
$$

它是闭集，因此

$$
C\in\mathcal{B}(\mathbb{R}).
$$

另一方面，

$$
m(C)=0.
$$

因为 Lebesgue 测度是完备的，所以任意

$$
A\subseteq C
$$

都是 Lebesgue 可测的，而且

$$
m(A)=0.
$$

但并不是 Cantor 集的每一个子集都是 Borel 集。

事实上 Cantor 集的基数为连续统

$$
|C|=\mathfrak{c},
$$

所以它的子集个数是

$$
2^{\mathfrak{c}}.
$$

另一方面，$\mathbb{R}$ 中 Borel 集的总数只有

$$
\mathfrak{c}.
$$

由 Cantor 定理，

$$
2^{\mathfrak{c}}>\mathfrak{c}.
$$

因此必然存在

$$
A\subseteq C
$$

不是 Borel 集。

然而它仍然 Lebesgue 可测。

所以

$$
\mathcal{B}(\mathbb{R})\subsetneq\mathcal{L}(\mathbb{R}).
$$

### 正则性

Lebesgue 可测集合可以非常复杂。

但是一个重要而且非常有用的事实是：

它们在测度意义下可以由拓扑上比较良好的集合逼近。

对于 Lebesgue 可测集

$$
E\subseteq\mathbb{R}^{n},
$$

有外正则性

$$
m(E)=\inf\{m(O):E\subseteq O,\ O\text{ open}\}.
$$

也就是说，可以从外面用开集逼近 $E$。

还有内正则性

$$
m(E)=\sup\{m(K):K\subseteq E,\ K\text{ compact}\}.
$$

也就是说，可以从内部用紧集逼近 $E$。

特别地，如果

$$
m(E)<\infty,
$$

那么对于任意 $\varepsilon>0$，都存在开集 $O$ 和紧集 $K$，满足

$$
K\subseteq E\subseteq O
$$

并且

$$
m(O\setminus E)<\varepsilon,
$$

$$
m(E\setminus K)<\varepsilon.
$$

这说明即使 $E$ 本身非常不规则，在只关心测度的情况下，我们仍然可以把它替换成几乎一样大的开集或紧集。

拓扑结构与测度结构在这里真正发生了联系。

### 不可测集

到这里可能会产生一个自然的问题：

既然 Lebesgue 可测集已经非常广泛，为什么不干脆把

$$
\mathcal{P}(\mathbb{R})
$$

中的所有集合都定义为可测？

问题在于，我们无法同时保留所有希望 Lebesgue 测度拥有的性质。

经典例子是 Vitali 集。

在区间

$$
[0,1]
$$

上定义等价关系

$$
x\sim y\Longleftrightarrow x-y\in\mathbb{Q}.
$$

也就是说，如果两个实数之差是有理数，就把它们归入同一个等价类。

利用选择公理，可以从每个等价类中恰好选出一个代表元。

这些代表元组成一个集合 $V$，称为 Vitali 集。

考虑所有有理数

$$
q\in\mathbb{Q}\cap[-1,1]
$$

以及平移集合

$$
V+q.
$$

不同的这些集合两两不交。

同时它们的并覆盖 $[0,1]$，并被包含在一个有限区间中，例如

$$
[-1,2].
$$

如果 $V$ 是 Lebesgue 可测的，那么由平移不变性，

$$
m(V+q)=m(V).
$$

若

$$
m(V)=0,
$$

则可数个 $V+q$ 的并仍然测度为零。

但这个并覆盖 $[0,1]$，与

$$
m([0,1])=1
$$

矛盾。

若

$$
m(V)>0,
$$

则由于存在可数无限多个两两不交的平移，

$$
\sum_{q}m(V+q)=+\infty.
$$

但它们全部位于有限测度集合 $[-1,2]$ 中，又产生矛盾。

因此 $V$ 不可能 Lebesgue 可测。

所以并不是我们“不愿意”给所有集合定义长度。

而是在要求平移不变性、可数可加性以及普通区间具有通常长度的条件下，不可测集必然出现。

这也是为什么测度论从一开始就必须认真选择 $\sigma$-代数。

## 小结

现在可以把本文的主要结构重新整理一次。

实数首先是一个有序域。

真正使它区别于有理数的，是完备性：

$$
\mathbb{R}\quad\text{是完备有序域}.
$$

完备性使极限过程能够稳定地留在实数体系内部。

进一步把距离抽象成度量以后，我们得到度量空间

$$
(X,d),
$$

并可以在其中定义收敛、Cauchy 序列、完备性和紧致性。

另一方面，为了描述集合的大小，我们首先指定允许测量的集合系统

$$
\mathcal{F},
$$

得到可测空间

$$
(X,\mathcal{F}).
$$

再加入满足可数可加性的测度 $\mu$，得到

$$
(X,\mathcal{F},\mu).
$$

真正构造 Lebesgue 测度时，顺序则恰好相反。

我们先在所有集合上建立一个比较粗糙的外测度

$$
\mu^{*},
$$

然后利用 Carathéodory 条件

$$
\mu^{*}(A)=\mu^{*}(A\cap E)+\mu^{*}(A\cap E^{c})
$$

筛选出可测集合。

最后把外测度限制到这些集合上，得到真正的测度。

在欧氏空间中，这个过程最终给出

$$
(\mathbb{R}^{n},\mathcal{L},m),
$$

也就是 Lebesgue 测度空间
