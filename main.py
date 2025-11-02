
# change these to the values in game
max_mana = 0
mana_regen = 0 # x/5, input x
aura_cost = 0
uproot_cost = 0
aura_count_target = 0
delay = 0

current_mana = max_mana

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

total_time_per_cycle = (aura_count_target + 1) * (.003 * 110)
max_cycles = 1000
cycle_count = 0

while current_mana > 0 and cycle_count < max_cycles:
    cycle_count += 1
    
    for _ in range(aura_count_target):
        if current_mana < aura.cost * (0.7 if uproot.mask else 1.0):
            print(f"Insufficient mana after {cycle_count * total_time_per_cycle} seconds")
            break
        aura.cast_aura()
    else:  # Only executes if loop wasn't broken
        uproot.switch_mask()
        current_mana += (mana_regen/5) * total_time_per_cycle
        if current_mana >= max_mana:
            print("Infinite Sustain, gained mana after 1 cycle")
            break
        continue
    break
