# 赋范空间与 $L^{p}$ 空间

## 引言

第 I 篇建立了测度空间与 $\mathbb{R}^{n}$ 上的 Lebesgue 测度，第 II 篇在一般测度空间上定义了可测函数与 Lebesgue 积分，并证明了单调收敛定理、Fatou 引理与控制收敛定理。本篇转换视角：不再逐个研究函数，而是把一整类函数视为一个向量空间中的点，用积分度量这些点的“大小”与“距离”。这一视角下最基本的对象是 $L^{p}$ 空间。

$L^{p}$ 空间把三种结构结合在一起：线性结构（函数可以相加与数乘），度量结构（范数诱导距离，从而可以谈论收敛、Cauchy 列与完备性），以及测度结构（范数由积分给出）。本篇的主线如下：第 1 节介绍赋范空间与 Banach 空间的基本语言；第 2 节定义 $L^{p}$ 空间，并说明为什么必须把几乎处处相等的函数视为同一个元素；第 3 节证明 Young、Hölder 与 Minkowski 不等式及其取等条件；第 4 节证明 $1\le p<\infty$ 时 $L^{p}$ 的完备性（Riesz–Fischer 定理）；第 5 节单独讨论 $L^{\infty}$；第 6 节比较不同指数的 $L^{p}$ 空间；第 7 节讨论稠密子集与可分性；第 8 节简要介绍 $L^{p}$ 的对偶空间。

### 约定

- $\mathbb{K}$ 表示 $\mathbb{R}$ 或 $\mathbb{C}$。除特别声明外，$(X,\mathcal{M},\mu)$ 是一个测度空间；“a.e.”（几乎处处）均相对于 $\mu$ 而言。$m$ 表示 $\mathbb{R}^{n}$ 上的 Lebesgue 测度。
- 可测函数、非负可测函数的积分以及可积函数的积分沿用第 II 篇的定义。复值函数 $f=u+iv$ 可测是指 $u,v$ 均可测；当 $|f|$ 可积时定义 $\int f\,\mathrm{d}\mu=\int u\,\mathrm{d}\mu+i\int v\,\mathrm{d}\mu$。此时 $\bigl|\int f\,\mathrm{d}\mu\bigr|\le\int|f|\,\mathrm{d}\mu$：取 $|\alpha|=1$ 使 $\alpha\int f\,\mathrm{d}\mu=\bigl|\int f\,\mathrm{d}\mu\bigr|$，则
$$
\Bigl|\int f\,\mathrm{d}\mu\Bigr|=\int \operatorname{Re}(\alpha f)\,\mathrm{d}\mu\le\int|f|\,\mathrm{d}\mu .
$$
- 在 $[0,\infty]$ 中约定 $0\cdot\infty=0$，$1/\infty=0$，$\infty^{1/p}=\infty$。
- 对 $1\le p\le\infty$，称满足 $\frac1p+\frac1q=1$ 的 $q\in[1,\infty]$ 为 $p$ 的**共轭指数**；$p=1$ 时 $q=\infty$，$p=\infty$ 时 $q=1$。当 $1<p<\infty$ 时 $q=\frac{p}{p-1}$，并且 $(p-1)q=p$。

## 1. 赋范空间与 Banach 空间

### 1.1 范数

第 I 篇在一般集合上引入了度量。当集合本身是向量空间时，更自然的做法是先度量每个向量的“长度”，再由长度得到距离。

**定义 1.1**（范数）
设 $V$ 是域 $\mathbb{K}$ 上的向量空间。映射 $\lVert \cdot\rVert:V\to[0,\infty)$ 称为 $V$ 上的一个**范数（norm）**，如果对任意 $x,y\in V$ 与 $\alpha\in\mathbb{K}$：

(i) （正定性）$\lVert x\rVert=0$ 蕴含 $x=0$；

(ii) （齐次性）$\lVert \alpha x\rVert=|\alpha|\,\lVert x\rVert$；

(iii) （三角不等式）$\lVert x+y\rVert\le\lVert x\rVert+\lVert y\rVert$。

只满足 (ii)(iii) 的映射称为**半范数（seminorm）**。配备了范数的向量空间 $(V,\lVert \cdot\rVert)$ 称为**赋范空间**。

**注 1.2**

(i) 齐次性可以弱化为 $\lVert \alpha x\rVert\le|\alpha|\,\lVert x\rVert$ 对一切 $\alpha$ 成立：当 $\alpha\ne0$ 时 $\lVert x\rVert=\lVert \alpha^{-1}(\alpha x)\rVert\le|\alpha|^{-1}\lVert \alpha x\rVert$，反向不等式随之成立；当 $\alpha=0$ 时 $\lVert 0\rVert=\lVert 0\cdot 0\rVert\le 0$。

(ii) 三角不等式说的是“和的范数不超过范数之和”，而不是相反。

(iii) 范数是单个向量的函数；由它定义的 $d(x,y)=\lVert x-y\rVert$ 是 $V$ 上的一个度量：正定性给出 $d(x,y)=0\Leftrightarrow x=y$，齐次性（取 $\alpha=-1$）给出对称性，三角不等式给出度量的三角不等式。这个度量还满足平移不变性 $d(x+z,y+z)=d(x,y)$ 与伸缩性 $d(\alpha x,\alpha y)=|\alpha|d(x,y)$。因此并非每个度量都来自范数：例如 $\mathbb{R}$ 上的离散度量（$x\ne y$ 时 $d(x,y)=1$）满足 $d(2,0)=d(1,0)=1$，不满足伸缩性。

以下凡谈及赋范空间中的收敛、Cauchy 列、开集与闭集，均指相对于度量 $d(x,y)=\lVert x-y\rVert$ 而言。

**命题 1.3**
设 $(V,\lVert \cdot\rVert)$ 是赋范空间。

(i) 对任意 $x,y\in V$，$\bigl|\lVert x\rVert-\lVert y\rVert\bigr|\le\lVert x-y\rVert$；特别地，范数是 $V$ 上的连续函数。

(ii) 若 $x_{n}\to x$，$y_{n}\to y$，$\alpha_{n}\to\alpha$（$\alpha_n\in\mathbb{K}$），则 $x_{n}+y_{n}\to x+y$，$\alpha_{n}x_{n}\to\alpha x$。

*证明.*　
(i) 由三角不等式 $\lVert x\rVert\le\lVert x-y\rVert+\lVert y\rVert$，同理 $\lVert y\rVert\le\lVert y-x\rVert+\lVert x\rVert$，而 $\lVert y-x\rVert=\lVert x-y\rVert$。

(ii) $\lVert (x_{n}+y_{n})-(x+y)\rVert\le\lVert x_{n}-x\rVert+\lVert y_{n}-y\rVert\to0$。又
$$
\lVert \alpha_{n}x_{n}-\alpha x\rVert\le|\alpha_{n}|\,\lVert x_{n}-x\rVert+|\alpha_{n}-\alpha|\,\lVert x\rVert,
$$
而 $(|\alpha_{n}|)$ 有界，故右端趋于 $0$。 $\square$

### 1.2 Banach 空间与级数判别法

**定义 1.4**（Banach 空间）
赋范空间 $V$ 中的序列 $(x_{n})$ 称为 **Cauchy 列**，如果对任意 $\varepsilon>0$ 存在 $N$，使得 $m,n\ge N$ 时 $\lVert x_{m}-x_{n}\rVert<\varepsilon$。若 $V$ 中每个 Cauchy 列都收敛到 $V$ 中某个元素，则称 $V$ 是**完备的**；完备的赋范空间称为 **Banach 空间**。

在赋范空间中可以谈论级数。称 $\sum_{k=1}^{\infty}x_{k}$ **收敛**，如果部分和 $S_{n}=\sum_{k=1}^{n}x_{k}$ 在 $V$ 中收敛；称它**绝对收敛**，如果 $\sum_{k=1}^{\infty}\lVert x_{k}\rVert<\infty$。在 $\mathbb{R}$ 中绝对收敛蕴含收敛，这正是 $\mathbb{R}$ 的完备性的一种表述。下面的定理说明这一现象在一般赋范空间中恰好刻画了完备性，它将是证明 $L^{p}$ 完备性的工具。

**定理 1.5**（完备性的级数判别法）
赋范空间 $V$ 是完备的，当且仅当 $V$ 中每个绝对收敛的级数都在 $V$ 中收敛。

*证明.*　
必要性：设 $V$ 完备且 $\sum\lVert x_{k}\rVert<\infty$。对 $m>n$，
$$
\lVert S_{m}-S_{n}\rVert=\Bigl\|\sum_{k=n+1}^{m}x_{k}\Bigr\|\le\sum_{k=n+1}^{\infty}\lVert x_{k}\rVert\xrightarrow[n\to\infty]{}0,
$$
故 $(S_{n})$ 是 Cauchy 列，从而收敛。

充分性：设 $(x_{n})$ 是 Cauchy 列。依次选取 $n_{1}<n_{2}<\cdots$，使得 $m,n\ge n_{k}$ 时 $\lVert x_{m}-x_{n}\rVert<2^{-k}$。令 $y_{1}=x_{n_{1}}$，$y_{k+1}=x_{n_{k+1}}-x_{n_{k}}$，则 $\sum_{k}\lVert y_{k}\rVert\le\lVert y_{1}\rVert+\sum_{k}2^{-k}<\infty$。由假设 $\sum y_{k}$ 收敛到某个 $x\in V$，而它的第 $k$ 个部分和恰是 $x_{n_{k}}$，所以 $x_{n_{k}}\to x$。最后，对给定的 $\varepsilon>0$ 取 $N$ 使 $m,n\ge N$ 时 $\lVert x_{m}-x_{n}\rVert<\varepsilon$，再取 $k$ 使 $n_{k}\ge N$ 且 $\lVert x_{n_{k}}-x\rVert<\varepsilon$，则 $n\ge N$ 时
$$
\lVert x_{n}-x\rVert\le\lVert x_{n}-x_{n_{k}}\rVert+\lVert x_{n_{k}}-x\rVert<2\varepsilon .
$$
故 $x_{n}\to x$。 $\square$

### 1.3 有限维的例子：$\mathbb{K}^{n}$ 上的 $p$-范数

**例 1.6**（$\mathbb{K}^{n}$ 上的 $p$-范数）
对 $x=(x_{1},\dots,x_{n})\in\mathbb{K}^{n}$ 与 $1\le p<\infty$，令
$$
\lVert x\rVert_{p}=\Bigl(\sum_{i=1}^{n}|x_{i}|^{p}\Bigr)^{1/p},\qquad \lVert x\rVert_{\infty}=\max_{1\le i\le n}|x_{i}|.
$$
正定性与齐次性是显然的；$p=1$ 与 $p=\infty$ 时的三角不等式直接来自 $\mathbb{K}$ 中的三角不等式；$1<p<\infty$ 时的三角不等式就是离散形式的 Minkowski 不等式，将在第 3 节（推论 3.11）证明。由它诱导的距离 $d_{p}(x,y)=\lVert x-y\rVert_{p}$ 常称为 **Minkowski 距离**；$p=1,2,\infty$ 分别对应“曼哈顿距离”、欧氏距离与 Chebyshev 距离。由
$$
\lVert x\rVert_{\infty}\le\lVert x\rVert_{p}\le n^{1/p}\lVert x\rVert_{\infty}
$$
可知 $\lim_{p\to\infty}\lVert x\rVert_{p}=\lVert x\rVert_{\infty}$，这解释了记号 $\lVert \cdot\rVert_{\infty}$。图 1 画出了 $\mathbb{R}^{2}$ 中的单位球 $B_{p}=\{x:\lVert x\rVert_{p}\le1\}$。

> 图：$\mathbb{R}^{2}$ 中 $\{\lVert x\rVert_{p}\le1\}$ 的边界。$p\ge1$ 时单位球是凸集；$p=\tfrac12$ 时不是。

**例 1.7**（$0<p<1$ 时不是范数）
当 $0<p<1$ 时，仍可用同一公式定义 $\lVert x\rVert_{p}$，正定性与齐次性依然成立，但当 $n\ge2$ 时三角不等式不成立：取 $e_{1}=(1,0,\dots,0)$，$e_{2}=(0,1,0,\dots,0)$，则
$$
\lVert e_{1}+e_{2}\rVert_{p}=2^{1/p}>2=\lVert e_{1}\rVert_{p}+\lVert e_{2}\rVert_{p}.
$$
几何上，任何范数的单位球都是凸集，因为 $\lVert x\rVert,\lVert y\rVert\le1$ 与 $t\in[0,1]$ 蕴含 $\lVert tx+(1-t)y\rVert\le t\lVert x\rVert+(1-t)\lVert y\rVert\le1$；而图 1 中 $p=\tfrac12$ 的单位球不是凸的。

