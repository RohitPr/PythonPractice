# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# (0,8),(8,10) is not conflict at 8

# Example
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation:
# (0,30), (5,10) and (0,30),(15,20) will conflict


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals) -> bool:
        # Write your code here
        intervals.sort(key=lambda i: i.start)

        for a in range(1, len(intervals)):
            i1 = intervals[a-1]
            i2 = intervals[a]

            if i1.end > i2.start:
                return False

        return True
