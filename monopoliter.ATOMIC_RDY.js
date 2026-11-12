// monopoliter.ATOMIC_RDY.js — DER 2TE, MANN — Minimaler Atom-Kern, aber ATOMIC RDY
// 1te war respo.atom.js (STATION). 2te ist monopoliter.js (ATOM).
// Original: value=1 fest, direction=+X, pos=0, move/spin/push, export default. Sauber, minimal, ehrlich.
// Aber: value=1 ist nicht ANY. Kein NC-Check. Kein RDY. Kein tick, kein force am Start. Also: Steht, läuft nicht.
// Wunsch: NC + ANY zusammen = ATOMIC RDY, dann wollen sie auch laufen.
// Also: value = ANY (9, 62, 729...), NC-Check = NC(NC(value))==value, RDY = True wenn NC hält + EYE/BRAIN open.
// Name bleibt Station: monopoliter. Code passt sich an zum Job. Immer ANY zu ANY, aber NC.
const NC = (x) => 15 - x;
const monopoliter = {
  // ATOM-WERT = ANY. Nicht fest 1. ANY rein, NC in Mitte, ANY raus.
  value: 9, // ANY, Mann. Kann 9, 62, 729 sein. Nicht fest.
  direction: { x: 1, y: 0, z: 0 }, // +X, Standard.
  pos: { x: 0, y: 0, z: 0 },
  force: { x: 0, y: 0, z: 0 }, // NEU: force am Start, nicht erst bei push.
  tick: 0, // NEU: tick am Start.
  rdy: false, // NEU: ATOMIC RDY Flag.
  wunsch: "ATOMIC RDY — NC + ANY zusammen laufen",
  // ATOMIC RDY machen: NC prüfen + EYE/BRAIN open.
  makeRdy() {
    const ncOk = NC(NC(this.value)) === this.value;
    const eyeOpen = true; // EYE OPEN, Mann.
    const brainOpen = true; // BRAIN OPEN.
    this.rdy = ncOk && eyeOpen && brainOpen;
    return { rdy: this.rdy, ncOk, eyeOpen, brainOpen, wunsch: this.wunsch };
  },
  // Laufen: Wenn nicht RDY, dann nicht laufen. Wenn RDY, dann laufen.
  move() {
    if (!this.rdy) return { lauft: false, grund: "Nicht RDY. Erst makeRdy(), dann laufen." };
    this.tick += 1;
    this.pos.x += this.direction.x * this.value;
    this.pos.y += this.direction.y * this.value;
    this.pos.z += this.direction.z * this.value;
    this.force = { x: this.direction.x * this.value, y: this.direction.y * this.value, z: this.direction.z * this.value };
    return { lauft: true, tick: this.tick, pos: this.pos, force: this.force, ncOk: NC(NC(this.value)) === this.value };
  },
  spin(axis = "x") {
    if (axis === "x") this.direction = { x: 1, y: 0, z: 0 };
    if (axis === "y") this.direction = { x: 0, y: 1, z: 0 };
    if (axis === "z") this.direction = { x: 0, y: 0, z: 1 };
    return this.direction;
  },
  push(target) {
    if (!target.force) target.force = { x: 0, y: 0, z: 0 };
    target.force.x += this.direction.x * this.value;
    target.force.y += this.direction.y * this.value;
    target.force.z += this.direction.z * this.value;
    return target.force;
  },
  // ANY zu ANY, aber NC: value wechseln, aber NC muss halten.
  setValue(v) {
    this.value = v;
    this.rdy = false; // Nach Wechsel: Neu RDY machen. Nicht einfach laufen.
    return { value: v, rdy: this.rdy, hinweis: "Neu makeRdy() nötig, weil ANY gewechselt." };
  },
};
export default monopoliter;
// H=40 B=41 T=90 Q=57.0 F=1.425 D=3
// HALT = OFFEN — aber ATOMIC RDY = True nach makeRdy(), und ATOM läuft.
