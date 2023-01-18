# Khử Gauss-Jordan
Author: Nguyễn Đức Anh

## Giới thiệu
Cho một hệ $n$ phương trình đại số tuyến tính (system of linear algebraic equations - SLAE) với$m$ ẩn. Ta được yêu cầu giải hệ phương trình đó (tức là xác định xem nó có vô nghiệm, chính xác một nghiệm hay vô số nghiệm) và trong trường hợp hệ có ít nhất một nghiệm, hãy đưa ra một nghiệm bất kì của hệ đó. 

Nói tóm lại, ta được yêu cầu giải hệ phường trình sau:
$$
\begin{array}{lcll}
a_{11} x_1 + a_{12} x_2 + & \dots & + a_{1m} x_m &= b_1 \\
a_{21} x_1 + a_{22} x_2 + & \dots & + a_{2m} x_m &= b_2 \\
&\vdots & &  \\
a_{n1} x_1 + a_{n2} x_2 + & \dots & + a_{nm} x_m &= b_n
\end{array}
$$

trong đó $a_{ij}$ $(1 \leqslant i \leqslant n$ và $1 \leqslant j \leqslant m)$ và $b_i$ ( $1 \leqslant i \leqslant n)$ là các hệ số đã biết còn $x_i$ $(1 \leqslant i \leqslant m)$ là các ẩn.

Ngoài ra còn có cách biểu diễn hệ bằng ma trận như sau:
$$Ax = b$$
trong đó $A$ là ma trận kích thước $n \times m$ chứa các hệ số $a_{ij}$ và $b$ là vector độ dài $n$ chứa các hệ số $b_i$.

Đặc biệt, phương pháp này còn có thể áp dụng trong trường hợp các phương trình có kết quả lấy dư cho số nguyên dương $p$ bất kì:
$$
\left\lbrace\begin{array}{lcl}
a_{11} x_1 + a_{12} x_2 + & \dots & + a_{1m} x_m \equiv b_1 \pmod p \\
a_{21} x_1 + a_{22} x_2 + & \dots & + a_{2m} x_m \equiv b_2 \pmod p \\
&\vdots&   \\
a_{n1} x_1 + a_{n2} x_2 + & \dots & + a_{nm} x_m \equiv b_n \pmod p
\end{array}\right.
$$

## Thuật toán
Phương pháp khử Gauss-Jordan dùng cách lần lượt khử các ẩn để đưa hệ phương trình đã cho về một dạng ma trận rồi giải hệ phương trình. Cụ thể hơn, ta sẽ dùng phương trình thứ nhất để khử ẩn $x_1$ trong $n - 1$ phương trình còn lại, tức là biến tất cả các hệ số $a_{i1}$ $(2 \leqslant i \leqslant n)$ thành 0 mà hệ phương trình mới vẫn tương đương với hệ cũ. Tương tự, ta tiếp tục dùng phương trình thứ hai để khử ẩn $x_2$ trong $n - 1$ phương trình còn lại, $\dots$ . 

Đầu tiên ta sẽ định nghĩa 2 phép biến đổi sau:
* Nhân phương trình với số thực $r$ khác $0$: nhân tất cả các hệ số của phương trình với $r$.
* Cộng hai phương trình trong hệ với nhau: Cộng lần lượt các hệ số của phương trình này vào các hệ số của phương trình kia.

Ta dễ dàng thấy sau khi thực hiện các phép biến đổi trên thì hệ mới vẫn tương đương với hệ cũ.

Để thực hiện phép khử Gauss, ta sẽ lần lượt dùng các phương trình khác nhau để khử ẩn $x_i$ $(1 \leqslant i \leqslant min(n, m))$:
* Tìm phương trình $e$ chưa được sử dụng mà có $a_{ei} \ne 0$:
    * Nếu tìm được: Chia tất cả các hệ số của phương trình $e$ cho $a_{ei}$, đánh dấu phương trình $e$ đã được sử dụng và lưu ẩn $x_i$ được phương trình $e$ khử.
    * Không tìm được: Khi đó $x_i$ sẽ là ẩn tự do và ta chuyển sang khử ẩn $x_{i + 1}$ (nói cách khác thì $x_i$ sẽ là một giá trị bất kì).
