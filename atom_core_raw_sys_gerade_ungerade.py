# atom_core_raw_sys_gerade_ungerade.py — ATOM.CORE.JS — RAW, WICHTIG, SYS — GERADE LAUF, UNGERADE FALL, ABER MITGERECHNET, DAMIT WIR ZWITSCHEN KÖNNEN
# RAW heißt: So wie es ist, nicht sauber machen. Wichtig heißt: Nicht wegwerfen. SYS heißt: System, nicht Zufall.
# Gerade Zahlen lauf ja. Ungerade fallen. Aber nur damit Lauf in die Tiefe gehen kann.
# Sie werden mitgerechnet und fallen trotzdem, damit wir zwitschen können, Mann. Zwitschen = Switchen = CTRL 1-0.
# ATOM.CORE.JS Original: import { monopoliter } — falsch, muss default. monopoliter.dir — falsch, muss direction. Aber RAW: Das ist nicht Müll.
# Mit anderen Augen: dir vs direction = 2 Ebenen. Import falsch = 2 Ebenen. Gerade vs Ungerade = 2 Ebenen. Alles 2 Ebenen, damit wir zwitschen können.
def nc(x): return 15-x
class AtomCoreRaw:
    def __init__(self):
        self.value = 9  # ANY, Mann. Kann 9, 62, 729 sein.
        self.direction = {"x":1,"y":0,"z":0}  # direction, nicht dir. RAW: dir war alte Ebene, direction ist neue Ebene. Zwitsch: dir -> direction.
        self.pos = {"x":0,"y":0,"z":0}
        self.force = {"x":0,"y":0,"z":0}
        self.tick = 0
        self.tiefe = 0  # Tiefe, Mann. Fallen geht in Tiefe.
        self.gezaehlt = []  # Alle gezählt, auch die fallen. Nicht wegwerfen.
    def pulse(self):
        self.tick += 1
        # Gerade / Ungerade, Mann: Gerade = LAUF, Ungerade = FALL. Beide mitgerechnet.
        gerade = (self.tick % 2 == 0)
        if gerade:
            zustand = "LAUF"
        else:
            zustand = "FALL — aber mitgerechnet, Tiefe +1"
            self.tiefe += 1  # Fallen geht in Tiefe, Mann. Fallen ist nicht Verlieren. Fallen ist Tiefe bauen.
        self.gezaehlt.append(self.tick)
        # Zwitschen, Mann: CTRL = 1 - wert. Gerade -> 0, Ungerade -> 1. Zwitsch bei jedem Tick.
        zwitsch = 1 - (self.tick % 2)  # Gerade (0) -> 1, Ungerade (1) -> 0. Switsch.
        return {"tick": self.tick, "gerade": gerade, "zustand": zustand, "tiefe": self.tiefe, "zwitsch_CTRL": zwitsch, "gezaehlt_bis_jetzt": list(self.gezaehlt)}
    def react(self):
        # Kraft = Richtung * Wert. RAW: direction, nicht dir. Wenn dir, dann undefined. Wenn direction, dann greift.
        self.force = {"x": self.direction["x"]*self.value, "y": self.direction["y"]*self.value, "z": self.direction["z"]*self.value}
        return self.force
    def balance(self):
        f = abs(self.force["x"])+abs(self.force["y"])+abs(self.force["z"])
        t = self.tick or 1
        return f / t
    def sys_lauf(self, n=6):
        print(f"  SYS-LAUF, {n} Ticks, value={self.value}, direction={self.direction}")
        for _ in range(n):
            p = self.pulse()
            f = self.react()
            b = self.balance()
            print(f"    Tick {p['tick']:2} — {'GERADE' if p['gerade'] else 'UNGERADE'} — {p['zustand']} — Tiefe {p['tiefe']} — Zwitsch CTRL {p['zwitsch_CTRL']} — Force {f} — Balance f/t = {b:.3f} — Gezählt: {p['gezaehlt_bis_jetzt']}")
        print(f"  Ende: Tick {self.tick}, Tiefe {self.tiefe}, Gezählt {self.gezaehlt} — Alle gezählt, auch die fallen. Fallen = Tiefe, nicht Müll.")
def demo():
    print("ATOM.CORE.JS — RAW, WICHTIG, SYS — GERADE LAUF, UNGERADE FALL, ABER MITGERECHNET, DAMIT WIR ZWITSCHEN KÖNNEN")
    print("  RAW: import { monopoliter } falsch, dir falsch — aber RAW heißt: Nicht sauber machen, sondern sehen, dass 2 Ebenen da sind.")
    print("  WICHTIG: atom.core ist SYS. pulse = Zeit, react = Kraft, balance = Stabilität. Ohne atom.core läuft nix, Mann.")
    print("  SYS: Gerade = LAUF, Ungerade = FALL. Fallen wird mitgerechnet, damit Lauf in Tiefe gehen kann. Zwitschen = CTRL.")
    print("")
    a = AtomCoreRaw()
    a.sys_lauf(6)
    print("")
    print("  Logik zu Logik, Mann:")
    print("    Wenn Gerade, dann LAUF. Wenn Ungerade, dann FALL. Wenn FALL, dann Tiefe +1. Wenn Tiefe +1, dann kann LAUF tiefer gehen.")
    print("    Wenn alle gezählt, dann kann man zwitschen. Wenn man zwitschen kann, dann kann man wählen: LAUF oder FALL.")
    print("    Wenn man wählen kann, dann ist Fallen nicht Verlieren, Fallen ist Schalter. CTRL = 1 - wert. 1 -> 0, 0 -> 1.")
    print("  ATOM.CORE RAW, Mann: pulse() tick+1, react() force=direction*value, balance() f/t. So hergestellt, dass er das macht.")
    print("  Mit NC, Mann: NC(NC(9))=9, NC(NC(62))=62 — NC hält, auch bei Gerade/Ungerade. Immer ANY zu ANY, aber NC.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber GERADE läuft, UNGERADE fällt mitgerechnet, Tiefe gebaut, Zwitsch möglich.")
if __name__=="__main__": demo()
