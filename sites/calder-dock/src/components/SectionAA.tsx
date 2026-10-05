import { useEffect, useId, useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

// Drawing units: 15 px per foot. Full pond surface sits at y = 270.
const FT = 15
const FULL = 270
const MAX_UP = 1 // ft above full pond
const MAX_DOWN = 3 // ft below full pond
const DECK = 236
const HINGE = { x: 560, y: DECK }
const GANGWAY = 170
const FLOAT_X = 676
const FLOAT_W = 330

const BED: Array<[number, number]> = [
  [0, 226], [120, 228], [170, 233], [220, 246], [270, 268], [320, 300], [370, 333], [430, 366], [500, 392],
  [580, 414], [680, 433], [800, 450], [920, 462], [1040, 470], [1200, 476],
]

function bedY(x: number) {
  for (let i = 1; i < BED.length; i++) {
    const [x0, y0] = BED[i - 1]
    const [x1, y1] = BED[i]
    if (x <= x1) return y0 + ((x - x0) / (x1 - x0)) * (y1 - y0)
  }
  return BED[BED.length - 1][1]
}

const FIXED_PILES = [236, 316, 396, 476, 550]
const GUIDE_PILES = [760, 960]
const EMBED = 6 * FT

function waterPoints(wl: number) {
  // Find where the surface meets the bank, then trace the bed back under the water.
  let startX = 0
  for (let x = 0; x <= 1200; x += 2) {
    if (bedY(x) >= wl) { startX = x; break }
  }
  const pts = [`${startX},${wl}`, `1200,${wl}`, `1200,${bedY(1200)}`]
  for (let i = BED.length - 1; i >= 0; i--) if (BED[i][0] > startX) pts.push(`${BED[i][0]},${BED[i][1]}`)
  pts.push(`${startX},${wl}`)
  return pts.join(' ')
}

const bedPath = `M0 620 L${BED.map(([x, y]) => `${x} ${y}`).join(' L')} L1200 620 Z`

export function SectionAA() {
  const id = useId().replace(/:/g, '')
  const sectionRef = useRef<HTMLElement>(null)
  const waterRef = useRef<SVGPolygonElement>(null)
  const surfaceRef = useRef<SVGLineElement>(null)
  const floatRef = useRef<SVGGElement>(null)
  const gangRef = useRef<SVGLineElement>(null)
  const levelMarkRef = useRef<SVGGElement>(null)
  const levelTextRef = useRef<SVGTextElement>(null)
  const angleTextRef = useRef<SVGTextElement>(null)
  const readoutRef = useRef<HTMLOutputElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const state = useRef({ ft: 0 })

  const apply = (ft: number) => {
    state.current.ft = ft
    const wl = FULL - ft * FT
    waterRef.current?.setAttribute('points', waterPoints(wl))
    surfaceRef.current?.setAttribute('y1', String(wl))
    surfaceRef.current?.setAttribute('y2', String(wl))
    floatRef.current?.setAttribute('transform', `translate(0 ${wl - FULL})`)
    const floatTop = wl - 10
    const dy = floatTop - HINGE.y
    const dx = Math.sqrt(Math.max(0, GANGWAY * GANGWAY - dy * dy))
    gangRef.current?.setAttribute('x2', String(HINGE.x + dx))
    gangRef.current?.setAttribute('y2', String(floatTop))
    levelMarkRef.current?.setAttribute('transform', `translate(1110 ${wl})`)
    const label = ft === 0 ? 'Full pond' : `${ft > 0 ? '+' : '−'}${Math.abs(ft).toFixed(1)} ft`
    if (levelTextRef.current) levelTextRef.current.textContent = label
    const angle = Math.round((Math.atan2(dy, dx) * 180) / Math.PI)
    if (angleTextRef.current) angleTextRef.current.textContent = `Gangway ${angle}°`
    if (readoutRef.current) readoutRef.current.textContent = `${label} · gangway ${angle}°`
    if (inputRef.current && document.activeElement !== inputRef.current) inputRef.current.value = String(ft)
  }

  useEffect(() => {
    apply(0)
    const mm = gsap.matchMedia()
    mm.add('(prefers-reduced-motion: no-preference)', () => {
      const proxy = { ft: 0.6 }
      apply(proxy.ft)
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: sectionRef.current,
          start: 'top 72px',
          end: '+=130%',
          scrub: 0.6,
          pin: window.matchMedia('(min-width: 1024px)').matches,
        },
        onUpdate: () => apply(Math.round(proxy.ft * 10) / 10),
      })
      tl.to(proxy, { ft: -MAX_DOWN, duration: 1, ease: 'sine.inOut' }).to(proxy, { ft: 0, duration: 0.6, ease: 'sine.inOut' })
      return () => tl.kill()
    })
    return () => mm.revert()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <section ref={sectionRef} id="engineering" className="relative scroll-mt-20 overflow-hidden border-b border-ink/15 bg-shoal-2">
      <div className="mx-auto grid max-w-[1600px] gap-10 px-5 py-20 sm:px-8 lg:min-h-[calc(100svh-4.5rem)] lg:grid-cols-12 lg:items-center lg:px-12 lg:py-16">
        <div className="lg:col-span-4">
          <h2 className="display text-[clamp(2.2rem,3.6vw,3.4rem)]">Built for the lake you have in March and in August.</h2>
          <p className="mt-6 max-w-[46ch] text-lg text-ink-2">
            Lake levels move. A dock that is drawn for one water line ends up as a step down in summer or a climb in winter. We draw the section
            first and build to it.
          </p>
          <ul className="mt-8 space-y-4 text-ink-2">
            <li className="flex gap-4">
              <Mark />
              <span><strong className="text-ink">Piles driven to refusal</strong>, with embedment below the mudline sized for the soil we find.</span>
            </li>
            <li className="flex gap-4">
              <Mark />
              <span><strong className="text-ink">Deck height set above high water</strong>, so a wet spring never puts the boards under.</span>
            </li>
            <li className="flex gap-4">
              <Mark />
              <span><strong className="text-ink">Floats ride guide piles</strong> and a hinged gangway keeps the walk gentle at any level.</span>
            </li>
          </ul>
          <div className="mt-10 max-w-sm">
            <label htmlFor={`lvl-${id}`} className="caps text-ink-3">
              Try it — set the water level
            </label>
            <input
              ref={inputRef}
              id={`lvl-${id}`}
              type="range"
              min={-MAX_DOWN}
              max={MAX_UP}
              step={0.1}
              defaultValue={0}
              onInput={(e) => apply(Number((e.target as HTMLInputElement).value))}
              className="mt-3 h-11 w-full cursor-pointer accent-magenta"
            />
            <output ref={readoutRef} htmlFor={`lvl-${id}`} className="hydro block text-lg text-magenta" aria-live="polite" />
          </div>
        </div>

        <figure className="lg:col-span-8">
          <svg viewBox="0 84 1200 536" className="h-auto w-full" role="img" aria-label="Section drawing of a fixed piling dock and a floating dock, showing the float and gangway following the water level">
            <defs>
              <pattern id={`soil-${id}`} width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
                <rect width="12" height="12" fill="var(--color-land)" />
                <line x1="0" y1="0" x2="0" y2="12" stroke="var(--color-land-line)" strokeWidth="1" />
              </pattern>
            </defs>

            {/* water body and surface */}
            <polygon ref={waterRef} fill="var(--color-shoal)" opacity={0.95} />
            <line ref={surfaceRef} x1={0} x2={1200} stroke="var(--color-contour)" strokeWidth={1.5} />

            {/* full-pond reference */}
            <line x1={240} x2={1200} y1={FULL} y2={FULL} stroke="var(--color-ink)" strokeWidth={0.8} strokeDasharray="10 6" opacity={0.55} />
            <text x={1190} y={FULL + 24} textAnchor="end" fontSize={13} fill="var(--color-ink-2)" className="hydro">normal full pond</text>

            {/* fixed dock piles: hidden lines below the mudline */}
            {FIXED_PILES.map((x) => (
              <rect key={x} x={x - 6} y={DECK + 4} width={12} height={Math.max(0, bedY(x) - DECK - 4)} fill="#7a5a36" />
            ))}
            {/* fixed deck and framing */}
            <rect x={150} y={DECK - 8} width={HINGE.x - 150} height={10} fill="#9a6b3f" />
            <rect x={150} y={DECK + 2} width={HINGE.x - 150} height={10} fill="#5f4428" />

            {/* soil, drawn over pile bottoms so the hidden lines read as below grade */}
            <path d={bedPath} fill={`url(#soil-${id})`} opacity={0.92} />
            <path d={`M${BED.map(([x, y]) => `${x} ${y}`).join(' L')}`} fill="none" stroke="var(--color-land-line)" strokeWidth={2} />
            {FIXED_PILES.map((x) => (
              <rect key={x} x={x - 6} y={bedY(x)} width={12} height={EMBED} fill="none" stroke="var(--color-ink)" strokeWidth={1.1} strokeDasharray="4 3" />
            ))}

            {/* guide piles for the float */}
            {GUIDE_PILES.map((x) => (
              <g key={x}>
                <rect x={x - 7} y={196} width={14} height={bedY(x) - 196} fill="#7a5a36" />
                <rect x={x - 7} y={bedY(x)} width={14} height={EMBED} fill="none" stroke="var(--color-ink)" strokeWidth={1.1} strokeDasharray="4 3" />
              </g>
            ))}

            {/* the float rides the water */}
            <g ref={floatRef}>
              <rect x={FLOAT_X} y={FULL - 10} width={FLOAT_W} height={8} fill="#9a6b3f" />
              <rect x={FLOAT_X + 8} y={FULL - 2} width={FLOAT_W - 16} height={20} fill="#2d3e4a" />
              {GUIDE_PILES.map((x) => (
                <rect key={x} x={x - 11} y={FULL - 16} width={22} height={30} fill="none" stroke="var(--color-ink)" strokeWidth={2} rx={2} />
              ))}
            </g>

            {/* gangway */}
            <line ref={gangRef} x1={HINGE.x} y1={HINGE.y} stroke="var(--color-ink)" strokeWidth={6} strokeLinecap="round" />
            <circle cx={HINGE.x} cy={HINGE.y} r={5} fill="var(--color-paper)" stroke="var(--color-ink)" strokeWidth={2} />

            {/* live water-level mark */}
            <g ref={levelMarkRef}>
              <path d="M-9 -16 L9 -16 L0 -2 Z" fill="var(--color-magenta)" />
              <line x1={-14} x2={14} y1={4} y2={4} stroke="var(--color-magenta)" strokeWidth={1.2} />
              <line x1={-8} x2={8} y1={9} y2={9} stroke="var(--color-magenta)" strokeWidth={1.2} />
              <text ref={levelTextRef} x={-20} y={-6} textAnchor="end" fontSize={17} fill="var(--color-magenta)" className="hydro" />
            </g>

            {/* callouts */}
            <g fontSize={14} fill="var(--color-ink)" style={{ fontVariationSettings: "'wdth' 110" }}>
              <line x1={370} y1={bedY(370) + 70} x2={300} y2={560} stroke="var(--color-ink)" strokeWidth={0.8} />
              <text x={140} y={580}>Embedment below mudline</text>
              <line x1={300} y1={DECK - 8} x2={300} y2={160} stroke="var(--color-ink)" strokeWidth={0.8} />
              <text x={300} y={150} textAnchor="middle">Deck above high water</text>
              <line x1={860} y1={196} x2={860} y2={130} stroke="var(--color-ink)" strokeWidth={0.8} />
              <text x={860} y={120} textAnchor="middle">Float on guide piles</text>
              <text ref={angleTextRef} x={600} y={200} className="hydro" fontSize={17} fill="var(--color-magenta)" />
            </g>

            <text x={24} y={110} fontSize={15} fontWeight={650} fill="var(--color-ink)" style={{ fontVariationSettings: "'wdth' 125", letterSpacing: '0.16em' }}>
              SECTION A–A
            </text>
            <text x={24} y={132} fontSize={14} fill="var(--color-ink-2)" className="hydro">
              typical fixed dock with floating extension · not to scale
            </text>
          </svg>
        </figure>
      </div>
    </section>
  )
}

function Mark() {
  return (
    <svg viewBox="0 0 16 16" className="mt-1.5 size-4 shrink-0 text-magenta" aria-hidden="true">
      <circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" strokeWidth="1.4" />
      <circle cx="8" cy="8" r="2.2" fill="currentColor" />
    </svg>
  )
}
