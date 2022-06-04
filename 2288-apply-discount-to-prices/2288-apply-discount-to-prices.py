class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount = (100-discount)/100
        res = []

        for word in sentence.split():
            val = word[1:]
            if word[0] == '$' and val.isdigit():
                amount = word.split('$')[1]
                newAmount = (int(amount) * discount)
                res.append("$"+ format((newAmount),'.2f'))
            else:
                res.append(word)
        
        return " ".join(res)