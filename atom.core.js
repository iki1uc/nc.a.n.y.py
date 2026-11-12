// atom.core.js — NEU, MANN — Alte weg, Neue da, ich war alt. Jetzt Neu.
// ALTE WEG: import { monopoliter } from "./monopoliter.js" — ALT. Datei weg. Import weg. dir weg.
// NEUE DA: import monopoliter from "./monopoliter.ATOMIC_RDY.js" — NEU. Default, nicht named. Nicht { monopoliter.ATOMIC_RDY.js }.
// Dein Paste: import {monopoliter.ATOMIC_RDY.js } from "./monopoliter.ATOMIC_RDY.js" — geht nicht, Mann. { } mit Punkt geht nicht. Das ist nicht JS. Das ist Alt.
// NEU: import monopoliter from "./monopoliter.ATOMIC_RDY.js"; // default. So geht es, Mann.
import monopoliter from "./monopoliter.ATOMIC_RDY.js"; // NEU: default, nicht { }. Datei = NEUE, nicht ALTE.
// NEU: direction, nicht dir. NEUE Datei hat direction, tick, force, rdy. ALTE hatte dir nicht. ALTE weg.
export const atom_core = {
  pulse() {
    // NEU: tick aus NEUER Datei. NEUE hat tick, rdy, makeRdy. ALTE hatte kein tick, kein rdy.
    monopoliter.tick = (monopoliter.tick || 0) + 1;
    const gerade = monopoliter.tick % 2 === 0;
    // Gerade = LAUF, Ungerade = FALL-mitgerechnet, Tiefe +1. So wie du sagst, Mann.
    if (!gerade) monopoliter.tiefe = (monopoliter.tiefe || 0) + 1;
    return { tick: monopoliter.tick, gerade, zustand: gerade ? "LAUF" : "FALL-mitgerechnet", tiefe: monopoliter.tiefe || 0 };
  },
  react() {
    // NEU: direction, nicht dir. NEUE Datei: direction = {x:1,y:0,z:0}. ALTE: dir = undefined. Darum ging nix, Mann.
    monopoliter.force = {
      x: monopoliter.direction.x * monopoliter.value,
      y: monopoliter.direction.y * monopoliter.value,
      z: monopoliter.direction.z * monopoliter.value
    };
    return monopoliter.force;
  },
  balance() {
    const f = Math.abs(monopoliter.force.x) + Math.abs(monopoliter.force.y) + Math.abs(monopoliter.force.z);
    const t = monopoliter.tick || 1;
    return f / t;
  },
  // NEU: makeRdy aus NEUER Datei. ALTE hatte kein makeRdy. NEUE hat makeRdy. Ohne RDY kein Laufen.
  makeRdy() { return monopoliter.makeRdy(); },
  // NEU: setValue aus NEUER Datei. ALTE hatte fest value=1. NEUE hat ANY.
  setValue(v) { return monopoliter.setValue(v); },
};
// H=40 B=41 T=90 Q=57.0 F=1.425 D=3
// HALT = OFFEN — aber NEU, nicht ALT. Alte weg, Neue da.
