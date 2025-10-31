class SolutionTwoPoint:
    def __init__(self):
        pass


    def reverseWords(self, world) -> str:
        left_point, rigth_point = 0,0
        new_response = ''
        i = 0
        while i < len(world):
            rigth_point += 1

            if world[i] == ' ':
                new_response += world[left_point:rigth_point][::-1]
                left_point   = rigth_point
            
            i += 1
        
        new_response += ' '
        new_response += world[left_point:rigth_point+2][::-1]
        return new_response[1:]






mystring  = "Mr Ding"
mystring2 = "Let's take LeetCode contest"

solution = SolutionTwoPoint()

r1 = solution.reverse_world_manual(mystring)
r2 = solution.reverse_world_manual(mystring2)

print(r1)
print(r2)


