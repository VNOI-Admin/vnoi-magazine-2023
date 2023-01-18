# Bổ đề cháy cạnh
(Bổ đề Burnside & Định lý liệt kê Pólya)

Author: Nguyễn Hoàng Dũng

## Giới thiệu

Nếu bạn đã hoặc đang là một học sinh phổ thông, có lẽ câu hỏi dưới đây sẽ không quá xa lạ gì với các bạn:

> Đếm số đồng phân của các chất sau: $C_6H_4ClBr$, $C_6H_2Cl_2Br_2$, $C_6H_2IClBr_2$.

...

Mình sẽ lấy một ví dụ khác nhẹ nhàng hơn:

> Đếm số chuỗi hạt gồm $5$ hạt được tạo bởi các hạt màu đỏ, tím, vàng. Hay tổng quát hơn là đếm số chuỗi hạt gồm $n$ hạt được tạo bởi $k$ màu. 

![](./assets/burnside-lemma/1-example1.png)


Do mỗi hạt có $k$ cách tô nên hiển nhiên $n$ hạt sẽ có $k^n$ cách tô. 

Thực tế thì kết quả không đơn giản như vậy, chuỗi hạt của chúng ta có thể được xoay hoặc lật nên cách đếm ngây thơ sẽ không đúng.

![](./assets/burnside-lemma/2-example2.png)


Vậy, chúng ta sẽ giải quyết những bài toán đếm này như thế nào?

**Lý thuyết nhóm**, hay chính xác hơn, **bổ đề Burnside** sẽ cho chúng ta một phương pháp phù hợp để giải những dạng bài như trên.

## Bổ đề Burnside

*Công thức của Bổ đề Burnside được chứng minh bởi Burnside vào năm 1897, nhưng trước đó nó đã được khám phá ra vào năm 1887 bởi Frobenius, và sớm hơn nữa vào năm 1845 bởi Cauchy. Do đó thi thoảng nó cũng được gọi là Bổ đề Cauchy-Frobenius. Thú vị hơn là chính bản thân Burnside cũng viết trong cuốn sách của mình rằng khám phá này là của Frobenius.* <!-- ¯\\\_(ツ)\_/¯ -->

### Kiến thức cần biết (Giới thiệu qua về lý thuyết nhóm)

Do bổ đề Burnside là một kết quả từ lý thuyết nhóm, nên ta cần hiểu một số định nghĩa sau đây:

#### Nhóm, nhóm đối xứng

Trước hết, ta cần hiểu rõ về các phép biến đổi đối xứng, nghĩa là các phép biến đổi mà dưới tác động của chúng, hai chuỗi hạt được coi là một. Các phép biến đổi này sẽ tạo thành một **nhóm**.

Phép biến đổi đầu tiên, quan trọng nhất nhưng cũng kém thú vị nhất là phép biến đổi đơn vị: đơn giản là không làm gì cả:

![](./assets/burnside-lemma/3-symmetry.png)


Phép biến đổi thứ hai là phép xoay:

![](./assets/burnside-lemma/4-rotate.png)


Và phép biến đổi cuối cùng là phép lật:

![](./assets/burnside-lemma/5-flip.png)


Khi nói về nhóm, ta cũng phải quan tâm đến phép toán của nhóm, nhưng trong trường hợp này, kết quả của sự kết hợp (phép hợp) các phép xoay và lật với nhau, cũng ra các phép xoay và lật.

Định nghĩa chính xác của nhóm là:

> Một **nhóm** là một cặp $(G, +)$, với $G$ là một tập không rỗng và $+ : G × G → G$ là một phép toán thỏa mãn điều kiện:
> * **Tính kết hợp**: $(a + b) + c = a + (b + c)$ với mọi $a, b, c \in G$.
> * **Phần tử đơn vị**: Tồn tại $0 \in G$ sao cho $0 + a = a + 0 = a$ với mọi $a \in G$.
> * **Phần tử nghịch đảo**: Với mọi $a \in G$, tồn tại một phẩn tử nghịch đảo $-a \in G$ sao cho $a + (-a) = (-a) + a = 0$.

Nghĩ theo góc độ các phép biến đổi đối xứng, phần tử đơn vị có nghĩa là tồn tại phép biến đổi không làm gì cả, phần tử nghịch đảo nghĩa là mỗi phép biến đổi có cách làm ngược lại, và tính kết hợp nghĩa là các phép biến đổi hoạt động "ổn" khi ta cho thêm dấu ngoặc vào.

