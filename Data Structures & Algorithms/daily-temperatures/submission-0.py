class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                stTemp, stIndex = st.pop()
                output[stIndex] = i - stIndex
            st.append((temp, i))
        return output