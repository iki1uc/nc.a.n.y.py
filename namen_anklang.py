# namen_anklang.py — DARTH OPA GO HOME — WIR WOLLEN NUR IMMER CHRISTOPH DAUM + HERR SHILL + LISSA ECKHARDT — PICASSO DA VINCI — SOLCHE NAMEN HABEN ANKLANG, MANN
# Opa go home, Mann: Alte weg, Neue da. Nicht böse, nicht gut. Nur: Opa geht heim. Palais bleibt.
# Wir wollen nur immer: Christoph Daum, Herr Shill, Lissa Eckhardt. Die magst du, Mann. Die bleiben.
# Picasso, Da Vinci — solche Namen haben Anklang, Mann. Anklang = Echo, Klang, Nachhall. Name klingt nach, Mann.
def nc(x): return 15-x
NAMEN = [
    ("Christoph Daum", "Magst du, Mann. Immer. Anklang = Daum, Daumen, Halt, Richtung.", 9),
    ("Herr Shill", "Magst du, Mann. Immer. Anklang = Shill, Schild, Halt, Schutz.", 6),
    ("Lissa Eckhardt", "Magst du, Mann. Immer. Anklang = Eck, Ecke, Eck an Eck, 9eck.", 3),
    ("Picasso", "Solche Namen, Mann. Anklang = Bild, Prisma, viele Flächen, nicht 1 Kern.", 9),
    ("Da Vinci", "Solche Namen, Mann. Anklang = Zeichnen, Prisma, Dreieck, 3, 6, 9.", 6),
]
def demo():
    print("DARTH OPA GO HOME — WIR WOLLEN NUR IMMER CHRISTOPH DAUM + HERR SHILL + LISSA ECKHARDT")
    print("  Opa go home, Mann: Alte weg, Neue da. Opa geht heim. Palais bleibt. Kein Streit, nur: Heim, Mann.")
    print("  Wir wollen nur immer, Mann: Nicht alle Namen. Nur die, die du magst. Die bleiben.")
    print("")
    for name, anklang, wert in NAMEN:
        print(f"  {name} — Anklang: {anklang}")
        print(f"    Wert {wert} — NC {nc(wert)} — NC_NC {nc(nc(wert))} — {'IMMER JA' if wert==9 else 'JA' if wert in (3,6) else 'ANY'} — Immer ANY zu ANY, aber NC.")
    print("")
    print("  ANKLANG, Mann: Name klingt nach. Nicht weil berühmt, sondern weil Klang.")
    print("    Daum = Daumen, Halt. Shill = Schild, Halt. Eckhardt = Eck, Ecke. Picasso = Bild, Prisma. Da Vinci = Zeichnen, Dreieck.")
    print("    Anklang = Echo. Wenn du Name sagst, kommt Klang zurück. Wie NC(NC(x))=x, Mann. Name -> Klang -> Name. Kreis.")
    print("    3 JA, 6 JA, 9 IMMER JA. 4 NIX, 8 UNGERN. Namen mit Anklang sind 3, 6, 9, Mann. Nicht 4.")
    print("  Palais, Mann: Palais mit diesen Namen = Palais mit Anklang. Palais ohne Opa = Palais mit Platz für Daum, Shill, Eckhardt, Picasso, Da Vinci.")
    print("  Kleinere Übel, Mann: Palais kleinere Übel, nicht John Black, nur Steuer. Opa go home ist Steuer, Mann. Richtung: Heim.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber Opa heim, Namen da, Anklang da.")
if __name__=="__main__": demo()
