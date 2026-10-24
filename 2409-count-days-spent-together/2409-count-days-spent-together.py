class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getDay(date):
            month=int(date[:2])
            day=int(date[3:])
            return sum(days[:month-1])+day
        start=max(getDay(arriveAlice), getDay(arriveBob))
        end=min(getDay(leaveAlice), getDay(leaveBob))
        return max(0, end-start+1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna