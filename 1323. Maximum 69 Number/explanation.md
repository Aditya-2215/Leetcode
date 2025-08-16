## Approach 1: Mathematical Place-Value

### 🔎 How It Works

Let’s take num = 9669.

1. Initialize:

- `placeValue = 1` (unit place)

- `placeValue6 = -1`

2. Start processing digits from right to left:

- Last digit = 9 → skip.

- Next digit = 6 → store its place value = 10.

- Next digit = 6 → store its place value again = 100.

- Next digit = 9 → skip.

Final: placeValue6 = 100 (leftmost 6).

3. To flip that 6 into a 9:

- Difference between 6 and 9 = +3.

- Place value = 100.

- Add 3 × 100 = 300.

So: 9669 + 300 = 9969.

### 🔹 Key Idea

- Instead of converting to a string, this approach works purely with math.

- It scans digits from right → left and remembers the most significant (leftmost) 6.

- Then it adds 3 × placeValue to flip that digit.

### 🔹 Complexity

- Time Complexity: O(d), where d = number of digits.

- Space Complexity: O(1), since no extra data structure is used.








## Approach 2: String Manipulation Approach (Greedy)

### Walkthrough Example

Suppose num = 9669.

Convert to list → s = ['9', '6', '6', '9']

Iterate:

- First digit = '9' → skip

- Second digit = '6' → change to '9', so now s = ['9', '9', '6', '9']

- Stop (break) since only one change is allowed.

- Join back → "9969" → convert to integer → 9969

### Key Idea

By changing the first 6 from the left (most significant digit), we maximize the number because digits at the left contribute more to the value.

### Complexity

- Time Complexity: O(d), where d is the number of digits in num.

- Space Complexity: O(d), for storing the digits as a list.