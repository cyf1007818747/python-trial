# start to AC - 26:57
# AC
class Solution:
    def numberToWords(self, num: int) -> str:
        # edge cases (you forgot initially) !!
        if num == 0:
            return "Zero"
        
        # get numbers of billion, million, thounsand, single

        unit_nums = []
        while num:
            unit_nums.append(num % 1000)
            num //= 1000   
        
        # unit_nums = unit_nums[::-1]

        # match numbers to string, using a table:
        # > 0: nothing
        # > 1 - 10: explicit
        # > 11 - 19: explicit
        # > 20 - 99: 
        # >> num // 10 => twenty - ninty
        # >> num % 10 => nothing, one, two .. nine (same as above)
        # 100 - 999: num // 100 + Hundred, then deal with num % 100

        table = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            # // 6: "six"
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }

        units = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion"
        }

        rtn = ""

        for i in range(len(unit_nums) - 1, -1, -1):
            num = unit_nums[i]
            hundred = num // 100
            if hundred > 0:
                # // rtn += table[hundred]
                # // rtn += " Hundred"
                rtn += " " + table[hundred] + " Hundred"
            org_num = num
            num %= 100
            if 1 <= num <= 19:
                rtn += " " + table[num]
            elif 20 <= num <= 99:
                ten = num - (num % 10)
                rtn += " " + table[ten]
                if num % 10 > 0:
                    rtn += " " + table[num % 10]
            if org_num != 0 and i != 0:
                rtn += " " + units[i]
        
        # // return rtn
        return rtn.strip(" ") # should remove the leading space caused by line 52