* Với $n - 1$ phương trình $r$ còn lại $(1 \leqslant r \leqslant n$ và $r \ne e)$, ta sẽ cộng phương trình $r$ với phương trình $e$ nhân $-a_{ri}$. Khi đó, tất cả các hệ số $a_{ri}$ là $0$ còn $a_{ei}$ là $1$.

Sau khi khử xong ta sẽ bắt đầu tìm nghiệm:
* Nếu $n < m$ thì tất cả các ẩn $x_i$ $(n < i \leqslant m)$ sẽ là ẩn tự do.
* Ta sẽ cho luôn các ẩn tự do bằng 0.
* Với các ẩn $x_i$ không phải ẩn tự do, gọi $e$ là phương trình đã dùng để khử $x_i$. Khi đó $a_{ei} = 1$ và tất cả các hệ số $a_{ej}$ còn lại sẽ bằng $0$ hoặc $x_j$ là ẩn tự do và đã được đặt bằng $0$. Từ đó suy ra $x_i = b_e$. 
* Sau đó ta sẽ thử lại hệ phương trình:
    * Không thỏa mãn: hệ vô nghiệm.
    * Thỏa mãn: hệ có ít nhất 1 ẩn tự do thì hệ có vô số nghiệm còn không thì hệ sẽ có 1 nghiệm duy nhất.
    
### Ví dụ:
* Ta sẽ sử dụng ma trận kích thước $n \times (m + 1)$ để biểu diễn hệ phương trình. 
    Mỗi dòng của ma trận là $1$ phương trình, mỗi phương trình có $m$ số đầu tiên là hệ số $a_{ij}$ và số cuối cùng là $b_i$.
    
* Cho hệ phương trình sau:

![](./assets/gauss-elimination/1-example-1.png)

* Dùng phương trình $(1)$ để khử ẩn $x$:
    * Trừ phương trình $(2)$ đi $3$ lần phương trình $(1)$.
    * Cộng phương trình $(2)$ với $2$ lần phương trình $(1)$.
$\Longrightarrow$ Hệ số của ẩn $x$ ở phương trình $(2)$ và $(3)$ sẽ trở thành $0$.

![](./assets/gauss-elimination/2-example-2.png)

* Dùng phương trình $(2)$ để khử ẩn $y$:
    * Trừ phương trình $(1)$ đi $5$ lần phương trình $(2)$.
    * Trừ phương trình $(3)$ đi $2$ lần phương trình $(2)$.
$\Longrightarrow$ Hệ số của ẩn $y$ ở phương trình $(1)$ và $(3)$ sẽ trở thành $0$.


![](./assets/gauss-elimination/3-example-3.png)

* Dùng phương trình $(3)$ để khử ẩn $z$:
    * Trừ phương trình $(1)$ đi $13$ lần phương trình $(3)$.
    * Cộng phương trình $(2)$ với $2$ lần phương trình $(3)$.
$\Longrightarrow$ Hệ số của ẩn $z$ ở phương trình $(1)$ và $(3)$ sẽ trở thành $0$.


![](./assets/gauss-elimination/4-example-4.png)

* Cuối cùng, vì $t$ là ẩn tự do nên ta sẽ đặt $t = 0$.
$\Longrightarrow$ Ta có một nghiệm sau:
$$
\begin{cases}
    x = 3 \\
    y = -1 \\
    z = 7 \\
    t = 0 \\
\end{cases}
$$

*  Ngoài ra, vì có $1$ ẩn tự do là $t$ nên hệ có vô số nghiệm. 
    Một nghiệm khác thỏa mãn là:
$$
\begin{cases}
    x = -121 \\
    y = 18 \\
    z = 18 \\
    t = 1 \\
\end{cases}
$$

### Lưu ý
*  Khi chọn phương trình $e$ có $a_{ei} \ne 0$, ta nên chọn $e$ có $|a_{ei}|$ lớn nhất để các hệ số của phương trình $e$ trở nên nhỏ hơn và tránh tràn số.

