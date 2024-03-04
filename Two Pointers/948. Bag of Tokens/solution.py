
'''
My First Solution
Beats 100% of python solutions
even the optimized version of it (kind of ironic how leetcode works)
'''

class Solution(object):

    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        
        # face-up : lose power, gain score
        # face-down : gain power, lose score
        # we need to lose the minimum power to get highest score

        face_up = score = max_score = 0
        face_down = len(tokens) - 1
        while face_up <= face_down:
            minE = tokens[face_up]
            maxE = tokens[face_down]
            if score == 0 and power < minE:
                face_up += 1
                continue
            if score == 0 or power >= minE:
                # faceUp
                power -= minE
                score += 1
                face_up += 1
                # print(f'faceUp {tokens[face_up-1]} | power={power} score={score}')
            else:
                # faceDown
                power += maxE
                score -= 1
                face_down -= 1
                # print(f'faceDown {tokens[face_down+1]} | power={power} score={score}')
            max_score = max(max_score, score)
        return max_score