在信号处理中还常用记号 $\lVert x\rVert_{0}=\#\{i:x_{i}\ne0\}$（非零分量的个数）。它满足三角不等式，但不满足齐次性（$\lVert 2x\rVert_{0}=\lVert x\rVert_{0}$），因此也不是范数。注意 $\lVert x\rVert_{0}=\lim_{p\to0^{+}}\lVert x\rVert_{p}^{p}$，它是 $\lVert x\rVert_{p}^{p}$ 而不是 $\lVert x\rVert_{p}$ 的极限。

有限维空间中所有范数在拓扑上没有差别。

**定义 1.8**（等价范数）
向量空间 $V$ 上的两个范数 $\lVert \cdot\rVert$ 与 $\lVert \cdot\rVert'$ 称为**等价的**，如果存在常数 $0<c\le C$ 使得对一切 $x\in V$，$c\lVert x\rVert\le\lVert x\rVert'\le C\lVert x\rVert$。

等价范数给出相同的收敛序列、相同的 Cauchy 列与相同的开集。

**定理 1.9**
有限维向量空间上的任意两个范数都等价。

*证明.*　
取基 $e_{1},\dots,e_{n}$，把 $V$ 等同于 $\mathbb{K}^{n}$。只需证明任一范数 $\lVert \cdot\rVert$ 都与 $\lVert \cdot\rVert_{1}$ 等价。一方面，
$$
\lVert x\rVert=\Bigl\|\sum_{i}x_{i}e_{i}\Bigr\|\le\sum_{i}|x_{i}|\,\lVert e_{i}\rVert\le M\lVert x\rVert_{1},\qquad M=\max_{i}\lVert e_{i}\rVert .
$$
于是 $\bigl|\lVert x\rVert-\lVert y\rVert\bigr|\le M\lVert x-y\rVert_{1}$，即 $\lVert \cdot\rVert$ 关于 $\lVert \cdot\rVert_{1}$ 连续。另一方面，把 $\mathbb{K}^{n}$ 视为 $\mathbb{R}^{n}$ 或 $\mathbb{R}^{2n}$，由 Cauchy–Schwarz 不等式 $\lVert x\rVert_{1}\le\sqrt{n}\,\lVert x\rVert_{2}$，又显然 $\lVert x\rVert_{2}\le\lVert x\rVert_{1}$，所以 $\lVert \cdot\rVert_{1}$ 与欧氏范数给出相同的有界集与闭集。因此单位球面 $S=\{x:\lVert x\rVert_{1}=1\}$ 是欧氏意义下的有界闭集，由 Heine–Borel 定理（第 I 篇）是紧集。连续函数 $\lVert \cdot\rVert$ 在 $S$ 上取到最小值 $c$，且 $c>0$（$S$ 中不含 $0$）。对 $x\ne0$，
$$
\lVert x\rVert=\lVert x\rVert_{1}\,\Bigl\|\frac{x}{\lVert x\rVert_{1}}\Bigr\|\ge c\lVert x\rVert_{1}. 
$$

$\square$

**推论 1.10**
有限维赋范空间都是完备的；赋范空间的有限维子空间都是闭子空间。

*证明.*　
设 $(x^{(k)})$ 是有限维赋范空间中的 Cauchy 列。由定理 1.9，它关于 $\lVert \cdot\rVert_{1}$ 也是 Cauchy 列，于是每个坐标 $(x^{(k)}_{i})_{k}$ 都是 $\mathbb{K}$ 中的 Cauchy 列，由 $\mathbb{K}$ 的完备性收敛到某个 $x_{i}$。于是 $\lVert x^{(k)}-x\rVert_{1}\to0$，再由等价性 $\lVert x^{(k)}-x\rVert\to0$。第二个结论来自：度量空间中的完备子集是闭集。 $\square$

**注 1.11**
常说“$n$ 维赋范空间与 $\mathbb{K}^{n}$ 同构”，其精确含义是：$\mathbb{K}$ 上的 $n$ 维赋范空间与 $(\mathbb{K}^{n},\lVert \cdot\rVert_{2})$ 之间存在一个双向连续的线性同构（线性同胚），但一般*不是*等距同构。例如 $(\mathbb{R}^{2},\lVert \cdot\rVert_{\infty})$ 与 $(\mathbb{R}^{2},\lVert \cdot\rVert_{2})$ 之间不存在线性等距：线性映射把圆盘映成椭圆盘，而不可能映成正方形。

### 1.4 无穷维的例子

**例 1.12**（$C[a,b]$ 与上确界范数）
设 $C[a,b]$ 为 $[a,b]$ 上 $\mathbb{K}$ 值连续函数全体，令 $\lVert f\rVert_{u}=\max_{x\in[a,b]}|f(x)|$（称为**一致范数**或上确界范数）。则 $(C[a,b],\lVert \cdot\rVert_{u})$ 是 Banach 空间。

事实上，设 $(f_{n})$ 是 Cauchy 列。对每个 $x$，$|f_{n}(x)-f_{m}(x)|\le\lVert f_{n}-f_{m}\rVert_{u}$，故 $(f_{n}(x))$ 是 $\mathbb{K}$ 中的 Cauchy 列，记其极限为 $f(x)$。给定 $\varepsilon>0$，取 $N$ 使 $m,n\ge N$ 时 $\lVert f_{n}-f_{m}\rVert_{u}<\varepsilon$；在 $|f_{n}(x)-f_{m}(x)|<\varepsilon$ 中令 $m\to\infty$，得 $n\ge N$ 时 $\sup_{x}|f_{n}(x)-f(x)|\le\varepsilon$，即 $f_{n}\to f$ 一致收敛。一致收敛的连续函数列的极限连续：对 $x_{0}\in[a,b]$，取 $\delta>0$ 使 $|x-x_{0}|<\delta$ 时 $|f_{N}(x)-f_{N}(x_{0})|<\varepsilon$，则
$$
|f(x)-f(x_{0})|\le|f(x)-f_{N}(x)|+|f_{N}(x)-f_{N}(x_{0})|+|f_{N}(x_{0})-f(x_{0})|<3\varepsilon .
$$
故 $f\in C[a,b]$ 且 $\lVert f_{n}-f\rVert_{u}\to0$。

**例 1.13**（同一空间上的不完备范数）
在 $C[0,2]$ 上令 $\lVert f\rVert_{1}=\int_{0}^{2}|f(x)|\,\mathrm{d}x$。这是一个范数：若 $f$ 连续且 $|f(x_{0})|>0$，则 $|f|$ 在 $x_{0}$ 的某个邻域内大于 $|f(x_{0})|/2$，于是 $\lVert f\rVert_{1}>0$。但 $(C[0,2],\lVert \cdot\rVert_{1})$ 不完备。令
$$
f_{n}(x)=\begin{cases}0,&0\le x\le1,\\ n(x-1),&1<x<1+\tfrac1n,\\ 1,&1+\tfrac1n\le x\le2.\end{cases}
$$
当 $m>n$ 时 $f_{m}$ 与 $f_{n}$ 只在 $[1,1+\frac1n]$ 上不同，且差的绝对值不超过 $1$，故 $\lVert f_{m}-f_{n}\rVert_{1}\le\frac1n$，$(f_{n})$ 是 Cauchy 列。若存在连续函数 $f$ 使 $\lVert f_{n}-f\rVert_{1}\to0$，则 $\int_{0}^{1}|f|\le\lVert f-f_{n}\rVert_{1}\to0$，故 $f=0$ 于 $[0,1]$；对任意 $\delta\in(0,1)$，当 $n>1/\delta$ 时 $\int_{1+\delta}^{2}|f-1|\le\lVert f-f_{n}\rVert_{1}\to0$，故 $f=1$ 于 $[1+\delta,2]$，从而于 $(1,2]$。这与 $f$ 在 $1$ 处连续矛盾。

所以同一个向量空间可以在一个范数下完备而在另一个范数下不完备；特别地，$\lVert \cdot\rVert_{u}$ 与 $\lVert \cdot\rVert_{1}$ 在 $C[0,2]$ 上不等价，这与定理 1.9 形成对照。第 7 节将看到，这个空间的“完备化”正是 $L^{1}[0,2]$。

**例 1.14**（序列空间）
对 $1\le p<\infty$，令 $\ell^{p}$ 为满足 $\sum_{n}|x_{n}|^{p}<\infty$ 的 $\mathbb{K}$ 值序列 $x=(x_{n})_{n\ge1}$ 全体，$\lVert x\rVert_{p}=(\sum_{n}|x_{n}|^{p})^{1/p}$；令 $\ell^{\infty}$ 为有界序列全体，$\lVert x\rVert_{\infty}=\sup_{n}|x_{n}|$。例 2.9 将说明它们是计数测度下的 $L^{p}$ 空间，因此下文关于 $L^{p}$ 的所有结论（Minkowski 不等式、完备性等）都适用于 $\ell^{p}$。

### 1.5 有界线性映射

**定义 1.15**
设 $V,W$ 是 $\mathbb{K}$ 上的赋范空间。线性映射 $T:V\to W$ 称为**有界的**，如果存在常数 $C\ge0$ 使得对一切 $x\in V$，$\lVert Tx\rVert_{W}\le C\lVert x\rVert_{V}$。满足此式的最小常数
$$
\lVert T\rVert=\sup_{\lVert x\rVert_{V}\le1}\lVert Tx\rVert_{W}
$$
称为 $T$ 的**算子范数**。取 $W=\mathbb{K}$ 时，有界线性映射称为有界线性泛函；$V$ 上全体有界线性泛函构成的空间记为 $V^{*}$，称为 $V$ 的**对偶空间**，它在算子范数下是 Banach 空间（证明与例 1.12 类似，只用到 $\mathbb{K}$ 的完备性）。

**命题 1.16**
对线性映射 $T:V\to W$，以下三者等价：(a) $T$ 有界；(b) $T$ 连续；(c) $T$ 在 $0$ 处连续。

*证明.*　
(a)$\Rightarrow$(b)：$\lVert Tx-Ty\rVert_{W}=\lVert T(x-y)\rVert_{W}\le C\lVert x-y\rVert_{V}$，$T$ 是 Lipschitz 的。(b)$\Rightarrow$(c) 显然。(c)$\Rightarrow$(a)：存在 $\delta>0$ 使 $\lVert x\rVert_{V}\le\delta$ 时 $\lVert Tx\rVert_{W}\le1$。对 $x\ne0$，
$$
\lVert Tx\rVert_{W}=\frac{\lVert x\rVert_{V}}{\delta}\Bigl\|T\Bigl(\frac{\delta x}{\lVert x\rVert_{V}}\Bigr)\Bigr\|_{W}\le\frac{1}{\delta}\lVert x\rVert_{V}. 
$$

$\square$

## 2. $L^{p}$ 空间

### 2.1 $p$-范数与本质上确界

**定义 2.1**
设 $f$ 是 $X$ 上取值于 $\mathbb{K}$ 或 $[-\infty,\infty]$ 的可测函数。对 $0<p<\infty$，令
$$
\lVert f\rVert_{p}=\Bigl(\int_{X}|f|^{p}\,\mathrm{d}\mu\Bigr)^{1/p}\in[0,\infty].
$$
对 $p=\infty$，令
$$
\lVert f\rVert_{\infty}=\operatorname*{ess\,sup}_{X}|f|=\inf\bigl\{M\ge0:\ \mu(\{x:|f(x)|>M\})=0\bigr\}\in[0,\infty],
$$
其中 $\inf\varnothing=\infty$。$\lVert f\rVert_{\infty}$ 称为 $|f|$ 的**本质上确界（essential supremum）**，即 $|f|$ 的最小几乎处处上界。

**注 2.2**
定义中的条件“$\mu(\{|f|>M\})=0$”（即 $|f|\le M$ a.e.）不可省略：若要求 $|f|\le M$ 处处成立，得到的是普通上确界 $\sup|f|$，它会被零测集上的取值改变。例如 $f=\mathbf{1}_{\mathbb{Q}}$ 在 $\mathbb{R}$ 上满足 $\sup|f|=1$，而 $\lVert f\rVert_{\infty}=0$。

**引理 2.3**
对任意可测函数 $f$，$|f|\le\lVert f\rVert_{\infty}$ a.e.；即定义中的下确界是可以取到的。

*证明.*　
若 $\lVert f\rVert_{\infty}=\infty$，结论平凡。否则
$$
\{|f|>\lVert f\rVert_{\infty}\}=\bigcup_{k=1}^{\infty}\Bigl\{|f|>\lVert f\rVert_{\infty}+\tfrac1k\Bigr\},
$$
由下确界的定义右端每一项都是零测集，可数个零测集之并仍是零测集。 $\square$

