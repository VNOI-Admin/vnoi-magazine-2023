# XOR BASIS

Author: Nguyễn Minh Thiện

## Giới thiệu

Đây là một kỹ thuật được dùng để giải quyết một số bài toán có liên quan đến tổng xor của đoạn con (liên tiếp hoặc không liên tiếp) của mảng các số nguyên cho trước hoặc thêm phần tử vào mảng song song với việc truy vấn. 

Kỹ thuật này có thể được chia làm hai phần chính:
- Biểu diễn các số nguyên ở cơ số 2 và xem mỗi phần tử là một vector trong không gian vector $\mathbb{Z}^{d}_{2}$, với $d$ là số bit tối đa cần dùng để biểu diễn. Lúc này phép xor giữa các phần tử tương đương với phép cộng giữa các vector tương ứng trong không gian vector $\mathbb{Z}^{d}_{2}$. 
- Tìm mối liên hệ giữa yêu cầu của các truy vấn và cơ sở của không gian vector tìm được ở trên.

## Một số khái niệm

### Không gian Vector

Một tập $V \ne \varnothing$ được gọi là một không gian vector nếu $\mathit{V}$ được trang bị hai phép toán: phép cộng và phép nhân với một vô hướng. Các phần tử trong $V$ được gọi là các vector.
- $V$ phải có tính chất đóng, tức là $\forall x, y \in V \Longrightarrow x + y \in V$ và $\forall x \in V \Longrightarrow kx \in V$ với $k$ là một đại lượng vô hướng.
- Phép cộng phải có tính chất kết hợp và giao hoán.
- Phép nhân với một vô hướng phải có tính chất kết hợp và phân phối.
- Trong $V$ phải có phần tử $O$ gọi là vector không (chú ý không lẫn với số $0$).

Một số không gian vector đặc biệt:
- Không gian vector các tọa độ $\mathbb{R}^n = \{(x_1, x_2, \ldots, x_n)\}$.
- Không gian vector $M_{n \times m}$ các ma trận kích cỡ $n \times m$.
- Không gian vector $P_n(x)$ các đa thức bậc không quá $n$.
- Không gian vector $F$ các hàm số.
- ...

### Độc lập tuyến tính và phụ thuộc tuyến tính

Một tập các vector $\{v_1, v_2, \ldots, v_n\}$ được gọi là __độc lập tuyến tính__ nếu phương trình: $$x_1v_1 + x_2v_2 + \ldots + x_nv_n = O$$ chỉ có duy nhất một nghiệm tầm thường $x_1 = x_2 = \ldots = x_n = 0$.

Ngược lại nếu tồn tại $x_1, x_2, \ldots, x_n$ không đồng thời bằng không, sao cho: $$x_1v_1 + x_2v_2 + \ldots + x_nv_n = O$$ thì khi đó được gọi là __phụ thuộc tuyến tính__.

### Không gian vector $\mathbb{Z}_2^d$

$\mathbb{Z}_2$: $\mathbb{Z}_m$ là tập các số dư khi chia lấy dư cho $m$ và các phép toán trên $\mathbb{Z}_m$ cũng chia lấy dư cho $m$. Suy ra $\mathbb{Z}_2$ là tập các số dư khi chia lấy dư cho $2$ do đó $\mathbb{Z}_2 = \{0, 1\}$.

$\mathbb{Z}_2^d$: là một không gian vector $d$ chiều bao gồm tất cả các vector có $d$ tọa độ, mỗi tọa độ là một phần tử của $\mathbb{Z}_2$.
- Nếu hai vector $x, y \in \mathbb{Z}_2^d$ thì $x + y$ được định nghĩa là $x \oplus y$ ($\oplus$ là phép xor bit). Chú ý $x + y \in \mathbb{Z}_2^d$ phải thõa mãn. Cụ thể hơn:

\begin{tabular}{|c|c|c|c|c|}
\hline
    \textbf{} & \textbf{} & \textbf{$\oplus$} & \textbf{Tổng} & \textbf{Tổng mod 2} \\ \hline
    0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 1 & 1 & 1 & 1 \\ \hline
    1 & 0 & 1 & 1 & 1 \\ \hline
    1 & 1 & 0 & 2 & 0 \\ \hline
\end{tabular}
    
- Với $c \in \mathbb{Z}_2$, kí hiệu $cx = \underbrace{x + x + \ldots + x}_{c \text{ lần }x}$. Ta có $cx = 0$ nếu $c$ chẵn và $cx = x$ nếu $c$ lẻ. 

**Kể từ đây chúng ta chỉ quan tâm đến không gian vector $\mathbb{Z}_2^d$, mọi phép tính đều chia lấy dư cho 2 và xem phép $\oplus$ (xor bit) tương đương với phép $+$ trong $\mathbb{Z}_2^d$.**

### Bao tuyến tính (Linear span, gọi tắt là span)

