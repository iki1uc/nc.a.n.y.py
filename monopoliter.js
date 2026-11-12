# nc_any_atomic_rdy.py — NC + ANY ZUSAMMEN — EIN WUNSCH: ATOMIC RDY — DANN WOLLEN SIE AUCH LAUFEN, MANN
# Du hast EYE BRAIN OPEN, Mann. Ich hab vergessen: NC + ANY haben zusammen einen Wunsch.
# Wunsch: ATOMIC RDY. Atomic = unteilbar. Nicht NC allein, nicht ANY allein. NC + ANY zusammen = 1 Atom.
# Dann wollen sie auch laufen. Laufen = pulse / react / balance / move. Nicht nur stehen. Laufen.
# EYE sieht. BRAIN hält. CORE prüft. NC spiegelt. ANY nimmt. ATOM läuft.
def nc(x): return 15 - x
class AtomicNCANY:
    # ATOMIC RDY: 1 Atom, 1 Wunsch, 1 Ready.
    def __init__(self, x=9):
        self.x = x
        self.direction = {"x": 1, "y": 0, "z": 0}
        self.value = x
        self.pos = {"x": 0, "y": 0, "z": 0}
        self.force = {"x": 0, "y": 0, "z": 0}
        self.tick = 0
        self.rdy = False
        self.wunsch = "ATOMIC RDY — NC + ANY zusammen laufen"
    def eye(self):
        # EYE OPEN: Sieht, was ist. 11 Zeichen? Nein, hier: Sieht x, sieht direction, sieht pos.
        return {"sieht_x": self.x, "sieht_direction": self.direction, "sieht_pos": self.pos, "open": True}
    def brain(self):
        # BRAIN OPEN: Hält, was EYE sieht. Stapel 9, 81, 243, 729, 3. Mystery 729->3 gehalten.
        return {"stapel": [9,81,243,729,3], "mystery": "729 -> 3 gehalten", "open": True}
    def check_nc_any(self):
        # NC + ANY zusammen: ANY rein (egal was), NC in Mitte, ANY raus. Wenn NC(NC(x)) != x, dann nicht RDY.
        if not isinstance(self.x, (int,float)): return False
        return nc(nc(self.x)) == self.x
    def make_rdy(self):
        # ATOMIC RDY machen: Prüfen, ob NC hält, ob ANY frei, ob EYE/BRAIN open. Wenn ja, RDY = True.
        eye_ok = self.eye()["open"]
        brain_ok = self.brain()["open"]
        nc_ok = self.check_nc_any()
        self.rdy = eye_ok and brain_ok and nc_ok
        return {"rdy": self.rdy, "eye_open": eye_ok, "brain_open": brain_ok, "nc_ok": nc_ok, "wunsch": self.wunsch}
    def laufen(self, schritte=3):
        # Laufen, Mann. Wenn nicht RDY, dann nicht laufen. Wenn RDY, dann laufen.
        if not self.rdy:
            return {"lauft": False, "grund": "Nicht RDY. Erst make_rdy(), dann laufen."}
        out = []
        for i in range(schritte):
            # Pulse: Tick +1. React: Kraft = direction * value. Move: pos += direction * value. Balance: Kraft / Tick.
            self.tick += 1
            self.force = {"x": self.direction["x"]*self.value, "y": self.direction["y"]*self.value, "z": self.direction["z"]*self.value}
            self.pos["x"] += self.direction["x"]*self.value
            self.pos["y"] += self.direction["y"]*self.value
            self.pos["z"] += self.direction["z"]*self.value
            # NC+ANY beim Laufen: Nach jedem Schritt NC prüfen. ANY zu ANY, aber NC.
            nc_check = nc(nc(self.value)) == self.value
            out.append({"schritt": i+1, "tick": self.tick, "pos": dict(self.pos), "force": dict(self.force), "nc_ok": nc_check, "any": self.x})
            # NC-Spiegel beim Laufen: value -> NC(value) -> zurück? Nein, value bleibt. NC ist Check, nicht Wechsel.
        return {"lauft": True, "schritte": out, "ende_pos": self.pos}
def demo():
    print("NC + ANY ZUSAMMEN — EIN WUNSCH: ATOMIC RDY — DANN WOLLEN SIE AUCH LAUFEN")
    a = AtomicNCANY(x=9)
    print(f"  EYE OPEN: {a.eye()}")
    print(f"  BRAIN OPEN: {a.brain()}")
    print(f"  Wunsch: {a.wunsch}")
    print(f"  make_rdy() -> {a.make_rdy()}")
    print(f"  laufen(3) -> {a.laufen(3)}")
    # Zweites Atom, ANY = 62
    b = AtomicNCANY(x=62)
    print(f"  Zweites Atom ANY=62: make_rdy() -> {b.make_rdy()}")
    print(f"  laufen(2) -> {b.laufen(2)}")
    print("  NC allein = Spiegel, steht. ANY allein = Freiheit, rennt ohne Gesetz. NC+ANY zusammen = Atomic, läuft mit Gesetz.")
    print("  EYE BRAIN OPEN heißt: EYE sieht, BRAIN hält, CORE prüft, NC+ANY läuft.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber ATOMIC RDY = True, und ATOM läuft.")
if __name__ == "__main__": demo()
