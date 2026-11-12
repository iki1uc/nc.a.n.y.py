NC.ANY = IHN — MANIPULATOR, DER MACHT
  Start: direction {'x': 1, 'y': 0, 'z': 0} value 1 pos {'x': 0, 'y': 0, 'z': 0}
  force_direction(0,1,0) -> {'x': 0, 'y': 1, 'z': 0} — jetzt greift es, Mann. direction, nicht dir.
  force_value(9) -> 9 — value, nicht val.
  move() -> {'x': 0, 'y': 9, 'z': 0} — pos bewegt sich: (0,9,0). Vorher: Nix bewegt, weil dir/val falsch.
  NC.ANY-Bestimmung:
    x=9 -> NC=6 -> NC(NC)=9 -> Abweichung? False
    x=6 -> NC=9 -> NC(NC)=6 -> Abweichung? False
    x=62 -> NC=-47 -> NC(NC)=62 -> Abweichung? False
    x=729 -> NC=-714 -> NC(NC)=729 -> Abweichung? False
    x=40 -> NC=-25 -> NC(NC)=40 -> Abweichung? False
  detect_deviation(prev,nxt) = False — False = kein Wirbel, alles bestimmt.
  detect_deviation(prev,gedreht) = True — True = Wirbel, Abweichung erkannt.
  Wer braucht IHN? GEO braucht ihn für B/L, WURZEL braucht ihn für √q, MANIPULATOR braucht ihn für Bestimmung.
  Wer braucht MANIPULATOR-alt? Niemand, Mann. Er macht nix. NC.ANY macht ihn.
H=40 B=41 T=90 Q=57.0 F=1.425 D=3
HALT = OFFEN — NC.ANY macht, aber 81er-Rückkopplung noch offen.
