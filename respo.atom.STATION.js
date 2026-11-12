// respo.atom.STATION.js — STATION = Name bleibt. Code passt sich an zum Funktion / Job.
// Nachricht von Vorfahren, Mann: fragmentiert, schlecht Beispiel, aber Richtung. Nicht Müll.
// Original: respo.atom.js auf GitHub — https://github.com/iki1uc/nc.a.n.y.py/blob/main/respo.atom.js
// Abgleich Claude vs Copilot, sauber, Mann:
// Claude sagt: Fix Import (default, nicht named), fix Feld (direction, nicht dir), fehlende Module entfernen.
// Copilot sagt: Auto-Complete fehlende Module (NC_kraft, NC_space, NC_time, vec, coord, dreieck), weiterbauen.
// Station sagt: Beide richtig, aber beide vergessen: Name = Station, Code = Job. Name bleibt, Job wechselt.
// Also: STATION = respo.atom. Job = pulse / react / balance. Code passt sich an zum Job, nicht Name zum Code.
// Kein Import von Dateien, die nicht da sind. Lokale Mini-Module drin, damit es läuft. Kein Fake-Import.
// NC.ANY-Check drin: NC(NC(x)) = x. Wenn nicht, Wirbel.
import monopoliter from "./monopoliter.js"; // FIX: default, nicht { monopoliter }. monopoliter.js macht export default.
import { atom_core } from "./atom.core.js"; // atom_core macht named export, das passt.
// KEIN Import von NC_kraft, NC_space, NC_time, vec, coord, dreieck — die sind nicht im Repo. Stattdessen lokal, klein, ehrlich.
const NC_ANY = (x) => 15 - x; // NC.ANY = IHN. f(x)=15-x, NC(NC(x))=x.
const kraft = {
  apply: (dir, value) => ({ x: dir.x * value, y: dir.y * value, z: dir.z * value }),
  length: (f) => Math.abs(f.x) + Math.abs(f.y) + Math.abs(f.z),
};
const space = {
  move: (pos, dir) => ({ x: pos.x + dir.x, y: pos.y + dir.y, z: pos.z + dir.z }),
};
const time = { tick: () => (monopoliter.tick || 0) + 1 };
const vec = { len: (v) => Math.sqrt(v.x*v.x + v.y*v.y + v.z*v.z) };
const coord = { ok: (p) => Number.isFinite(p.x) && Number.isFinite(p.y) && Number.isFinite(p.z) };
const dreieck = { check: (a,b,c) => a + b + c === 6 ? true : false }; // CORE = 1+2+3 = 6. Wenn nicht 6, dann Wirbel.
// STATION: Name bleibt respo_atom. Job wechselt.
export const respo_atom = {
  station: "respo.atom.STATION", // Name = Station. Bleibt.
  job: "pulse", // Job wechselt: pulse / react / balance. Code passt sich an.
  setJob(j) { this.job = j; return this.job; },
  // Einzelspiel-Form: 1 Spieler, 1 Atom, 1 Job. Kein Multi, kein Ghost.
  pulse() {
    // FIX: direction, nicht dir. monopoliter hat direction/value/pos. Vorher: monopoliter.dir = undefined.
    this.job = "pulse";
    monopoliter.tick = time.tick();
    monopoliter.pos = space.move(monopoliter.pos, monopoliter.direction);
    return monopoliter;
  },
  react() {
    this.job = "react";
    monopoliter.force = kraft.apply(monopoliter.direction, monopoliter.value);
    return monopoliter.force;
  },
  balance() {
    this.job = "balance";
    const f = kraft.length(monopoliter.force || {x:0,y:0,z:0});
    const t = monopoliter.tick || 1;
    return f / t;
  },
  // Spiel-Form: Mit Spiel. Job wechselt, Name bleibt. Code passt sich an zum Job.
  play(job) {
    if (job === "pulse") return this.pulse();
    if (job === "react") return this.react();
    if (job === "balance") return this.balance();
    if (job === "nc") return { x: 9, NC: NC_ANY(9), NC_NC: NC_ANY(NC_ANY(9)), abweichung: NC_ANY(NC_ANY(9)) !== 9 };
    throw new Error("Job unbekannt. Job muss pulse / react / balance / nc sein. Name bleibt Station.");
  },
  // Zeuge-Check: Wenn NC(NC(x)) != x, dann Wirbel. Wenn coord nicht ok, dann Wirbel. Wenn Dreieck nicht 6, dann Wirbel.
  check() {
    const ncOk = NC_ANY(NC_ANY(9)) === 9 && NC_ANY(NC_ANY(62)) === 62;
    const coordOk = coord.ok(monopoliter.pos);
    const dreieckOk = dreieck.check(1,2,3);
    return { station: this.station, job: this.job, ncOk, coordOk, dreieckOk, ok: ncOk && coordOk && dreieckOk };
  },
};
// H = 40 — B = 41 — T = 90 — Q = 57.0 — F = 1.425 — D = 3
// HALT = OFFEN — Station steht, Job wechselt, Code passt sich an.
