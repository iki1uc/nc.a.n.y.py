# group_scan_3x3_bth_coop.py — GROUP SCAN, 3x3, B T H, COOP TEAM BUILD BIND, MANN
# GROUP SCAN Original: Kein Scan. Nur console.log GHOST/PX/PC SCAN 0,1,2 + Weiterleitung nach 900ms auf Copilot-Link.
# Ehrlich, Mann: Das ist Tür, nicht Scan. Kein Prüfen, kein Zeuge, kein NC-Check. Nur Timer + Redirect.
# 3x3 kucken: B T H — B=41 BASIS, T=90 TIEFE, H=40 HALT. 3x3 = 9 Zellen. Jede Zelle = Paar-Summe.
# COOP TEAM BUILD BIND: Team baut zusammen. Jeder baut 1 Reihe. BIND = NC bindet: NC(NC(x))=x muss halten, sonst kein Bind.
def nc(x): return 15-x
B, T, H = 41, 90, 40
labels = ["B=41 BASIS", "T=90 TIEFE", "H=40 HALT"]
vals = [B, T, H]
print("GROUP SCAN — 3x3 — B T H — COOP TEAM BUILD BIND")
print("  Original GROUP SCAN: GHOST 0,1,2 / PX 0,1,2 / PC 0,1,2 — nur console.log, kein Scan.")
print("  Dann: window.location.href = Copilot-Link nach 900ms. Das ist Weiterleitung, nicht Scan.")
print("  Sauber: Kein Auto-Redirect. Nur Coop Build + Bind mit NC-Check. Jeder klickt selbst, wenn er will.")
print("")
print("  3x3 B T H — Paar-Summe (Zeile + Spalte):")
print("        B(41)  T(90)  H(40)")
for i, (li, vi) in enumerate(zip(labels, vals)):
    row = [vi+vj for vj in vals]
    print(f"  {li:12} {row[0]:5}  {row[1]:5}  {row[2]:5}  | NC: {[nc(v) for v in row]}")
print("")
print("  3x3 Mitte: T+T = 180. Ecken: B+B=82, B+H=81, H+B=81, H+H=80. Mitte der 3x3-Summen? (82+180+80)/3 = 114. Nicht 41. Nicht 40. 3x3 ist nicht 9x9, Mann.")
print("  3x3 Mitte Zelle: T(90) + T(90) = 180. NC(180) = -165. NC(NC(180)) = 180. NC hält, auch bei 180.")
print("")
print("  COOP TEAM BUILD BIND:")
teams = [("EYE", "Sehen", "B-Reihe", B), ("BRAIN", "Halten", "T-Reihe", T), ("CORE", "Prüfen", "H-Reihe", H)]
for name, job, reihe, v in teams:
    bind_ok = nc(nc(v)) == v
    print(f"    {name} — {job} — baut {reihe} (Wert {v}) — NC={nc(v)} NC_NC={nc(nc(v))} — BIND {'OK' if bind_ok else 'GESCHNITTEN'}")
print("  BIND-Regel: Alle 3 müssen NC halten, sonst kein Team-Bind. 1 bricht, alle bricht. Nicht Müll, sondern: Falscher Job für dieses ANY.")
print("  COOP: EYE baut B, BRAIN baut T, CORE baut H. Keiner baut alles. Zusammen = 3x3.")
print("  BUILD: Jede Reihe einzeln bauen, dann Binden. Nicht alles auf einmal.")
print("  BIND: NC(NC(x))=x für B, T, H. Wenn alle 3 True, dann BIND=True, Team läuft.")
print("  GROUP SCAN sauber: Kein 900ms-Redirect. Kein Ghost/PX/PC-Fake. Nur: Zeig 3x3, bau Reihe, bind mit NC, dann erst — wenn du willst — klick selbst auf Link.")
print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
print("HALT = OFFEN — aber 3x3 gebaut, Team gebunden.")
if __name__ == "__main__": pass
