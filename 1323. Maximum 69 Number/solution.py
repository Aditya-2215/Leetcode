# Approach 1: Mathematical Place-Value Approach
# For better explanation you can visit explanation.md
class Solution:
    def maximum69Number(self, num: int) -> int:
        placeValue = 1          # 1️⃣ Keeps track of digit position (units, tens, hundreds…)
        placeValue6 = -1        # 2️⃣ Stores the place value of the *rightmost* '6'
        temp = num              # 3️⃣ Copy of num to process digits
        
        while temp > 0:         # 4️⃣ Loop until all digits are processed
            remain = temp % 10  # Extract the last digit
            if remain == 6:     
                placeValue6 = placeValue   # Store the place value if digit is '6'
            temp //= 10          # Remove the last digit
            placeValue *= 10     # Move to the next higher place (×10)
        
        if placeValue6 == -1:    # 5️⃣ No '6' found → return original number
            return num
        return num + 3 * placeValue6   # 6️⃣ Convert that '6' → '9' by adding 3 × placeValue

# Approach 2: String Manipulation Approach (Greedy)
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))                # 1️⃣ Convert the number into a list of characters (digits)
        for i in range(len(s)):           # 2️⃣ Loop through each digit from left to right
            if s[i] == '6':               # 3️⃣ When the first '6' is found
                s[i] = '9'                # 4️⃣ Change it into '9'
                break                     # 5️⃣ Stop immediately (only one digit can be changed)
        return int("".join(s))            # 6️⃣ Join the list back into a string, convert to int, and return
