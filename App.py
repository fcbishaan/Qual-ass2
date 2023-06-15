from flask import Flask, render_template, request
from typing import List
import collections

app = Flask(__name__)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get input values from the form
        nums = request.form['nums']
        k = int(request.form['k'])

        # Convert input values to a list of integers
        nums = list(map(int, nums.split(',')))

        # Calculate the sliding window maximum
        solution = Solution()
        result = solution.maxSlidingWindow(nums, k)

        return render_template('result.html', result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