Trong trường hợp của chúng ta thì, nhóm $G$ gồm các phép biến đổi đối xứng, phép toán là hợp của hai phép biến đổi và phần tử đơn vị là không làm gì. Trong lý thuyết nhóm, đây còn được gọi là nhóm nhị diện $D_n$.

Ngoài ra còn nhiều ví dụ về nhóm khác như, tập số nguyên với phép cộng $(\mathbb{Z}, +)$, tập số thực khác $0$ với phép nhân $(\mathbb{R} \setminus \{0\}, \times)$, ...

Một **nhóm đối xứng** là một nhóm mà phần tử của nó là các phép biến đổi của một đối tượng, và phép toán là phép toán hợp $\circ$ (giống như hợp của các hàm), ví dụ như phép xoay / lật như trên.

Một nhóm đối xứng đáng ra được viết là $(G, \circ)$ với tập các phép biến đổi và phép hợp được viết rõ ràng, nhưng phép hợp thường được ngụ ý hiểu, do đó một nhóm đối xứng thường được viết đơn giản là $G$.

#### Tác động nhóm

Ta có một tập $S$, ta nói nhóm $G$ *tác động* lên tập $S$ nếu với mọi phần tử $g$ trong $G$ và phần tử $s$ trong $S$, tồn tại $g \cdot s$ trong $S$ từ tác động của $G$ lên $s$, sao cho thỏa mãn 2 điều kiện sau:

1. Phần tử đơn vị $e$ là phần tử đơn vị trên $S$. Nghĩa là, với mọi $s$ trong $S$, $e \cdot s = s$.
2. Tác động nhóm phù hợp với phép toán của nhóm. Nghĩa là, với mọi $g$, $h$ trong $G$ và $s$ trong $S$, $(gh) \cdot s = g \cdot (h \cdot s)$

Xét với trường hợp của chúng ta, ta sẽ xét tập $S$ của tất cả các cách tô màu một chuỗi hạt (cả $k^n$ theo cách đếm ngây thơ).

Và bây giờ nhóm $D_n$ bên trên tác động lên $S$. Một phép xoay một cách tô màu sẽ ra một phép tô màu, và một phép lật cũng thế.

Với 2 cách tô màu trong $S$, nếu có thể biến từ một cách sang cách khác bằng phép xoay và lật, thì nó sẽ ứng với cùng một chuỗi hạt. Nghĩa là tác động của $D_n$ lên $S$ có thể biến đổi một cái thành cái kia. Trong lý thuyết nhóm, ta nói rằng hai cách tô màu ở trong cùng một **quỹ đạo** của $G$.

Nói một cách chính xác:

> Quỹ đạo của một phần tử $s$ là tất cả các phần tử $s'$ sao cho $s'$ có thể biến đổi được từ $S$ bằng một tác động, nghĩa là tồn tại $g$ trong $G$ sao cho $g \cdot s = s'$

Vậy thì hai cách tô màu ở trong cùng một quỹ đạo (có thể biến đổi từ một cái sang cái còn lại chỉ bằng xoay và lật) sẽ ứng với cùng một chuỗi hạt. Một quỹ đạo sẽ ứng với duy nhất một chuỗi hạt, và dễ thấy với mỗi chuỗi hạt có duy nhất một quỹ đạo ứng với nó. Vậy, để đếm số chuỗi hạt, ta sẽ đếm số quỹ đạo.

![](./assets/burnside-lemma/6-orbit.png)


Vậy chúng ta đếm số lượng quỹ đạo như thế nào?

### Phát biểu bổ đề

> **Bổ đề Burnside**:
> 
> Gọi $G$ là nhóm hữu hạn các phép biến đổi tác động lên tập $X$. Gọi $X / G$ là tập các quỹ đạo của $X$ (mỗi phần tử của $X / G$ là một quỹ đạo của $X$). Với mọi phần tử $g \in G$, gọi $X^g$ là tập các điểm bất biến (cố định) của $X$ đối với phép biến đổi $g$ ($X^g = \{x \in X \colon g \cdot x = x\}$). Khi đó,
> 
> $$|X / G| = \frac{1}{|G|} \sum_{g \in G} |X^g|$$

### Chứng minh bổ đề

*Việc chứng minh bổ đề Burnside không quá quan trọng đối với các ứng dụng thực tế, vì vậy nó sẽ được coi là bài tập cho bạn đọc.*  <!-- ¯\\\_(ツ)\_/¯ -->

### Ứng dụng

