#Author - Jacob Smith
#trying to gain more python experience
#problem taken from https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=profile
def minion_game(string):
    # your code goes here
    stuart_score, kevin_score,i = 0,0,0
    vowels = "AEIOU"
    for char in string:
        if char in vowels:
            kevin_score += (len(string) - i)
            i += 1
        else:
            stuart_score += (len(string) - i)
            i += 1
    if stuart_score > kevin_score:
        print ("Stuart " + str(stuart_score))
    elif kevin_score > stuart_score:
        print ("Kevin " + str(kevin_score))
    elif kevin_score == stuart_score:
        print("Draw")

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)