**引理 2.4**
设 $0<p\le\infty$，$f,g$ 可测。

(i) $\lVert f\rVert_{p}=0$ 当且仅当 $f=0$ a.e.；

(ii) 若 $f=g$ a.e.，则 $\lVert f\rVert_{p}=\lVert g\rVert_{p}$；

(iii) 若 $f$ 取值于 $\mathbb{K}$，$\alpha\in\mathbb{K}$，则 $\lVert \alpha f\rVert_{p}=|\alpha|\,\lVert f\rVert_{p}$。

*证明.*　
(i) $p<\infty$ 时，由第 II 篇，非负可测函数 $|f|^{p}$ 的积分为零当且仅当 $|f|^{p}=0$ a.e.。$p=\infty$ 时，若 $\lVert f\rVert_{\infty}=0$，由引理 2.3 得 $|f|\le0$ a.e.；反之显然。(ii) $p<\infty$ 时 $|f|^{p}=|g|^{p}$ a.e.，积分相同；$p=\infty$ 时，$\{|f|>M\}$ 与 $\{|g|>M\}$ 相差一个零测集。(iii) 由积分的齐次性（$p<\infty$）或由 $\{|\alpha f|>|\alpha|M\}=\{|f|>M\}$（$p=\infty$，$\alpha\ne0$）直接验证。 $\square$

### 2.2 $L^{p}$ 空间的定义

**定义 2.5**
对 $0<p\le\infty$，令
$$
\mathcal{L}^{p}(X,\mu)=\bigl\{f:X\to\mathbb{K}\ \big|\ f\text{ 可测},\ \lVert f\rVert_{p}<\infty\bigr\}.
$$

**命题 2.6**
$\mathcal{L}^{p}(X,\mu)$ 在逐点加法与数乘下是 $\mathbb{K}$ 上的向量空间。更精确地，对 $a,b\in\mathbb{K}$：
$$
|a+b|^{p}\le 2^{p-1}\bigl(|a|^{p}+|b|^{p}\bigr)\quad(1\le p<\infty),\qquad
|a+b|^{p}\le |a|^{p}+|b|^{p}\quad(0<p\le1).
$$

*证明.*　
数乘封闭性来自引理 2.4(iii)。对 $1\le p<\infty$，函数 $t\mapsto t^{p}$ 在 $[0,\infty)$ 上是凸的，故
$$
\Bigl(\frac{|a|+|b|}{2}\Bigr)^{p}\le\frac{|a|^{p}+|b|^{p}}{2},
$$
结合 $|a+b|\le|a|+|b|$ 即得第一个不等式。对 $0<p\le1$ 与 $s,t\ge0$，$s+t>0$，由于 $\frac{s}{s+t},\frac{t}{s+t}\in[0,1]$ 而 $p\le1$，有
$$
1=\frac{s}{s+t}+\frac{t}{s+t}\le\Bigl(\frac{s}{s+t}\Bigr)^{p}+\Bigl(\frac{t}{s+t}\Bigr)^{p},
$$
即 $(s+t)^{p}\le s^{p}+t^{p}$；取 $s=|a|$，$t=|b|$ 即得第二个不等式。把这两个不等式应用于 $a=f(x)$，$b=g(x)$ 并积分，可知 $f,g\in\mathcal{L}^{p}$ 时 $f+g\in\mathcal{L}^{p}$（$p<\infty$）。$p=\infty$ 时，由引理 2.3，$|f+g|\le\lVert f\rVert_{\infty}+\lVert g\rVert_{\infty}$ a.e.。 $\square$

然而 $\lVert \cdot\rVert_{p}$ 在 $\mathcal{L}^{p}$ 上一般不满足正定性：例如 $f=\mathbf{1}_{\{0\}}$ 在 $(\mathbb{R},m)$ 上满足 $\lVert f\rVert_{p}=0$，但 $f\ne0$。补救的办法是不区分几乎处处相等的函数。关系“$f\sim g\iff f=g$ a.e.”是 $\mathcal{L}^{p}$ 上的等价关系（传递性来自两个零测集之并仍是零测集），且 $\mathcal{N}=\{f:f=0\ \text{a.e.}\}$ 是 $\mathcal{L}^{p}$ 的线性子空间。

**定义 2.7**（$L^{p}$ 空间）
对 $0<p\le\infty$，定义商空间
$$
L^{p}(X,\mu)=\mathcal{L}^{p}(X,\mu)/\mathcal{N},
$$
其元素是等价类 $[f]=\{g\in\mathcal{L}^{p}:g=f\ \text{a.e.}\}$，运算为 $[f]+[g]=[f+g]$，$\alpha[f]=[\alpha f]$，并令 $\lVert [f]\rVert_{p}=\lVert f\rVert_{p}$。

由引理 2.4(ii)，$\lVert [f]\rVert_{p}$ 与代表元的选取无关；由引理 2.4(i)，$\lVert [f]\rVert_{p}=0$ 当且仅当 $[f]=[0]$。因此，一旦在第 3 节证明了 $1\le p\le\infty$ 时的三角不等式，$L^{p}(X,\mu)$ 就是赋范空间。

**注 2.8**（记号约定）

(i) 按惯例我们把等价类 $[f]$ 与它的代表元 $f$ 等同，写作 $f\in L^{p}$；诸如 $f\ge0$、$f\le g$、$f=g$ 之类的关系都理解为几乎处处成立。但必须记住 $L^{p}$ 的元素不是函数：当单点是零测集时（例如 $(\mathbb{R}^{n},m)$），“$f\in L^{p}(\mathbb{R})$ 在 $0$ 处的值”没有意义。

(ii) 若 $f$ 取值于 $[-\infty,\infty]$ 且 $\lVert f\rVert_{p}<\infty$（$p<\infty$），则 $f$ 几乎处处有限（否则 $|f|^{p}=\infty$ 于正测集上），因而与一个有限值函数几乎处处相等；所以允许 $L^{p}$ 的代表元取广义实数值不会带来任何变化。

(iii) $L^{p}$ 对任何测度空间都有定义，不限于 Lebesgue 测度。当 $X=\mathbb{R}^{n}$ 或其可测子集 $E$ 并配备 Lebesgue 测度时，记作 $L^{p}(\mathbb{R}^{n})$、$L^{p}(E)$、$L^{p}[a,b]$ 等；在不引起混淆时也简写为 $L^{p}(X)$ 或 $L^{p}$。

### 2.3 两个基本例子

**例 2.9**（计数测度与 $\ell^{p}$）
设 $X=\mathbb{N}$，$\mathcal{M}=\mathcal{P}(\mathbb{N})$，$\mu$ 为计数测度（$\mu(A)=\#A$）。每个函数 $f:\mathbb{N}\to\mathbb{K}$ 都可测。对非负的 $f$，简单函数 $f\mathbf{1}_{\{1,\dots,N\}}$ 单调上升趋于 $f$，由单调收敛定理
$$
\int_{\mathbb{N}}f\,\mathrm{d}\mu=\lim_{N\to\infty}\sum_{n=1}^{N}f(n)=\sum_{n=1}^{\infty}f(n).
$$
由于唯一的零测集是 $\varnothing$，等价类只含一个函数，并且 $\lVert f\rVert_{\infty}=\sup_{n}|f(n)|$。因此 $L^{p}(\mathbb{N},\mu)=\ell^{p}$（$0<p\le\infty$），范数与例 1.14 相同。同理，$X=\{1,\dots,n\}$ 上的计数测度给出 $(\mathbb{K}^{n},\lVert \cdot\rVert_{p})$，即例 1.6。

**例 2.10**（幂函数）
设 $\alpha>0$，$0<p<\infty$。则
$$
x^{-\alpha}\in L^{p}(0,1)\iff \alpha p<1,\qquad x^{-\alpha}\in L^{p}(1,\infty)\iff \alpha p>1 .
$$
事实上，$x^{-\alpha p}\mathbf{1}_{[\varepsilon,1)}$ 当 $\varepsilon\downarrow0$ 时单调上升趋于 $x^{-\alpha p}\mathbf{1}_{(0,1)}$，由单调收敛定理以及连续函数在闭区间上的 Lebesgue 积分等于 Riemann 积分（第 II 篇），
$$
\int_{(0,1)}x^{-\alpha p}\,\mathrm{d}x=\lim_{\varepsilon\to0^{+}}\int_{\varepsilon}^{1}x^{-\alpha p}\,\mathrm{d}x=\begin{cases}\dfrac{1}{1-\alpha p},&\alpha p<1,\\[2mm] \infty,&\alpha p\ge1.\end{cases}
$$
$(1,\infty)$ 上的情形同理。于是 $x^{-\alpha}\mathbf{1}_{(0,1)}$ 只属于指数较小的 $L^{p}$（局部奇性惩罚大的 $p$），而 $x^{-\alpha}\mathbf{1}_{(1,\infty)}$ 只属于指数较大的 $L^{p}$（在无穷远处衰减过慢惩罚小的 $p$）。这一对照将在第 6 节中反复出现。

## 3. Young、Hölder 与 Minkowski 不等式

### 3.1 Young 不等式

**引理 3.1**（Young 不等式）
设 $1<p<\infty$，$q$ 为其共轭指数，$a,b\ge0$。则
$$
ab\le\frac{a^{p}}{p}+\frac{b^{q}}{q},
$$
且等号成立当且仅当 $a^{p}=b^{q}$。

*证明.*　
若 $a=0$ 或 $b=0$，左端为 $0$，右端非负，并且右端为 $0$ 当且仅当 $a=b=0$，即当且仅当 $a^{p}=b^{q}$。设 $a,b>0$。由于 $(e^{t})''=e^{t}>0$，指数函数严格凸：对 $\lambda\in(0,1)$，
$$
e^{\lambda s+(1-\lambda)t}\le\lambda e^{s}+(1-\lambda)e^{t},
$$
且等号当且仅当 $s=t$ 时成立。取 $\lambda=\frac1p$（从而 $1-\lambda=\frac1q$），$s=\log a^{p}$，$t=\log b^{q}$，左端为 $e^{\log a+\log b}=ab$，右端为 $\frac{a^{p}}{p}+\frac{b^{q}}{q}$；等号当且仅当 $a^{p}=b^{q}$。 $\square$

**注 3.2**
Young 不等式有一个直观的几何解释（图 2）：曲线 $y=x^{p-1}$ 与其反函数 $x=y^{q-1}$（注意 $(p-1)(q-1)=1$）将矩形 $[0,a]\times[0,b]$ 覆盖在两块区域之中，两块区域的面积分别是 $\int_{0}^{a}x^{p-1}\,\mathrm{d}x=\frac{a^{p}}{p}$ 与 $\int_{0}^{b}y^{q-1}\,\mathrm{d}y=\frac{b^{q}}{q}$；当且仅当 $b=a^{p-1}$（即 $a^{p}=b^{q}$）时两块区域恰好拼成矩形。

> 图：Young 不等式的几何解释（图中 $p=3$，$q=\tfrac32$）。两块阴影区域覆盖矩形 $[0,a]\times[0,b]$。

### 3.2 Hölder 不等式

回忆内积空间 $V$ 中的 Cauchy–Schwarz 不等式 $|\langle u,v\rangle|\le\lVert u\rVert\,\lVert v\rVert$。Hölder 不等式是它在 $L^{p}$ 框架下的推广。

**定理 3.3**（Hölder 不等式）
设 $1\le p\le\infty$，$q$ 为其共轭指数，$f,g$ 是 $X$ 上的 $\mathbb{K}$ 值可测函数。则
$$
\lVert fg\rVert_{1}=\int_{X}|fg|\,\mathrm{d}\mu\le\lVert f\rVert_{p}\,\lVert g\rVert_{q}
$$
（两端在 $[0,\infty]$ 中取值）。特别地，若 $f\in L^{p}$，$g\in L^{q}$，则 $fg\in L^{1}$ 且 $\bigl|\int_{X}fg\,\mathrm{d}\mu\bigr|\le\lVert f\rVert_{p}\lVert g\rVert_{q}$。

*证明.*　
情形 $p=1$，$q=\infty$：由引理 2.3，$|fg|\le\lVert g\rVert_{\infty}|f|$ a.e.（按约定 $0\cdot\infty=0$），积分即得。$p=\infty$ 的情形对称。

