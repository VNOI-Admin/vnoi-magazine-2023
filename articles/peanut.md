# :peanut: rang

Author: Trần Xuân Bách

## Giới thiệu

Chắc hẳn khi học toán các bạn đã phải vẽ đồ thị của một đa thức $P$ có bậc $1$, $2$ rồi. Cách làm phổ biến nhất là ta vẽ ra một vài điểm $(x, P(x))$ trên giấy, rồi nối chúng lại với nhau ~~và hi vọng nhìn nó đúng~~. Vậy đã bao giờ bạn nghĩ đến bài toán ngược lại:

> Từ một số điểm $(x_i, P(x_i))$ cho trước, những đa thức $P(x)$ nào có đồ thị đi qua các điểm đó?

Có thể chứng minh được rằng có vô hạn đa thức $P$ thỏa mãn. Tuy nhiên, việc tìm đa thức $P$ có bậc nhỏ nhất (**nội suy - interpolate**) thì khó hơn nhiều.
Vào năm 1795, nhà toán học Joseph-Louis Lagrange đưa ra một công thức tổng quát để nội suy ra đa thức này, gọi là **nội suy Lagrange**. Phương pháp này được dùng nhiều trong lập trình thi đấu, và cũng được dùng trong mật mã học, với ví dụ điển hình là [thuật toán Shamir](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing).

## Nội suy Lagrange

Ở cốt lõi của nội suy là định lí sau:

### Định lí 1

> Với mọi số tự nhiên $n \ge 0$ và mọi tập $n + 1$ điểm $(x_1, y_1), (x_2, y_2), \dots, (x_{n+1}, y_{n+1})$ với $x_1 < x_2 < \ldots < x_{n+1}$, **tồn tại** **duy nhất** một đa thức $P(x)$ bậc $n$ sao cho $P(x_i) = y_i$ với mọi $i$.

Ta sẽ chứng minh hai phần của định lí này: sự **tồn tại** của đa thức $p$ và tính **duy nhất** của nó.

#### Chứng minh tính duy nhất
Ta giả sử phản chứng: Tồn tại hai đa thức $P$ và $Q$ khác nhau đều thỏa mãn điều kiện trên.

Xét đa thức $R = P - Q$, ta có:

- Vì $P$ và $Q$ đều có bậc $n$, nên $R$ có bậc tối đa là $n$.
- Với mọi $i$, $R(x_i) = P(x_i) - Q(x_i) = y_i - y_i = 0$, vậy $R$ có $n + 1$ nghiệm $x_0, x_1, \dots, x_n$.

Theo [Định lí cơ bản của đại số](https://vi.wikipedia.org/wiki/%C4%90%E1%BB%8Bnh_l%C3%BD_c%C6%A1_b%E1%BA%A3n_c%E1%BB%A7a_%C4%91%E1%BA%A1i_s%E1%BB%91), $R$ phải là đa thức không, vậy $P = Q$ (vô lí với giả sử phản chứng).

![Trích SGK toán lớp 7 tập 2](./assets/peanut/img1.png)

Vậy tồn tại tối đa một đa thức $P$ thỏa mãn điều kiện của đề bài.

#### Chứng minh sự tồn tại
Ta sẽ chỉ ra một cách để xây dựng đa thức $P$ thỏa mãn. Ý tưởng ở đây là ta sẽ tách $P$ thành $n$ đa thức con:
$$
P = P_1 + P_2 + ... + P_{n+1}$$

Trong đó, mỗi đa thức con $P_i$ sẽ thỏa mãn:

- $P_i(x_i) = y_i$
- $P_i(x_j) = 0$ $(\forall j \ne i)$.

Ta sẽ thêm các thừa số $(x - x_j)$ vào $P_i$ để khiến $P_i(x_j) = 0$, rồi sau đó nhân nó với một giá trị thích hợp để $P_i(x_i) = y_i$.

Cuối cùng công thức tổng quát cho $P_i$ và $P$ là:
$$
\begin{array}{rl}
P_i(x) = & y_i \times
\frac{x - x_1}{x_i - x_1} \times
\dots \times
\frac{x - x_{i - 1}}{x_i - x_{i - 1}} \times \\
& 
\qquad \times \frac{x - x_{i + 1}}{x_i - x_{i + 1}} \times
\dots \times
\frac{x - x_{n+1}}{x_i - x_{n+1}} \\
= & y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j} \\
\Rightarrow
P(x) =& y_1 \prod_{j \ne 1} \frac{x - x_j}{x_1 - x_j} + \dots + \\
      & \qquad + y_{n+1} \prod_{j \ne {n+1}} \frac{x - x_j}{x_{n+1} - x_j} \\
