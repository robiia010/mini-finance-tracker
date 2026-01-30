import json

def run():
    try:
        with open('data.json', 'r') as f:
            m = json.load(f)
    except:
        m = {"b": 0, "t": []}

    while True:
        print(f"\nBalans: {m['b']}")
        s = input("1.Kir  2.Chiq  3.List  4.Off: ")

        if s == '1':
            v = int(input("+: "))
            m['b'] += v
            m['t'].append(f"+{v}")
        elif s == '2':
            v = int(input("-: "))
            m['b'] -= v
            m['t'].append(f"-{v}")
        elif s == '3':
            print(m['t'])
        elif s == '4':
            with open('data.json', 'w') as f:
                json.dump(m, f)
            break

if name == "main":
    run()
