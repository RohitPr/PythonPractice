# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for a in emails:
            name, domain = a.split('@')
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)

        return len(seen)