Một không gian vector $V$ được span bởi một tập các vector $S = \{v_1, v_2, \ldots, v_n\}$ chứa tất cả các vector $x$ được biểu diễn thông qua một tổ hợp tuyến tính của các vector trong $S$.
$$\text{span}(S) = \left\{\sum_{i = 1}^n c_i v _i \, \middle| \, v_i \in S, c_i \in \{0, 1\} \right\}$$
lúc này ta nói $V$ được span bởi $S$, $V$ được sinh bởi $S$ hay $S$ sinh ra $V$.

_Chú ý:_ do chỉ xét trên $\mathbb{Z}_2^d$ nên $c_i$ cũng phải thuộc $\mathbb{Z}_2^d$. Do đó trong tổ hợp trên mỗi $v_i$ chỉ có hai trạng thái là __xuất hiện__ hoặc __không xuất hiện__.

__Ví dụ:__ tìm span$(\{2, 5\})$, span$(\{2, 5, 7\})$ và span$(\{\})$?
- Ta có $2 \oplus 5 = 7$, suy ra:
$$\begin{array}{l}
	\text{span}(\{2, 5\}) =\text{span}(\{2, 5, 7\}) = \{0, 2, 5, 7\} \\
	\text{span}(\{\})= \{0\}
\end{array}$$

Một số tính chất quan trọng:
- Nếu $v_{n + 1} \in \text{span}(\{v_1, v_2, \ldots, v_n\})$ thì: 
$\begin{array}{l}
\text{span}(\{v_1, v_2, \ldots, v_n, v_{n + 1}\}) \\
\quad = \text{span}(\{v_1, v_2, \ldots, v_n\})
\end{array}$

- $
\begin{array}{l}
\text{span}(\{v_1 + v_3, v_2, \ldots, v_n\}) \\
\quad = \text{span}(\{v_1, v_2, \ldots, v_n\})
\end{array}$

### Cơ sở (Basis)

Một tập các vector $B = \{v_1, v_2, \ldots, v_n\}$ được gọi là cơ sở của một không gian vector $V$ nếu span$(B) = V$ và $B$ là __độc lập tuyến tính__. Khi đó $n$ được gọi là __số chiều__ của $V$ và kí hiệu là $\text{dim}(V)$.

__Ví dụ:__ Xét không gian vector $V = \{0, 2, 5, 7\}$, ta có $\{2, 5\}$ là một cơ sở của $V$ nhưng $\{2, 5, 7\}$ thì không vì tập này là không độc lập tuyến tính do $2 \oplus 5 \oplus 7 = 0$. Và dĩ nhiên $\{2, 7\}$ và $\{5, 7\}$ cũng là các cơ sở của $V$.

_Chú ý:_ số phần tử phân biệt trong không gian vector $V$ được span bởi một cơ sở $B = \{v_1, v_2, \ldots, v_n\}$ là $|V| = 2^n$.

### Ma trận

#### Không gian hàng và không gian cột

Xét một ma trận $M$ kích cỡ $n \times m$ ($n$ hàng và $m$ cột):
$$
M = 
\begin{bmatrix}
	v_{1,1} & v_{1,2} & \cdots & v_{1,m} \\
	v_{2,1} & v_{2,2} & \cdots & v_{2,m} \\
	\vdots & \vdots & \ddots & \vdots \\
	v_{n,1} & v_{n,2} & \cdots & v_{n,m} 
\end{bmatrix}
$$
- Chia ma trận $M$ thành các vector hàng, ta được:
  $$row_i = [v_{i, 1}, v_{i, 2}, \ldots, v_{i, m}]$$
- Chia ma trận $M$ thành các vector cột, ta được:
  $$col_i = [v_{1, i}, v_{2, i}, \ldots, v_{n, i}]$$
- Khi đó không gian hàng và không gian cột của ma trận $M$ được định nghĩa như sau:
  $$\begin{array}{rl}
  RS(M)  &= \text{span}(\{row_1, row_2, \ldots, row_n\}) \\
  CS(M)  &= \text{span}(\{col_1, col_2, \ldots, col_m\})\end{array}$$

#### Hạng của ma trận

