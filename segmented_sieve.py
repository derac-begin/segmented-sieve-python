#!/usr/bin/env python
# coding: utf-8

# # セグメント化エラトステネスの篩（ふるい）

# **セグメント化エラトステネスの篩**は、メモリ効率を向上させるための改良版です。  
# 大きなnに対する素数計算を効率化します。  
# 以下にPythonでの実装例を示します。

# In[3]:


import math

def segmented_sieve(n):
    """
    nまでの素数をセグメント化エラトステネスの篩を用いて計算します。

    引数:
    n -- 上限の整数

    戻り値:
    nまでの素数のリスト
    """
    if n <= 1:
        return []

    limit = int(math.sqrt(n)) + 1
    primes = sieve_of_eratosthenes(limit)  # √nまでの素数を取得

    segment_size = limit  # セグメントのサイズを√nに設定
    low = limit
    high = 2 * limit

    result_primes = list(primes)  # 最初のセグメントの結果を初期化

    while low <= n:
        if high > n:
            high = n + 1
        segment = [True] * segment_size  # セグメント内の素数判定リスト

        for p in primes:
            start = (low + p - 1) // p * p  # セグメント内の最初のpの倍数
            for i in range(start, high, p):
                if i >= low:
                    segment[i - low] = False  # 倍数をFalseに設定

        for i in range(low, high):
            if segment[i - low]:
                result_primes.append(i)  # 素数を結果に追加

        low = high
        high += segment_size

    return sorted(list(set(result_primes)))  # 重複除去とソート


# In[4]:


def sieve_of_eratosthenes(limit):
    """
    エラトステネスの篩を用いてlimitまでの素数を計算します。
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return [p for p in range(limit + 1) if is_prime[p]]


# # 使用例

# In[5]:


n = 1000000
primes = segmented_sieve(n)
print(f"{n}までの素数の数: {len(primes)}")


# # 解説:

# ## `sieve_of_eratosthenes(limit) :`

# これは、与えられた`limit`までの素数を計算するための標準的なエラトステネスの篩の実装です。  
# `limit`までの各数に対して、それが素数であるかどうかを示すブール値のリストを初期化します。  
# 2から`limit`の平方根までの各素数pに対して、pの倍数を合成数としてマークします。  
# 最後に、マークされていない数（つまり、素数）のリストを返します。

# ## `segmented_sieve(n) :`

# この関数は、セグメント化されたエラトステネスの篩を実装し、nまでの素数を計算します。  
# まず、`sqrt(n)`までの素数を`sieve_of_eratosthenes`関数を使って計算します。  
# これらの素数は、セグメント内の合成数をマークするために使用されます。  

# 次に、範囲`[1, n]`をセグメントに分割します。セグメントのサイズは`sqrt(n)`に設定されます。  
# 各セグメントに対して、そのセグメント内の数が素数であるかどうかを示すブール値のリストを作成します。  

# セグメント内の各素数pに対して、pの倍数を合成数としてマークします。  
# マークされていない数（つまり、素数）を結果リストに追加します。  

# すべてのセグメントが処理されるまで、このプロセスを繰り返します。  
# 最後に、結果の素数リストを返します。

# ## セグメント化エラトステネスの篩の利点:

# ### メモリ効率が良い:

# セグメント化エラトステネスの篩は、一度にメモリにロードする必要があるデータの量を減らすことによって、エラトステネスの篩の**メモリ効率を向上**させます。  
# これは、**nが非常に大きい**場合に特に重要です。

# ### 計算効率が良い:

# セグメント化されたエラトステネスの篩は、メモリへのアクセスパターンを改善することによって、エラトステネスの篩の**計算効率も向上**させます。
# これにより、**キャッシュの利用効率が向上**し、**「実行時間が短縮」**されます。
