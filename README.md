# Maximum 69 Number 🔢
## Problem Statement

You are given a positive integer `num` consisting only of the digits **6** and **9**.
Return the maximum number you can get by changing **at most one digit** (`6` becomes `9`, and `9` becomes `6`)

## Examples

**Example 1**

```
Input: num = 9669
Output: 9969
```

**Example 2**

```
Input: num = 9996
Output: 9999
```

**Example 3**

```
Input: num = 9999
Output: 9999
```

---

## Constraints

* `1 <= num <= 10^4`
* `num` consists of only digits `6` and `9`.

---

## Solution Explanation

* We traverse the digits from right to left.
* Track the **leftmost digit** that is `6`.
* Changing this digit to `9` gives the **maximum number**.
* Finally, add `3 * placeValue` to the original number (because `9 - 6 = 3`).
* If no `6` exists, return the original number.

---

## Python Code

```python
class Solution:
    def maximum69Number(self, num: int) -> int:
        placeValue = 1
        placeValue6 = -1
        temp = num
        while temp > 0:
            remain = temp % 10
            if remain == 6:
                placeValue6 = placeValue
            temp //= 10
            placeValue *= 10
        if placeValue6 == -1:
            return num
        return num + 3 * placeValue6
```

---

## Complexity Analysis

* **Time Complexity:** `O(d)` where `d` = number of digits in `num`
* **Space Complexity:** `O(1)` (only a few variables used)

---

## Alternative Approach (One-liner)

You can also solve this by converting to a string and replacing the first `6` with `9`:

```python
def maximum69Number(num: int) -> int:
    return int(str(num).replace('6', '9', 1))
