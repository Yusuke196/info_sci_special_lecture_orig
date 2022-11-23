"""
https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_E
"""

from pprint import pprint


def main():
    S1 = input()
    S2 = input()
    INF = 2000
    dist = [[INF] * (len(S2) + 1) for _ in range(len(S1) + 1)]
    dist[0][0] = 0

    for i in range(len(S1) + 1):
        for j in range(len(S2) + 1):
            # 次の3つのアプローチを試し、編集距離dist[i][j]が最も小さくなるように更新していく
            if i > 0 and j > 0:
                # 対応づけ操作（二次元配列distにおける右下への矢印、何も加算しない）
                if S1[i - 1] == S2[j - 1]:
                    dist[i][j] = dist[i - 1][j - 1]
                # 変更操作（二次元配列distにおける右下への矢印、1を加算する）
                else:
                    dist[i][j] = dist[i - 1][j - 1] + 1
            # 削除操作（二次元配列distにおける下への矢印、1を加算する）
            if i > 0:
                dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
            # 挿入操作（二次元配列distにおける右への矢印、1を加算する）
            if j > 0:
                dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

    print(dist[-1][-1])


if __name__ == '__main__':
    main()
