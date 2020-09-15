def privetomatka(name):
    def new_privetikman(count):
        for _ in range(count):
            print(f"Hello, {name}")
    return new_privetikman


bober = privetomatka('Bob')
sasher = privetomatka('Sasha')
irsher = privetomatka('Ira')


bober(4)
sasher(3)
