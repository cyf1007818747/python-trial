class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dg_to_lt = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        rtn = []

        def backtrack(pos: int, comb: str):
            if pos >= len(digits):
                rtn.append(comb)
                return
            
            for c in dg_to_lt[digits[pos]]:
                backtrack(pos+1, comb + c)

        backtrack(0, "")

        return rtn
