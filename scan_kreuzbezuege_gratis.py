# scan_kreuzbezuege_gratis.py — JEDE SEITE MIT NAME SCAN KANN KREUZBEZÜGE GRATIS VON ALLEM, MANN
# Regel, Mann: Wenn Name "scan" enthält, dann Kreuzbezüge gratis. Kein Import, kein Bezahlen, kein Fragen. Nur Name.
# Nicht Müll, sondern Nachricht: Scan = Sehen + Verbinden. Scan sieht alles, also darf Scan alles verlinken.
# PY JA. Vol.1.en. Eck an Eck und Ecken. Immer ANY zu ANY, aber NC.
def nc(x): return 15-x
ALLE = [
    ("defrag.provokation.py", "EYE + BRAIN + CORE, Zeuge SHA-256, HALT OFFEN"),
    ("rawator.py", "Kreis 729->81->9->3->1->729, CIRC.LER, CTRL"),
    ("nc_any_ihn.py", "NC.ANY = IHN, MANIPULATOR der macht, direction/value"),
    ("any_zu_any_aber_nc.py", "Immer ANY zu ANY, aber NC, NC(NC(x))=x"),
    ("nc_any_atomic_rdy.py", "NC+ANY zusammen, Wunsch ATOMIC RDY, dann laufen"),
    ("monopoliter.ATOMIC_RDY.js", "2te, Atom-Kern, value=ANY, RDY, tick, pos, force"),
    ("respo.atom.STATION.js", "1te, Station, Name bleibt, Code passt sich an zum Job"),
    ("atom.core.js", "Atom-Reaktion, pulse/react/balance"),
    ("group_scan_3x3_bth_coop.py", "GROUP SCAN sauber, kein 900ms-Redirect, 3x3 BTH, COOP BIND"),
    ("scan_b_h_t_eck_an_eck.py", "SCAN B.H.T, Eck an Eck, Ecken, Diagonale 131=131"),
    ("vol1_en_py.py", "Vol.1.en, PY JA, 1 Vol, 1 Index, 1 Ori"),
    ("ori.html", "Ori, MAINBOARD HARDWARE, 1409 Zeilen, CPU/GPU/RAM/SSD"),
    ("index.html / GROUP SCAN", "Index klein, GROUP SCAN, kein Scan, nur Tür — weg vom Index"),
    ("WURZEL-Q-729", "81x3x9=2187, √q, Verdichtung, Verlust protokolliert"),
    ("GEO.Y.X.Z", "DER/DIE/DAS, B=(a+b+c)/3, L=1-B, 5 Krallen, Gatekeeper"),
    ("lol.PL", "729 AUTO.ZOOM, MINI 81 -> MAXI 729, Zoom=Zeit"),
]
def ist_scan_seite(name):
    # Scan-Regel: Name enthält "scan" (klein). Dann gratis. Sonst nicht gratis, nur mit NC-Check.
    return "scan" in name.lower()
def kreuzbezuege_gratis(seiten_name):
    # Wenn Scan-Seite, dann alle Kreuzbezüge gratis. Wenn nicht Scan, dann nur mit NC-Check.
    if ist_scan_seite(seiten_name):
        return {"seite": seiten_name, "ist_scan": True, "gratis": True, "kreuzbezuege": ALLE, "grund": "Name enthält scan -> gratis von allem."}
    else:
        return {"seite": seiten_name, "ist_scan": False, "gratis": False, "kreuzbezuege": [], "grund": "Name enthält kein scan -> nicht gratis. Nur mit NC-Check."}
def demo():
    print("JEDE SEITE MIT NAME SCAN KANN KREUZBEZÜGE GRATIS VON ALLEM")
    print("  Regel: scan im Name -> gratis. Kein Import, kein Bezahlen, kein Fragen. Nur Name.")
    print("  Scan = Sehen + Verbinden. Scan sieht alles, also darf Scan alles verlinken.")
    print("")
    for test in ["scan.b.h.t.html.js", "GROUP SCAN", "group_scan_3x3_bth_coop.py", "scan_kreuzbezuege_gratis.py", "ori.html", "index.html", "monopoliter.js"]:
        r = kreuzbezuege_gratis(test)
        print(f"  Seite {test!r} -> ist_scan={r['ist_scan']} gratis={r['gratis']} — {r['grund']}")
        if r["gratis"]:
            print(f"    Kreuzbezüge gratis: {len(r['kreuzbezuege'])} Stück von allem.")
            for name, was in r["kreuzbezuege"]:
                print(f"      - {name} : {was}")
        print("")
    print("  Eck an Eck, Mann: Scan-Seite an Scan-Seite = Kreuzbezug an Kreuzbezug. Scan sieht Scan, Scan verlinkt Scan.")
    print("  B.H.T Ecken: Scan sieht Ecken, Scan verlinkt Ecken. B+B=82, B+T=131, T+B=131, T+T=180 — alle gratis.")
    print("  NC-Check für Scan: NC(NC(82))=82, NC(NC(131))=131, NC(NC(180))=180 — alle True. Scan hält NC, auch gratis.")
    print("  COOP: EYE baut Scan, BRAIN hält Scan, CORE prüft Scan. Zusammen = Kreuzbezüge gratis.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — aber Scan kann Kreuzbezüge gratis von allem.")
if __name__=="__main__": demo()
