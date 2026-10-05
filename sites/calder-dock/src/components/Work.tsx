import { useMemo, useState } from 'react'
import { AnimatePresence, motion } from 'motion/react'
import { NauticalChart } from '@/components/NauticalChart'
import { DockPlan } from '@/components/DockPlan'
import { NumberTicker } from '@/components/magicui/number-ticker'
import { Ripple } from '@/components/magicui/ripple'
import { buildField, nearestWater, type FieldShape } from '@/lib/chart'
import { cn } from '@/lib/utils'
import { business, projects } from '@/data'

const W = 1200
const H = 760
const SEED = 23
const COLS = 220

// A winding reach of lake with coves on both banks.
const reachShape: FieldShape = (x, y, n) => {
  const center = 0.52 + Math.sin(x * 5.2 + 0.6) * 0.1
  const g = Math.abs(y - center) - 0.25
  const h = g * 2.6 + n(x * 2.6 + 11, y * 2.6) * 1.15
  return h > 0 ? h * 35 : h * 70
}

export function Work() {
  const [active, setActive] = useState(projects[0].id)
  const field = useMemo(() => buildField(reachShape, { seed: SEED, width: W, height: H, cols: COLS }), [])
  const pins = useMemo(
    () =>
      projects.map((p) => {
        const spot = nearestWater(field, p.at[0] * W, p.at[1] * H, 5, 14)
        return { ...p, x: spot.x, y: spot.y, depth: spot.depth }
      }),
    [field],
  )
  const current = pins.find((p) => p.id === active) ?? pins[0]

  return (
    <section id="work" className="scroll-mt-20 border-b border-ink/15 bg-paper py-20 sm:py-28">
      <div className="mx-auto max-w-[1600px] px-5 sm:px-8 lg:px-12">
        <div className="grid gap-6 lg:grid-cols-12 lg:items-end">
          <h2 className="display text-[clamp(2.3rem,4.6vw,4.2rem)] lg:col-span-7">Every job, plotted where it stands.</h2>
          <p className="max-w-[52ch] text-lg text-ink-2 lg:col-span-5">
            Each dock starts as a sounding on the chart: the depth at the end of the pier decides whether we drive piles or float it, how tall the
            deck sits and how the lift is carried. Select a pin to see what we built there.
          </p>
        </div>

        <div className="mt-12 grid gap-8 lg:grid-cols-12">
          <div className="lg:col-span-8">
            <div className="relative aspect-[1200/760] w-full">
              <NauticalChart
                shape={reachShape}
                seed={SEED}
                width={W}
                height={H}
                cols={COLS}
                soundingSpacing={60}
                label={`Chart of a reach of ${business.water} with ${projects.length} project locations`}
              >
                {(f) => (
                  <>
                    {pins.map((p) => (
                      <DockPlan key={p.id} field={f} x={p.x} y={p.y} head={p.id === 'pine' ? 90 : 40} />
                    ))}
                    <g transform="translate(40 700)" aria-hidden="true">
                      <rect width={60} height={6} fill="var(--color-ink)" />
                      <rect x={60} width={60} height={6} fill="none" stroke="var(--color-ink)" />
                      <rect x={120} width={60} height={6} fill="var(--color-ink)" />
                      <text y={24} fontSize={13} fill="var(--color-ink-2)">0</text>
                      <text x={180} y={24} fontSize={13} fill="var(--color-ink-2)" textAnchor="middle">
                        500 ft
                      </text>
                    </g>
                  </>
                )}
              </NauticalChart>

              {pins.map((p, i) => {
                const on = p.id === active
                return (
                  <button
                    key={p.id}
                    type="button"
                    onClick={() => setActive(p.id)}
                    aria-pressed={on}
                    aria-label={`${p.name}: ${p.type}`}
                    className="group absolute flex size-11 -translate-x-1/2 -translate-y-1/2 cursor-pointer items-center justify-center"
                    style={{ left: `${(p.x / W) * 100}%`, top: `${(p.y / H) * 100}%` }}
                  >
                    {on && <Ripple mainCircleSize={34} mainCircleOpacity={0.3} numCircles={4} className="mask-none scale-[0.42]" />}
                    <span
                      className={cn(
                        'relative flex size-7 items-center justify-center rounded-full border-2 text-[0.7rem] font-bold tnum transition-all duration-200',
                        on
                          ? 'scale-110 border-magenta bg-magenta text-white'
                          : 'border-magenta bg-paper text-magenta group-hover:bg-magenta-tint',
                      )}
                    >
                      {String.fromCharCode(65 + i)}
                    </span>
                  </button>
                )
              })}
            </div>
            <p className="mt-4 max-w-[70ch] text-sm text-ink-3">
              <span className="caps text-magenta">Note A</span> Soundings in feet below normal full pond. Plotted jobs and photographs are illustrative.
            </p>
          </div>

          <div className="lg:col-span-4">
            <div role="tablist" aria-label="Projects" className="mb-6 flex flex-wrap gap-2">
              {pins.map((p, i) => (
                <button
                  key={p.id}
                  role="tab"
                  type="button"
                  aria-selected={p.id === active}
                  onClick={() => setActive(p.id)}
                  className={cn(
                    'min-h-11 cursor-pointer rounded-[2px] border px-3 text-sm transition-colors duration-200',
                    p.id === active ? 'border-ink bg-ink text-paper' : 'border-ink/25 text-ink-2 hover:border-ink',
                  )}
                >
                  <span className="mr-1.5 font-bold text-magenta tnum">{String.fromCharCode(65 + i)}</span>
                  {p.name}
                </button>
              ))}
            </div>

            <AnimatePresence mode="wait">
              <motion.article
                key={current.id}
                role="tabpanel"
                initial={{ opacity: 0, y: 12, filter: 'blur(6px)' }}
                animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
                exit={{ opacity: 0, y: -8, filter: 'blur(4px)' }}
                transition={{ duration: 0.45, ease: [0.16, 1, 0.3, 1] }}
              >
                <div className="neat bg-paper-2">
                  <img src={current.photo} alt={current.alt} loading="lazy" className="aspect-[4/3] w-full object-cover" />
                </div>
                <h3 className="display-md mt-7 text-3xl">{current.name}</h3>
                <p className="hydro mt-1 text-lg text-contour">{current.water}</p>
                <p className="mt-3 font-semibold">{current.type}</p>
                <p className="mt-2 text-ink-2">{current.note}</p>
                <dl className="mt-6 grid grid-cols-3 border-y border-ink/20 py-4">
                  <div>
                    <dt className="caps text-ink-3">Depth</dt>
                    <dd className="display-md mt-1 text-2xl tnum">
                      <NumberTicker value={current.depth} className="text-ink" /> ft
                    </dd>
                  </div>
                  <div>
                    <dt className="caps text-ink-3">Piles</dt>
                    <dd className="display-md mt-1 text-2xl tnum">
                      {current.piles ? <NumberTicker value={current.piles} className="text-ink" /> : '—'}
                    </dd>
                  </div>
                  <div>
                    <dt className="caps text-ink-3">Length</dt>
                    <dd className="display-md mt-1 text-2xl tnum">
                      <NumberTicker value={current.span} className="text-ink" /> ft
                    </dd>
                  </div>
                </dl>
                <p className="mt-3 text-sm text-ink-3">Decking: {current.decking}</p>
              </motion.article>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  )
}
