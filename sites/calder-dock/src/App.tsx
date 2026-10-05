import { useEffect, useState, type FormEvent } from 'react'
import { ArrowRight, BrickWall, Hammer, Mail, Menu, Phone, Plus, Ship, Warehouse, Waves, X, Fence } from 'lucide-react'
import { Hero } from '@/components/Hero'
import { Work } from '@/components/Work'
import { SectionAA } from '@/components/SectionAA'
import { Marquee } from '@/components/magicui/marquee'
import { BlurFade } from '@/components/magicui/blur-fade'
import { business, decking, faqs, photos, process, services, towns } from '@/data'
import { cn } from '@/lib/utils'

const NAV = [
  { href: '#work', label: 'Work' },
  { href: '#services', label: 'Services' },
  { href: '#engineering', label: 'Engineering' },
  { href: '#process', label: 'Process' },
  { href: '#commercial', label: 'Commercial' },
  { href: '#faq', label: 'FAQ' },
]

const SERVICE_ICONS = { fixed: Fence, float: Waves, house: Warehouse, lift: Ship, wall: BrickWall, repair: Hammer }

export default function App() {
  return (
    <>
      <a href="#main" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60] focus:bg-paper focus:p-3">
        Skip to content
      </a>
      <Nav />
      <main id="main">
        <Hero />
        <Towns />
        <Work />
        <Services />
        <SectionAA />
        <Craft />
        <Process />
        <Commercial />
        <Faq />
        <Visit />
      </main>
      <Footer />
    </>
  )
}

function Wordmark({ invert = false }: { invert?: boolean }) {
  return (
    <a href="#top" className="flex items-baseline gap-2 leading-none" aria-label={`${business.name}, home`}>
      <span
        className={cn('text-[1.35rem] font-[780] tracking-[0.06em]', invert ? 'text-night-ink' : 'text-ink')}
        style={{ fontVariationSettings: "'wdth' 125" }}
      >
        CALDER
      </span>
      <span className={cn('hydro text-[1.05rem]', invert ? 'text-night-dim' : 'text-contour')}>Dock &amp; Marine</span>
    </a>
  )
}

