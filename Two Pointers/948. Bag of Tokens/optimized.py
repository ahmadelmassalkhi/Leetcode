class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        # face-up : lose power, gain score
        # face-down : gain power, lose score
        # we need to lose the minimum power to get highest score

        tokens.sort()

        score = maxScore = 0
        left = 0
        right = len(tokens) - 1

        while left <= right:
            if tokens[left] <= power:
                # faceUp
                power -= tokens[left]
                score += 1
                left += 1
                maxScore = max(maxScore, score)
            elif score >= 1:
                # faceDown
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break # score=0 => we can't faceDown
                      # power < minimum => we can't faceUp
                      # => we are done
        return maxScore