情形 $1<p<\infty$。若 $\lVert f\rVert_{p}=0$ 或 $\lVert g\rVert_{q}=0$，则由引理 2.4，$f=0$ a.e. 或 $g=0$ a.e.，于是 $fg=0$ a.e.，两端都是 $0$。若二者都不为 $0$ 而其中之一为 $\infty$，右端为 $\infty$，不等式平凡。以下设 $A=\lVert f\rVert_{p}$，$B=\lVert g\rVert_{q}$ 都属于 $(0,\infty)$。对每个 $x$，以 $a=|f(x)|/A$，$b=|g(x)|/B$ 应用 Young 不等式：
$$
\frac{|f(x)g(x)|}{AB}\le\frac{1}{p}\frac{|f(x)|^{p}}{A^{p}}+\frac{1}{q}\frac{|g(x)|^{q}}{B^{q}}.
$$
两边积分，右端等于 $\frac1p\cdot1+\frac1q\cdot1=1$，于是 $\lVert fg\rVert_{1}\le AB$。最后一个结论来自约定部分的 $\bigl|\int h\bigr|\le\int|h|$。 $\square$

**注 3.4**
证明的逻辑顺序是：先把 $f,g$ 按范数归一化，对归一化后的函数逐点应用 Young 不等式，再积分。归一化要求 $0<\lVert f\rVert_{p},\lVert g\rVert_{q}<\infty$，因此范数为 $0$ 或 $\infty$ 的情形必须单独处理。还应注意两个函数分别以指数 $p$ 与 $q$ 度量：右端是 $(\int|f|^{p})^{1/p}(\int|g|^{q})^{1/q}$，指数满足 $1\le p,q\le\infty$。

**推论 3.5**（Cauchy–Schwarz 不等式）
若 $f,g\in L^{2}(X,\mu)$，则 $\bigl|\int_{X}f\bar{g}\,\mathrm{d}\mu\bigr|\le\lVert f\rVert_{2}\lVert g\rVert_{2}$。因此 $\langle f,g\rangle=\int_{X}f\bar{g}\,\mathrm{d}\mu$ 是 $L^{2}$ 上的内积，且 $\langle f,f\rangle=\lVert f\rVert_{2}^{2}$。

这对任意测度空间都成立，不限于 $L^{2}(S^{1})$。结合第 4 节的完备性，$L^{2}(X,\mu)$ 是一个 Hilbert 空间。取计数测度即得离散形式：
$$
\sum_{n}|x_{n}y_{n}|\le\Bigl(\sum_{n}|x_{n}|^{p}\Bigr)^{1/p}\Bigl(\sum_{n}|y_{n}|^{q}\Bigr)^{1/q}.
$$

**推论 3.6**（广义 Hölder 不等式）
设 $0<p,q,r\le\infty$ 满足 $\frac1r=\frac1p+\frac1q$，$f,g$ 可测，则 $\lVert fg\rVert_{r}\le\lVert f\rVert_{p}\lVert g\rVert_{q}$。

*证明.*　
若 $r=\infty$，则 $p=q=\infty$，由引理 2.3，$|fg|\le\lVert f\rVert_{\infty}\lVert g\rVert_{\infty}$ a.e.。设 $r<\infty$。若 $p=\infty$，则 $q=r$，$|fg|^{r}\le\lVert f\rVert_{\infty}^{r}|g|^{r}$ a.e.，积分即得；$q=\infty$ 同理。若 $p,q<\infty$，则 $\frac{p}{r},\frac{q}{r}>1$ 且 $\frac{r}{p}+\frac{r}{q}=1$，对 $|f|^{r}$ 与 $|g|^{r}$ 以指数 $\frac pr,\frac qr$ 应用定理 3.3：
$$
\int|f|^{r}|g|^{r}\,\mathrm{d}\mu\le\Bigl(\int|f|^{p}\,\mathrm{d}\mu\Bigr)^{r/p}\Bigl(\int|g|^{q}\,\mathrm{d}\mu\Bigr)^{r/q},
$$
两边开 $r$ 次方即可。 $\square$

由归纳法，若 $\frac1r=\sum_{i=1}^{k}\frac{1}{p_{i}}$，则 $\lVert f_{1}\cdots f_{k}\rVert_{r}\le\prod_{i}\lVert f_{i}\rVert_{p_{i}}$。

### 3.3 Hölder 不等式的取等条件

**定理 3.7**

(i) 设 $1<p<\infty$，$f\in L^{p}$，$g\in L^{q}$。则 $\lVert fg\rVert_{1}=\lVert f\rVert_{p}\lVert g\rVert_{q}$ 当且仅当存在不全为零的常数 $\alpha,\beta\ge0$，使得 $\alpha|f|^{p}=\beta|g|^{q}$ a.e.。当 $\lVert f\rVert_{p},\lVert g\rVert_{q}>0$ 时，这等价于
$$
\frac{|f|^{p}}{\lVert f\rVert_{p}^{p}}=\frac{|g|^{q}}{\lVert g\rVert_{q}^{q}}\quad\text{a.e.}
$$

(ii) 设 $f\in L^{1}$，$g\in L^{\infty}$。则 $\lVert fg\rVert_{1}=\lVert f\rVert_{1}\lVert g\rVert_{\infty}$ 当且仅当在集合 $\{f\ne0\}$ 上几乎处处有 $|g|=\lVert g\rVert_{\infty}$。

*证明.*　
(i) 若 $\lVert f\rVert_{p}=0$，则等式两端都为 $0$，而 $\alpha=1,\beta=0$ 满足条件；反之，若条件对 $\beta=0$ 成立，则 $\alpha>0$，$f=0$ a.e.，等式成立。$\lVert g\rVert_{q}=0$ 或 $\alpha=0$ 的情形对称。以下设 $A=\lVert f\rVert_{p}>0$，$B=\lVert g\rVert_{q}>0$，令 $F=|f|/A$，$G=|g|/B$，
$$
H=\frac{F^{p}}{p}+\frac{G^{q}}{q}-FG .
$$
由 Young 不等式 $H\ge0$ a.e.，且由定理 3.3 的证明，$\int H\,\mathrm{d}\mu=1-\frac{\lVert fg\rVert_{1}}{AB}$。因此等式成立 $\iff\int H=0\iff H=0$ a.e.（第 II 篇）$\iff F^{p}=G^{q}$ a.e.（Young 不等式的取等条件），即 $|f|^{p}/A^{p}=|g|^{q}/B^{q}$ a.e.，这是 $\alpha=A^{-p}$，$\beta=B^{-q}$ 时的条件。反之，若 $\alpha|f|^{p}=\beta|g|^{q}$ a.e. 且 $\alpha,\beta$ 不全为零，由 $A,B>0$ 知 $\alpha,\beta$ 都必须为正（例如 $\alpha=0$ 将迫使 $g=0$ a.e.），积分得 $\alpha A^{p}=\beta B^{q}$，从而 $|f|^{p}/A^{p}=|g|^{q}/B^{q}$ a.e.。

(ii) 由 Hölder 不等式 $\lVert fg\rVert_{1}<\infty$，且
$$
\lVert f\rVert_{1}\lVert g\rVert_{\infty}-\lVert fg\rVert_{1}=\int_{X}|f|\bigl(\lVert g\rVert_{\infty}-|g|\bigr)\,\mathrm{d}\mu ,
$$
被积函数几乎处处非负（引理 2.3）。所以差为零当且仅当 $|f|(\lVert g\rVert_{\infty}-|g|)=0$ a.e.，即在 $\{f\ne0\}$ 上几乎处处 $|g|=\lVert g\rVert_{\infty}$。 $\square$

**例 3.8**
$p=1,q=\infty$ 时的取等条件有时被误述为“$f$ 与 $g$ 几乎处处有相同的支集”。这既不充分也不必要。在 $[0,1]$ 上取 $f\equiv1$，$g(x)=x$：$\{f\ne0\}$ 与 $\{g\ne0\}$ 只差零测集，但 $\lVert fg\rVert_{1}=\tfrac12<1=\lVert f\rVert_{1}\lVert g\rVert_{\infty}$。反之取 $f=\mathbf{1}_{[0,1/2]}$，$g\equiv1$：支集不同，但 $\lVert fg\rVert_{1}=\tfrac12=\lVert f\rVert_{1}\lVert g\rVert_{\infty}$。又在 $1<p<\infty$ 的情形，条件“存在 $\lambda\ge0$ 使 $|f|^{p}=\lambda|g|^{q}$”遗漏了 $g=0$、$f\ne0$ 的情形（此时等式 $0=0$ 平凡成立），这正是定理中需要两个不全为零的系数 $\alpha,\beta$ 的原因。

### 3.4 Minkowski 不等式

**定理 3.9**（Minkowski 不等式）
设 $1\le p\le\infty$，$f,g\in L^{p}(X,\mu)$。则 $f+g\in L^{p}$ 且
$$
\lVert f+g\rVert_{p}\le\lVert f\rVert_{p}+\lVert g\rVert_{p}.
$$
因此当 $1\le p\le\infty$ 时 $\lVert \cdot\rVert_{p}$ 是 $\mathcal{L}^{p}$ 上的半范数，$L^{p}(X,\mu)$ 是赋范空间。

*证明.*　
$p=1$：积分 $|f+g|\le|f|+|g|$ 即可。$p=\infty$：由引理 2.3，在一个零测集之外 $|f+g|\le|f|+|g|\le\lVert f\rVert_{\infty}+\lVert g\rVert_{\infty}$。

设 $1<p<\infty$。由命题 2.6，$f+g\in L^{p}$，即 $\lVert f+g\rVert_{p}<\infty$；若 $\lVert f+g\rVert_{p}=0$，结论平凡，故设 $0<\lVert f+g\rVert_{p}<\infty$。由于 $(p-1)q=p$，
$$
\bigl\||f+g|^{p-1}\bigr\|_{q}=\Bigl(\int|f+g|^{p}\,\mathrm{d}\mu\Bigr)^{1/q}=\lVert f+g\rVert_{p}^{p/q}=\lVert f+g\rVert_{p}^{p-1}<\infty .
$$
于是由 $|f+g|\le|f|+|g|$ 与 Hölder 不等式，
$$
\begin{aligned}
\lVert f+g\rVert_{p}^{p}&=\int|f+g|\,|f+g|^{p-1}\,\mathrm{d}\mu
\le\int|f|\,|f+g|^{p-1}\,\mathrm{d}\mu+\int|g|\,|f+g|^{p-1}\,\mathrm{d}\mu\\
&\le\bigl(\lVert f\rVert_{p}+\lVert g\rVert_{p}\bigr)\,\lVert f+g\rVert_{p}^{p-1}.
\end{aligned}
$$
两边除以 $\lVert f+g\rVert_{p}^{p-1}\in(0,\infty)$ 即得结论。 $\square$

**注 3.10**
证明中“先证 $\lVert f+g\rVert_{p}<\infty$”一步是必要的：若不知道 $\lVert f+g\rVert_{p}$ 有限，最后一步就是以 $\infty$ 作除数。上面的证明对一般测度空间成立，有限和与级数的情形只是计数测度下的特例。

**推论 3.11**（离散 Minkowski 不等式）
对 $1\le p<\infty$ 与 $\mathbb{K}$ 值序列（有限或无限）$(x_{k})$，$(y_{k})$，
$$
\Bigl(\sum_{k}|x_{k}+y_{k}|^{p}\Bigr)^{1/p}\le\Bigl(\sum_{k}|x_{k}|^{p}\Bigr)^{1/p}+\Bigl(\sum_{k}|y_{k}|^{p}\Bigr)^{1/p}.
$$
特别地，$(\mathbb{K}^{n},\lVert \cdot\rVert_{p})$ 与 $\ell^{p}$（$1\le p\le\infty$）都是赋范空间。

*证明.*　
对 $\{1,\dots,n\}$ 或 $\mathbb{N}$ 上的计数测度应用定理 3.9（例 2.9）；若右端为 $\infty$ 则无需证明。 $\square$

常见的“积分形式”的 Minkowski 不等式 $\bigl(\int_{a}^{b}|f+g|^{p}\bigr)^{1/p}\le\bigl(\int_{a}^{b}|f|^{p}\bigr)^{1/p}+\bigl(\int_{a}^{b}|g|^{p}\bigr)^{1/p}$ 就是 $X=[a,b]$ 时的定理 3.9，只需 $f,g\in L^{p}[a,b]$，$1\le p<\infty$。

**定理 3.12**（Minkowski 不等式的取等条件）
设 $1<p<\infty$，$f,g\in L^{p}$。则 $\lVert f+g\rVert_{p}=\lVert f\rVert_{p}+\lVert g\rVert_{p}$ 当且仅当存在 $\lambda\ge0$，使得 $f=\lambda g$ a.e. 或 $g=\lambda f$ a.e.。

*证明.*　
充分性：若 $g=\lambda f$，则 $\lVert f+g\rVert_{p}=(1+\lambda)\lVert f\rVert_{p}=\lVert f\rVert_{p}+\lVert g\rVert_{p}$。

