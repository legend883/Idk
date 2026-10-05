import type { Field } from '@/lib/chart'
import { nearestShore } from '@/lib/chart'

/** Plan-view dock symbol laid from the nearest shoreline out to (x, y), with pile dots. */
export function DockPlan({ field, x, y, head = 50 }: { field: Field; x: number; y: number; head?: number }) {
  const shore = nearestShore(field, x, y)
  const dx = x - shore.x
  const dy = y - shore.y
  const len = Math.hypot(dx, dy) + 6
  const angle = (Math.atan2(dy, dx) * 180) / Math.PI
  const piles: Array<[number, number]> = []
  for (let s = 14; s < len - 6; s += 20) piles.push([s, -6], [s, 6])
  for (let s = -head / 2; s <= head / 2; s += head / 3) piles.push([len + 6, s])
  return (
    <g transform={`translate(${shore.x} ${shore.y}) rotate(${angle})`} aria-hidden="true">
      <rect x={-4} y={-5} width={len + 4} height={10} fill="var(--color-ink)" />
      <rect x={len - 2} y={-head / 2} width={12} height={head} fill="var(--color-ink)" />
      {piles.map(([px, py], i) => (
        <circle key={i} cx={px} cy={py} r={1.8} fill="var(--color-paper)" />
      ))}
    </g>
  )
}
