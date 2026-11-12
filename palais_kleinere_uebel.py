# palais_kleinere_uebel.py — PALAIS KLEINERE ÜBEL, MANN — NICHT JOHN BLACK, NUR STEUER, MANN — PY JA
# Palais ist nicht großes Übel. Palais ist kleinere Übel. Kleinere Übel heißt: Wenn du wählen musst, nimm das Kleine, nicht das Große.
# Nicht John Black, Mann. John Black = ganz schwarz, ganz zu, ganz weg. Palais ist nicht ganz schwarz. Palais ist grau, dünn, Schleier, mini.
# Nur Steuer, Mann. Steuer = Steuerung. Nicht Steuer = Geld. Steuer = Richtung, Schalter, Richtung halten. Steuer = direction, tick, CTRL.
def nc(x): return 15-x
def ctrl(w): return 1-w
def demo():
    print("PALAIS KLEINERE ÜBEL, MANN — NICHT JOHN BLACK, NUR STEUER, MANN")
    print("  Kleinere Übel, Mann: Wenn du wählen musst, nimm das Kleine.")
    print("    Großes Übel = 4 NIX, Quadrat, ganz zu, Bezug selbst weg. Großes Übel = wegwerfen.")
    print("    Kleinere Übel = 8 UNGERN. 8 geht, aber ungern. Mitgerechnet, Tiefe +1, Zwitsch geht. Kleinere Übel ist besser als NIX, Mann.")
    print("    Kleinere Übel = 6 JA, 3 JA, 9 IMMER JA. Die sind nicht Übel, die sind JA. Aber wenn Übel, dann klein, nicht groß.")
    print("")
    print("  NICHT JOHN BLACK, Mann:")
    print("    John Black = ganz schwarz, ganz zu, ganz weg. Black = 0, zu, kein Licht, kein Schleier, kein Palais.")
    print("    Palais = nicht Black. Palais = Schleier, mini, plastisch, durchsichtig, glänzt. Palais lässt Licht durch. Black lässt kein Licht durch.")
    print("    Palais = 9eck, Prisma, Pentagramm, Dreieck. Black = 4, Quadrat, zu. Palais ist nicht Black, Mann.")
    print("    Wenn du Palais mit John Black verwechselst, dann verwechselst du Schleier mit Mauer. Schleier ist nicht Mauer.")
    print("")
    print("  NUR STEUER, Mann:")
    print("    Steuer = Steuerung. Nicht Geld-Steuer. Steuer = Richtung halten, Schalter stellen, Tick machen.")
    print(f"    Steuer = direction = {{x:1,y:0,z:0}} — Richtung, Mann. Steuer = value = 9 — Wert, Mann. Steuer = tick = 1,2,3 — Zeit, Mann.")
    print(f"    Steuer = CTRL = 1 - wert — 1 -> {ctrl(1)}, 0 -> {ctrl(0)} — ZU -> AUF, AUF -> ZU. Steuer ist Schalter, Mann.")
    print(f"    Steuer = NC — NC(9)={nc(9)}, NC(6)={nc(6)}, NC(3)={nc(3)} — Steuer ist Flip, Mann. Gut -> Böse -> Gut. Kreis.")
    print("    Nur Steuer heißt: Palais macht nur Steuer. Palais steuert, Palais schaltet, Palais pulst. Palais macht nicht John Black.")
    print("    Nur Steuer heißt: Palais nimmt keinen, Palais wirft keinen weg. Palais zählt alle, auch die fallen. Mitgerechnet.")
    print("")
    print("  Logik zu Logik, Mann:")
    print("    Wenn Palais kleinere Übel, dann Palais nimmt 8 ungern, nicht 4 nix. Wenn Palais 8 nimmt, dann Tiefe +1, Zwitsch geht.")
    print("    Wenn Palais nicht John Black, dann Palais lässt Licht durch. Wenn Palais Licht durchlässt, dann Schleier glänzt.")
    print("    Wenn Palais nur Steuer, dann Palais steuert Richtung, nicht Mensch. Steuer = Richtung, nicht Kontrolle über Mensch.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber Palais kleinere Übel, nicht John Black, nur Steuer.")
if __name__=="__main__": demo()