= & \sum_{i=1}^{n+1} y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}
\end{array}$$

Bạn đọc có thể tự kiểm chứng rằng đa thức $P$ thỏa mãn điều kiện của định lí trên. Cách xây dựng $P(x)$ trên được gọi là nội suy Lagrange.

### Cài đặt mẫu

#### C++

```cpp
const int N = 1000 + 5;

struct Point{
    double x, y;
} data[N];

// Tính giá trị của P tại x
double interpolation(int n, double x){
    double ans = 0;
    for (int i = 1; i <= n + 1; i++){
        // Tính giá trị của P_i tại x
        double val = data[i].y;
        for (int j = 1; j <= n + 1; j++){
            if (i == j)
                continue;
            val *= (x - data[j].x) / (data[i].x - data[j].x;
        }
        ans += val;
    }
    return ans;
}
```

#### Python

```python
def interpolation(data, x):
    ans = 0
    for i in range(len(data)):
        val = data[i].y
        for j in range(len(data)):
            if i == j:
                continue
            val *= (x - data[j].x) / (data[i].x - data[j].x)
        ans += val
    return ans
```

#### Phân tích

Cách cài đặt trên có độ phức tạp là $\mathcal O(n^2)$ ($2$ vòng `for` lồng nhau).

## Thuật toán SSS

Thuật toán Chia sẻ bí mật Shamir (Shamir's Secret Sharing  - SSS) là một trong những ứng dụng điển hình nhất của phép nội suy đa thức. SSS là một thuật toán dùng để chia sẻ một *bí mật* nào đó cho nhiều người, sao cho không người nào nắm giữ được bất kì thông tin quan trọng nào của bí mật đó. Để làm được điều này, SSS tách bí mật ra thành $n$ phần, mà chỉ khi ta nắm giữ được ít nhất $k$ phần thì ta mới xây dựng lại được bí mật này. Thuật toán này có *tính bảo mật tuyệt đối*, tức là một kẻ gian không thể nào tìm được bí mật đó kể cả khi hắn có vô hạn thời gian và năng lực tính toán.

### Phương thức hoạt động

Giả sử ta đang muốn chia sẻ một bí mật $S$ ra thành $n$ phần $S_1, S_2, \dots, S_n$, sao cho chỉ khi ta nắm giữ được $k$ phần thì ta mới tìm được $S$, và nếu ta chỉ nắm giữ được $k-1$ trở xuống thì ta sẽ không bao giờ tìm được **bất kì thông tin gì** từ $S$. Để dễ hiểu cho bạn đọc ta sẽ giả sử ta đang làm việc với các số nguyên.

Ta sẽ xây dựng một đa thức $P(x) = p_0 + p_1 \times x^1 + \dots + p_{k-1} \times x^{k-1}$ có bậc $k-1$, sao cho:
- $p_0 = S$.
- $p_1, \dots, p_{k-1}$ là các số nguyên được chọn ngẫu nhiên.

Sau đó, mỗi phần $S_i$ của bí mật sẽ là một cặp số $(i, P(i))$.

Nếu ta có $k$ phần bí mật $(x_1, y_1)$, $(x_2, y_2)$, $\dots$, $(x_k, y_k)$, ta có thể dùng nội suy đa thức để tính $P(0) = \sum_{i=1}^{k} y_i \prod_{j \ne i} \frac{0 - x_j}{x_i - x_j}$.
Nhận thấy $P(0)$ cũng bằng $p_0 + p_1 \times 0^1 + \dots + p_{k-1} \times 0^{k-1} = p_0 = S$, vậy ta đã dựng lại được bí mật $S$.

Nếu ta chỉ sở hữu $k-1$ phần bí mật, với mỗi giá trị $y_k$ bất kì, ta có thể sinh ra được một đa thức $P$ thoả mãn. Do vậy, có vô vàn đa thức $P$ thoả mãn, với vô vàn các giá trị khác nhau cho $P(0)$. Điều này đồng nghĩa với việc nắm giữ $\le k-1$ phần không đưa ra bất kì thông tin gì về bí mật.

![Có vô số đa thức bậc hai đi qua hai điểm cho trước như trên](./assets/peanut/img2.png)

Trên thực tế, các giá trị $S, S_i, p_i, x_i, y_i$ thường được tính theo modulo của một số nguyên tố đủ lớn $p$, với lí do sẽ được đề cập sau.

## Ví dụ: CTF BabySSS

### Giới thiệu

[Capture the flag (CTF)](https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity)) là một dạng kì thi khá giống với lập trình thi đấu, với mục đích là thử thách các kĩ năng nhận diện và xử lí lỗ hổng bảo mật của thí sinh. Để giải được bài, thí sinh cần phải tìm được một "lá cờ" (flag) được giấu trong một trang web hoặc phần mềm, bằng cách lợi dụng các lỗ hổng bảo mật được cố tình đưa vào từ ban ra đề.

