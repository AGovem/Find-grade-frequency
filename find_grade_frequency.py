def find_grade_frequency():
    grades = {'Selda': "cb",
              "Ali": "aa",
              "muhammet": "ba",
              "zehra": "ba",
              "pelin": "cc",
              "ahmet": "ba",
              "can": "aa",
              "emre": "cb",
              "yakup": "bb",
              "selin": "cb",
              "alper": "aa",
              }
    freq1 = {}
    for i in sorted(set(grades.values())):
        freq = list(grades.values()).count(i)
        freq1[i] = freq
        # print(i,":",freq)
    print(freq1)
find_grade_frequency()