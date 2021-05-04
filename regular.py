import shuntingReg
import Thompson

if __name__ == "__main__":
    tests = [  ["(a.b|b*)",   ["ab", "b", "bb", "a"]]
             , ["a.(b.b)*.a", ["aa", "abba", "aba"]]
    ]
    a_list = []
    
    myfile = open("graphTextFile.txt", "r")
    for element in myfile:
        oneLine = element.strip()
        full_line = oneLine.split()
        a_list.append(full_line) 
    myfile.close()
  
    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingReg.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = Thompson.re_to_nfa(postfix)
        print(f"Thompson: {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()