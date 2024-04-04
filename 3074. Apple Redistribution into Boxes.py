class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot = sum(apple)
        capacity.sort(reverse=True)
        num = 0

        for box_size in capacity:
            tot -= box_size
            num += 1
            if tot <= 0:
                break

        return num