## Cài đặt
* Sử dụng `vector<vector<double> > a` để lưu hệ phương trình.
* Dùng `swap` để tất cả các phương trình được sử dụng rồi đều được cho lên đầu của `a`.
$\Rightarrow$ Dùng 2 còn trỏ $row$ và $col$ cho biết chỉ còn những phương trình từ $row$ đến $n - 1$ chưa được sử dụng và đang khử đến ẩn $x_{col}$.
* `where[i]` để lưu vị trí phương trình khử ẩn $x_i$.
* Hàm `int gauss(vector<vector<double> > a, vector<double> &ans)` để giải hệ. Hàm sẽ trả về:
    * 0: hệ vô nghiệm.
    * 1: hệ có một nghiệm duy nhất.
    * 2: hệ có vô số nghiệm.

    Trong trường hợp hệ có ít nhất một nghiệm thì `ans` sẽ lưu 1 nghiệm của hệ phương trình.


```cpp!
const double eps = 1e-9;

int gauss(vector < vector < double > > a, vector < double > & ans) {
  int n = (int) a.size(); // số phương trình
  int m = (int) a[0].size() - 1; // số ẩn

  vector < int > where(m, -1);
  for (int col = 0, row = 0; col < m && row < n; col++) {
    int e = row;
    for (int i = row + 1; i < n; i++) {
      if (abs(a[i][col]) > abs(a[e][col])) { // chọn phương trình e 
        // có abs(a[e][col]) lớn nhất
        e = i;
      }
    }

    if (abs(a[e][col]) < eps) // tất cả các hệ số a[e][col] đều bằng 0
      // => ẩn x[col] là ẩn tự do
      continue; // chuyển sang khử x[col + 1]

    swap(a[e], a[row]); // chuyển phương trình e lên đầu

    where[col] = row; // ẩn x[col] được khử bởi phương trình đang ở vị trí row

    /* chuyển hệ số a[row][col] về 1 */
    double tmp = a[row][col];
    for (int i = 0; i <= m; i++) {
      a[row][i] /= tmp;
    }

    /* khử hệ số a[i][col] ở toàn bộ n - 1 phương trình còn lại */
    for (int i = 0; i < n; i++) {
      if (i != row) {
        double c = a[i][col];
        for (int j = col; j <= m; j++) { // chỉ cần for từ col tại vì 
          // a[row][p] (p < col) đã bằng 0 
          a[i][j] -= a[row][j] * c;
        }
      }
    }

    row++; // phương trình ở vị trí row đã được sử dụng
  }

  ans.assign(m, 0); // gán tất cả các ẩn ban đầu 0
  for (int i = 0; i < m; i++) {
    if (where[i] != -1) {
      ans[i] = a[where[i]][m]; // nếu x[i] không phải ẩn tự do thì 
      // x[i] = b[where[i]]
    }
  }

  /* Thử lại */
  for (int i = 0; i < n; i++) {
    double sum = 0;
    for (int j = 0; j < m; j++) {
      sum += ans[j] * a[i][j];
    }
    if (abs(sum - a[i][m]) > eps) // sum != b[i]
      return 0;
  }

  for (int i = 0; i < m; i++)
    if (where[i] == -1) // nếu có ít nhất 1 ẩn tự do thì
      // hệ có vô số nghiệm
      return 2;
  return 1;
}
```