必要性：若 $f=0$ a.e.，则 $f=0\cdot g$；$g=0$ 同理。设 $\lVert f\rVert_{p},\lVert g\rVert_{p}>0$，于是 $\lVert f+g\rVert_{p}=\lVert f\rVert_{p}+\lVert g\rVert_{p}>0$。记 $h=|f+g|^{p-1}$，则 $\lVert h\rVert_{q}=\lVert f+g\rVert_{p}^{p-1}>0$。在定理 3.9 的证明中，
$$
\lVert f+g\rVert_{p}^{p}\le\int(|f|+|g|)h\,\mathrm{d}\mu\le\bigl(\lVert f\rVert_{p}+\lVert g\rVert_{p}\bigr)\lVert h\rVert_{q}=\lVert f+g\rVert_{p}^{p},
$$
所以两处不等号都是等号。

第一处取等给出 $\int(|f|+|g|-|f+g|)h\,\mathrm{d}\mu=0$，被积函数非负，故在 $S=\{f+g\ne0\}$ 上几乎处处 $|f+g|=|f|+|g|$。第二处是两个 Hölder 不等式 $\int|f|h\le\lVert f\rVert_{p}\lVert h\rVert_{q}$ 与 $\int|g|h\le\lVert g\rVert_{p}\lVert h\rVert_{q}$ 之和，所以两者都取等。由定理 3.7(i)，
$$
\frac{|f|^{p}}{\lVert f\rVert_{p}^{p}}=\frac{h^{q}}{\lVert h\rVert_{q}^{q}}=\frac{|f+g|^{p}}{\lVert f+g\rVert_{p}^{p}}\quad\text{a.e.},
$$
即 $|f|=s|f+g|$ a.e.，其中 $s=\lVert f\rVert_{p}/\lVert f+g\rVert_{p}>0$；同理 $|g|=t|f+g|$ a.e.，$t=\lVert g\rVert_{p}/\lVert f+g\rVert_{p}>0$。特别地，在 $X\setminus S$ 上 $f=g=0$ a.e.。

在 $S$ 上，对复数 $z=f(x)$，$w=g(x)$，由 $|z+w|^{2}=|z|^{2}+|w|^{2}+2\operatorname{Re}(z\bar w)$，条件 $|z+w|=|z|+|w|$ 等价于 $z\bar w=|z||w|\ge0$，即 $z,w$ 中一个是另一个的非负倍数；由此 $z=\frac{|z|}{|z+w|}(z+w)$。因此在 $S$ 上几乎处处 $f=s(f+g)$，$g=t(f+g)$，而这两式在 $X\setminus S$ 上也几乎处处成立。于是 $tf=st(f+g)=sg$ a.e.，即 $f=\frac{s}{t}g$ a.e.。 $\square$

**注 3.13**
$p=1$ 时，$\lVert f+g\rVert_{1}=\lVert f\rVert_{1}+\lVert g\rVert_{1}$ 当且仅当 $|f+g|=|f|+|g|$ a.e.，即 $f\bar g\ge0$ a.e.；这不要求 $f,g$ 成比例，例如任意两个非负函数都取等。$p=\infty$ 时也没有比例刻画：$f=\mathbf{1}_{[0,1]}$，$g=\mathbf{1}_{[0,2]}$ 满足 $\lVert f+g\rVert_{\infty}=2=\lVert f\rVert_{\infty}+\lVert g\rVert_{\infty}$。

### 3.5 $0<p<1$ 的情形

**命题 3.14**（反向 Minkowski 不等式）
设 $0<p<1$，$f,g$ 是非负可测函数，则 $\lVert f+g\rVert_{p}\ge\lVert f\rVert_{p}+\lVert g\rVert_{p}$。

*证明.*　
由于 $f+g\ge f$，$f+g\ge g$，若 $\lVert f\rVert_{p}$ 或 $\lVert g\rVert_{p}$ 为 $\infty$，左端也为 $\infty$；若其中之一为 $0$，结论也显然。设 $a=\lVert f\rVert_{p}$，$b=\lVert g\rVert_{p}$ 属于 $(0,\infty)$，令 $u=f/a$，$v=g/b$，$\lambda=\frac{a}{a+b}$，则
$$
f+g=(a+b)\bigl(\lambda u+(1-\lambda)v\bigr).
$$
函数 $t\mapsto t^{p}$ 在 $[0,\infty)$ 上是凹的，故 $(\lambda u+(1-\lambda)v)^{p}\ge\lambda u^{p}+(1-\lambda)v^{p}$。积分并利用 $\int u^{p}=\int v^{p}=1$，得 $\int(f+g)^{p}\,\mathrm{d}\mu\ge(a+b)^{p}$。 $\square$

**例 3.15**
若 $X$ 中存在不交的可测集 $A,B$，$0<\mu(A),\mu(B)<\infty$，则对 $0<p<1$，
$$
\lVert \mathbf{1}_{A}+\mathbf{1}_{B}\rVert_{p}=\bigl(\mu(A)+\mu(B)\bigr)^{1/p}>\mu(A)^{1/p}+\mu(B)^{1/p}=\lVert \mathbf{1}_{A}\rVert_{p}+\lVert \mathbf{1}_{B}\rVert_{p},
$$
严格不等号来自 $r=\frac1p>1$ 时 $(s+t)^{r}>s^{r}+t^{r}$（$s,t>0$）。所以此时 $\lVert \cdot\rVert_{p}$ 不是半范数。

**注 3.16**
需要注意：反向不等式只对*非负*函数且 $0<p<1$ 成立（对一般函数，取 $g=-f$ 即得反例）；$p=1$ 时是通常的三角不等式；$p=0$ 时公式本身没有意义。另一方面，由命题 2.6，对 $0<p<1$，
$$
d_{p}(f,g)=\int_{X}|f-g|^{p}\,\mathrm{d}\mu
$$
满足三角不等式，是 $L^{p}$ 上的平移不变度量，并且用与定理 4.1 相同的方法可以证明 $(L^{p},d_{p})$ 是完备的。但一般而言 $L^{p}$（$0<p<1$）不能赋范；例如可以证明 $L^{p}[0,1]$ 上唯一的连续线性泛函是零泛函。本篇以下主要讨论 $1\le p\le\infty$。

### 3.6 平行四边形法则

**命题 3.17**
设 $X$ 中存在不交的可测集 $A,B$，$0<\mu(A),\mu(B)<\infty$，$1\le p\le\infty$。则 $L^{p}(X,\mu)$ 的范数满足平行四边形法则
$$
\lVert f+g\rVert_{p}^{2}+\lVert f-g\rVert_{p}^{2}=2\lVert f\rVert_{p}^{2}+2\lVert g\rVert_{p}^{2}\qquad(\forall f,g\in L^{p})
$$
当且仅当 $p=2$。

*证明.*　
$p=2$ 时，展开 $\lVert f\pm g\rVert_{2}^{2}=\lVert f\rVert_{2}^{2}\pm2\operatorname{Re}\langle f,g\rangle+\lVert g\rVert_{2}^{2}$ 相加即得。设 $p\ne2$。$p<\infty$ 时取 $f=\mu(A)^{-1/p}\mathbf{1}_{A}$，$g=\mu(B)^{-1/p}\mathbf{1}_{B}$；$p=\infty$ 时取 $f=\mathbf{1}_{A}$，$g=\mathbf{1}_{B}$。则 $\lVert f\rVert_{p}=\lVert g\rVert_{p}=1$，右端为 $4$。由于 $A,B$ 不交，$|f\pm g|^{p}=|f|^{p}+|g|^{p}$，故 $p<\infty$ 时 $\lVert f\pm g\rVert_{p}=2^{1/p}$，左端为 $2\cdot2^{2/p}\ne4$；$p=\infty$ 时 $\lVert f\pm g\rVert_{\infty}=1$，左端为 $2\ne4$。 $\square$

由 Jordan–von Neumann 定理（范数由内积诱导当且仅当满足平行四边形法则），在上述条件下，$L^{p}$ 空间中只有 $L^{2}$ 的范数来自内积。

## 4. 完备性：Riesz–Fischer 定理

**定理 4.1**（Riesz–Fischer）
设 $1\le p<\infty$，则 $L^{p}(X,\mu)$ 是 Banach 空间。

*证明.*　
由定理 1.5，只需证明 $L^{p}$ 中绝对收敛的级数收敛。设 $f_{k}\in L^{p}$，$\sum_{k=1}^{\infty}\lVert f_{k}\rVert_{p}=S<\infty$。令
$$
G_{n}=\sum_{k=1}^{n}|f_{k}|,\qquad G=\sum_{k=1}^{\infty}|f_{k}|:X\to[0,\infty].
$$
由 Minkowski 不等式，$\lVert G_{n}\rVert_{p}\le\sum_{k=1}^{n}\lVert f_{k}\rVert_{p}\le S$。由于 $G_{n}^{p}\uparrow G^{p}$，单调收敛定理给出
$$
\int_{X}G^{p}\,\mathrm{d}\mu=\lim_{n\to\infty}\int_{X}G_{n}^{p}\,\mathrm{d}\mu\le S^{p}<\infty .
$$
因此 $G<\infty$ a.e.：令 $E=\{G<\infty\}$，则 $\mu(X\setminus E)=0$。对 $x\in E$，数项级数 $\sum_{k}f_{k}(x)$ 绝对收敛，由 $\mathbb{K}$ 的完备性收敛。令
$$
F(x)=\begin{cases}\sum_{k=1}^{\infty}f_{k}(x),&x\in E,\\ 0,&x\notin E.\end{cases}
$$
$F$ 是可测函数 $\mathbf{1}_{E}\sum_{k\le n}f_{k}$ 的逐点极限，故可测；又 $|F|\le G$，所以 $F\in L^{p}$。最后，记 $S_{n}=\sum_{k=1}^{n}f_{k}$，则在 $E$ 上
$$
|F-S_{n}|=\Bigl|\sum_{k>n}f_{k}\Bigr|\le\sum_{k>n}|f_{k}|\le G,\qquad |F-S_{n}|\to0 .
$$
于是 $|F-S_{n}|^{p}\to0$ a.e. 且 $|F-S_{n}|^{p}\le G^{p}\in L^{1}$，由控制收敛定理 $\lVert F-S_{n}\rVert_{p}\to0$。所以级数 $\sum f_{k}$ 在 $L^{p}$ 中收敛到 $F$。 $\square$

**注 4.2**
证明中有两个步骤不可省略，并且不应混淆几乎处处收敛与 $L^{p}$ 收敛：(a) 用 Minkowski 不等式与单调收敛定理证明 $G=\sum|f_{k}|\in L^{p}$，从而级数几乎处处绝对收敛，极限函数才有定义；(b) 用控制收敛定理把几乎处处收敛提升为 $L^{p}$ 收敛。从 Cauchy 列出发的写法中，还需要“有收敛子列的 Cauchy 列收敛”这一步，它已包含在定理 1.5 的证明中。

**推论 4.3**
$\ell^{p}$（$1\le p<\infty$）是 Banach 空间；对任意测度空间，$L^{2}(X,\mu)$ 是 Hilbert 空间。

证明中的函数 $G$ 还给出以下有用的结论。

**定理 4.4**（几乎处处收敛的子列）
设 $1\le p<\infty$，$f_{n}\to f$ 于 $L^{p}$。则存在子列 $(f_{n_{k}})$ 与 $h\in L^{p}$，使得 $f_{n_{k}}\to f$ a.e.，并且对一切 $k$ 有 $|f_{n_{k}}|\le h$ a.e.。

*证明.*　
选取 $n_{1}<n_{2}<\cdots$ 使 $\lVert f_{n_{k}}-f\rVert_{p}\le2^{-k}$。令 $G=\sum_{k}|f_{n_{k}}-f|$。与定理 4.1 的证明相同，$\lVert G\rVert_{p}\le\sum_{k}2^{-k}=1$，于是 $G<\infty$ a.e.，从而收敛级数的通项 $|f_{n_{k}}-f|\to0$ a.e.。又 $|f_{n_{k}}|\le|f|+G=:h\in L^{p}$。 $\square$

下面两个例子说明，在有限测度空间上 $L^{p}$ 收敛与几乎处处收敛互不蕴含，因此定理 4.4 中取子列是必要的。

**例 4.5**（打字机序列）
在 $[0,1]$ 上，对 $n=2^{j}+i$（$j\ge0$，$0\le i<2^{j}$）令 $f_{n}=\mathbf{1}_{[i2^{-j},(i+1)2^{-j}]}$。则 $\lVert f_{n}\rVert_{p}^{p}=2^{-j}\to0$，即对每个 $1\le p<\infty$，$f_{n}\to0$ 于 $L^{p}$。但对每个 $x\in[0,1]$，第 $j$ 代的 $2^{j}$ 个区间覆盖 $[0,1]$，所以 $f_{n}(x)=1$ 对无穷多个 $n$ 成立；而当 $j\ge2$ 时 $x$ 至多属于第 $j$ 代中的两个区间，所以 $f_{n}(x)=0$ 也对无穷多个 $n$ 成立。因此 $(f_{n}(x))$ 在每一点都发散。另一方面，子列 $f_{2^{j}}=\mathbf{1}_{[0,2^{-j}]}$ 在 $(0,1]$ 上趋于 $0$，与定理 4.4 一致。