Với bổ đề Burnside, chúng ta có thể giải quyết bài toán. Để cho đơn giản, ta hãy lấy $n = 5$. Khi đó, với mọi phần tử của $D_5$, ta phải đếm số lượng điểm mà nó cố định (số cách tô tương đương sau khi được xoay hoặc lật).

Đầu tiên, xét phần tử đơn vị, vì nó không làm gì nên nó sẽ cố định tất cả $k^5$ cách tô màu:

![](./assets/burnside-lemma/7-application.png)


Sau đó xét tới phép lật. Mỗi phép lật có trục đi qua các hạt như sau:

![](./assets/burnside-lemma/8-flip-through-axis.png)


Và bốn hạt còn lại được chia thành hai nhóm, đối xứng với nhau qua trục:

![](./assets/burnside-lemma/9-flip-through-axis2.png)


Vậy để một cách tô màu được cố định bởi phép lật, hạt ở trên trục có thể tô bất cứ màu nào, và các hạt khác phải cùng màu với hạt đối xứng với nó. Do đó với mỗi trục ta cố định được $k^3$ phần tử. Vì có $5$ trục đi qua mỗi hạt, ta có tổng cộng $5k^3$.

Cuối cùng, xét tới phép xoay. Đầu tiên là xoay 72 độ theo chiều kim đồng hồ (chuyển tất cả các hạt sang hạt bên cạnh theo chiều kim đồng hồ):

![](./assets/burnside-lemma/10-rotate.png)


Để cách tô được cố định bởi phép xoay này, hạt 1 phải giống hạt 2, hạt 2 phải giống hạt 3, 3 giống 4, 4 giống 5 và 5 giống 1. Do đó tất cả các hạt phải có cùng màu, nghĩa là có $n$ cách tô.

Với ba cách xoay còn lại chúng ta có thể lập luận tương tự, vậy tổng lại phép quay có $4k$ cách tô.

Theo bổ đề Burnside, số lượng quỹ đạo, cũng là số lượng chuỗi hạt, là:

$$ \frac{k^5+5k^3+4k}{10} $$

## Định lý liệt kê Pólya

Ta có thể phần nào thấy rằng việc chọn $k = 5$ là một số nguyên tố khiến cho phép xoay chỉ có thể tô cùng một màu, vậy nếu $k$ khác đi thì sao, hoặc với $k$ lớn hơn và ta không còn có thể xét tay như trên?

Định lý liệt kê Pólya sẽ giúp ta làm điều đó.

Định lý liệt kê Pólya là một tổng quát của bổ đề Burnside, và nó cũng cung cấp một công cụ thuận tiện hơn để tìm số lớp tương đương. Ở đây chúng ta chỉ nhắc đến một trường hợp đặc biệt của định lý liệt kê Pólya, trường hợp này sẽ rất hữu ích trong thực tế. Công thức chung của định lý sẽ không được nhắc đến.

*Định lý này đã được Redfield phát hiện trước Pólya vào năm 1927, nhưng công bố của ông không được các nhà toán học chú ý. Pólya độc lập đạt được kết quả tương tự vào năm 1937, và công bố của ông thành công hơn.* <!-- ¯\\\_(ツ)\_/¯ -->

Với trường hợp của chúng ta, ta đánh số các hạt từ $1$ đến $k$ và coi như các phép xoay và lật là các **hoán vị bất biến** (nghĩa là hoán vị không thay đổi đối tượng mà chỉ là cách biểu diễn), phép toán là phép hợp hai hoán vị. Và nhóm $G$ khi đó ta sẽ gọi là **nhóm các hoán vị bất biến**. 

*Tìm tất cả các hoán vị bất biến như vậy với định nghĩa của một đối tượng là một bước quan trọng để áp dụng bổ đề Burnside và định lý liệt kê Pólya. Những hoán vị bất biến này phụ thuộc vào từng bài toán cụ thể nhưng trong hầu hết các trường hợp, việc tìm một số hoán vị “cơ bản” bằng tay là đủ để sinh ra tất cả các hoán vị khác bằng máy.*

Sau đó, ta có thể phát biểu định lý như sau:

### Phát biểu định lý

> **Trường hợp đặc biệt của định lý liệt kê Pólya**:
> 
> Ta gọi $C(\pi)$ là số chu trình trong hoán vị $\pi$, $k$ là số giá trị mà mỗi phần tử có thể nhận. Khi đó,
> 
> $$|X / G| = \frac{1}{|G|} \sum_{\pi \in G} k^{C(\pi)}$$

### Chứng minh định lý

