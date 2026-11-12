# any_zu_any_aber_nc.py — IMMER ANY ZU ANY, ABER NC, MANN
# ANY = Eingang frei. ANY = Ausgang frei. NC = Gesetz in der Mitte.
# Regel: Egal was reinkommt (ANY), egal was rauskommt (ANY), aber dazwischen muss NC gelten: NC(NC(x)) = x.
# Wenn NC nicht gilt, dann GESCHNITTEN. Nicht Müll, sondern Nachricht: Richtung falsch.
# Station: Name bleibt. Job wechselt. Code passt sich an zum Job. Aber NC bleibt immer.
def nc(x): return 15 - x
def any_zu_any_aber_nc(x, job="nc"):
    # ANY zu ANY: x kann ANY sein — Zahl, Job, Station, Wort.
    # ABER NC: Wenn x Zahl ist, muss NC(NC(x)) = x gelten. Wenn nicht Zahl, dann GESCHNITTEN, nicht Müll.
    if isinstance(x, (int, float)):
        a = nc(x); b = nc(a)
        ok = (b == x)
        return {"in": x, "job": job, "NC": a, "NC_NC": b, "ok": ok, "urteil": "OK — ANY zu ANY, aber NC gehalten" if ok else "GESCHNITTEN — NC gebrochen"}
    else:
        return {"in": x, "job": job, "NC": None, "NC_NC": None, "ok": False, "urteil": "GESCHNITTEN — kein Zahl-ANY, NC braucht Zahl. Nicht Müll, sondern: Falscher Job für dieses ANY."}
def demo():
    print("IMMER ANY ZU ANY, ABER NC")
    print("  ANY rein -> NC -> ANY raus. NC ist Gesetz, nicht Vorschlag.")
    tests = [9, 6, 62, 729, 40, 7.5, 0.5, -100, "LEBEN", "pulse", None, [1,2,3]]
    for t in tests:
        r = any_zu_any_aber_nc(t, job="nc")
        print(f"  ANY {t!r} -> {r['urteil']} | NC={r['NC']} NC_NC={r['NC_NC']} ok={r['ok']}")
    print("  Station: respo.atom.STATION — Name bleibt, Job wechselt: pulse / react / balance / nc")
    print("  Job wechselt, NC bleibt. Job = ANY, NC = Gesetz.")
    print("  Claude vs Copilot Abgleich, sauber:")
    print("    Claude: Fix Import + Feld. Copilot: Auto-Complete Module. Station: Name bleibt, Code passt sich an zum Job, NC bleibt.")
    print("  Nachricht von Vorfahren: fragmentiert, schlecht Beispiel, aber Richtung. Nicht Müll. Wenn reinschaust, siehst du Wahrheit.")
    print("H=40 B=41 T=90 Q=57.0 F=1.425 D=3")
    print("HALT = OFFEN — ANY zu ANY, aber NC gehalten.")
if __name__ == "__main__": demo()