**例 4.6**
在 $[0,1]$ 上令 $g_{n}=n^{1/p}\mathbf{1}_{(0,1/n)}$。则 $g_{n}\to0$ 处处成立，但 $\lVert g_{n}\rVert_{p}=1$，$g_{n}$ 不在 $L^{p}$ 中收敛到 $0$。

几乎处处收敛加上一个 $L^{p}$ 控制函数可以推出 $L^{p}$ 收敛（控制收敛定理）；几乎处处（或依测度）收敛何时能提升为 $L^{1}$ 收敛的确切刻画是 Vitali 收敛定理，其关键条件是一致可积性，见补充篇《一致可积性与 $L^{1}$ 收敛》。下面是另一个常用的充分条件。

**命题 4.7**
设 $1\le p<\infty$，$f_{n},f\in L^{p}$，$f_{n}\to f$ a.e.，且 $\lVert f_{n}\rVert_{p}\to\lVert f\rVert_{p}$。则 $\lVert f_{n}-f\rVert_{p}\to0$。

*证明.*　
由命题 2.6，$\Phi_{n}=2^{p-1}(|f_{n}|^{p}+|f|^{p})-|f_{n}-f|^{p}\ge0$，且 $\Phi_{n}\to2^{p}|f|^{p}$ a.e.。由 Fatou 引理，
$$
2^{p}\int|f|^{p}\le\liminf_{n\to\infty}\int\Phi_{n}=2^{p}\int|f|^{p}-\limsup_{n\to\infty}\int|f_{n}-f|^{p},
$$
这里用到了 $\int|f_{n}|^{p}\to\int|f|^{p}$。由于 $\int|f|^{p}<\infty$，得 $\limsup\int|f_{n}-f|^{p}\le0$。 $\square$

## 5. $L^{\infty}$ 空间

### 5.1 本质上确界的性质

**命题 5.1**
设 $U\subseteq\mathbb{R}^{n}$ 为开集，$f:U\to\mathbb{K}$ 连续。则 $\lVert f\rVert_{L^{\infty}(U)}=\sup_{U}|f|$。

*证明.*　
“$\le$”显然。设 $t<\sup_{U}|f|$，则 $\{x\in U:|f(x)|>t\}$ 是非空开集，包含某个开球，因而测度为正；于是任何 $M\le t$ 都不是 $|f|$ 的几乎处处上界，$\lVert f\rVert_{\infty}\ge t$。 $\square$

特别地，连续函数若几乎处处相等则处处相等，所以 $f\mapsto[f]$ 把 $(C[a,b],\lVert \cdot\rVert_{u})$ 等距地嵌入 $L^{\infty}[a,b]$（对 $(a,b)$ 应用上述命题，并注意 $\sup_{(a,b)}|f|=\max_{[a,b]}|f|$）。

### 5.2 完备性

**定理 5.2**

(i) $f_{n}\to f$ 于 $L^{\infty}$，当且仅当存在零测集 $N$，使得 $f_{n}\to f$ 在 $X\setminus N$ 上一致收敛。

(ii) $L^{\infty}(X,\mu)$ 是 Banach 空间。

*证明.*　
(i) 若 $\lVert f_{n}-f\rVert_{\infty}\to0$，令 $N=\bigcup_{n}\{|f_{n}-f|>\lVert f_{n}-f\rVert_{\infty}\}$，由引理 2.3 它是可数个零测集之并，从而是零测集；在 $X\setminus N$ 上 $\sup|f_{n}-f|\le\lVert f_{n}-f\rVert_{\infty}\to0$。反之，若 $f_{n}\to f$ 在 $X\setminus N$ 上一致收敛，则 $\lVert f_{n}-f\rVert_{\infty}\le\sup_{X\setminus N}|f_{n}-f|\to0$。

(ii) 设 $(f_{n})$ 是 $L^{\infty}$ 中的 Cauchy 列。令
$$
N=\bigcup_{m,n}\bigl\{|f_{m}-f_{n}|>\lVert f_{m}-f_{n}\rVert_{\infty}\bigr\}\ \cup\ \bigcup_{n}\bigl\{|f_{n}|>\lVert f_{n}\rVert_{\infty}\bigr\},
$$
这是可数个零测集之并，$\mu(N)=0$。在 $X\setminus N$ 上 $\sup|f_{m}-f_{n}|\le\lVert f_{m}-f_{n}\rVert_{\infty}$，所以 $(f_{n})$ 在 $X\setminus N$ 上一致 Cauchy。令 $f=\lim f_{n}$ 于 $X\setminus N$，$f=0$ 于 $N$，则 $f$ 可测。给定 $\varepsilon>0$，取 $N_{\varepsilon}$ 使 $m,n\ge N_{\varepsilon}$ 时 $\lVert f_{m}-f_{n}\rVert_{\infty}<\varepsilon$，令 $m\to\infty$ 得 $n\ge N_{\varepsilon}$ 时 $\sup_{X\setminus N}|f_{n}-f|\le\varepsilon$。于是 $|f|\le\lVert f_{N_{\varepsilon}}\rVert_{\infty}+\varepsilon$ 于 $X\setminus N$，$f\in L^{\infty}$，并且 $\lVert f_{n}-f\rVert_{\infty}\le\varepsilon$。 $\square$

**注 5.3**
证明的关键在于：每个不等式 $|f_{m}-f_{n}|\le\lVert f_{m}-f_{n}\rVert_{\infty}$ 只在一个零测集之外成立，而指标 $(m,n)$ 只有可数个，因此可以把所有例外集合并成一个零测集 $N$，在其补集上得到真正的一致收敛。这里可数性是本质的。

由此 $\ell^{\infty}$ 是 Banach 空间。结合定理 4.1，对一切 $1\le p\le\infty$，$L^{p}(X,\mu)$ 都是 Banach 空间。

### 5.3 $\lVert f\rVert_{p}$ 当 $p\to\infty$ 时的极限

**定理 5.4**
设存在 $0<r<\infty$ 使 $f\in L^{r}$。则 $\lim_{p\to\infty}\lVert f\rVert_{p}=\lVert f\rVert_{\infty}$（在 $[0,\infty]$ 中）。

*证明.*　
若 $f=0$ a.e.，结论平凡。设 $\lVert f\rVert_{\infty}>0$。

下界：取 $0<t<\lVert f\rVert_{\infty}$，令 $A_{t}=\{|f|>t\}$。由本质上确界的定义 $\mu(A_{t})>0$；由 Chebyshev 不等式 $\mu(A_{t})\le t^{-r}\lVert f\rVert_{r}^{r}<\infty$。于是
$$
\lVert f\rVert_{p}\ge\Bigl(\int_{A_{t}}t^{p}\,\mathrm{d}\mu\Bigr)^{1/p}=t\,\mu(A_{t})^{1/p}\xrightarrow[p\to\infty]{}t,
$$
故 $\liminf_{p\to\infty}\lVert f\rVert_{p}\ge t$；令 $t\uparrow\lVert f\rVert_{\infty}$ 得 $\liminf\lVert f\rVert_{p}\ge\lVert f\rVert_{\infty}$。

上界：若 $\lVert f\rVert_{\infty}=\infty$，已完成。否则对 $p>r$，$|f|^{p}=|f|^{p-r}|f|^{r}\le\lVert f\rVert_{\infty}^{p-r}|f|^{r}$ a.e.，故
$$
\lVert f\rVert_{p}\le\lVert f\rVert_{\infty}^{1-r/p}\,\lVert f\rVert_{r}^{r/p}\xrightarrow[p\to\infty]{}\lVert f\rVert_{\infty},
$$
这里用到了 $0<\lVert f\rVert_{r}<\infty$。 $\square$

若 $\mu(X)<\infty$，则 $L^{\infty}\subseteq L^{r}$（定理 6.1），上述定理适用于每个 $f\in L^{\infty}$。一般情形下假设 $f\in L^{r}$ 不能去掉：$f\equiv1$ 在 $\mathbb{R}$ 上满足 $\lVert f\rVert_{p}=\infty$（$p<\infty$），而 $\lVert f\rVert_{\infty}=1$。

### 5.4 不可分性

称度量空间是**可分的**，如果它有可数稠密子集。

**命题 5.5**
$L^{\infty}[0,1]$ 与 $\ell^{\infty}$ 都不可分。

*证明.*　
对 $t\in(0,1]$ 令 $f_{t}=\mathbf{1}_{[0,t]}$。若 $s<t$，则 $|f_{s}-f_{t}|=1$ 于正测集 $(s,t]$ 上，故 $\lVert f_{s}-f_{t}\rVert_{\infty}=1$。于是开球 $B(f_{t},\frac12)$（$t\in(0,1]$）两两不交，共有不可数个；任何稠密子集都必须与每个球相交，所以不可数。对 $\ell^{\infty}$，考虑子集 $A\subseteq\mathbb{N}$ 的示性序列 $\mathbf{1}_{A}$，它们有不可数个，且两两距离为 $1$。 $\square$

## 6. $L^{p}$ 空间之间的包含关系

### 6.1 有限测度空间

**定理 6.1**
设 $\mu(X)<\infty$，$0<p<q\le\infty$。则 $L^{q}(X,\mu)\subseteq L^{p}(X,\mu)$，并且
$$
\lVert f\rVert_{p}\le\mu(X)^{\frac1p-\frac1q}\lVert f\rVert_{q}.
$$
特别地，当 $1\le p<q\le\infty$ 时，包含映射 $L^{q}\hookrightarrow L^{p}$ 是有界线性映射，其算子范数等于 $\mu(X)^{1/p-1/q}$（在常数函数处取到）。

*证明.*　
$q=\infty$：$\int|f|^{p}\le\lVert f\rVert_{\infty}^{p}\mu(X)$。$q<\infty$：对 $|f|^{p}$ 与 $1$ 以指数 $r=\frac qp>1$ 及其共轭指数 $r'=\frac{q}{q-p}$ 应用 Hölder 不等式：
$$
\int|f|^{p}\cdot1\,\mathrm{d}\mu\le\Bigl(\int|f|^{q}\,\mathrm{d}\mu\Bigr)^{p/q}\mu(X)^{1-p/q}.
$$
两边开 $p$ 次方即可。对常数函数 $f\equiv1$，$\lVert 1\rVert_{p}=\mu(X)^{1/p}$，两边相等。 $\square$

在概率空间（$\mu(X)=1$）上，$\lVert f\rVert_{p}$ 关于 $p$ 单调不减，$L^{\infty}\subseteq L^{q}\subseteq L^{p}\subseteq L^{1}$（$1\le p<q\le\infty$）。

**注 6.2**（关于闭图像定理）
包含映射的连续性也可以用闭图像定理得到。闭图像定理的表述是：设 $V,W$ 是 Banach 空间，$T:V\to W$ 是定义在*整个* $V$ 上的线性映射；若 $T$ 的图像 $\{(x,Tx):x\in V\}$ 在 $V\times W$ 中是闭的，则 $T$ 有界。论证如下：若已知 $L^{q}\subseteq L^{p}$（$1\le p,q\le\infty$），设 $f_{n}\to f$ 于 $L^{q}$ 且 $f_{n}\to g$ 于 $L^{p}$，由定理 4.4（$p$ 或 $q$ 为 $\infty$ 时由定理 5.2）先取子列使其几乎处处收敛到 $f$，再从中取子列几乎处处收敛到 $g$，得 $f=g$ a.e.，所以图像是闭的，包含映射有界。但这一论证预设了包含关系本身；而包含关系在一般测度空间中并不成立（例 6.3）。在 $\mu(X)<\infty$ 时，Hölder 不等式直接给出了显式常数，无需闭图像定理。

### 6.2 一般情形不存在包含关系

**例 6.3**
定理 6.1 中的有限测度假设不可去掉。在 $(\mathbb{R},m)$ 上，设 $0<p<q<\infty$，由例 2.10：
$$
x^{-1/p}\mathbf{1}_{(1,\infty)}\in L^{q}\setminus L^{p},\qquad x^{-1/q}\mathbf{1}_{(0,1)}\in L^{p}\setminus L^{q}.
$$
（前者：$\frac{q}{p}>1$ 而 $\frac pp=1$；后者：$\frac pq<1$ 而 $\frac qq=1$。）又 $1\in L^{\infty}(\mathbb{R})\setminus L^{p}(\mathbb{R})$，$x^{-1/(2p)}\mathbf{1}_{(0,1)}\in L^{p}(\mathbb{R})\setminus L^{\infty}(\mathbb{R})$。所以在 $\mathbb{R}$ 上任意两个不同指数的 $L^{p}$ 空间互不包含。