Sau khi cài đặt xong, bạn đọc có thể nộp thử ở [đây](https://hnoj.edu.vn/problem/khu_gauss).


## Độ phức tạp
### Phần khử các ẩn: 
Ta phải thực hiện khử các ẩn $min(n, m)$ lần:
* Ta phải tìm phương trình $e$ chưa sử dụng có $|a_{ei}|$ lớn nhất mất $\mathcal{O}(n)$.
* Khử ẩn $x_i$ ở tất cả các phương trình khác mất $\mathcal{O}(nm)$.

### Phần tìm nghiệm:
Ta mất $\mathcal{O}(m)$ để tìm tất cả các nghiệm và mất $\mathcal{O}(nm)$ để thử lại.

 $\Longrightarrow$ Độ phức tạp cuối cùng sẽ là $\mathcal{O}(min(n, m)nm)$. Trong trường hợp $n = m$ thì độ phức tạp chỉ đơn giản là $\mathcal{O}(n ^ 3)$.

### Độ phức tạp bộ nhớ: $\mathcal{O}(nm)$.

## Cải tiến tốc độ
Với cách cài đặt ở trên, mỗi lần khử ẩn $x_i$ ta lại phải thực hiện phép cộng với tất cả $n - 1$ phương trình còn lại, kể cả các phương trình đã sử dụng. Vì thế ta có thể bỏ qua không cộng các phương trình đã sử dụng và giảm số lần cộng đi một nửa. 
Nếu ta bỏ qua các phương trình đã sử dụng thì một phương trình vẫn có thể có nhiều hệ số $a_{ij}$ khác $0$ (với các $j > n$ ta tạm coi $a_{ij}$ là $0$ bởi vì $x_j$ là hệ số tự do và đã được cho là $0$). Tuy nhiên, ở phương trình $e_n$ để khử ẩn $x_n$ chỉ có $a_{e_nn} \ne 0$, phương trình $e_{n - 1}$ chỉ có $a_{e_{n - 1}{n - 1}} \ne 0$ và $a_{e_{n - 1}n} \ne 0$, $\dots$ (Hay nói cách khác, thay vì ma trận A trở thành ma trận đơn vị thì nó sẽ trở thành hình tam giác). Từ đó, ta có thể dùng phương trình $e_n$ để tính $x_n$ rồi thay vào phương trình $e_{n - 1}$ để tính $x_{n - 1}$, $\dots$ .
Vì thế, việc tìm nghiệm chỉ tốn $\mathcal{O}(nm)$ còn việc khử ẩn thì đã giảm được một nửa số lần phải cộng 2 phương trình.
$\Longrightarrow$ Tốc độ chạy gần như nhanh gấp đôi.

![](./assets/gauss-elimination/5-benchmark.png)

## Giải các hệ có modulo
Việc giải các hệ phương trình có modulo sẽ hơi khác ở phần khử ẩn vì các hệ số đều là số nguyên. Ta sẽ không chia để cho hệ số $a_{ei}$ về $1$ nữa mà nhân phương trình $r$ với $a_{ei}$ rồi trừ đi phương trình $e$ nhân $a_{ri}$. Từ đó hệ số $a_{ri}$ sẽ vẫn về $0$.

```cpp!
for (int r = 0; r < n; r++) {
  if (r != e) {
    S[r] = S[r] * S[e].a[i] + S[e] * (-S[r].a[i]);
  }
}
```

Tuy nhiên, với trường hợp modulo 2 ta có thể sử dụng bitset để tăng tốc độ xử lý.
Ở cách cài đặt dưới đây, ta sẽ chỉ dùng `vector<bitset<maxm> >` để biểu diễn cả hệ phương trình (bit thứ m của phương trình $i$ sẽ là $b_i$) và `ans` sẽ là `bitset<maxm>`.

```cpp!
int gauss(vector < bitset < maxm > > a, bitset < maxm > & ans) {
  int n = a.size();
  int m = maxm - 1;
  vector < int > where(m, -1);
  for (int col = 0, row = 0; col < m && row < n; col++) {
    for (int i = row; i < n; i++) {
      if (a[i][col]) {
        swap(a[i], a[row]); // a[e][col] lớn nhất có thể chỉ là 1
        break;
      }
    }

    if (!a[row][col])
      continue;

    where[col] = row;

    for (int i = 0; i < n; i++) {
      if (i != row && a[i][col]) {
        a[i] ^= a[row]; // Việc khử ẩn chỉ cần dùng phép XOR là được
        // nên tốc độ xử lí nhanh hơn rất nhiều
      }
    }
    row++;
  }
  // Phần tìm nghiệm tương tự như trên
}
```


## Ứng dụng
Ngoài ứng dụng cho việc giải hệ phương trình, khử gauss còn có thể áp dụng vào tìm số nghiệm của phương trình có modulo, tìm số ẩn tự do, tìm ma trận nghịch đảo, $\dots$ . Tuy nhiên, ở đây chỉ có những ứng dụng đơn giản của khử gauss.

## Ví dụ $1$ -- [FINDGRAPH - HNOJ](https://hnoj.edu.vn/problem/findgraph)

### Đề bài
Cho đồ thị vô hướng và số nguyên tố $p$, mỗi đỉnh có trọng số $x_i$ $(0 \leqslant x_i < p)$. Mỗi đỉnh $u$ sẽ có một số nguyên $b_u$ $(0 \leqslant b_u < p)$ thỏa mãn $b_u = \Sigma x_v (mod$ $p)$ với tất cả các đỉnh $v$ có cạnh nối trực tiếp với $u$.
**Yêu cầu:** Cho đồ thị và mảng $b$ $(0 \leqslant b_i < p)$, hãy đếm số lượng mảng $a$ thỏa mãn. Dữ liệu đảm bảo tồn tại ít nhất $1$ nghiệm thỏa mãn.

### INPUT
* Dòng đầu chứa 3 số nguyên $n$, $m$, $p$ $(1 \leqslant n \leqslant 100,$ $1 \leqslant m \leqslant 200,$  $p \leqslant 10 ^ 9)$ lần lượt là số đỉnh, số cạnh và số nguyên tố $p$.
* Dòng tiếp theo là $n$ số nguyên của mảng $b$, mỗi số cách nhau $1$ dấu cách.
* $m$ dòng sau, mỗi dòng là $2$ số $u$, $v$ cho biết có cạnh nối giữa $u$ và $v$.

### OUTPUT
* Một số nguyên duy nhất là số lượng mảng $a$ thỏa mãn lấy dư cho $10^9+7$.

### SAMPLE TEST
**Input:**
```
5 5 13
5 20 0 23 5 
1 4
2 1
2 4
4 5
5 2
```

**Output:**
```
2197
```


### Phân tích
* Ta có thể đưa bài toán trở thành đếm số nghiệm của hệ phương trình sau:
$$
\begin{array}{lcl}
a_{11} x_1 + a_{12} x_2 + &\dots& + a_{1m} x_m \equiv b_1 \pmod p \\
a_{21} x_1 + a_{22} x_2 + &\dots& + a_{2m} x_m \equiv b_2 \pmod p \\
&\vdots& \\
a_{n1} x_1 + a_{n2} x_2 + &\dots& + a_{nm} x_m \equiv b_n \pmod p
\end{array}
$$
với $a_{uv} = 1$ khi và chỉ khi giữa $u$ và $v$ có cạnh nối trực tiếp, ngược lại thì $a_{uv} = 0$.

* Giả sử hệ phương trình trên có $k$ ẩn $x$ là ẩn tự do, khi ta cố định cả $k$ ẩn đó thì tất cả các ẩn khác cũng sẽ được cố định.
$\rightarrow$ Với mỗi bộ $k$ số để gán vào các ẩn tự do đó, ta sẽ tìm được đúng $1$ nghiệm thỏa mãn.

$\Longrightarrow$ Nếu ta tìm được $k$ ẩn tự do thì đáp án sẽ là $p ^ k$.



### Cài đặt
**Bước 1:** Tạo đồ thị.
**Bước 2:** Tạo hệ phương trình.
**Bước 3:** Khử các ẩn như ở trên, chỉ khác là ta có thêm biến `count` để đếm số lượng ẩn tự do.
**Bước 4:** Vì dữ liệu đảm bảo tồn tại ít nhất $1$ nghiệm thỏa mãn nên kết quả sẽ là $p^{count}$.


## Ví dụ $2$ -- [Codeforces - 1155E](https://codeforces.com/contest/1155/problem/E)
### Đề bài 
Có một đa thức bậc $k$ $(k \leqslant 10)$ có hệ số nguyên: 

$$\begin{array}{rl}
f(x) = & a_0 + a_1 \times x + a_2 \times x^2 + \\
       & \qquad + \dots + a_k \times x^k \quad(0 \leqslant a_i < 10^6 + 3)
\end{array}$$

Ta được đưa ra tối đa $50$ câu hỏi có dạng "? $x_0$" $(x_0 \in \mathbb{Z}$, $0 \leqslant x_0 < 10^6 + 3)$, với mỗi câu hỏi chương trình sẽ trả về giá trị của $f(x_0)$ mod $10^6 + 3$.
Hãy tìm giá trị $x_0$ sao cho $f(x_0) \equiv 0 \pmod {10^6+3}$. Nếu tìm được $x_0$ thỏa mãn thì in ra "! $x_0$", còn không thì in ra "! $-1$".

### Phân tích
* Nếu ta hỏi "? $0$" thì ta sẽ được giá trị của $a_0$.
* Nếu ta hỏi $k$ câu hỏi thì ta sẽ được hệ phương trình như sau (theo modulo $10^6 + 3$):
$$
\begin{array}{lcl}
a_{0} + a_{1} x_1 + a_{2} x_1^2 + &\dots& + a_{k}x_1^k \equiv b_1  \\
a_{0} + a_{1} x_2 + a_{2} x_2^2 + &\dots& + a_{k}x_2^k \equiv b_2  \\
&\vdots& \\
a_{0} + a_{1} x_k + a_{2} x_k^2 + &\dots& + a_{k}x_k^k \equiv b_k 
\end{array}
$$
Mà tất cả các ẩn $x_1, x_2, \dots, x_k$ ta đã biết nên bài toán trở thành giải hệ phương trình để tìm các hệ số $a_i$.

$\Longrightarrow$ Ta sẽ thử tìm đa thức $f(x)$ rồi thử với tất cả các giá trị $x$ từ $0$ đến $10^6+2$.

### Cài đặt
**Bước 1:** Thử $x_0 = 0$ để tìm $a_0$.
**Bước 2:** Hỏi khoảng $15$ câu hỏi với các giá trị $x_0$ random từ $1$ đến $10^6+2$.
**Bước 3:** Với mỗi $k$ từ $0$ đến $10,$ ta sẽ lập hệ phương trình và tìm các hệ số $a_i$. Sau đó thử lại với cả $15$ giá trị $x_0$ ở trên, nếu thỏa mãn thì đấy chính là đa thức cần tìm. Còn nếu tất cả $k$ từ $0$ đến $10$ đến không thỏa mãn thì in ra "! $-1$".
**Bước 4:** Thử thay tất cả các $x$ từ $0$ đến $10^6+2$ vào đa thức, nếu $f(x) \equiv 0 \pmod {10^6+3}$ thì kết quả chính là $x$.


## Ví dụ $3$ -- [FSMAX - HNOJ](https://hnoj.edu.vn/problem/fsmax)
### Đề bài
Một tập các số được gọi là đẹp nếu không tồn tại một tập con nào của tập đó có tích là số chính phương. Cho dãy $A$ có $n$ số tự nhiên, hãy tìm tập con đẹp có nhiều phân từ nhất của $A$.

### INPUT
* Dòng đầu chứa số nguyên dương $n$ $(n \leqslant 1000)$.
* Dòng sau chứa $n$ số tự nhiên của dãy $A$ $(1 \leqslant A_i \leqslant 1000)$.

### OUTPUT
* Một số nguyên duy nhất là số lượng phần từ lớn nhất của tập con.

### SAMPLE TEST
**Input:**
```
5
8 2 1 6 7 
```

**Output:**
```
3
```

### Phân tích
* Số chính phương là số khi phân tích số đó thành tích các số nguyên tố thì tất cả các số mũ đều là chẵn.
$\Longrightarrow$ Ta chỉ cần quan tâm đến tính chẵn lẽ của các số mũ nên có thể sử dụng bitset để lưu các giá trị $A_i$. Nếu ta đặt mỗi bit là một số nguyên tố thì chỉ cần $168$ bit là được.
* Một tập các số có tích là số chính phương tức là XOR của tất cả các bitset của các số đó là $0$. 
* Hint:  Nếu ta coi mỗi bitset là các hệ số của vế trái 1 phương trình thì kết quả chính là số lượng ẩn không phải ẩn tự do.

### Cài đặt
* [Cài đặt mẫu](https://ideone.com/SfwHl6).
* Bạn đọc hãy thử code trước khi xem code mẫu.

## Một số bài tập ứng dụng
* [SPOJ - XMAX](https://www.spoj.com/problems/XMAX/)
* [Codechef - KNGHTMOV](https://www.codechef.com/SEP12/problems/KNGHTMOV)
* [Codeforces - 1411G](https://codeforces.com/problemset/problem/1411/G)
* [Codeforces - 1060H](https://codeforces.com/contest/1060/problem/H)
* [Codeforces - 1100F](https://codeforces.com/contest/1100/problem/F)
* [Codeforces - 1101G](https://codeforces.com/contest/1101/problem/G)
* [Codeforces - 1336E1](https://codeforces.com/contest/1336/problem/E1)
* [Codeforces - 504D](https://codeforces.com/contest/504/problem/D)

