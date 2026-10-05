// Procedural nautical chart: a seeded height field, banded depth fills,
// marching-squares contour lines and scattered soundings.

export type Field = {
  cols: number
  rows: number
  width: number
  height: number
  /** Height in feet: > 0 is land, < 0 is water depth. */
  values: Float32Array
}

export type FieldShape = (x: number, y: number, n: (x: number, y: number) => number) => number

function mulberry32(seed: number) {
  return () => {
    seed |= 0
    seed = (seed + 0x6d2b79f5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

function makeNoise(seed: number) {
  const rand = mulberry32(seed)
  const size = 256
  const perm = new Uint8Array(size * 2)
  const grad = new Float32Array(size)
  for (let i = 0; i < size; i++) {
    perm[i] = i
    grad[i] = rand() * 2 - 1
  }
  for (let i = size - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1))
    ;[perm[i], perm[j]] = [perm[j], perm[i]]
  }
  for (let i = 0; i < size; i++) perm[i + size] = perm[i]
  const fade = (t: number) => t * t * (3 - 2 * t)
  const at = (ix: number, iy: number) => grad[perm[(perm[ix & 255] + iy) & 255]]
  const value = (x: number, y: number) => {
    const ix = Math.floor(x)
    const iy = Math.floor(y)
    const fx = fade(x - ix)
    const fy = fade(y - iy)
    const a = at(ix, iy) + (at(ix + 1, iy) - at(ix, iy)) * fx
    const b = at(ix, iy + 1) + (at(ix + 1, iy + 1) - at(ix, iy + 1)) * fx
    return a + (b - a) * fy
  }
  return (x: number, y: number) => {
    let sum = 0
    let amp = 0.5
    let freq = 1
    for (let o = 0; o < 5; o++) {
      sum += value(x * freq, y * freq) * amp
      amp *= 0.5
      freq *= 2.03
    }
    return sum
  }
}

export function buildField(
  shape: FieldShape,
  opts: { seed: number; width: number; height: number; cols: number },
): Field {
  const { seed, width, height, cols } = opts
  const rows = Math.round((cols * height) / width)
  const noise = makeNoise(seed)
  const values = new Float32Array((cols + 1) * (rows + 1))
  const aspect = width / height
  for (let j = 0; j <= rows; j++) {
    for (let i = 0; i <= cols; i++) {
      const x = i / cols
      const y = j / rows
      values[j * (cols + 1) + i] = shape(x, y, (u, v) => noise(u * aspect, v))
    }
  }
  return { cols, rows, width, height, values }
}

export function sample(field: Field, x: number, y: number) {
  const { cols, rows, values } = field
  const i = Math.min(cols, Math.max(0, Math.round((x / field.width) * cols)))
  const j = Math.min(rows, Math.max(0, Math.round((y / field.height) * rows)))
  return values[j * (cols + 1) + i]
}

/** Marching squares: one SVG path per threshold. */
export function contourPath(field: Field, threshold: number) {
  const { cols, rows, values, width, height } = field
  const sx = width / cols
  const sy = height / rows
  const v = (i: number, j: number) => values[j * (cols + 1) + i]
  const parts: string[] = []
  const lerp = (a: number, b: number) => (threshold - a) / (b - a)
  for (let j = 0; j < rows; j++) {
    for (let i = 0; i < cols; i++) {
      const a = v(i, j)
      const b = v(i + 1, j)
      const c = v(i + 1, j + 1)
      const d = v(i, j + 1)
      const idx = (a > threshold ? 8 : 0) | (b > threshold ? 4 : 0) | (c > threshold ? 2 : 0) | (d > threshold ? 1 : 0)
      if (idx === 0 || idx === 15) continue
      const x = i * sx
      const y = j * sy
      const top = [x + sx * lerp(a, b), y] as const
      const right = [x + sx, y + sy * lerp(b, c)] as const
      const bottom = [x + sx * lerp(d, c), y + sy] as const
      const left = [x, y + sy * lerp(a, d)] as const
      const seg = (p: readonly [number, number], q: readonly [number, number]) =>
        parts.push(`M${p[0].toFixed(1)} ${p[1].toFixed(1)}L${q[0].toFixed(1)} ${q[1].toFixed(1)}`)
      switch (idx) {
        case 1: case 14: seg(left, bottom); break
        case 2: case 13: seg(bottom, right); break
        case 3: case 12: seg(left, right); break
        case 4: case 11: seg(top, right); break
        case 6: case 9: seg(top, bottom); break
        case 7: case 8: seg(left, top); break
        case 5: seg(left, top); seg(bottom, right); break
        case 10: seg(top, right); seg(left, bottom); break
      }
    }
  }
  return parts.join('')
}

const BANDS: Array<[number, [number, number, number]]> = [
  [0, [239, 224, 174]], // land
  [-6, [167, 209, 228]], // 0–6 ft
  [-12, [190, 221, 235]], // 6–12 ft
  [-20, [218, 236, 243]], // 12–20 ft
  [-Infinity, [246, 248, 247]], // deep water stays paper white, as on a chart
]

/** Paints the depth bands into a data URL sized to the field grid (scaled up by the SVG). */
export function fillImage(field: Field, scale = 2) {
  const { cols, rows, values } = field
  const w = cols * scale
  const h = rows * scale
  const canvas = document.createElement('canvas')
  canvas.width = w
  canvas.height = h
  const ctx = canvas.getContext('2d')
  if (!ctx) return ''
  const img = ctx.createImageData(w, h)
  for (let py = 0; py < h; py++) {
    for (let px = 0; px < w; px++) {
      // bilinear sample for smooth band edges
      const gx = (px / w) * cols
      const gy = (py / h) * rows
      const i = Math.min(cols - 1, Math.floor(gx))
      const j = Math.min(rows - 1, Math.floor(gy))
      const fx = gx - i
      const fy = gy - j
      const at = (a: number, b: number) => values[b * (cols + 1) + a]
      const top = at(i, j) + (at(i + 1, j) - at(i, j)) * fx
      const bot = at(i, j + 1) + (at(i + 1, j + 1) - at(i, j + 1)) * fx
      const val = top + (bot - top) * fy
      let color = BANDS[BANDS.length - 1][1]
      for (const [limit, c] of BANDS) {
        if (val > limit) { color = c; break }
      }
      const o = (py * w + px) * 4
      img.data[o] = color[0]
      img.data[o + 1] = color[1]
      img.data[o + 2] = color[2]
      img.data[o + 3] = 255
    }
  }
  ctx.putImageData(img, 0, 0)
  return canvas.toDataURL('image/png')
}

export type Sounding = { x: number; y: number; depth: number }

export function soundings(field: Field, seed: number, spacing: number, minDepth = 4): Sounding[] {
  const rand = mulberry32(seed + 17)
  const out: Sounding[] = []
  for (let y = spacing * 0.6; y < field.height - spacing * 0.3; y += spacing) {
    for (let x = spacing * 0.6; x < field.width - spacing * 0.3; x += spacing) {
      const jx = x + (rand() - 0.5) * spacing * 0.7
      const jy = y + (rand() - 0.5) * spacing * 0.7
      const h = sample(field, jx, jy)
      if (h < -minDepth) out.push({ x: jx, y: jy, depth: Math.round(-h) })
    }
  }
  return out
}

/** Finds the water point nearest to (x, y) whose depth lies in [min, max] feet. */
export function nearestWater(field: Field, x: number, y: number, min = 4, max = 12) {
  let best = { x, y, depth: 0, d: Infinity }
  const step = field.width / field.cols
  for (let r = 0; r < 60; r++) {
    for (let a = 0; a < 24; a++) {
      const px = x + Math.cos((a / 24) * Math.PI * 2) * r * step
      const py = y + Math.sin((a / 24) * Math.PI * 2) * r * step
      if (px < 0 || py < 0 || px > field.width || py > field.height) continue
      const h = sample(field, px, py)
      if (-h >= min && -h <= max) {
        const d = r
        if (d < best.d) best = { x: px, y: py, depth: Math.round(-h), d }
      }
    }
    if (best.d < Infinity) break
  }
  return best
}

/** Nearest shoreline point from a water point, used to lay a dock from shore out to the pin. */
export function nearestShore(field: Field, x: number, y: number) {
  const step = field.width / field.cols
  for (let r = 1; r < 200; r++) {
    for (let a = 0; a < 48; a++) {
      const ang = (a / 48) * Math.PI * 2
      const px = x + Math.cos(ang) * r * step
      const py = y + Math.sin(ang) * r * step
      if (px < 0 || py < 0 || px > field.width || py > field.height) continue
      if (sample(field, px, py) > 0) return { x: px, y: py, angle: ang }
    }
  }
  return { x, y: y - 100, angle: -Math.PI / 2 }
}