### 6.3 序列空间：包含关系反向

**定理 6.4**
设 $0<p<q\le\infty$。则 $\ell^{p}\subseteq\ell^{q}$，且 $\lVert x\rVert_{q}\le\lVert x\rVert_{p}$。包含是严格的。

*证明.*　
$q=\infty$：对每个 $n$，$|x_{n}|^{p}\le\sum_{k}|x_{k}|^{p}$。设 $q<\infty$，$x\ne0$。由齐次性不妨设 $\lVert x\rVert_{p}=1$，则 $|x_{n}|\le1$，从而 $|x_{n}|^{q}\le|x_{n}|^{p}$，求和得 $\lVert x\rVert_{q}^{q}\le1$。严格性：$x_{n}=n^{-1/p}$ 满足 $\sum n^{-q/p}<\infty$ 而 $\sum n^{-1}=\infty$，所以 $x\in\ell^{q}\setminus\ell^{p}$。 $\square$

比较例 2.10：有限测度排除了“在无穷远处太大”的现象，从而小指数的空间更大；计数测度下每个非空集合的测度至少为 $1$，排除了“局部奇性”，从而大指数的空间更大。在 $\mathbb{R}$ 上两种现象同时存在，于是没有任何包含关系。

### 6.4 插值不等式

**定理 6.5**（插值不等式）
设 $0<p<r<q\le\infty$，$\theta\in(0,1)$ 由
$$
\frac1r=\frac{\theta}{p}+\frac{1-\theta}{q}
$$
确定。则对 $f\in L^{p}\cap L^{q}$，
$$
\lVert f\rVert_{r}\le\lVert f\rVert_{p}^{\theta}\,\lVert f\rVert_{q}^{1-\theta}.
$$
特别地，$L^{p}\cap L^{q}\subseteq L^{r}$。

*证明.*　
$q=\infty$ 时 $\theta=\frac pr$，且 $|f|^{r}=|f|^{p}|f|^{r-p}\le\lVert f\rVert_{\infty}^{r-p}|f|^{p}$ a.e.，积分并开 $r$ 次方得 $\lVert f\rVert_{r}\le\lVert f\rVert_{p}^{p/r}\lVert f\rVert_{\infty}^{1-p/r}$。设 $q<\infty$。把 $|f|$ 写成 $|f|^{\theta}\cdot|f|^{1-\theta}$，对指数 $\frac{p}{\theta}$、$\frac{q}{1-\theta}$ 应用广义 Hölder 不等式（推论 3.6，条件 $\frac1r=\frac{\theta}{p}+\frac{1-\theta}{q}$ 恰好满足）：
$$
\lVert f\rVert_{r}\le\bigl\||f|^{\theta}\bigr\|_{p/\theta}\,\bigl\||f|^{1-\theta}\bigr\|_{q/(1-\theta)}=\lVert f\rVert_{p}^{\theta}\,\lVert f\rVert_{q}^{1-\theta}. 
$$

$\square$

**注 6.6**
插值不等式等价于说：函数 $\frac1p\mapsto\log\lVert f\rVert_{p}$ 在它取有限值的区间上是凸函数。对线性算子的类似结论是 Riesz–Thorin 插值定理，这里不展开。

**推论 6.7**
设 $0<p<r<q\le\infty$。则 $L^{r}\subseteq L^{p}+L^{q}$，即每个 $f\in L^{r}$ 可以写成 $f=g+h$，其中 $g\in L^{p}$，$h\in L^{q}$。

*证明.*　
令 $g=f\mathbf{1}_{\{|f|>1\}}$，$h=f\mathbf{1}_{\{|f|\le1\}}$。在 $\{|f|>1\}$ 上 $|f|^{p}\le|f|^{r}$，故 $g\in L^{p}$。若 $q=\infty$，则 $|h|\le1$；若 $q<\infty$，则在 $\{|f|\le1\}$ 上 $|f|^{q}\le|f|^{r}$，故 $h\in L^{q}$。 $\square$

直观上，$f$ 的“高峰”部分属于小指数空间，“低平”部分属于大指数空间。

## 7. 稠密子集与可分性

### 7.1 简单函数

回忆第 II 篇的逼近定理：对非负可测函数 $f:X\to[0,\infty]$，存在简单函数列 $0\le\varphi_{1}\le\varphi_{2}\le\cdots$ 逐点收敛到 $f$，并且在 $f$ 有界的任何集合上一致收敛。对 $\mathbb{K}$ 值可测函数 $f=u+iv$，分别对 $u^{\pm},v^{\pm}$ 应用此定理，得到简单函数 $\varphi_{n}=(a_{n}-b_{n})+i(c_{n}-d_{n})$，其中 $0\le a_{n}\uparrow u^{+}$ 等。由于 $a_{n}$ 与 $b_{n}$ 的支集不交，$|a_{n}-b_{n}|=a_{n}+b_{n}\le|u|$，同理 $|c_{n}-d_{n}|\le|v|$，故
$$
|\varphi_{n}|\le|f|,\qquad \varphi_{n}\to f\ \text{逐点},
$$
且在 $f$ 有界的集合上一致收敛。

**定理 7.1**

(i) 设 $1\le p<\infty$。形如 $\sum_{i=1}^{N}a_{i}\mathbf{1}_{E_{i}}$（$a_{i}\in\mathbb{K}$，$\mu(E_{i})<\infty$）的简单函数全体在 $L^{p}(X,\mu)$ 中稠密。

(ii) 简单函数全体在 $L^{\infty}(X,\mu)$ 中稠密。

*证明.*　
(i) 设 $f\in L^{p}$，取上述 $\varphi_{n}$。若 $\varphi_{n}$ 在集合 $E$ 上取非零值 $a$，则 $|f|\ge|a|$ 于 $E$，由 Chebyshev 不等式 $\mu(E)\le|a|^{-p}\lVert f\rVert_{p}^{p}<\infty$，所以 $\varphi_{n}$ 属于所述的类。又 $|f-\varphi_{n}|^{p}\le(2|f|)^{p}\in L^{1}$，且 $|f-\varphi_{n}|^{p}\to0$ 逐点，由控制收敛定理 $\lVert f-\varphi_{n}\rVert_{p}\to0$。

(ii) 设 $f\in L^{\infty}$。在零测集 $\{|f|>\lVert f\rVert_{\infty}\}$ 上把 $f$ 改为 $0$，得到处处有界的代表元；此时 $\varphi_{n}\to f$ 在 $X$ 上一致收敛，故 $\lVert f-\varphi_{n}\rVert_{\infty}\le\sup_{X}|f-\varphi_{n}|\to0$。 $\square$

**注 7.2**
在 (i) 中“$\mu(E_{i})<\infty$”是自动的：$L^{p}$（$p<\infty$）中的简单函数在每个非零取值的集合上测度有限。在 (ii) 中不能要求 $\mu(E_{i})<\infty$：若 $\mu(X)=\infty$，任何这样的简单函数 $\varphi$ 在一个无穷测度集上为零，于是 $\lVert 1-\varphi\rVert_{\infty}\ge1$。

### 7.2 $\mathbb{R}^{n}$ 上的连续紧支函数

以 $C_{c}(\mathbb{R}^{n})$ 记 $\mathbb{R}^{n}$ 上支集 $\operatorname{supp} f=\overline{\{f\ne0\}}$ 为紧集的 $\mathbb{K}$ 值连续函数全体。这样的函数有界且在一个有限测度集之外为零，因此 $C_{c}(\mathbb{R}^{n})\subseteq L^{p}(\mathbb{R}^{n})$ 对一切 $0<p\le\infty$ 成立。

**引理 7.3**（$\mathbb{R}^{n}$ 中的 Urysohn 引理）
设 $K\subseteq U\subseteq\mathbb{R}^{n}$，$K$ 紧，$U$ 开。则存在 $g\in C_{c}(\mathbb{R}^{n})$，$0\le g\le1$，$g=1$ 于 $K$，且 $\operatorname{supp} g\subseteq U$。

*证明.*　
若 $U=\mathbb{R}^{n}$，令 $\delta=1$；否则令 $\delta=\inf_{x\in K}d(x,U^{c})$。函数 $x\mapsto d(x,U^{c})$ 连续且在 $K$ 上为正，在紧集 $K$ 上取到最小值，所以 $\delta>0$（$K=\varnothing$ 时取 $g=0$）。令
$$
g(x)=\max\Bigl(0,\ 1-\frac{2\,d(x,K)}{\delta}\Bigr).
$$
$d(\cdot,K)$ 是 $1$-Lipschitz 的，故 $g$ 连续，$0\le g\le1$，$g=1$ 于 $K$。$\operatorname{supp} g\subseteq\{x:d(x,K)\le\delta/2\}$，后者是有界闭集，因而是紧集；并且其中的点到 $K$ 的距离小于 $\delta$，不可能属于 $U^{c}$，所以它包含于 $U$。 $\square$

**定理 7.4**
设 $1\le p<\infty$。则 $C_{c}(\mathbb{R}^{n})$ 在 $L^{p}(\mathbb{R}^{n})$ 中稠密。

*证明.*　
由定理 7.1(i) 与 Minkowski 不等式，只需证明：对每个满足 $m(E)<\infty$ 的可测集 $E$ 与 $\varepsilon>0$，存在 $g\in C_{c}(\mathbb{R}^{n})$ 使 $\lVert \mathbf{1}_{E}-g\rVert_{p}<\varepsilon$。（若 $\lVert \mathbf{1}_{E_{i}}-g_{i}\rVert_{p}<\varepsilon$，则 $\lVert \sum a_{i}\mathbf{1}_{E_{i}}-\sum a_{i}g_{i}\rVert_{p}<\varepsilon\sum|a_{i}|$。）由 Lebesgue 测度的正则性（第 I 篇），存在紧集 $K$ 与开集 $U$，$K\subseteq E\subseteq U$，$m(U\setminus K)<\varepsilon^{p}$。取引理 7.3 中的 $g$，则 $\mathbf{1}_{K}\le g\le\mathbf{1}_{U}$，从而 $|g-\mathbf{1}_{E}|\le\mathbf{1}_{U\setminus K}$：在 $K$ 上两者都为 $1$，在 $U$ 外两者都为 $0$，在 $U\setminus K$ 上两者都在 $[0,1]$ 中。于是
$$
\lVert g-\mathbf{1}_{E}\rVert_{p}\le m(U\setminus K)^{1/p}<\varepsilon. 
$$

$\square$

**注 7.5**

(i) 这一结论的一般形式是：$X$ 为局部紧 Hausdorff 空间，$\mu$ 为 $X$ 上的 Radon 测度时，$C_{c}(X)$ 在 $L^{p}(X,\mu)$（$1\le p<\infty$）中稠密；本篇只证明了 $\mathbb{R}^{n}$ 的情形。同样的证明对开集 $U\subseteq\mathbb{R}^{n}$ 上的 $C_{c}(U)$ 与 $L^{p}(U)$ 也成立。

(ii) 结论对 $p=\infty$ 不成立。事实上 $\mathbf{1}_{[0,1]}$ 到 $C_{c}(\mathbb{R})$ 的 $L^{\infty}$ 距离至少为 $\frac12$：若连续函数 $g$ 满足 $\lVert g-\mathbf{1}_{[0,1]}\rVert_{\infty}=c<\frac12$，则集合 $\{x\in(0,1):|g(x)-1|>c\}$ 是零测的开集，从而为空集，即 $|g-1|\le c$ 于 $(0,1)$，由连续性 $g(1)\ge1-c>\frac12$；同理 $|g|\le c$ 于 $(1,2)$，$g(1)\le c<\frac12$，矛盾。

(iii) 由定理 4.1 与定理 7.4，$L^{p}(\mathbb{R}^{n})$ 是一个包含 $C_{c}(\mathbb{R}^{n})$ 作为稠密子空间的 Banach 空间，即 $(C_{c}(\mathbb{R}^{n}),\lVert \cdot\rVert_{p})$ 的完备化。同理 $L^{1}[0,2]$ 是例 1.13 中不完备空间 $(C[0,2],\lVert \cdot\rVert_{1})$ 的完备化。

作为稠密性的典型应用，我们证明平移在 $L^{p}$ 中是连续的。对 $h\in\mathbb{R}^{n}$ 令 $(\tau_{h}f)(x)=f(x-h)$。由 Lebesgue 测度的平移不变性（第 I 篇），对示性函数、从而对简单函数、再由单调收敛定理对非负可测函数有 $\int f(x-h)\,\mathrm{d}x=\int f(x)\,\mathrm{d}x$，因此 $\lVert \tau_{h}f\rVert_{p}=\lVert f\rVert_{p}$。