*Định lý liệt kê Pólya là hệ quả trực tiếp của bổ đề Burnside, vì vậy việc chứng minh nó sẽ được coi là bài tập cho bạn đọc.* <!-- ¯\\\_(ツ)\_/¯ -->

### Ứng dụng: Tô màu vòng cổ

![](./assets/burnside-lemma/11-application.png)

> Đếm số vòng cổ khác nhau từ $n$ hạt, mỗi hạt có thể được tô bằng một trong các màu $k$. Khi so sánh hai vòng cổ, chúng có thể được xoay, nhưng không được đảo ngược (tức là chỉ cho phép dịch chuyển vòng tròn).

(Đây là phiên bản dễ hơn của bài toán ở trên mà không có phép lật.)

Trong bài toán này ta có thể tìm ngay được nhóm các hoán vị bất biến:

$$\begin{array}{rl}
\pi_0 &= 1 2 3 \dots n\\
\pi_1 &= 2 3 \dots n 1\\
\pi_2 &= 3 \dots n 12\\
&\dots\\
\pi_{n-1} &= n 1 2 3\dots\end{array}$$

Ta hãy tìm một công thức rõ ràng để tính toán $C(\pi_i)$. Trước tiên, chúng tôi lưu ý rằng hoán vị $\pi_i$ có ở vị trí $j$-th giá trị $i + j$ (tính theo mô-đun $n$). Nếu ta xét cấu trúc chu trình cho $\pi_i$, ta thấy rằng $1$ chuyển thành $1 + i$, $1 + i$ chuyển thành $1 + 2i$, chuyển thành $1 + 3i$, v.v., cho đến một số có dạng $1 + k n$. Lập luận tương tự cho các phần tử còn lại. Do đó, chúng ta thấy rằng tất cả các chu trình đều có cùng độ dài, cụ thể là $\frac{\text{lcm}(i, n)}{i} = \frac{n}{\gcd(i, n)}$. Vì vậy, số chu kỳ trong $\pi_i$ sẽ bằng $\gcd(i, n)$.

Thay các giá trị này vào định lý liệt kê Pólya, ta thu được công thức:

$$\frac{1}{n} \sum_{i=1}^n k^{\gcd(i, n)}$$

Bạn có thể để công thức này ở dạng này hoặc bạn có thể đơn giản hóa nó hơn nữa. Hãy thay đổi thứ tự tính tổng để nó lặp trên tất cả các ước của $n$. Trong công thức ban đầu sẽ có nhiều số hạng tương đương: nếu $i$ không phải là ước của $n$, thì có thể tìm được ước sau khi tính $\gcd(i, n)$. Do đó, đối với mỗi ước số $d ~|~ n$ số hạng của nó $k^{\gcd(d, n)} = k^d$ sẽ xuất hiện trong tổng nhiều lần, tức là câu trả lời cho bài toán có thể được viết lại thành

$$\frac{1}{n} \sum_{d ~|~ n} C_d k^d,$$

trong đó $C_d$ là số các số $i$ với $\gcd(i, n) = d$. Chúng ta có thể tìm được một biểu thức rõ ràng cho giá trị này. Bất kỳ số $i$ nào như vậy đều có dạng $i = d j$ với $\gcd(j, n / d) = 1$ (nếu không thì $\gcd(i, n) > d$). Vì vậy, chúng tôi có thể đếm số $j$ với tính chất này. Phi hàm Euler cho ta $C_d = \phi(n / d)$, và do đó ta có đáp án:

$$\frac{1}{n} \sum_{d ~|~ n} \phi\left(\frac{n}{d}\right) k^d$$

Cài đặt mẫu:

```cpp=
#include <bits/stdc++.h>
using namespace std;

const int MOD = (int)1e9 + 7;

int power(int a, int b) {
    int ans = 1;
    while (b > 0) {
        if (b % 2 == 1) {
            ans = 1LL * ans * a % MOD;
        }
        a = 1LL * a * a % MOD;
        b /= 2;
    }
    return ans;
}

int inverse(int a) {
    return power(a, MOD - 2);
}

int main() {
    int t;
    cin >> t;
    
    for (int tc = 1; tc <= t; tc++) {
        int n, k;
        cin >> n >> k;
        
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            ans = (ans + power(k, __gcd(i, n))) % MOD;
        }
        
        ans = 1LL * ans * inverse(n) % MOD;
        cout << "Case " << tc << ": " << ans << '\n';
    }    
}
```