CTF không chỉ đơn giản và thân thiện hơn với thí sinh mới so với lập trình thi đấu, mà còn phổ cập cho thí sinh các kiến thức cơ bản về bảo mật thông tin nói riêng và máy tính nói chung. 

Mình và một vài người bạn có tham gia một kì thi vào ngày 25-27/11, mang tên [HITCON CTF](https://ctf2022.hitcon.org/). Bài thi dễ nhất của phần mật mã mang tên BabySSS, và như bạn đọc có thể đoán, ta phải tìm ra một lỗ hổng nào đó trong phần mềm cài đặt thuật toán SSS của ban tổ chức để từ đó lấy được flag.

### Đề bài

[Link](https://ctf2022.hitcon.org/dashboard/#8)

> I implemented a toy [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) for fun. Can you help me check is there any issues with this?

Ta cũng được cho thêm một file nén `babysss.tar.gz`, trong đó bao gồm hai file:

- `chall.py`

```python=
from random import SystemRandom
from Crypto.Cipher import AES
from hashlib import sha256
from secret import flag

rand = SystemRandom()


def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])


DEGREE = 128
SHARES_FOR_YOU = 8  # I am really stingy :)

poly = [rand.getrandbits(64) for _ in range(DEGREE + 1)]
shares = []
for _ in range(SHARES_FOR_YOU):
    x = rand.getrandbits(16)
    y = polyeval(poly, x)
    shares.append((x, y))
print(shares)

secret = polyeval(poly, 0x48763)
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR)
print(cipher.encrypt(flag))
print(cipher.nonce)
```

- `output.txt`[{Đây là file có nội dung rất dài, các bạn vui lòng tải file từ trang web để xem đầy đủ}].

```python
[(41458, 30158948896...
```

### Hướng suy nghĩ

#### Phân tích code
Đầu tiên, hãy đọc từng đoạn code một:

- Dòng 1-6

  ```python
  from random import SystemRandom
  from Crypto.Cipher import AES
  from hashlib import sha256
  from secret import flag
  
  rand = SystemRandom()
  ```
  
  Đây là những thư viện mà `chall.py` sẽ sử dụng - có thể thấy ta import AES và sha256 là cách mã hóa và hash phổ biến. Ta cũng thấy có một biến `flag` được import từ module `secret`, ta đoán rằng đây chính là flag mà mình cần tìm.
  
  Bình thường CTF cũng có vài bài lợi dụng việc tìm seed được dùng cho random để mô phỏng lại việc mã hóa `flag`, tuy nhiên khi mình tra tài liệu thì nó bảo là `SystemRandom` không mô phỏng lại được luôn.
![Tài liệu chính thức của Python về `SystemRandom`](./assets/peanut/img3)

- Dòng 9-22

  ```python
  def polyeval(poly, x):
      return sum([a * x**i for i, a in enumerate(poly)])
  
  
  DEGREE = 128
  SHARES_FOR_YOU = 8  # I am really stingy :)
  
  poly = [rand.getrandbits(64) for _ in range(DEGREE + 1)]
  shares = []
  for _ in range(SHARES_FOR_YOU):
      x = rand.getrandbits(16)
      y = polyeval(poly, x)
      shares.append((x, y))
  print(shares)
  ```
  
  - Hàm `polyeval` là để tính giá trị của đa thức `poly` tại điểm `x`.
  - Hai biến sau cho biết rằng đa thức của chúng ta có bậc là $128$, nhưng ta chỉ được biết đúng $8$ điểm. Về mặt lí thuyết ta phải biết đúng $128$ điểm thì ta mới tìm được đa thức `poly`.
  - Các hệ số của `poly` là các số $64$-bit ngẫu nhiên, tức là các số nằm trong khoảng $[0, 2^{64})$.
  - Các giá trị $x$ của cặp điểm $(x, y = \text{poly}(x))$ là số $16$-bit ngẫu nhiên.
  - Cuối cùng, ta được cho biết thông tin của $8$ điểm ngẫu nhiên ở file `output.txt`

- Dòng 24-28

  ```python
  secret = polyeval(poly, 0x48763)
  key = sha256(str(secret).encode()).digest()[:16]
  cipher = AES.new(key, AES.MODE_CTR)
  print(cipher.encrypt(flag))
  print(cipher.nonce)
  ```
  
  Gọi `secret` là giá trị của `poly` tại $x = 0\text{x}48673$. Ta mã hóa `flag` cần tìm bằng AES với `key` ở đây là hash SHA256 của `secret`, rồi in ra `flag` và phần `nonce` được thêm vào.
  
  Do phần này không quan trọng đến lời giải nên mình sẽ tạm bỏ qua cách xử lí phần này. Bạn đọc chỉ cần biết rằng nếu mình có giá trị của `secret`, thì kết hợp với hai giá trị được in ra ở phía trên, có thể tìm lại được `flag` ban đầu.

#### Tìm lỗ hổng

Khi mình đọc trang Wikipedia của thuật toán SSS đã được link trong đề bài, mình để ý đến một đoạn nói về "Vấn đề về việc tính toán bằng số nguyên". Cụ thể hơn, câu đầu của đoạn như sau:

> Phiên bản đơn giản hơn của thuật toán trên, mà dùng số nguyên để tính toán thay vì dùng modulo, vẫn hoạt động. Tuy nhiên, nó lại có một vấn đề bảo mật: Kẻ xấu sẽ có thêm thông tin về $S$ với mỗi phần mà hắn có được.

Sau đó, có một ví dụ nói về việc khi chỉ có được $2$ điểm trong khi $k = 3$, ta đã có thể rút gọn số giá trị có thể của $S$ về $150$ số bằng phương pháp đồng dư. Đoạn code trên cũng tính toán bằng số nguyên, vậy ta có thể làm tương tự được không?

Hãy quay lại các cặp giá trị $(x_1, y_1), \dots, (x_8, y_8)$, ta có:
$$
\begin{array}{rl}
y_i =& \text{poly}(x_i) \\
=& \text{poly}[0] + \text{poly}[1] \times x_i + \dots + \\
    & \qquad + \text{poly}[128] \times x_i^{128} \\
\Rightarrow y_i \equiv & \text{poly}[0] \pmod {x_i}
\end{array}$$

Vậy ta có $8$ biểu thức đồng dư như sau:
$$
\begin{array}{rl}
\text{poly}[0] &\equiv y_1 \pmod {x_1} \\
\text{poly}[0] &\equiv y_2 \pmod {x_2} \\
\dots \\
\text{poly}[0] &\equiv y_8 \pmod {x_8} \\
\end{array}$$

Chắc hẳn nhiều bạn sẽ nhận ra đây chính là [định lí thặng dư Trung Hoa](https://en.wikipedia.org/wiki/Chinese_remainder_theorem). Sử dụng định lí này, ta sẽ tìm được giá trị của $\text{poly}[0] \bmod \text{lcm}(x_1, x_2, \dots, x_8)$. Do $\text{poly}[0]$ là một số ngẫu nhiên có $64$ bit, nên nếu giá trị của hàm $\text{lcm}$ trên không nhỏ hơn $2^{64}$ thì ta đã tìm được giá trị thỏa mãn duy nhất của $\text{poly}[0]$.

Để kiểm tra điều kiện trên, ta có thể viết một đoạn code nhỏ `helper.py` như sau:

```python
import math

shares = [(41458, ...

shares_x = [point[0] for point in shares]
print("shares_x =", shares_x)
print("lcm =", math.lcm(*shares_x))
print("2^64 =", 2 ** 64)
```

![Kết quả của đoạn code trên](./assets/peanut/img4.png)
    
Vậy ta đã tìm được giá trị của $\text{poly}[0]$, làm thế nào để tìm nốt các hệ số còn lại của đa thức? Ta sẽ dùng một mẹo như sau:
$$
\begin{array}{clcl}
& y_i &=&  \text{poly}[0] + \text{poly}[1] \times x_i + \\
 & & & + \dots + \text{poly}[128] \times x_i^{128} \\
\iff & y_i - \text{poly}[0] &=& \text{poly}[1] \times x_i + \\
 & & & + \dots + \text{poly}[128] \times x_i^{128} \\
\iff & \frac{y_i - \text{poly}[0]}{x_i} & =& \text{poly}[1] + \text{poly}[2] \times x_i + \\ 
 & & & + \dots + \text{poly}[128] \times x_i^{127} \\
\end{array}$$

Ta có thể thấy vế phải biến thành một đa thức có bậc là $127$ với các hệ số lần lượt là $\text{poly}[1], \dots, \text{poly}[128]$. Làm tương tự như $\text{poly}[0]$, ta sẽ lần lượt tìm được các giá trị $\text{poly}[1], \dots, \text{poly}[128]$.

### Lời giải

```python=
import ast
from hashlib import sha256
from Crypto.Cipher import AES

# Đọc giá trị từ file output.txt
with open("output.txt") as f:
    shares = ast.literal_eval(f.readline())
    ciphertext = ast.literal_eval(f.readline())
    nonce = ast.literal_eval(f.readline())

# Mình đổi loại của shares[i] từ tuple sang list
# để có thể sửa giá trị của shares về sau
for i in range(len(shares)):
    shares[i] = list(shares[i])

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

DEGREE = 128
SHARES_FOR_YOU = 8  # I am really stingy :)

poly = []
for d in range(DEGREE + 1):
    values = []
    mods = []
    for [x, y] in shares:
        values.append(y % x)
        mods.append(x)

    # Dùng hàm CRT của Sagemath để tính giá trị của poly[0]
    val = CRT(values, mods)
    poly.append(val)
    
    # Mẹo đã nói ở trên
    for i in range(len(shares)):
        shares[i][1] = (shares[i][1] - val) // shares[i][0]

# Tìm lại flag sau khi biết được secret
secret = polyeval(poly, int(0x48763))
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR, nonce = nonce)
flag = cipher.decrypt(ciphertext)
print(flag)
```
