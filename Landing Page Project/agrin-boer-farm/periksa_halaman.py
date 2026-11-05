#!/usr/bin/env python3
"""Memotret dan memeriksa satu halaman di 360/768/1440 px. Keluar 1 bila ada FAIL."""
import argparse, json, pathlib, sys

JS = r"""(w) => {
const out = {fail: [], warn: []};
const add = (lvl, id, msg) => out[lvl].push({id, msg});
const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el);
  return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05; };
const rgb = c => { const m = (c || '').match(/[\d.]+/g); return m ? m.map(Number) : null; };
const lum = ([r, g, b]) => { const f = v => (v /= 255) <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
const hsl = ([r, g, b]) => { r /= 255; g /= 255; b /= 255; const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2;
  if (mx === mn) return {h: 0, s: 0, l}; const d = mx - mn, s = l > .5 ? d / (2 - mx - mn) : d / (mx + mn);
  let h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; return {h: h * 60, s, l}; };
const txt = el => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 50);
const all = [...document.querySelectorAll('body *')].filter(vis);

// FAIL: scroll horizontal
if (document.documentElement.scrollWidth > innerWidth + 1) {
  const lebar = all.filter(e => e.getBoundingClientRect().right > innerWidth + 1).slice(0, 3).map(e => e.tagName.toLowerCase() + (e.className ? '.' + String(e.className).split(' ')[0] : ''));
  add('fail', 'scroll-horizontal', `lebar halaman ${document.documentElement.scrollWidth}px > layar ${innerWidth}px; pelaku: ${lebar.join(', ')}`); }

// FAIL: kontras teks di bawah AA (dilewati bila latar berupa gambar/gradien)
const bgOf = el => { for (let e = el; e; e = e.parentElement) { const s = getComputedStyle(e);
  if (s.backgroundImage !== 'none') return null; const c = rgb(s.backgroundColor); if (c && (c[3] ?? 1) > 0.9) return c; } return [255, 255, 255]; };
const low = [];
for (const el of all) {
  if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
  const s = getComputedStyle(el), fg = rgb(s.color), bg = bgOf(el); if (!fg || !bg) continue;
  const L1 = lum(fg), L2 = lum(bg), ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
  const px = parseFloat(s.fontSize), besar = px >= 24 || (px >= 18.66 && +s.fontWeight >= 700);
  if (ratio < (besar ? 3 : 4.5)) low.push(`"${txt(el)}" ${ratio.toFixed(2)}:1`); }
if (low.length) add('fail', 'kontras', `${low.length} teks di bawah AA, mis. ${low.slice(0, 3).join('; ')}`);

// FAIL: placeholder & penanda data
const body = document.body.innerText;
const ph = body.match(/\[BUTUH DATA[^\]]*\]|lorem ipsum|isi di sini|<NAMA>|\bTODO\b|xxx/gi);
if (ph) add('fail', 'placeholder', `masih ada: ${[...new Set(ph)].slice(0, 4).join(', ')}`);

// FAIL: judul melebihi batas baris (2 di >=600px, 3 di bawahnya)
const maks = w < 600 ? 3 : 2;
for (const h of document.querySelectorAll('h1,h2,h3,h4,h5,h6')) { if (!vis(h)) continue;
  const r = document.createRange(); r.selectNodeContents(h);
  const baris = new Set([...r.getClientRects()].filter(x => x.width > 1).map(x => Math.round(x.top))).size;
  if (baris > maks) add('fail', 'judul-panjang', `"${txt(h)}" ${baris} baris (maks ${maks})`); }

// FAIL: font web gagal dimuat (jatuh ke font cadangan)
const sistem = /^(arial|helvetica|georgia|times new roman|times|verdana|tahoma|system-ui|-apple-system|blinkmacsystemfont|segoe ui|sans-serif|serif|monospace|ui-sans-serif|ui-serif|inherit)$/i;
const termuat = new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/["']/g, '').toLowerCase()));
for (const el of [document.body, document.querySelector('h1')].filter(Boolean)) {
  const fam = getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim();
  if (!sistem.test(fam) && !termuat.has(fam.toLowerCase())) add('fail', 'font-gagal', `"${fam}" tidak termuat pada <${el.tagName.toLowerCase()}>`); }

// FAIL: tautan tanpa tujuan & nomor WA lokal
const mati = [...document.querySelectorAll('a')].filter(a => vis(a) && (!a.getAttribute('href') || /^(#|javascript:)$/i.test(a.getAttribute('href').trim())));
if (mati.length) add('fail', 'tautan-mati', `${mati.length} tautan tanpa tujuan, mis. ${mati.slice(0, 3).map(a => '"' + txt(a) + '"').join(', ')}`);
const wa0 = [...document.querySelectorAll('a[href*="wa.me/0"], a[href*="phone=0"]')];
if (wa0.length) add('fail', 'wa-format', `${wa0.length} tautan WhatsApp memakai 08…, harus 628…`);

// WARN: struktur judul
const h1 = [...document.querySelectorAll('h1')].filter(vis);
if (h1.length !== 1) add('warn', 'h1', `ada ${h1.length} h1; layar pertama butuh tepat satu`);

// WARN: larangan gaya (boleh dikalahkan brand lewat --izinkan)
for (const h of document.querySelectorAll('h1,h2,h3')) { const p = h.previousElementSibling; if (!p || !vis(p) || !vis(h)) continue;
  const sp = getComputedStyle(p), sh = getComputedStyle(h), t = txt(p);
  if (t && t.length < 40 && parseFloat(sp.fontSize) <= parseFloat(sh.fontSize) * 0.6 &&
      (sp.textTransform === 'uppercase' || parseFloat(sp.letterSpacing) > 1 || parseFloat(sp.borderRadius) >= 12))
    add('warn', 'eyebrow', `label kecil di atas judul: "${t}"`); }
for (const el of all) { const s = getComputedStyle(el);
  if (/gradient/.test(s.backgroundImage)) { const warna = (s.backgroundImage.match(/rgba?\([^)]*\)/g) || []).map(rgb);
    if (s.webkitBackgroundClip === 'text' || warna.some(c => hsl(c).s > 0.12 && (c[3] ?? 1) > 0.1)) add('warn', 'gradien', `${el.tagName.toLowerCase()} "${txt(el)}"`); }
  if (s.backdropFilter && s.backdropFilter !== 'none') add('warn', 'kaca', `backdrop-filter pada ${el.tagName.toLowerCase()}`);
  const sh = s.boxShadow; if (sh !== 'none') { const c = rgb(sh), blur = parseFloat((sh.match(/(\d+)px\s+(\d+)px\s+(\d+)px/) || [])[3] || 0);
    if (c && hsl(c).s > 0.25 && blur >= 16) add('warn', 'glow', `bayangan berwarna pada ${el.tagName.toLowerCase()} "${txt(el)}"`); } }
for (const n of document.querySelectorAll('nav, header')) { const s = getComputedStyle(n), r = n.getBoundingClientRect();
  if (/fixed|sticky/.test(s.position) && parseFloat(s.borderRadius) >= 20 && r.width < innerWidth * 0.95) add('warn', 'nav-pil', 'navigasi pil melayang'); }
for (const h of document.querySelectorAll('h1,h2,h3')) { const sh = getComputedStyle(h);
  for (const c of h.querySelectorAll('span,em,i,strong,b,mark')) { const sc = getComputedStyle(c);
    if (sc.color !== sh.color || sc.fontStyle !== sh.fontStyle || sc.fontFamily !== sh.fontFamily || sc.backgroundImage !== 'none')
      { add('warn', 'kata-aksen', `kata bergaya beda di judul "${txt(h)}": "${txt(c)}"`); break; } } }
const emo = body.match(/\p{Extended_Pictographic}/gu); if (emo) add('warn', 'emoji', `${emo.length} emoji, mis. ${emo.slice(0, 5).join(' ')}`);
const klaim = body.match(/\b(terbaik|termurah|terpercaya|terlengkap|nomor satu|paling murah|no\.?\s?1)\b|#1\b/gi);
if (klaim) add('warn', 'klaim-superlatif', `${[...new Set(klaim.map(k => k.toLowerCase()))].join(', ')} (untuk nakes: penghalang di QA)`);
const grup = new Map(); for (const el of all) { const ik = el.firstElementChild;
  if (!ik || !/svg|img|i/i.test(ik.tagName) || ik.getBoundingClientRect().width > 72 || !el.querySelector('h3,h4,p')) continue;
  const k = el.parentElement; grup.set(k, (grup.get(k) || 0) + 1); }
for (const [k, n] of grup) if (n >= 3) add('warn', 'kartu-ikon', `${n} kartu berikon seragam berderet di <${k.tagName.toLowerCase()}>`);
const bodyBg = rgb(getComputedStyle(document.body).backgroundColor) || [255, 255, 255], hb = hsl(bodyBg);
const tombol = [...document.querySelectorAll('a,button')].filter(vis).map(b => rgb(getComputedStyle(b).backgroundColor)).filter(c => c && (c[3] ?? 1) > 0.5).map(hsl);
if (hb.h >= 22 && hb.h <= 62 && hb.s >= .16 && hb.l >= .88 && tombol.some(t => t.h >= 6 && t.h <= 30 && t.s >= .38 && t.l >= .42 && t.l <= .72)) add('warn', 'palet-krem-terakota', 'latar krem dengan aksen terakota');
if (tombol.some(t => t.h >= 244 && t.h <= 295 && t.s >= .42 && t.l >= .3 && t.l <= .8)) add('warn', 'palet-ungu', 'tombol ungu/indigo');
if ([...document.querySelectorAll('[class*=swiper],[class*=slick],[class*=carousel],[class*=slider],[class*=splide],[class*=owl-]')].some(e => vis(e) && e.getBoundingClientRect().top < innerHeight))
  add('warn', 'slider-hero', 'slider/carousel di layar pertama');
for (const el of all) { const s = getComputedStyle(el), r = el.getBoundingClientRect();
  if (s.position === 'fixed' && r.width * r.height > innerWidth * innerHeight * 0.4 && !el.matches('header,nav')) { add('warn', 'popup', `lapisan tetap menutup ${Math.round(r.width * r.height / (innerWidth * innerHeight) * 100)}% layar`); break; } }
if (w < 600) { const judulCta = [document.querySelector('h1'), ...document.querySelectorAll('main a, main button')].filter(e => e && vis(e));
  for (const wa of document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"]')) { if (getComputedStyle(wa).position !== 'fixed' && getComputedStyle(wa.parentElement).position !== 'fixed') continue;
    const r = wa.getBoundingClientRect();
    if (judulCta.some(e => e !== wa && !wa.contains(e) && (q => !(q.right < r.left || q.left > r.right || q.bottom < r.top || q.top > r.bottom))(e.getBoundingClientRect())))
      { add('warn', 'wa-menutupi', 'tombol WA melayang menutupi judul/tombol di layar pertama'); break; } } }
return out; }"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", help="path index.html atau URL")
    ap.add_argument("--out", default="periksa", help="folder hasil (default: ./periksa)")
    ap.add_argument("--izinkan", default="", help="id WARN yang dikecualikan brand, pisah koma")
    ap.add_argument("--lebar", default="360,768,1440")
    a = ap.parse_args()
    url = a.target if a.target.startswith("http") else pathlib.Path(a.target).resolve().as_uri()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    izin = {x.strip() for x in a.izinkan.split(",") if x.strip()}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Playwright belum terpasang: pip install playwright && playwright install chromium. "
                 "Kalau tidak bisa, lakukan kritik manual dan catat di LAUNCH.md.")
    hasil, ada_fail = {}, False
    with sync_playwright() as p:
        br = p.chromium.launch()
        for w in [int(x) for x in a.lebar.split(",")]:
            pg = br.new_page(viewport={"width": w, "height": 800 if w < 600 else 900})
            gagal_unduh = []  # font yang tidak sampai karena jaringan, bukan karena halaman salah
            pg.on("requestfailed", lambda q: gagal_unduh.append(q.url)
                  if q.resource_type in ("font", "stylesheet") and "font" in q.url else None)
            pg.goto(url, wait_until="load", timeout=45000)
            try:
                pg.wait_for_load_state("networkidle", timeout=8000)
            except Exception:
                pass  # font/CDN lambat bukan alasan berhenti; font-gagal akan melaporkannya
            # gulir sampai bawah supaya animasi reveal dan gambar lazy ikut tampil
            pg.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=innerHeight*0.7){scrollTo(0,y);await new Promise(r=>setTimeout(r,150))}scrollTo(0,0)}")
            pg.wait_for_timeout(1200)
            pg.screenshot(path=str(out / f"{w}-layar1.png"))
            pg.screenshot(path=str(out / f"{w}-penuh.png"), full_page=True)
            r = pg.evaluate(JS, w)
            if gagal_unduh:  # jaringan memblokir: belum terbukti salah, tapi wajib dicek ulang
                for x in [x for x in r["fail"] if x["id"] == "font-gagal"]:
                    r["fail"].remove(x)
                    r["warn"].append({"id": "font-tak-teruji", "msg": x["msg"] + " — jaringan memblokir unduhan font; "
                                      "buka halaman di browser biasa sebelum deploy dan catat di LAUNCH.md"})
            r["warn"] = [x for x in r["warn"] if x["id"] not in izin]
            hasil[w] = r
            ada_fail |= bool(r["fail"])
            pg.close()
        br.close()
    (out / "laporan.json").write_text(json.dumps(hasil, ensure_ascii=False, indent=2))
    for w, r in hasil.items():
        print(f"\n== {w}px: {len(r['fail'])} FAIL, {len(r['warn'])} WARN")
        for lvl in ("fail", "warn"):
            for x in r[lvl]:
                print(f"  {lvl.upper():4} {x['id']}: {x['msg']}")
    print(f"\nScreenshot & laporan.json di {out.resolve()} — buka semua screenshot sebelum menilai.")
    sys.exit(1 if ada_fail else 0)


if __name__ == "__main__":
    main()