function Nav() {
  const [open, setOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])
  return (
    <header
      className={cn(
        'sticky top-0 z-50 border-b bg-paper/95 backdrop-blur-sm transition-[border-color,box-shadow] duration-300',
        scrolled ? 'border-ink/20 shadow-[0_8px_24px_-18px_rgb(13_28_38/0.5)]' : 'border-transparent',
      )}
    >
      <div className="mx-auto flex h-[4.5rem] max-w-[1600px] items-center justify-between gap-6 px-5 sm:px-8 lg:px-12">
        <Wordmark />
        <nav aria-label="Primary" className="hidden lg:block">
          <ul className="flex items-center gap-7 text-[0.95rem] font-medium text-ink-2">
            {NAV.map((n) => (
              <li key={n.href}>
                <a href={n.href} className="py-2 transition-colors duration-200 hover:text-magenta">
                  {n.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <div className="flex items-center gap-3">
          <a href={business.phoneHref} className="hidden items-center gap-2 text-sm font-semibold tnum xl:flex">
            <Phone aria-hidden="true" className="size-4 text-magenta" />
            {business.phone}
          </a>
          <a href="#visit" className="btn-primary hidden !min-h-11 !py-2.5 text-sm sm:inline-flex">
            Request a site visit
          </a>
          <button
            type="button"
            className="flex size-11 cursor-pointer items-center justify-center lg:hidden"
            aria-expanded={open}
            aria-controls="mobile-nav"
            aria-label={open ? 'Close menu' : 'Open menu'}
            onClick={() => setOpen((o) => !o)}
          >
            {open ? <X className="size-6" /> : <Menu className="size-6" />}
          </button>
        </div>
      </div>
      {open && (
        <nav id="mobile-nav" aria-label="Mobile" className="border-t border-ink/15 bg-paper px-5 pb-6 pt-2 lg:hidden">
          <ul className="divide-y divide-ink/10">
            {NAV.map((n) => (
              <li key={n.href}>
                <a href={n.href} onClick={() => setOpen(false)} className="display-md block py-4 text-2xl">
                  {n.label}
                </a>
              </li>
            ))}
          </ul>
          <a href="#visit" onClick={() => setOpen(false)} className="btn-primary mt-4 w-full justify-center">
            Request a site visit
          </a>
        </nav>
      )}
    </header>
  )
}

function Towns() {
  return (
    <section aria-label="Service area" className="border-b border-ink/15 bg-shoal py-5">
      <Marquee className="[--duration:48s] [--gap:3rem]" repeat={3}>
        {towns.map((t) => (
          <span key={t} className="flex items-center gap-12 whitespace-nowrap">
            <span className="hydro text-2xl text-ink sm:text-3xl">{t}</span>
            <svg viewBox="0 0 20 20" className="size-4 text-magenta" aria-hidden="true">
              <circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" strokeWidth="1.5" />
              <circle cx="10" cy="10" r="2.5" fill="currentColor" />
            </svg>
          </span>
        ))}
      </Marquee>
    </section>
  )
}

function Services() {
  return (
    <section id="services" className="scroll-mt-20 border-b border-ink/15 py-20 sm:py-28">
      <div className="mx-auto grid max-w-[1600px] gap-14 px-5 sm:px-8 lg:grid-cols-12 lg:px-12">
        <div className="lg:col-span-7">
          <h2 className="display text-[clamp(2.3rem,4.6vw,4.2rem)]">What we build on the water.</h2>
          <p className="mt-6 max-w-[54ch] text-lg text-ink-2">
            One crew from first sounding to last board: no handing your shoreline to a subcontractor you never met.
          </p>
          <table className="mt-12 w-full border-collapse text-left">
            <caption className="caps pb-3 text-left text-ink-3">Legend</caption>
            <tbody>
              {services.map((s) => {
                const Icon = SERVICE_ICONS[s.key]
                return (
                  <tr key={s.key} className="group border-t border-ink/20 last:border-b">
                    <td className="w-14 py-6 align-top">
                      <span className="flex size-10 items-center justify-center rounded-full border border-ink/25 text-contour transition-colors duration-200 group-hover:border-magenta group-hover:text-magenta">
                        <Icon aria-hidden="true" className="size-5" strokeWidth={1.5} />
                      </span>
                    </td>
                    <td className="py-6 align-top">
                      <div className="grid gap-2 sm:grid-cols-[38%_1fr] sm:gap-6">
                        <h3 className="display-md text-xl font-[680] sm:text-2xl">{s.name}</h3>
                        <p className="text-ink-2">{s.line}</p>
                      </div>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
        <div className="grid grid-cols-2 gap-5 self-start lg:col-span-5 lg:mt-24">
          <figure className="col-span-2">
            <img src={photos.boathouse} alt="Two-story boathouse with rooftop sundeck and a pontoon boat on its lift" loading="lazy" className="aspect-[3/2] w-full object-cover" />
            <figcaption className="hydro mt-2 text-sm text-ink-3">Boathouse with roof deck</figcaption>
          </figure>
          <figure>
            <img src={photos.floating} alt="Floating dock with composite decking and kayaks at golden hour" loading="lazy" className="aspect-[4/5] w-full object-cover" />
            <figcaption className="hydro mt-2 text-sm text-ink-3">Floating dock</figcaption>
          </figure>
          <figure>
            <img src={photos.seawall} alt="Stone riprap and seawall along a lakefront lawn" loading="lazy" className="aspect-[4/5] w-full object-cover" />
            <figcaption className="hydro mt-2 text-sm text-ink-3">Seawall &amp; riprap</figcaption>
          </figure>
        </div>
      </div>
    </section>
  )
}

function Craft() {
  return (
    <section className="border-b border-ink/15 py-20 sm:py-28">
      <div className="mx-auto grid max-w-[1600px] gap-12 px-5 sm:px-8 lg:grid-cols-12 lg:px-12">
        <div className="lg:col-span-5">
          <div className="neat">
            <img src={photos.hardware} alt="Galvanized through-bolts joining a timber piling to a doubled beam beneath hardwood decking" loading="lazy" className="aspect-[4/5] w-full object-cover" />
          </div>
          <p className="hydro mt-5 text-sm text-ink-3">Detail B · through-bolted pile-to-beam connection, hot-dip galvanized</p>
        </div>
        <div className="flex flex-col lg:col-span-7 lg:pl-8">
          <h2 className="display text-[clamp(2.3rem,4.6vw,4.2rem)]">The details you’ll stand on for decades.</h2>
          <p className="mt-6 max-w-[56ch] text-lg text-ink-2">
            Most docks fail at their connections and their decking, not their piles. We through-bolt instead of nailing, use hot-dip galvanized or
            stainless hardware throughout, and help you pick a deck surface for how you actually use the water.
          </p>
          <div className="mt-10 overflow-x-auto">
            <table className="w-full min-w-[520px] border-collapse text-left text-[0.95rem]">
              <caption className="caps pb-3 text-left text-ink-3">Decking we install</caption>
              <thead>
                <tr className="border-y border-ink text-ink-3">
                  <th scope="col" className="caps py-3 pr-4 font-semibold">Surface</th>
                  <th scope="col" className="caps py-3 pr-4 font-semibold">Underfoot</th>
                  <th scope="col" className="caps py-3 pr-4 font-semibold">Upkeep</th>
                  <th scope="col" className="caps py-3 font-semibold">Service life</th>
                </tr>
              </thead>
              <tbody>
                {decking.map((d) => (
                  <tr key={d.name} className="border-b border-ink/20">
                    <th scope="row" className="py-4 pr-4 font-semibold">{d.name}</th>
                    <td className="py-4 pr-4 text-ink-2">{d.feel}</td>
                    <td className="py-4 pr-4 text-ink-2">{d.upkeep}</td>
                    <td className="py-4">
                      <LifeBar level={d.life} />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="mt-12 grid items-end gap-6 sm:grid-cols-[0.8fr_1fr]">
            <img src={photos.hands} alt="Gloved hands measuring a fresh-cut hardwood deck board" loading="lazy" className="aspect-[4/5] w-full object-cover" />
            <blockquote className="border-t border-ink pt-5">
              <p className="display-md text-2xl leading-snug">“Measure from the water, not from the house.”</p>
              <footer className="hydro mt-3 text-ink-3">How every Calder plan starts</footer>
            </blockquote>
          </div>
        </div>
      </div>
    </section>
  )
}

function LifeBar({ level }: { level: string }) {
  const n = level === 'Longest' ? 3 : level === 'Long' ? 2 : 1
  return (
    <span className="flex items-center gap-2">
      <span className="flex gap-1" aria-hidden="true">
        {[1, 2, 3].map((i) => (
          <span key={i} className={cn('h-2 w-5', i <= n ? 'bg-contour' : 'bg-ink/12')} />
        ))}
      </span>
      <span className="text-ink-2">{level}</span>
    </span>
  )
}

function Process() {
  return (
    <section id="process" className="scroll-mt-20 border-b border-ink/15 bg-paper-2 py-20 sm:py-28">
      <div className="mx-auto grid max-w-[1600px] gap-14 px-5 sm:px-8 lg:grid-cols-12 lg:px-12">
        <div className="lg:col-span-5">
          <div className="lg:sticky lg:top-28">
            <h2 className="display text-[clamp(2.3rem,4.6vw,4.2rem)]">Course to a finished dock.</h2>
            <p className="mt-6 max-w-[44ch] text-lg text-ink-2">Five legs, one project lead, and no surprises on the invoice.</p>
            <img src={photos.piledriver} alt="Barge-mounted pile driver setting a timber piling while two crew members guide it" loading="lazy" className="mt-10 hidden aspect-[4/5] w-full max-w-md object-cover lg:block" />
          </div>
        </div>
        <ol className="relative lg:col-span-7">
          <span aria-hidden="true" className="absolute bottom-6 left-[19px] top-6 border-l-2 border-dashed border-magenta/50" />
          {process.map((p, i) => (
            <li key={p.leg} className="relative pb-12 pl-16 last:pb-0">
              <span className="absolute left-0 top-0 flex size-10 items-center justify-center rounded-full border-2 border-magenta bg-paper-2 text-sm font-bold text-magenta tnum">
                {i + 1}
              </span>
              <BlurFade inView direction="up" offset={12} delay={0.05}>
                <h3 className="display-md pt-1.5 text-2xl sm:text-3xl">{p.leg}</h3>
                <p className="mt-3 max-w-[58ch] text-lg text-ink-2">{p.body}</p>
              </BlurFade>
            </li>
          ))}
        </ol>
      </div>
    </section>
  )
}

function Commercial() {
  return (
    <section
      id="commercial"
      className="scroll-mt-20 bg-night py-20 text-night-ink sm:py-28"
      style={{
        backgroundImage:
          'linear-gradient(to right, rgb(42 104 128 / 0.18) 1px, transparent 1px), linear-gradient(to bottom, rgb(42 104 128 / 0.18) 1px, transparent 1px)',
        backgroundSize: '120px 120px',
      }}
    >
      <div className="mx-auto grid max-w-[1600px] gap-12 px-5 sm:px-8 lg:grid-cols-12 lg:items-center lg:px-12">
        <figure className="lg:col-span-7">
          <img src={photos.marina} alt="Community marina with covered slips and a wide wooden walkway in morning light" loading="lazy" className="aspect-[3/2] w-full object-cover outline outline-1 outline-offset-[6px] outline-night-line" />
        </figure>
        <div className="lg:col-span-5 lg:pl-6">
          <h2 className="display text-[clamp(2.2rem,4vw,3.6rem)] text-white">Marinas, HOAs and waterfront businesses.</h2>
          <p className="mt-6 max-w-[48ch] text-lg text-night-dim">
            Bigger docks, more stakeholders, the same standard. We phase work around your members and customers, and give you one project lead
            from proposal to punch list.
          </p>
          <ul className="mt-8 divide-y divide-night-line/60 border-y border-night-line/60">
            {['Community docks & covered slip rows', 'Restaurant and public tie-up docks', 'Phased replacement & repairs', 'Permitting and board presentations'].map((t) => (
              <li key={t} className="flex items-center gap-4 py-4">
                <svg viewBox="0 0 16 16" className="size-3.5 shrink-0 text-[#e06bb3]" aria-hidden="true">
                  <circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" strokeWidth="1.5" />
                  <circle cx="8" cy="8" r="2.2" fill="currentColor" />
                </svg>
                {t}
              </li>
            ))}
          </ul>
          <a href="#visit" className="mt-10 inline-flex min-h-12 items-center gap-2 border-b border-current py-2 font-semibold text-white transition-colors duration-200 hover:text-[#f2a6d4]">
            Talk to us about a commercial project
            <ArrowRight aria-hidden="true" className="size-4" />
          </a>
        </div>
      </div>
    </section>
  )
}

function Faq() {
  return (
    <section id="faq" className="scroll-mt-20 border-b border-ink/15 py-20 sm:py-28">
      <div className="mx-auto grid max-w-[1600px] gap-12 px-5 sm:px-8 lg:grid-cols-12 lg:px-12">
        <h2 className="display text-[clamp(2.3rem,4.6vw,4.2rem)] lg:col-span-5">Questions we hear on every shoreline.</h2>
        <div className="lg:col-span-7">
          {faqs.map((f) => (
            <details key={f.q} className="group border-t border-ink/25 last:border-b">
              <summary className="flex min-h-16 cursor-pointer list-none items-center justify-between gap-6 py-5 [&::-webkit-details-marker]:hidden">
                <span className="display-md text-xl font-[650] sm:text-2xl">{f.q}</span>
                <Plus aria-hidden="true" className="size-5 shrink-0 text-magenta transition-transform duration-300 group-open:rotate-45" />
              </summary>
              <p className="max-w-[62ch] pb-7 text-lg text-ink-2">{f.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  )
}

type FormState = 'idle' | 'sending' | 'sent' | 'error'

function Visit() {
  const [status, setStatus] = useState<FormState>('idle')
  const [name, setName] = useState('')

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const form = e.currentTarget
    if (!form.checkValidity()) {
      form.reportValidity()
      return
    }
    setStatus('sending')
    const data = new FormData(form)
    setName(String(data.get('name') ?? '').split(' ')[0])
    // Connect a form service (e.g. Formspree or Netlify Forms) by setting VITE_FORM_ENDPOINT.
    const endpoint = import.meta.env.VITE_FORM_ENDPOINT as string | undefined
    try {
      if (endpoint) {
        const res = await fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        if (!res.ok) throw new Error('send failed')
      } else {
        await new Promise((r) => setTimeout(r, 700))
      }
      setStatus('sent')
    } catch {
      setStatus('error')
    }
  }

  const field = 'mt-2 block w-full rounded-[2px] border border-ink/30 bg-paper px-4 py-3 text-base text-ink placeholder:text-ink-3 transition-colors duration-200 hover:border-ink/60 focus:border-magenta focus:outline-none focus:ring-2 focus:ring-magenta/25'
  const label = 'block text-sm font-semibold text-ink'

  return (
    <section id="visit" className="scroll-mt-20 bg-shoal py-20 sm:py-28">
      <div className="mx-auto grid max-w-[1600px] gap-12 px-5 sm:px-8 lg:grid-cols-12 lg:px-12">
        <div className="lg:col-span-5">
          <h2 className="display text-[clamp(2.5rem,5vw,4.6rem)]">Request a site visit.</h2>
          <p className="mt-6 max-w-[44ch] text-lg text-ink-2">
            We’ll come out, sound the water at your shoreline and walk the bank with you. You get a drawn plan and a fixed-price proposal. The visit
            is free and there’s no obligation.
          </p>
          <ul className="mt-10 space-y-4 text-lg">
            <li>
              <a href={business.phoneHref} className="flex items-center gap-3 font-semibold tnum hover:text-magenta">
                <Phone aria-hidden="true" className="size-5 text-magenta" />
                {business.phone}
              </a>
            </li>
            <li>
              <a href={`mailto:${business.email}`} className="flex items-center gap-3 font-semibold hover:text-magenta">
                <Mail aria-hidden="true" className="size-5 text-magenta" />
                {business.email}
              </a>
            </li>
            <li className="hydro text-ink-2">{business.hours}</li>
          </ul>
          <img src={photos.evening} alt="Dock at twilight with string lights leading back to a lit lake house" loading="lazy" className="mt-12 hidden aspect-[4/5] w-full max-w-sm object-cover lg:block" />
        </div>

        <div className="lg:col-span-7">
          <div className="bg-paper p-6 shadow-[0_24px_60px_-30px_rgb(13_28_38/0.45)] sm:p-10">
            {status === 'sent' ? (
              <div role="status" className="flex min-h-[420px] flex-col justify-center">
                <svg viewBox="0 0 48 48" className="size-12 text-magenta" aria-hidden="true">
                  <circle cx="24" cy="24" r="21" fill="none" stroke="currentColor" strokeWidth="2" />
                  <circle cx="24" cy="24" r="6" fill="currentColor" />
                </svg>
                <h3 className="display-md mt-6 text-3xl">Thanks{name ? `, ${name}` : ''} — you’re on the chart.</h3>
                <p className="mt-4 max-w-[46ch] text-lg text-ink-2">
                  We’ll call within one business day to set a time for your site visit. If it’s urgent, call {business.phone}.
                </p>
              </div>
            ) : (
              <form onSubmit={onSubmit} noValidate className="grid gap-6 sm:grid-cols-2">
                <div>
                  <label htmlFor="f-name" className={label}>Your name</label>
                  <input id="f-name" name="name" required autoComplete="name" className={field} />
                </div>
                <div>
                  <label htmlFor="f-phone" className={label}>Phone</label>
                  <input id="f-phone" name="phone" type="tel" required autoComplete="tel" className={field} />
                </div>
                <div className="sm:col-span-2">
                  <label htmlFor="f-email" className={label}>Email</label>
                  <input id="f-email" name="email" type="email" required autoComplete="email" className={field} />
                </div>
                <div className="sm:col-span-2">
                  <label htmlFor="f-address" className={label}>Property address</label>
                  <input id="f-address" name="address" autoComplete="street-address" placeholder="Street, town" className={field} />
                </div>
                <div>
                  <label htmlFor="f-type" className={label}>Project</label>
                  <select id="f-type" name="project" className={cn(field, 'cursor-pointer')} defaultValue="">
                    <option value="" disabled>Choose one</option>
                    <option>New dock</option>
                    <option>Boathouse</option>
                    <option>Boat or PWC lift</option>
                    <option>Repair or re-deck</option>
                    <option>Seawall / shoreline</option>
                    <option>Commercial / HOA</option>
                  </select>
                </div>
                <div>
                  <label htmlFor="f-when" className={label}>When would you like it done?</label>
                  <select id="f-when" name="timeline" className={cn(field, 'cursor-pointer')} defaultValue="">
                    <option value="" disabled>Choose one</option>
                    <option>As soon as possible</option>
                    <option>Within 6 months</option>
                    <option>This time next year</option>
                    <option>Just exploring</option>
                  </select>
                </div>
                <div className="sm:col-span-2">
                  <label htmlFor="f-msg" className={label}>
                    Tell us about your shoreline <span className="font-normal text-ink-3">(optional)</span>
                  </label>
                  <textarea id="f-msg" name="message" rows={4} placeholder="Water depth if you know it, the boat you have, what isn’t working today…" className={field} />
                </div>
                <div className="flex flex-wrap items-center gap-5 sm:col-span-2">
                  <button type="submit" disabled={status === 'sending'} className="btn-primary cursor-pointer disabled:cursor-wait disabled:opacity-70">
                    {status === 'sending' ? 'Sending…' : 'Request my site visit'}
                    <ArrowRight aria-hidden="true" className="size-4" />
                  </button>
                  <p className="text-sm text-ink-3">We reply within one business day.</p>
                </div>
                {status === 'error' && (
                  <p role="alert" className="text-sm font-semibold text-magenta sm:col-span-2">
                    That didn’t send. Please try again, or call us at {business.phone}.
                  </p>
                )}
              </form>
            )}
          </div>
        </div>
      </div>
    </section>
  )
}

function Footer() {
  return (
    <footer className="bg-night text-night-dim">
      <div className="mx-auto max-w-[1600px] px-5 py-14 sm:px-8 lg:px-12">
        <div className="grid gap-10 border border-night-line p-6 sm:p-8 lg:grid-cols-12">
          <div className="lg:col-span-5">
            <Wordmark invert />
            <p className="hydro mt-4 text-lg">{business.region}</p>
            <p className="mt-6 max-w-[40ch] text-sm">
              Docks, boathouses, lifts and shoreline, designed and built by one crew. {business.license}.
            </p>
          </div>
          <div className="text-sm lg:col-span-3">
            <p className="caps text-night-ink">Chart</p>
            <ul className="mt-3 space-y-2">
              {NAV.map((n) => (
                <li key={n.href}>
                  <a href={n.href} className="hover:text-white">{n.label}</a>
                </li>
              ))}
            </ul>
          </div>
          <div className="text-sm lg:col-span-4">
            <p className="caps text-night-ink">Contact</p>
            <ul className="mt-3 space-y-2">
              <li><a href={business.phoneHref} className="tnum hover:text-white">{business.phone}</a></li>
              <li><a href={`mailto:${business.email}`} className="hover:text-white">{business.email}</a></li>
              <li>{business.hours}</li>
            </ul>
            <a href="#visit" className="mt-6 inline-flex items-center gap-2 font-semibold text-white hover:text-[#f2a6d4]">
              Request a site visit <ArrowRight aria-hidden="true" className="size-4" />
            </a>
          </div>
        </div>
        <div className="mt-6 flex flex-wrap items-center justify-between gap-4 text-xs">
          <span className="tnum">{business.position} · Soundings in feet</span>
          <span>© {new Date().getFullYear()} {business.name}</span>
        </div>
      </div>
    </footer>
  )
}
