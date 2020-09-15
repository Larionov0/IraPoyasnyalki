def privetomatka(name):
    def new_privetikman():
        print(f"Hello, {name}")
    return new_privetikman


bober = privetomatka('Bob')
sasher = privetomatka('Sasha')
irsher = privetomatka('Ira')

sasher()
bober()
bober()
irsher()
sasher()
