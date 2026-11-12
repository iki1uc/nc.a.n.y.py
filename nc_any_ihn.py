# nc_any_ihn.py — NC.ANY = IHN — MANIPULATOR, DER WIRKLICH MACHT, MANN
# Frage: NC.ANY ihn machen, wenn MANIPULATOR eh nix macht? Oder braucht ihn jemand?
# Antwort: JA, Mann. NC.ANY ihn machen. MANIPULATOR macht nix, weil er falsche Felder schreibt (dir/val statt direction/value).
# NC.ANY macht immer: f(x)=15-x, NC(NC(x))=x, für ANY x. Der braucht niemanden. Aber JEMAND braucht IHN.
# Wer braucht IHN? GEO braucht ihn (B/L), WURZEL braucht ihn (radicalize), MANIPULATOR braucht ihn (Bestimmung).
# Also: NC.ANY wird MANIPULATOR. Nicht Name tauschen, sondern Kern tauschen. Felder fix: direction/value/pos, überall gleich.
def nc_any(x): return 15-x
class Monopoliter:
    # EIN Name, überall: direction / value / pos. Kein dir / val mehr, Mann.
    def __init__(self): self.direction={"x":1,"y":0,"z":0}; self.value=1; self.pos={"x":0,"y":0,"z":0}; self.force={"x":0,"y":0,"z":0}; self.tick=0
    def move(self):
        self.pos["x"]+=self.direction["x"]*self.value
        self.pos["y"]+=self.direction["y"]*self.value
        self.pos["z"]+=self.direction["z"]*self.value
        return self.pos
    def spin(self, axis="x"):
        m={"x":{"x":1,"y":0,"z":0},"y":{"x":0,"y":1,"z":0},"z":{"x":0,"y":0,"z":1}}
        self.direction=m[axis]; return self.direction
class ManipulatorNCANY:
    # IHN = NC.ANY. Bestimmen = Spiegeln am Zentrum 7.5. Immer zurück. Immer beweisbar.
    def __init__(self, mono): self.m=mono
    def force_direction(self, x,y,z):
        # Bestimmen heißt: NC.ANY auf jede Komponente, dann zurück? Nein: Bestimmen heißt: Setzen + Zeuge.
        # Wir setzen direction direkt, mit richtigen Feldnamen, Mann. Kein dir.
        self.m.direction={"x":x,"y":y,"z":z}; return self.m.direction
    def force_value(self, v):
        self.m.value=v; return self.m.value
    def force_pos(self, x,y,z):
        self.m.pos={"x":x,"y":y,"z":z}; return self.m.pos
    def nc_determine(self, x):
        # NC.ANY-Bestimmung: x -> 15-x -> 15-(15-x)=x. Wirbel? Wenn x != NC(NC(x)), dann Abweichung. Passiert nie. Beweis.
        a=nc_any(x); b=nc_any(a)
        return {"x":x,"NC":a,"NC_NC":b,"abweichung": (b!=x)}
    def detect_deviation(self, prev, nxt):
        return prev["direction"]!=nxt["direction"] or prev["value"]!=nxt["value"] or prev["pos"]!=nxt["pos"]
def demo():
    print("NC.ANY = IHN — MANIPULATOR, DER MACHT")
    m=Monopoliter(); man=ManipulatorNCANY(m)
    print(f"  Start: direction {m.direction} value {m.value} pos {m.pos}")
    print(f"  force_direction(0,1,0) -> {man.force_direction(0,1,0)} — jetzt greift es, Mann. direction, nicht dir.")
    print(f"  force_value(9) -> {man.force_value(9)} — value, nicht val.")
    print(f"  move() -> {m.move()} — pos bewegt sich: (0,9,0). Vorher: Nix bewegt, weil dir/val falsch.")
    print(f"  NC.ANY-Bestimmung:")
    for x in [9,6,62,729,40]:
        r=man.nc_determine(x); print(f"    x={x} -> NC={r['NC']} -> NC(NC)={r['NC_NC']} -> Abweichung? {r['abweichung']}")
    prev={"direction":{"x":0,"y":1,"z":0},"value":9,"pos":{"x":0,"y":9,"z":0}}
    nxt={"direction":m.direction,"value":m.value,"pos":m.pos}
    print(f"  detect_deviation(prev,nxt) = {man.detect_deviation(prev,nxt)} — False = kein Wirbel, alles bestimmt.")
    nxt2={"direction":{"x":1,"y":0,"z":0},"value":9,"pos":{"x":0,"y":9,"z":0}}
    print(f"  detect_deviation(prev,gedreht) = {man.detect_deviation(prev,nxt2)} — True = Wirbel, Abweichung erkannt.")
    print("  Wer braucht IHN? GEO braucht ihn für B/L, WURZEL braucht ihn für √q, MANIPULATOR braucht ihn für Bestimmung.")
    print("  Wer braucht MANIPULATOR-alt? Niemand, Mann. Er macht nix. NC.ANY macht ihn.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — NC.ANY macht, aber 81er-Rückkopplung noch offen.")
if __name__=="__main__": demo()