Người ta chứng minh được rằng dim$(RS(M))$ $=$ dim$(CS(M))$ và được kí hiệu là dim$(M)$ hay còn được biết đến là hạng (rank) của ma trận $M$, kí hiệu rank$(M)$.
(Tham khảo phần chứng minh [tại đây](https://math.stackexchange.com/questions/332908/looking-for-an-intuitive-explanation-why-the-row-rank-is-equal-to-the-column-ran))

#### Không gian hạch (Null space)

Để hiểu rõ được phần này, bạn cần phải quen thuộc với [phép nhân ma trận](https://vi.wikipedia.org/wiki/Ph%C3%A9p_nh%C3%A2n_ma_tr%E1%BA%ADn).

Không gian hạch của một ma trận $M$, kí hiệu là null$(M)$ là tập các vector $x \in \mathbb{R}^m$ (được viết ở dạng cột) sao cho: $$M \cdot x = O$$

Giả sử:
$$M = 
\begin{bmatrix}
	v_{1,1} & v_{1,2} & \cdots & v_{1,m} \\
	v_{2,1} & v_{2,2} & \cdots & v_{2,m} \\
	\vdots & \vdots & \ddots & \vdots \\
	v_{n,1} & v_{n,2} & \cdots & v_{n,m} 
\end{bmatrix}
,\quad
x = 
\begin{bmatrix}
	x_1 \\
	x_2 \\
	\ldots \\
	x_m 
\end{bmatrix}$$
Khi đó $(x_1, x_2, \ldots, x_m)$ là nghiệm của hệ phương trình:
$$\begin{cases}
	v_{1, 1}x_1 + v_{1, 2}x_2 + \ldots + v_{1, m}x_m = 0 \\
	v_{2, 1}x_1 + v_{2, 2}x_2 + \ldots + v_{2, m}x_m = 0 \\
	\ldots \\
	v_{n, 1}x_1 + v_{n, 2}x_2 + \ldots + v_{n, m}x_m = 0
\end{cases}$$

__Đặc biệt:__ nếu ma trận $M$ kích cỡ $n \times m$ gồm $m$ vector $v \in \mathbb{Z}_2^n$ và vector $x \in \mathbb{Z}_2^m$ (các vector $v$ và $x$ được viết ở dạng cột):
$$
\begin{array}{rl}
M &= 
\begin{bmatrix}
	| & | & \ldots & | \\
	v_1 & v_2 & \ldots & v_m \\
	| & | & \ldots & |
\end{bmatrix} \\
& \equiv
\begin{bmatrix}
	v_{1,1} & v_{2,1} & \cdots & v_{m,1} \\
	v_{1,2} & v_{2,2} & \cdots & v_{m,2} \\
	\vdots & \vdots & \ddots & \vdots \\
	v_{1,n} & v_{2,n} & \cdots & v_{m,n} 
\end{bmatrix}
\\
x &= 
\begin{bmatrix}
	x_1 \\
	x_2 \\
	\ldots \\
	x_m 
\end{bmatrix}
\end{array}$$

Khi đó:
$$ \begin{array}{l}
M \cdot x = O \\
\Longleftrightarrow 
\begin{cases}
	v_{1, 1}x_1 + v_{2, 1}x_2 + \ldots + v_{m, 1}x_m \equiv 0 \\
	v_{1, 2}x_1 + v_{2, 2}x_2 + \ldots + v_{m, 2}x_m \equiv 0 \\
	\ldots \\
	v_{1, n}x_1 + v_{2, n}x_2 + \ldots + v_{m, n}x_m \equiv 0 
\end{cases}
\end{array}
$$

_Lưu ý các phương trình trong hệ phương trình trên là đồng dư theo **modulo $2$**_.

Để ý rằng không gian hạch cũng là một không gian vector, vì:
$$\begin{array}{rl}
\left\lbrace\begin{array}{rl}
M\cdot a &= O \\
M \cdot b & = O
\end{array}\right.
 & \Longrightarrow M \cdot (a + b) = O \\
M \cdot a = O & \Longrightarrow M \cdot (ca) = O
\end{array}$$

#### Số vô hiệu (Nullity)

Số vô hiệu của một ma trận $M$ chính là số chiều của không gian hạch của $M$: $$\text{nullity}(M) = \text{dim}(\text{null}(M))$$

#### Định lý về hạng và số vô hiệu

Định lý này phát biểu rằng với một ma trận $M$ kích cỡ $n \times m$ thì: $$\text{rank}(M) + \text{nullity}(M) = \text{số cột} = m$$
Phần chứng minh khá phức tạp và đòi hỏi giới thiệu thêm nhiều khái niệm nên các bạn có thể tham khảo [tại đây](https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem#First_proof).

## Thuật toán tìm cơ sở của một không gian vector

Tiếp theo chúng ta sẽ đi vào phần chính của bài viết này đó chính là làm thế nào để có thể tìm cơ sở của một không gian vector, trong đó mỗi vector là một phần tử của $\mathbb{Z}_2^d$ một cách hiệu quả. Chúng ta sẽ phân tích thuật toán thông qua bài toán dưới đây.

### [XOR Closure](https://csacademy.com/contest/archive/task/xor-closure/)

__Đề bài__

Cho một mảng $a$ có $n$ phần tử phân biệt $a_1, a_2, \ldots, a_n$. Yêu cầu tìm số phần tử ít nhất cần thêm vào mảng $a$ sao cho điều sau luôn đúng: với mọi $x, y$ thuộc $a$ thì $x \oplus y$ cũng thuộc $a$.

__Giới hạn__ 
- $1 \leq n \leq 10^5$.
- $0 \leq a_i \leq 10^{18}$.

__Lời giải__

Để ý rằng chúng ta cần thỏa mãn điều kiện $\forall x, y \in a$ thì $x \oplus y \in a$. Do đó cần phải xây dựng được __cơ sở $B$__ của không gian vector $V$ được span bởi mảng $a$. Khi đó đáp án của bài toán chính là $2^{\text{dim}(\text{span}(a))} - n = 2^{|B|} - n$.

Chúng ta sẽ xét lần lượt từng phần tử như sau:
- Giả sử chúng ta đã xét đến $a_1, a_2, \ldots, a_{i - 1}$ và có cơ sở $B$. Chúng ta cần cập nhật $B$ sao cho $a_i$ cũng có thể được biểu diễn thông qua các vector trong $B$.
- Kiểm tra xem $a_i$ có thể được biểu diễn thông qua các vector trong $B$ hay không. 
	- Nếu có thì không cần làm gì cả.
	- Ngược lại chỉ cần thêm $a_i$ vào $B$.

Phần khó nhất đó chính là làm thế nào để có thể kiểm tra xem $a_i$ có thể được biểu diễn thông qua các vector trong $B$ hay không.
- Nếu xem xét tất cả $2^i$ tổ hợp tuyến tính của các vector trong $B$ thì rõ ràng sẽ không đủ thời gian.
- Với một số nguyên dương $x$, định nghĩa msb$(x)$ $=$ vị trí của most significant bit trong $x$. Ví dụ: 
	$$
	\text{msb}(5) = \text{msb}(7) = 2 \\
	\text{msb}(3) = 1, \text{msb}(1) = 0
	$$
- Giả sử chúng ta có cơ sở $B = \{b_1, b_2, \ldots, b_k\}$ của $a_1, a_2, \ldots, a_{i - 1}$ sao cho $\text{msb}(b_1) < \text{msb}(b_2) < \ldots < \text{msb}(b_k)$.
- Khi đó chỉ cần duyệt $j$ từ $1..k$. Nếu $a_i + b_j < a_i$ $(\text{msb}(a_i) = \text{msb}(b_j))$ thì thay $a_i = a_i + b_j$. Nếu cuối cùng $a_i = 0$ thì $a_i$ có thể được biểu diễn thông qua các vector trong $B$. Ngược lại thêm giá trị hiện tại của $a_i$ vào vị trí thích hợp trong $B$ sao cho vẫn giữ được thứ tự giảm dần của msb.
- __Ví dụ:__ kiểm tra xem $x = 20$ có thuộc $\text{span}(\{26, 15, 3, 1\})$ hay không?
	$$\begin{array}{rl}
	26 &= 11010_2 \\ 
	15 &= 01111_2 \\
	3 &= 00011_2 \\
	1 &= 00001_2 \\
	20 &= 10100_2
	\end{array}$$

	- $x \oplus 26 = \mathbf{14} < x \Rightarrow$ cập nhật $x = 14$.
	- $x \oplus 15 = \mathbf{1} < x \Rightarrow$ cập nhật $x = 1$.
	- $x \oplus 3 = \mathbf{2} > x$.
	- $x \oplus 1 = \mathbf{0} < x \Rightarrow$ cập nhật $x = 0$.

	Vậy $20 = 26 \oplus 15 \oplus 1$ và $20 \in \text{span}(\{26, 15, 3, 1\})$.
- __Tổng quát:__ thuật toán trên cho phép tìm giá trị nhỏ nhất của $(a_i + v)$ với $v \in \text{span}(\{b_1, b_2, \ldots, b_k\})$.
- __Ví dụ:__ xét $x = 9$ và $\text{span}(\{26, 15, 3, 1\})$. Khi đó giá trị nhỏ nhất có thể đạt được là: $$9 \oplus 15 \oplus 3 \oplus 1 = \mathbf{4} = 100_2.$$

__Code mẫu__:
```cpp
vector<long long> basis;
int sz;
void insertVector(long long mask) {
    // duyệt các phần tử theo thứ tự giá trị msb giảm dần.
    for (int i = 0; i < sz; ++i) {
        mask = min(mask, mask ^ basis[i]);
    }
    if (mask != 0) {
        basis.push_back(mask);
        sz++;
        int i = sz - 1;
        // giữ các giá trị msb sao cho vẫn theo thứ tự giảm dần.
        while (i > 0 && basis[i - 1] < basis[i]) {
            swap(basis[i - 1], basis[i]);
            i--;
        }
    }
}
```

__Phân tích độ phức tạp__

Vì các phần tử có kiểu `long long` nên cần tối đa 64 bit để biểu diễn. Đặt $d = basis.size() = \text{dim}(\text{span}(a)) \leq 64$ thì độ phức tạp mỗi lần thêm một vector là $\mathcal{O}(d)$. Độ phức tạp tổng cộng cho việc thêm $n$ vector là $\mathcal{O}(n d)$.

Để ý rằng trong thuật toán trên $v_i$ chỉ được thêm vào mảng `basis` khi không có phần tử $b_j$ nào mà $\text{msb}(b_j) = \text{msb}(v_i)$. Do đó các giá trị $\text{msb}(b_j)$ trong $B$ là phân biệt. Khi đó có thể cải tiến code như sau:

__Code cải tiến__
```cpp!
vector<long long> basis;
void insertVector(long long mask) {
    for (int i = 0; i < (int) basis.size(); ++i) {
        mask = min(mask, mask ^ basis[i]);
    }
    if (mask != 0) {
      	basis.push_back(mask);
        // chỉ cần thêm vào cuối mảng, không cần giữ giá trị msb theo thứ tự giảm dần.
    }
}
```

__Code hoàn chỉnh__
```cpp!
#include <bits/stdc++.h>
using namespace std;

vector<long long> basis;
void insertVector(long long mask) {
    for (int i = 0; i < (int) basis.size(); ++i) {
        mask = min(mask, mask ^ basis[i]);
    }
    if (mask != 0) {
        basis.push_back(mask);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        insertVector(a[i]);
    }
    long long ret = (1LL << basis.size()) - n;
    cout << ret << '\n';

    return 0;
}
```

## Một số bài tập ví dụ

### [Codechef - XORCMPNT](https://www.codechef.com/problems/XORCMPNT)

__Tóm tắt đề bài__

Cho $2^K$ trạm điện (được đánh số từ $0$ đến $2^K - 1$). Ban đầu không có đường nối giữa các trạm. Bạn được cho $M$ số nguyên $x_1, x_2, \ldots, x_M$, giữa hai trạm $u, v$ khác nhau sẽ có một đường nối trực tiếp nếu tồn tại chỉ số $i$ thõa mãn $u \oplus v = x_i$. Hai trạm $u, v$ được gọi là cùng một thành phần liên thông nếu chúng có đường nối trực tiếp với nhau hoặc gián tiếp qua các trạm khác.
Bạn cần xử lý $T$ trường hợp. Mỗi trường hợp yêu cầu tìm số thành phần liên thông được tạo thành.

__Giới hạn__
- $1 \leq T \leq 10^5$.
- $1 \leq K \leq 30$.
- $1 \leq M \leq 10^5$.
- $0 \leq x_i < 2^K$.
- Tổng $M$ trong tất cả các trường hợp không quá $10^5$.

__Lời giải__

- Do $K \leq 30$ nên chúng ta không thể xem xét hết tất cả $2^K$ trạm.
- Giả sử chúng ta có ba trạm như sau: $u \oplus v = x_i, v \oplus w = x_j$. Khi đó hai trạm $u$ và $w$ sẽ có đường đi gián tiếp qua trạm $v$ và thuộc cùng một thành phần liên thông và $u \oplus w = x_i \oplus x_j$.
- Do đó hai trạm $u, v$ bất kì sẽ thuộc cùng một thành phần liên thông nếu $u \oplus v = x_i \oplus x_{i + 1} \oplus \ldots \oplus x_j$, với $\{x_i, x_{i + 1}, \ldots, x_j\}$ là một tập con bất kì của $\{x_1, x_2, \ldots, x_M\}$. Đặt $z = x_i \oplus x_{i + 1} \oplus \ldots \oplus x_j$, suy ra $z \in \text{span}(\{x_1, x_2, \ldots, x_M\})$ và đặt $d = \text{dim}(\text{span}(\{x_1, x_2, \ldots, x_M\}))$.
- Xét một trạm $u$ bất kì, ta có các trạm cùng một thành phần liên thông với $u$ là $v$ ($v \ne u$) sao cho $u \oplus v = z \Longrightarrow v = u \oplus z$. Có tất cả $2^d$ giá trị $z$ khác nhau (bao gồm cả $z = 0$ và $v = u$) nên sẽ có tất cả $2^d - 1$ trạm $v$ như vậy.
- Như vậy mỗi trạm $u$ bất kì sẽ liên thông với $2^d - 1$ trạm khác. Cho nên mỗi thành phần liên thông đều có $2^d$ trạm và do đó sẽ có tất cả $2^K / 2^d$ thành phần liên thông.

__Code mẫu__

```cpp!
#include <bits/stdc++.h>
using namespace std;

vector<int> basis;
void insertVector(int mask) {
    for (int i = 0; i < (int) basis.size(); ++i) {
        mask = min(mask, mask ^ basis[i]);
    }
    if (mask != 0) {
        basis.push_back(mask);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int k, m;
        cin >> k >> m;
        vector<int> a(m);
        for (int i = 0; i < m; ++i) {
            cin >> a[i];
        }
        // xây dựng mảng cơ sở của không gian vector được span bởi {x_1, x_2,..., x_m}.
        basis.clear();
        for (int i = 0; i < m; ++i) {
            insertVector(a[i]);
        }
        int d = (int) basis.size();
        cout << (1 << k) / (1 << d) << '\n';
    }   
    return 0;
}
```

__Phân tích độ phức tạp__

Hàm `insertVector` có độ phức tạp là $\mathcal{O}(d)$, với $d$ là số chiều của không gian vector được span bởi $\{x_1, x_2, \ldots, x_M\}$ (kích thước của mảng `basis`) trong trường hợp này $x_i < 2^K$ nên $d \leq K$. Độ phức tạp tổng cộng $\mathcal{O}(M K)$.

### [Maximum XOR over all subsets](https://codeforces.com/blog/entry/60003)

__Đề bài__

Cho tập $S$ có $n$ phần tử $a_1, a_2, \ldots, a_n$. Hãy cho biết tổng XOR lớn nhất trong tất cả các tập con của $S$ là bao nhiêu?

__Giới hạn__
- $1 \leq n \leq 10^5$.
- $0 \leq a_i < 2^{20}$.

__Lời giải__
- Do $n$ khá lớn nên ta không thể xét hết tất cả $2^n$ tập con của $S$.
- Nhận xét rằng do $a_i < 2^{20}$ nên ta có thể tìm cơ sở $B$ của không gian vector $V$ được span bởi $S$. Khi đó chỉ cần duyệt hết tất cả $2^{|B|}$ tập con của $B$ ($|B| \leq 20$). Độ phức tạp $\mathcal{O}(2^{|B|})$.

__Chứng minh__
- Giả sử $B = \{b_1, b_2, \ldots, b_k\}$.
- Do mỗi phần tử trong tập $S$ đều được biểu diễn thông qua các phần tử trong $B$ ($a_i = \sum_{i = 1}^k c_ib_i, c_i \in \{0, 1\}$) nên xét một tập con bất kì $\{a_1, a_2, \ldots, a_m\}$, khi đó $a_1 + a_2 + \ldots + a_m$ cũng sẽ biểu diễn được thông qua các phần tử trong $B$.

__Code mẫu__

```cpp
int k = (int) basis.size();
int answer = 0;
// duyệt qua tất cả 2^k tập con.
for (int mask = 0; mask < (1 << k); ++mask) {
    int cur = 0; // lưu tổng xor của tập con hiện tại.
    for (int i = 0; i < k; ++i) {
        if (mask & (1 << i)) {
            cur ^= basis[i];
        }
    }
    answer = max(answer, cur);
}
cout << answer << '\n';
```

__Tối ưu hơn__
- Chúng ta có thể dùng ý tưởng tham lam bằng cách ưu tiên set cho bit có `index` lớn hơn trong `res` bằng 1. Vì các bit phía sau dù đều bằng 1 thì vẫn sẽ không tối ưu nếu bit $i$ bằng 0: $2^0 + 2^1 + \ldots + 2^{i - 1} = 2^i - 1 < 2^i$. Độ phức tạp $\mathcal{O}(|B|)$.
```cpp!
int k = (int) basis.size();
// không cần duyệt theo thứ tự giảm dần msb do các giá trị msb trong mảng basis là phân biệt.
int answer = 0;
for (int i = 0; i < k; ++i) {
    answer = max(answer, answer ^ basis[i]);
}
cout << answer << '\n';
```

### [Codefoces 895C - Square subsets](https://codeforces.com/contest/895/problem/C)

__Tóm tắt đề bài__

Cho một mảng $a$ gồm $n$ số nguyên dương. Tìm số cách khác nhau để chọn ra từ mảng $a$ một tập con khác rỗng sao cho tích của các phần tử được chọn là một số chính phương. Hai cách chọn được coi là khác nhau nếu tồn tại một vị trí được chọn bởi tập này mà không được chọn bởi tập kia. 
Do đáp án có thể rất lớn nên bạn cần in ra đáp án sau khi chia lấy dư cho $10^9 + 7$.

__Giới hạn__
- $1 \leq n \leq 10^5$.
- $1 \leq a_i \leq 70$.

__Lời giải__

Bài này có thể giải bằng quy hoạch động bitmask. Nhưng mình sẽ giới thiệu một cách tiếp cận khác đơn giản hơn và độ phức tạp thấp hơn, áp dụng __định lí về hạng và số vô hiệu__ của ma trận.

- Ta biết rằng mọi số nguyên dương $x$ bất kì đều được biểu diễn thành tích các thừa số nguyên tố $p_1^{k_1} \cdot p_2^{k_2} \cdots p_m^{k_m}$ (trong đó $p_i$ là các số nguyên tố, $k_i \ge 0$). $x$ là số chính phương khi và chỉ khi các số $k_1, k_2, \ldots, k_m$ đều là số chẵn.
- Với mỗi số, chúng ta chỉ cần quan tâm các vị trí $i$ mà $k_i$ là số lẻ. Chỉ có $19$ số nguyên tố trong đoạn $[1, 70]$ nên có thể coi mỗi số là một vector trong $\mathbb{Z}_2^{19}$ và phép nhân hai số tương đương với phép cộng hai vector tương ứng. Khi đó số chính phương chính là một vector không ($O$).
- Đặt $v_i$ là vector tương ứng của $a_i$ trong $\mathbb{Z}_2^{19}$. Khi đó ta biểu diễn lại mảng $a$ thành một ma trận kích cỡ $19 \times n$ như sau (các vector $v_i$ được viết ở dạng cột):
	$$M = 
	\begin{bmatrix}
		| & | & \ldots & | \\
		v_1 & v_2 & \ldots & v_n \\
		| & | & \ldots & |
	\end{bmatrix}
	$$
- Chúng ta cần tìm tất cả các vector $x = [x_1, x_2, \ldots, x_n]$ ($x \in \mathbb{Z}_2^n$), trong đó $x_i = 0$ tương ứng với $a_i$ không được chọn và $x_i = 1$ tương ứng với $a_i$ được chọn, sao cho: $$M \cdot x = O$$
- Số vector $x$ thõa mãn chính bằng số vector trong không gian hạch của $M$ và bằng $2^{\text{nullity}(M)}$ (bao gồm cả cách chọn tập rỗng từ $a$). Khi đó đáp án chính là $2^{\text{nullity}(M)} - 1$. 
- Theo định lí về hạng và số vô hiệu: $$\text{rank}(M) + \text{nullity}(M) = \text{số cột} = n$$ Dễ dàng suy ra:
$$\begin{array}{rl}
\text{nullity}(M)
& = n - \text{rank}(M) \\
& = n - \text{dim}(\text{CS}(M)) \\
& = n - \text{dim}(\text{span}(a))
\end{array}$$

__Code mẫu__
```cpp!
#include <bits/stdc++.h>
using namespace std;

const int MOD = (int) 1e9 + 7;

vector<int> primes, basis;
const int MAX_VAL = 70;

void precompute() {
    // Tìm các số nguyên tố <= 70.
    for (int i = 2; i <= MAX_VAL; ++i) {
        bool is_prime = true;
        for (int j = 2; j * j <= i; ++j) {
            if (i % j == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            primes.push_back(i);
        }
    }
}

void insertVector(int mask) {
    for (int i = 0; i < (int) basis.size(); ++i) {
        mask = min(mask, mask ^ basis[i]);
    }
    if (mask != 0) {
        basis.push_back(mask);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();
    int n;
    cin >> n;
    vector<int> a(n), cnt(MAX_VAL + 1);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        cnt[a[i]]++;
    }
    // Tìm vector v tương ứng.
    for (int i = 0; i <= MAX_VAL; ++i) {
        if (!cnt[i]) continue;
        int v = 0, cur = i;
        for (int j = 0; j < (int) primes.size(); ++j) {
            int k = 0;
            while (cur % primes[j] == 0) {
                cur /= primes[j];
                k++;
            }
            // Nếu k lẻ thì đặt bit thứ j bằng 1.
            if (k & 1) {
                v += (1 << j);
            }
        }
        insertVector(v);
    }
    int d = (int) basis.size();
    int nullity = n - d;
    int answer = 1;
    for (int i = 0; i < nullity; ++i) {
        answer = answer * 2 % MOD;
    }
    cout << (answer == 0 ? MOD - 1 : answer - 1) << '\n';
    return 0;
}
```

__Độ phức tạp__
- Đặt $m = max\{a_i\}, d = basis.size()$.
- Độ phức tạp là $\mathcal{O}(m\sqrt{m} + md\log{m} + n) = \mathcal{O}(n)$.

__Tổng quát__

Cho một mảng $a$ gồm $n$ phần tử và một số nguyên $s$. Tìm số tập con của $a$ sao cho tổng xor các phần tử đúng bằng $s$. Giới hạn: $1 \leq n \leq 10^5, 0 \leq a_i < 2^{31}, 0 \leq s < 2^{31}$.

__Phân tích__
- Coi mỗi phần tử $a_i$ là một vector thuộc không gian vector $\mathbb{Z}_2^d$. Biểu diễn lại $a$ bằng một ma trận $M$ kích cỡ $d \times n$ như sau:
	$$M = 
	\begin{bmatrix}
		| & | & \ldots & | \\
		a_1 & a_2 & \ldots & a_n \\
		| & | & \ldots & |
	\end{bmatrix}
	\equiv
	\begin{bmatrix}
		a_{1,1} & a_{2,1} & \cdots & a_{n,1} \\
		a_{1,2} & a_{2,2} & \cdots & a_{n,2} \\
		\vdots & \vdots & \ddots & \vdots \\
		a_{1,d} & a_{2,d} & \cdots & a_{n,d} 
	\end{bmatrix}$$
- Đầu tiên ta cần kiểm tra xem $s$ có thể được biểu diễn thông qua các vector $a_i$ hay không. Nếu không thì đáp án là $0$, ngược lại giả sử $s = a_i + a_{i + 1} + \ldots + a_j$ (với $\{a_i, a_{i + 1}, \ldots, a_j\}$ là một tập con bất kì của $a$).
- Khi đó ta cần tìm số vector $x = [x_1, x_2, \ldots, x_n]$ ($x \in \mathbb{Z}_2^n$) sao cho:
	$$\begin{array}{rl}
	& M \cdot x = s \\
	\Leftrightarrow &
	\begin{cases}
		a_{1, 1}x_1 + a_{2, 1}x_2 + \ldots + a_{n, 1}x_n \\
            \quad \equiv a_{i, 1} + a_{i + 1, 1} + \ldots + a_{j, 1} \pmod 2 \\
		a_{1, 2}x_1 + a_{2, 2}x_2 + \ldots + a_{n, 2}x_n \\
            \quad \equiv a_{i, 2} + a_{i + 1, 2} + \ldots + a_{j, 2} \pmod 2 \\
		\vdots \\
		a_{1, d}x_1 + a_{2, d}x_2 + \ldots + a_{n, d}x_n \\
            \quad \equiv a_{i, d} + a_{i + 1, d} + \ldots + a_{j, d} \pmod 2
	\end{cases}
	\end{array}$$
	Bằng phép biến đổi tương đương ta có được đáp án tương tự.

### [(Zero XOR Subset)-less](https://codeforces.com/contest/1101/problem/G)

__Đề bài__

Cho một mảng các số nguyên $a$ gồm $n$ phần tử.
Nhiệm vụ của bạn là chia mảng đã cho thành nhiều nhất các đoạn, sao cho:
- Mỗi phần tử chỉ thuộc một đoạn.
- Mỗi đoạn chứa ít nhất một phần tử.
- Không tồn tại một tập khác rỗng các đoạn sao cho tổng xor các phần tử bằng $0$.

In ra số đoạn nhiều nhất có thể chia thành. Hoặc $-1$ nếu không tồn tại cách chia.

__Giới hạn__
- $1 \leq n \leq 2 \cdot 10^5$.
- $0 \leq a_i \leq 10^9$.

__Phân tích__
- Ta sẽ xem tổng xor của các phần tử trong mỗi đoạn là một vector trong $\mathbb{Z}_2^{30}$.
- Dễ thấy rằng trong cách chia của đáp án thì tập các vector phải là độc lập tuyến tính.
- Giả sử ta có một cách chia thõa mãn như sau (với số đoạn là nhiều nhất có thể): $[l_1 = 1, r_1], [l_2 = r_1 + 1, r_2], \ldots, [l_m = r_{m - 1} + 1, r_m = n]$. Gọi $v_i$ là tổng xor của đoạn thứ $i$. Khi đó ta có tập $S = \{v_1, v_2, \ldots, v_m\}$ là độc lập tuyến tính và $\mathbf{\text{dim}(\text{span}(S)) = m}$.
- Theo tính chất của tập độc lập tuyến tính thì tập $Q = \{v_1, v_1 + v_2, \ldots, v_1 + v_2 + \ldots + v_m\} = \{p_{r_1}, p_{r_2}, \ldots, p_{r_m}\}$ (với $p_i$ là tổng xor của $i$ phần tử đầu tiên) cũng độc lập tuyến tính và $\text{dim}(\text{span}(Q)) = \text{dim}(\text{span}(S))$.
- Do cách chia trên đã là tối ưu nên ta có thể thêm bất kì $p_i$ nào vào $Q$ mà vẫn giữ nguyên số vector độc lập tuyến tính ($\text{dim}(\text{span}(Q))$ không đổi).
- Đáp án cuối cùng là $\text{dim}(\text{span}(\{p_1, p_2, \ldots, p_n\}))$. Ngoại trừ trường hợp $p_n = 0$ thì không có cách chia nào nên in ra $-1$.

__Code mẫu__
```cpp!
#include <bits/stdc++.h>
using namespace std;

vector<int> basis;
void insertVector(int mask) {
    for (int i = 0; i < (int) basis.size(); ++i) {
        mask = min(mask, mask ^ basis[i]);
    }
    if (mask != 0) {
        basis.push_back(mask);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    int p = 0; // lưu tổng xor của i phần tử đầu tiên.
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        p ^= a[i];
        insertVector(p);
    }
    // nếu p_n = 0 thì không có đáp án.
    if (p == 0) {
        cout << -1 << '\n';
    }
    else {
        cout << basis.size() << '\n'; 
    }
    return 0;
}
```

__Độ phức tạp__

Độ phức tạp là $\mathcal{O}(nd)$ (với $a_i \leq 10^9$ thì $d = basis.size() \leq 30$).

## Bài tập áp dụng

- [Codeforces - Godzilla and Pretty XOR](https://codeforces.com/group/qcIqFPYhVr/contest/203881/problem/S) (bạn cần tham gia nhóm [tại đây](https://codeforces.com/group/qcIqFPYhVr))
- [Codeforces - Round 473 - Div.2 - F](https://codeforces.com/contest/959/problem/F)
- [Atcoder - Xor Battle](https://atcoder.jp/contests/agc045/tasks/agc045_a)
- [Atcoder - Xor Sum 3](https://atcoder.jp/contests/abc141/tasks/abc141_f)
- [Atcoder - Spices](https://atcoder.jp/contests/abc236/tasks/abc236_f)
- [Codeforces - Global round 11 - E. Xum](https://codeforces.com/problemset/problem/1427/E)
- [Hackerearth - Chef & Chutneys](https://www.hackerearth.com/problem/algorithm/chef-f59c8115/)
- [Atcoder - Xor Query](https://atcoder.jp/contests/abc223/tasks/abc223_h)
- [Codeforces - Round 635 - Div.1 - E1](https://codeforces.com/contest/1336/problem/E1)
## Các nguồn tham khảo

- [Codeforces blog - A Beautiful Technique for Some XOR Related Problems](https://codeforces.com/blog/entry/68953)
- [Codeforces blog - 2 Special cases of Gaussian](https://codeforces.com/blog/entry/60003)
- [Benjamin Qi - Vector in $\mathbb{Z}_2^d$](https://drive.google.com/drive/folders/1Ll8EuA3p64JLmzImfQu5qiWvc6_QTa0E?usp=sharing)
- [USACO - Xor basis](https://usaco.guide/adv/xor-basis?lang=cpp)
