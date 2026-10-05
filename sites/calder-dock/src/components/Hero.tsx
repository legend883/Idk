import { ArrowRight, Phone } from 'lucide-react'
import { CompassRose, NauticalChart } from '@/components/NauticalChart'
import { DockPlan } from '@/components/DockPlan'
import { TextAnimate } from '@/components/magicui/text-animate'
import { BlurFade } from '@/components/magicui/blur-fade'
import { nearestWater, type FieldShape } from '@/lib/chart'
import { business, photos } from '@/data'

const W = 1000
const H = 820

// Wooded shore along the top and left; the cove opens to deep water bottom-right.
const coveShape: FieldShape = (x, y, n) => {
  const g = (0.5 - x) * 1.25 + (0.4 - y) * 1.05 + Math.sin(x * 9 + 1.3) * 0.06
  const h = g + n(x * 2.1 + 3, y * 2.1) * 1.05
  return h > 0 ? h * 40 : h * 85
}

export function Hero() {
  return (
    <section id="top" className="relative border-b border-ink/15">
      <div className="mx-auto grid max-w-[1600px] lg:min-h-[calc(100svh-4.5rem)] lg:grid-cols-12">
        <div className="relative z-10 flex flex-col justify-between gap-12 px-5 pb-12 pt-10 sm:px-8 lg:col-span-5 lg:py-14 lg:pl-12 lg:pr-10">
          <div>
            <TextAnimate
              as="h1"
              by="word"
              animation="blurInUp"
              duration={0.9}
              once
              className="display text-[clamp(2.6rem,4.9vw,4.6rem)] text-ink"
            >
              Docks engineered from the lakebed up.
            </TextAnimate>
            <BlurFade delay={0.7} direction="up" offset={10}>
              <p className="mt-7 max-w-[34ch] text-lg leading-relaxed text-ink-2 sm:text-xl">
                We sound the water, draw the plan and drive every pile ourselves — fixed docks, floating docks, boathouses and lifts built to
                stay level and solid through every season on the lake.
              </p>
            </BlurFade>
          </div>

          <BlurFade delay={0.95} direction="up" offset={10}>
            <div className="flex flex-wrap items-center gap-x-8 gap-y-3">
              <a href="#visit" className="btn-primary">
                Request a site visit
                <ArrowRight aria-hidden="true" className="size-4" />
              </a>
              <a href={business.phoneHref} className="btn-ghost tnum">
                <Phone aria-hidden="true" className="size-4" />
                {business.phone}
              </a>
            </div>
            <dl className="mt-10 grid max-w-md grid-cols-3 gap-6 border-t border-ink/20 pt-5 text-sm">
              <div>
                <dt className="caps text-ink-3">We build</dt>
                <dd className="mt-1 font-semibold">Residential</dd>
              </div>
              <div>
                <dt className="caps text-ink-3">And</dt>
                <dd className="mt-1 font-semibold">Marinas & HOAs</dd>
              </div>
              <div>
                <dt className="caps text-ink-3">Waters</dt>
                <dd className="mt-1 font-semibold">{business.water}</dd>
              </div>
            </dl>
          </BlurFade>
        </div>

        <div className="relative h-[78svh] min-h-[520px] lg:col-span-7 lg:h-auto">
          <NauticalChart
            shape={coveShape}
            seed={7}
            width={W}
            height={H}
            cols={220}
            soundingSpacing={58}
            revealFrom={{ x: 690, y: 400 }}
            label={`Chart of a ${business.water} cove with a proposed dock plotted at fourteen feet of water`}
          >
            {(field) => {
              const pin = nearestWater(field, 690, 400, 12, 18)
              return (
                <>
                  <DockPlan field={field} x={pin.x} y={pin.y} />
                  <g transform={`translate(${pin.x} ${pin.y})`}>
                    <circle r={16} fill="none" stroke="var(--color-magenta)" strokeWidth={1.4} />
                    <circle r={3.5} fill="var(--color-magenta)" />
                    <path d="M-16 -6 L-110 -80 L-330 -80" fill="none" stroke="var(--color-magenta)" strokeWidth={1} />
                    <text x={-118} y={-90} textAnchor="end" fill="var(--color-magenta)" fontSize={15} fontWeight={650} style={{ fontVariationSettings: "'wdth' 120", letterSpacing: '0.1em' }}>
                      PROPOSED DOCK
                    </text>
                    <text x={-118} y={-58} textAnchor="end" className="hydro" fill="var(--color-magenta)" fontSize={17}>
                      {pin.depth} ft at the T-head · 28 piles
                    </text>
                  </g>
                  <text
                    x={830}
                    y={640}
                    className="hydro"
                    fill="var(--color-contour)"
                    fontSize={30}
                    letterSpacing="0.3em"
                    textAnchor="middle"
                    transform="rotate(-12 830 640)"
                  >
                    {business.water.toUpperCase()}
                  </text>
                  <CompassRose x={780} y={150} r={64} />
                </>
              )
            }}
          </NauticalChart>

          <figure className="absolute bottom-5 left-5 w-[min(54%,500px)] bg-paper p-2 shadow-[0_18px_40px_-20px_rgb(13_28_38/0.55)] sm:bottom-8 sm:left-8">
            <img
              src={photos.hero}
              alt="Covered two-slip boathouse with hardwood deck and timber pilings on a misty lake at sunrise"
              className="aspect-[16/10] w-full object-cover"
              width={1344}
              height={760}
              fetchPriority="high"
            />
            <figcaption className="flex items-baseline justify-between gap-4 px-1 pt-2 text-xs text-ink-2">
              <span className="caps">Inset · Heron Point</span>
              <span className="hydro hidden text-sm sm:inline">covered two-slip boathouse</span>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>
  )
}
