import { useEffect, useId, useMemo, useRef, useState, type ReactNode } from 'react'
import gsap from 'gsap'
import { buildField, contourPath, fillImage, soundings, type Field, type FieldShape } from '@/lib/chart'
import { cn } from '@/lib/utils'

type Props = {
  shape: FieldShape
  seed: number
  width: number
  height: number
  cols?: number
  soundingSpacing?: number
  /** Point the sonar-sweep reveal grows from, in chart units. */
  revealFrom?: { x: number; y: number }
  className?: string
  label: string
  children?: (field: Field) => ReactNode
}

const CONTOURS = [
  { t: -6, dash: '' },
  { t: -12, dash: '' },
  { t: -20, dash: '6 4' },
  { t: -30, dash: '2 4' },
]

export function NauticalChart({
  shape,
  seed,
  width,
  height,
  cols = 200,
  soundingSpacing = 64,
  revealFrom,
  className,
  label,
  children,
}: Props) {
  const field = useMemo(() => buildField(shape, { seed, width, height, cols }), [shape, seed, width, height, cols])
  const [fill, setFill] = useState('')
  const sweepRef = useRef<SVGCircleElement>(null)
  const id = useId().replace(/:/g, '')
  const paths = useMemo(
    () => ({
      shore: contourPath(field, 0),
      lines: CONTOURS.map((c) => ({ ...c, d: contourPath(field, c.t) })),
      marks: soundings(field, seed, soundingSpacing),
    }),
    [field, seed, soundingSpacing],
  )

  useEffect(() => {
    setFill(fillImage(field, 3))
  }, [field])

  useEffect(() => {
    const el = sweepRef.current
    if (!el || !revealFrom) return
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const full = Math.hypot(width, height)
    if (reduce) {
      el.setAttribute('r', String(full))
      return
    }
    const tween = gsap.fromTo(el, { attr: { r: 0 } }, { attr: { r: full }, duration: 2.4, ease: 'expo.out', delay: 0.25 })
    return () => {
      tween.kill()
    }
  }, [revealFrom, width, height])

  const ticks = useMemo(() => {
    // Chart border graduation: alternating ink / paper bars along the neat line.
    const out: Array<{ x: number; y: number; w: number; h: number }> = []
    const step = 40
    const t = 7
    for (let x = 0, k = 0; x < width; x += step, k++) {
      if (k % 2 === 0) out.push({ x, y: 0, w: step, h: t }, { x, y: height - t, w: step, h: t })
    }
    for (let y = 0, k = 0; y < height; y += step, k++) {
      if (k % 2 === 0) out.push({ x: 0, y, w: t, h: step }, { x: width - t, y, w: t, h: step })
    }
    return out
  }, [width, height])

  const masked = revealFrom ? `url(#sweep-${id})` : undefined

  return (
    <svg
      viewBox={`0 0 ${width} ${height}`}
      preserveAspectRatio="xMidYMid slice"
      className={cn('block h-full w-full', className)}
      role="img"
      aria-label={label}
    >
      {revealFrom && (
        <defs>
          <mask id={`sweep-${id}`}>
            <rect width={width} height={height} fill="black" />
            <circle ref={sweepRef} cx={revealFrom.x} cy={revealFrom.y} r={0} fill="white" />
          </mask>
        </defs>
      )}
      <rect width={width} height={height} fill="var(--color-paper)" />
      <g mask={masked}>
        {fill && <image href={fill} width={width} height={height} preserveAspectRatio="none" />}
        {paths.lines.map((l) => (
          <path
            key={l.t}
            d={l.d}
            fill="none"
            stroke="var(--color-contour)"
            strokeWidth={0.9}
            strokeDasharray={l.dash || undefined}
            opacity={0.75}
            vectorEffect="non-scaling-stroke"
          />
        ))}
        <path d={paths.shore} fill="none" stroke="var(--color-land-line)" strokeWidth={1.6} strokeLinecap="round" vectorEffect="non-scaling-stroke" />
        <g className="hydro" fill="var(--color-ink-2)" fontSize={13} textAnchor="middle" aria-hidden="true">
          {paths.marks.map((m, i) => (
            <text key={i} x={m.x} y={m.y}>
              {m.depth}
            </text>
          ))}
        </g>
        {children?.(field)}
      </g>
      <g fill="var(--color-ink)" aria-hidden="true">
        {ticks.map((t, i) => (
          <rect key={i} {...t} />
        ))}
      </g>
      <rect x={0.5} y={0.5} width={width - 1} height={height - 1} fill="none" stroke="var(--color-ink)" strokeWidth={1} />
      <rect x={7.5} y={7.5} width={width - 15} height={height - 15} fill="none" stroke="var(--color-ink)" strokeWidth={0.6} />
    </svg>
  )
}

export function CompassRose({ x, y, r, className }: { x: number; y: number; r: number; className?: string }) {
  const ticks = Array.from({ length: 72 }, (_, i) => i * 5)
  return (
    <g transform={`translate(${x} ${y})`} className={className} aria-hidden="true" color="var(--color-magenta)">
      <circle r={r} fill="none" stroke="currentColor" strokeWidth={1.2} />
      <circle r={r * 0.82} fill="none" stroke="currentColor" strokeWidth={0.6} />
      {ticks.map((deg) => {
        const long = deg % 30 === 0
        const a = (deg * Math.PI) / 180
        const r1 = long ? r * 0.82 : r * 0.9
        return (
          <line
            key={deg}
            x1={Math.sin(a) * r1}
            y1={-Math.cos(a) * r1}
            x2={Math.sin(a) * r}
            y2={-Math.cos(a) * r}
            stroke="currentColor"
            strokeWidth={long ? 1.1 : 0.6}
          />
        )
      })}
      {[0, 90, 180, 270].map((deg) => (
        <text
          key={deg}
          x={Math.sin((deg * Math.PI) / 180) * r * 0.66}
          y={-Math.cos((deg * Math.PI) / 180) * r * 0.66 + 4}
          fontSize={r * 0.16}
          textAnchor="middle"
          fill="currentColor"
          fontWeight={600}
          style={{ fontVariationSettings: "'wdth' 112" }}
        >
          {deg === 0 ? 'N' : deg}
        </text>
      ))}
      <path d={`M0 ${-r * 0.5} L${r * 0.07} 0 L0 ${r * 0.5} L${-r * 0.07} 0Z`} fill="currentColor" opacity={0.9} />
      <path d={`M${-r * 0.5} 0 L0 ${r * 0.07} L${r * 0.5} 0 L0 ${-r * 0.07}Z`} fill="currentColor" opacity={0.35} />
      <circle r={2.5} fill="var(--color-paper)" stroke="currentColor" />
    </g>
  )
}
