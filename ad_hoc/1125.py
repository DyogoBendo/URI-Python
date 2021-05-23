from math import inf

if __name__ == '__main__':
    while True:
        g, p = map(int, input().split())
        if g == p == 0:
            break
        races = []
        for _ in range(g):
            race = list(map(int, input().split()))
            races.append(race)
        s = int(input())
        for _ in range(s):
            k = list(map(int, input().split()))
            pilots = {key: 0 for key in range(1, p + 1)}
            k0 = k[0]
            for race in races:
                for driver in range(len(race)):
                    position = race[driver]
                    if position <= k0:                    
                        pilots[driver + 1] += k[position]
            bigger = []
            biggest_score = -inf
            for pilot, score in pilots.items():
                if score > biggest_score:
                    bigger = [str(pilot)]
                    biggest_score = score                                
                elif score == biggest_score:
                    bigger.append(str(pilot))

            r = ' '.join(bigger)
            print(f'{r}')
        