### Ứng dụng: Tô màu hình xuyến
![](./assets/burnside-lemma/12-application.png)

Thông thường, chúng ta không thể có được một công thức rõ ràng cho số lớp tương đương. Trong nhiều bài toán, số lượng hoán vị trong một nhóm có thể quá lớn để tính toán thủ công và không thể tính toán số chu trình trong chúng.

Trong trường hợp đó, ta nên tìm một số hoán vị "cơ bản" một cách thủ công để sinh ra toàn bộ nhóm $G$. Tiếp theo, chúng ta có thể viết một chương trình sẽ sinh tất cả các hoán vị của nhóm $G$, đếm số chu trình trong chúng và tính đáp án bằng công thức.

> Xét ví dụ về bài toán tô màu hình xuyến.
> Có một tờ giấy kẻ ca-rô $n \times m$ ($n < m$), một số ô được tô màu đen.
> 
> Sau đó, một hình trụ thu được bằng cách dán hai mặt có chiều dài $m$ lại với nhau. Sau đó, một hình xuyến thu được từ hình trụ bằng cách dán hai vòng tròn (trên và dưới) lại với nhau mà không xoắn. Nhiệm vụ là tính toán số lượng hình xuyến có màu khác nhau, giả sử rằng chúng ta không thể nhìn thấy các đường được dán và hình xuyến có thể được xoay.

Chúng ta lại bắt đầu với một tờ giấy $n \times m$. Dễ dàng thấy rằng các loại phép biến đổi sau bảo toàn lớp tương đương: sự dịch chuyển vòng tròn của các hàng, sự dịch chuyển vòng tròn của các cột và xoay tờ giấy $180^\circ$. Cũng dễ dàng nhận thấy rằng các phép biến hình này có thể sinh ra toàn bộ nhóm các phép biến hình bất biến. Nếu bằng cách nào đó chúng ta đánh số các ô của tờ giấy, thì chúng ta có thể viết ba hoán vị $p_1$, $p_2$, $p_3$ tương ứng với các kiểu biến đổi này.

Tiếp theo, chỉ còn việc tạo ra tất cả các hoán vị thu được dưới dạng một tích. Hiển nhiên là tất cả các hoán vị như vậy đều có dạng $p_1^{i_1} p_2^{i_2} p_3^{i_3}$ trong đó $i_1 = 0 \dots m-1$, $i_2 = 0 \dots n-1$, $i_3 = 0 \dots 1$.

Cài đặt mẫu:
```cpp=
using Permutation = vector<int>;

void operator*=(Permutation& p, Permutation const& q) {
    Permutation copy = p;
    for (int i = 0; i < p.size(); i++)
        p[i] = copy[q[i]];
}

int countCycles(Permutation p) {
    int cnt = 0;
    for (int i = 0; i < p.size(); i++) {
        if (p[i] != -1) {
            cnt++;
            for (int j = i; p[j] != -1;) {
                int next = p[j];
                p[j] = -1;
                j = next;
            }
        }
    }
    return cnt;
}

int solve(int n, int m) {
    Permutation p(n*m), p1(n*m), p2(n*m), p3(n*m);
    for (int i = 0; i < n*m; i++) {
        p[i] = i;
        p1[i] = (i % n + 1) % n + i / n * n;
        p2[i] = (i / n + 1) % m * n + i % n;
        p3[i] = (m - 1 - i / n) * n + (n - 1 - i % n);
    }

    set<Permutation> s;
    for (int i1 = 0; i1 < n; i1++) {
        for (int i2 = 0; i2 < m; i2++) {
            for (int i3 = 0; i3 < 2; i3++) {
                s.insert(p);
                p *= p3;
            }
            p *= p2;
        }
        p *= p1;
    }

    int sum = 0;
    for (Permutation const& p : s) {
        sum += 1 << countCycles(p); // 2 ^ countCycles(p)
    }
    return sum / s.size();
}
```

*Như vậy, qua bổ đề Burnside và định lý liệt kê Pólya, ta có thể rút ra bài học rằng, thằng nói trò đùa của bạn to hơn bạn sẽ nổi tiếng hơn bạn.*
<!-- ¯\\\_(ツ)\_/¯ -->

## Đọc thêm

Tham khảo: 
- [cp-algorithms](https://cp-algorithms.com/combinatorics/burnside.html)
- [Brilliant](https://brilliant.org/wiki/burnsides-lemma/)
- [almostsurelymath](https://almostsurelymath.blog/2019/09/18/necklaces-and-groups-the-burnside-lemma/)
