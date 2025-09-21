# -*- coding: utf-8 -*-

import collections

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        left, right = map(
            list,
            zip(*(map(int, line.split()) for line in f)),
        )
        r_hist = dict(collections.Counter(right)) 
        print(sum(key * r_hist[key] for key in left if key in r_hist))
