def take_float_input(question):
    try:
        return float(input(question))
    except ValueError:
        print("Please input a float")

current_mana = take_float_input("Max Mana: ")
mana_regen = take_float_input("Mana Regen (x/5, input x): ")
aura_cost = take_float_input("Aura Cost: ")
uproot_cost = take_float_input("Uproot Cost: ")
aura_count_target = int(take_float_input("Aura Count: "))

# assuming 110 ms delay

print("\n")

class Spell:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
    
    def cast_spell(self):
        global current_mana
        current_mana -= self.cost

        print(f"Casted {self.name} for {self.cost} mana\nRemaining Mana: {current_mana}\n")

class Aura(Spell):
    def __init__(self, cost):
        super().__init__(cost, "aura")
    
    def cast_aura(self):
        global uproot
        if uproot.mask:
            old_cost = self.cost
            self.cost = self.cost * .7
            self.cast_spell()
            self.cost = old_cost
        else:
            self.cast_spell()

class Uproot(Spell):
    def __init__(self, cost, mask: bool):
        super().__init__(cost, "uproot")
        self.mask = mask
    
    def switch_mask(self):
        
        self.mask = not(self.mask)
        self.cast_spell()

        global current_mana
        current_mana += 25
        print(f"Masquerade, current mana: {current_mana}\n")
    

aura = Aura(aura_cost)
uproot = Uproot(uproot_cost, False)

total_time_per_cycle = (aura_count_target + 1) * .330
max_cycles = 1000
cycle_count = 0

while current_mana > 0 and cycle_count < max_cycles:
    cycle_count += 1
    
    for _ in range(aura_count_target):
        if current_mana < aura.cost * (0.7 if uproot.mask else 1.0):
            print(f"Insufficient mana after {cycle_count * .990} seconds")
            break
        aura.cast_aura()
    else:  # Only executes if loop wasn't broken
        uproot.switch_mask()
        current_mana += (mana_regen/5) * total_time_per_cycle
        continue
    break