**定理 7.6**（平移的连续性）
设 $1\le p<\infty$，$f\in L^{p}(\mathbb{R}^{n})$。则 $\lim_{h\to0}\lVert \tau_{h}f-f\rVert_{p}=0$。

*证明.*　
给定 $\varepsilon>0$，由定理 7.4 取 $g\in C_{c}(\mathbb{R}^{n})$ 使 $\lVert f-g\rVert_{p}<\varepsilon$，设 $\operatorname{supp} g\subseteq B(0,R)$。$g$ 在紧集上连续、在其外为零，因而在 $\mathbb{R}^{n}$ 上一致连续，所以 $\sup_{x}|g(x-h)-g(x)|\to0$（$h\to0$）。当 $|h|\le1$ 时 $\tau_{h}g-g$ 在 $B(0,R+1)$ 之外为零，故
$$
\lVert \tau_{h}g-g\rVert_{p}\le\sup_{x}|g(x-h)-g(x)|\cdot m\bigl(B(0,R+1)\bigr)^{1/p}\xrightarrow[h\to0]{}0 .
$$
于是
$$
\lVert \tau_{h}f-f\rVert_{p}\le\lVert \tau_{h}(f-g)\rVert_{p}+\lVert \tau_{h}g-g\rVert_{p}+\lVert g-f\rVert_{p}<2\varepsilon+\lVert \tau_{h}g-g\rVert_{p},
$$
所以 $\limsup_{h\to0}\lVert \tau_{h}f-f\rVert_{p}\le2\varepsilon$。 $\square$

$p=\infty$ 时结论不成立：对 $f=\mathbf{1}_{[0,1]}$ 与任意 $0<|h|<1$，$\tau_{h}f-f$ 在一个正测集上取值 $\pm1$，故 $\lVert \tau_{h}f-f\rVert_{\infty}=1$。

### 7.3 可分性

**定理 7.7**
设 $1\le p<\infty$。则 $L^{p}(\mathbb{R}^{n})$ 是可分的。

*证明.*　
对 $j\ge0$，称形如 $\prod_{i=1}^{n}[k_{i}2^{-j},(k_{i}+1)2^{-j})$（$k\in\mathbb{Z}^{n}$）的集合为 $j$ 阶二进方体。令 $\mathcal{D}$ 为系数属于 $\mathbb{Q}+i\mathbb{Q}$（实情形为 $\mathbb{Q}$）的二进方体示性函数的有限线性组合全体，它是可数集。

给定 $f\in L^{p}$ 与 $\varepsilon>0$，取 $g\in C_{c}(\mathbb{R}^{n})$ 使 $\lVert f-g\rVert_{p}<\varepsilon$，并取正整数 $R$ 使 $\operatorname{supp} g\subseteq Q_{R}=[-R,R)^{n}$。由 $g$ 的一致连续性，存在 $j$ 使同一个 $j$ 阶二进方体中任意两点 $x,y$ 满足 $|g(x)-g(y)|<\eta$，其中 $\eta>0$ 待定。$Q_{R}$ 恰被有限个 $j$ 阶二进方体 $Q$ 所铺满；对每个这样的 $Q$，取其中一点 $x_{Q}$ 与 $c_{Q}\in\mathbb{Q}+i\mathbb{Q}$ 使 $|c_{Q}-g(x_{Q})|<\eta$，令 $\psi=\sum_{Q}c_{Q}\mathbf{1}_{Q}\in\mathcal{D}$。则在 $Q_{R}$ 上 $|g-\psi|<2\eta$，在 $Q_{R}$ 之外 $g=\psi=0$，于是
$$
\lVert g-\psi\rVert_{p}\le2\eta\,(2R)^{n/p}.
$$
取 $\eta$ 使右端小于 $\varepsilon$，得 $\lVert f-\psi\rVert_{p}<2\varepsilon$。 $\square$

**注 7.8**
可分性不是一般测度空间上 $L^{p}$（$1\le p<\infty$）的性质。设 $X$ 为不可数集（例如 $\mathbb{R}$），$\mu$ 为计数测度，则函数 $e_{x}=\mathbf{1}_{\{x\}}$（$x\in X$）满足 $\lVert e_{x}-e_{y}\rVert_{p}=2^{1/p}$（$x\ne y$），与命题 5.5 的论证相同，$L^{p}(X,\mu)$ 不可分。一个常用的充分条件是：$\mu$ 为 $\sigma$-有限，且 $\mathcal{M}$ 由可数个集合生成（模零测集）；此时 $L^{p}(X,\mu)$（$1\le p<\infty$）可分。$L^{\infty}$ 则在几乎所有有意义的无穷情形下都不可分（命题 5.5）。

## 8. 对偶空间简介

本节只做简要讨论，完整的表示定理需要 Radon–Nikodym 定理，留待以后。

**命题 8.1**
设 $1\le p\le\infty$，$q$ 为其共轭指数，$g\in L^{q}(X,\mu)$。则
$$
\Lambda_{g}(f)=\int_{X}fg\,\mathrm{d}\mu\qquad(f\in L^{p})
$$
定义了 $L^{p}$ 上的有界线性泛函，且 $\lVert \Lambda_{g}\rVert\le\lVert g\rVert_{q}$。若 $1<p\le\infty$，或 $p=1$ 且 $\mu$ 为 $\sigma$-有限，则 $\lVert \Lambda_{g}\rVert=\lVert g\rVert_{q}$。于是在这些情形下 $g\mapsto\Lambda_{g}$ 是从 $L^{q}$ 到 $(L^{p})^{*}$ 的线性等距（特别地是单射）。

*证明.*　
$\Lambda_{g}(f)$ 与代表元的选取无关，关于 $f$ 线性，并由 Hölder 不等式 $|\Lambda_{g}(f)|\le\lVert f\rVert_{p}\lVert g\rVert_{q}$。下面设 $g\ne0$，证明反向不等式。令 $\operatorname{sgn} z=z/|z|$（$z\ne0$），$\operatorname{sgn}0=0$，则 $g\,\overline{\operatorname{sgn} g}=|g|$。

$1<p<\infty$：令 $f=|g|^{q-1}\overline{\operatorname{sgn} g}$。则 $|f|^{p}=|g|^{(q-1)p}=|g|^{q}$，$\lVert f\rVert_{p}=\lVert g\rVert_{q}^{q/p}<\infty$，且 $\Lambda_{g}(f)=\int|g|^{q}=\lVert g\rVert_{q}^{q}$。于是
$$
\lVert \Lambda_{g}\rVert\ge\frac{\lVert g\rVert_{q}^{q}}{\lVert g\rVert_{q}^{q/p}}=\lVert g\rVert_{q}^{q(1-1/p)}=\lVert g\rVert_{q}.
$$

$p=\infty$（$q=1$）：令 $f=\overline{\operatorname{sgn} g}$，则 $\lVert f\rVert_{\infty}\le1$，$\Lambda_{g}(f)=\lVert g\rVert_{1}$。

$p=1$（$q=\infty$），$\mu$ 为 $\sigma$-有限：取 $0<t<\lVert g\rVert_{\infty}$，则 $A=\{|g|>t\}$ 满足 $\mu(A)>0$。设 $X=\bigcup_{k}X_{k}$，$X_{k}$ 递增且 $\mu(X_{k})<\infty$，则 $\mu(A\cap X_{k})\uparrow\mu(A)>0$，故存在 $k$ 使 $B=A\cap X_{k}$ 满足 $0<\mu(B)<\infty$。令 $f=\mu(B)^{-1}\mathbf{1}_{B}\overline{\operatorname{sgn} g}$，则 $\lVert f\rVert_{1}=1$，且
$$
\Lambda_{g}(f)=\frac{1}{\mu(B)}\int_{B}|g|\,\mathrm{d}\mu\ge t .
$$
所以 $\lVert \Lambda_{g}\rVert\ge t$；令 $t\uparrow\lVert g\rVert_{\infty}$ 即可。 $\square$

**定理 8.2**（$L^{p}$ 的 Riesz 表示定理）

(i) 设 $1<p<\infty$。则对每个 $\Lambda\in(L^{p})^{*}$，存在唯一的 $g\in L^{q}$ 使 $\Lambda=\Lambda_{g}$；从而 $(L^{p})^{*}$ 与 $L^{q}$ 等距同构。

(ii) 设 $\mu$ 为 $\sigma$-有限。则 $(L^{1})^{*}$ 与 $L^{\infty}$ 等距同构（同样通过 $g\mapsto\Lambda_{g}$）。

证明需要 Radon–Nikodym 定理（或者对 (i) 使用 $L^{p}$ 的一致凸性），此处从略。唯一性与等距性已由命题 8.1 给出；困难在于满射性。注意表示泛函的函数 $g$ 属于 $L^{q}$ 而不是 $L^{p}$。

**例 8.3**（$\sigma$-有限性不可省略）
设 $X=\{a\}$，$\mu(\{a\})=\infty$。则 $\int|f|\,\mathrm{d}\mu=|f(a)|\cdot\infty$，故 $L^{1}=\{0\}$，$(L^{1})^{*}=\{0\}$；但 $X$ 没有非空零测集，$L^{\infty}=\mathbb{K}$。映射 $g\mapsto\Lambda_{g}$ 是零映射，不是单射。

**注 8.4**（$p=\infty$ 的情形）
由命题 8.1，$L^{1}$ 等距地嵌入 $(L^{\infty})^{*}$，但一般不是满射，因此“$(L^{p})^{*}=L^{q}$”对 $p=\infty$ 一般不成立。以 $\ell^{\infty}$ 为例：在收敛序列构成的子空间 $c$ 上，$\ell(x)=\lim_{n}x_{n}$ 是范数为 $1$ 的有界线性泛函；由 Hahn–Banach 定理，它可以保范延拓为 $\ell^{\infty}$ 上的 $\Lambda$。若 $\Lambda=\Lambda_{y}$，$y\in\ell^{1}$，则 $y_{k}=\Lambda(e_{k})=\lim_{n}(e_{k})_{n}=0$ 对每个 $k$ 成立，于是 $\Lambda=0$，与 $\Lambda(1,1,\dots)=1$ 矛盾。

**注 8.5**
当 $\mu$ 为 $\sigma$-有限时，$L^{\infty}=(L^{1})^{*}$，由 Banach–Alaoglu 定理，$L^{\infty}$ 的闭单位球在弱$^{*}$拓扑 $\sigma(L^{\infty},L^{1})$ 下是紧的。对 $1<p<\infty$，定理 8.2 说明 $(L^{p})^{**}\cong(L^{q})^{*}\cong L^{p}$，即 $L^{p}$ 是自反的。这些将在泛函分析部分讨论。

## 小结

下表总结了本篇关于 $L^{p}(X,\mu)$ 的主要结论（“$\mathbb{R}^{n}$”表示结论在 $(\mathbb{R}^{n},m)$ 上成立，但在一般测度空间中可能不成立）。$0<p<1$ 一列第 2–5 行的结论，可用度量 $d_{p}$ 代替范数、按 $p\ge1$ 时的相同证明得到。

| 性质 | $0<p<1$ | $1\le p<\infty$ | $p=\infty$ |
|---|---|---|---|
| $\lVert \cdot\rVert_{p}$ 是范数 | 否 | 是 | 是 |
| 完备 | 是（度量 $d_{p}$） | 是 | 是 |
| 简单函数稠密 | 是 | 是 | 是 |
| $C_{c}$ 稠密 | 是（$\mathbb{R}^{n}$） | 是（$\mathbb{R}^{n}$） | 否 |
| 可分 | 是（$\mathbb{R}^{n}$） | 是（$\mathbb{R}^{n}$） | 否 |
| 对偶 | 平凡（$\mathbb{R}^{n}$） | $L^{q}$（$p=1$ 需 $\sigma$-有限） | 一般真包含 $L^{1}$ |

主要的证明工具只有三件：Young 不等式（由凸性得到）导出 Hölder 不等式，Hölder 不等式导出 Minkowski 不等式；Minkowski 不等式配合单调收敛与控制收敛定理给出完备性；而 Lebesgue 测度的正则性给出 $C_{c}$ 的稠密性与可分性。不同 $L^{p}$ 空间之间的关系则完全取决于测度在“局部”和“无穷远处”的行为。

## 参考文献

1. G. B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999.
2. W. Rudin, *Real and Complex Analysis*, 3rd ed., McGraw–Hill, 1987.
3. H. Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*, Springer, 2011.
4. E. M. Stein and R. Shakarchi, *Real Analysis: Measure Theory, Integration, and Hilbert Spaces*, Princeton University Press, 2005.
