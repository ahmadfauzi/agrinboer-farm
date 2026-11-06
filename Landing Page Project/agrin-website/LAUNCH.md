# LAUNCH.md — Website Peternakan Agrin Boer Farm

**Status: PRATINJAU (data dummy) — belum untuk dibagikan ke pelanggan.** QA Tahap 6: 5 Nov 2026.

- Preview branch: https://claude-bold-darwin-5yxfnr.agrinboer-farm.pages.dev/
- Produksi: https://agrinboer-farm.pages.dev/ — website peternakan tayang 6 Nov 2026 (PR #5), masih data dummy.
- Host: Cloudflare Pages, output directory `site`, tanpa build command.

## Penghalang deploy (wajib beres sebelum dibagikan)
- [ ] Penanda `[BUTUH DATA]`: beranda 9, aqiqah 16, tabungan 8, kunjungan 9, lotion 6, burger 6.
- [ ] Nilai `{DUMMY}`/`data-dummy`: nomor WA (`WA_NUMBER` di `site/situs.js`), harga, bobot, porsi, setoran, kapasitas, durasi, menu.
- [ ] Foto asli untuk semua slot `data-sementara` (kambing, kandang, kunjungan, lotion, burger, peta).
- [ ] Materi hukum aqiqah ditinjau ustaz.
- [ ] [CEK] klaim: Kartu Kambing berjalan; skema tertulis Tabungan Qurban; lotion dari susu kambing Agrin; daging burger dari kambing Agrin; aturan keselamatan kunjungan; fungsi lotion sesuai label.
- [ ] Nomor izin: notifikasi BPOM lotion; halal & izin pangan burger — tampil hanya bila nomornya diberikan.
- [x] Font di-host sendiri (`site/fonts/`), tidak lagi memuat Google Fonts.

## Hasil pemeriksaan
### Screenshot (arah-visual-web-id, 360/768/1440) — 6 halaman + 404
- FAIL tersisa hanya `placeholder` (disengaja). 404: 0 FAIL, 0 WARN.
- WARN diterima: `wa-menutupi` di beranda 360 (bilah WA tersembunyi saat diperiksa; alasan di project.md).
- Diperbaiki: judul hero halaman lini 3–4 baris → 2/3 baris; label penanda pos terbaca sebagai eyebrow → dibungkus; tombol WA di kontak melar.

### Lighthouse (mobile, preview, setelah font self-host)
| Halaman | Performa | Aksesibilitas | Praktik terbaik | SEO | FCP | LCP | CLS |
|---|---|---|---|---|---|---|---|
| Beranda | 99 | 100 | 100 | 66* | 1,2 s | 1,8 s | 0 |
| Tabungan Qurban | 100 | 100 | 100 | 66* | 0,9 s | 1,5 s | 0 |
| Aqiqah (sebelum font self-host) | 97 | 100 | 100 | 66* | — | 2,0 s | 0 |
| Kunjungan (sebelum font self-host) | 98 | 100 | 100 | 66* | — | 2,0 s | 0 |

*SEO 66 hanya karena audit `is-crawlable`: Cloudflare memberi header `x-robots-tag: noindex` pada URL preview. Cek ulang di URL produksi setelah merge.
Sebelum font self-host, LCP beranda 3,5 s (performa 83).

### Kode (antislop-code-id)
- Tidak ada `href="#"`, `alert()`, `console.log`, `!important`, statistik/testimoni karangan. Semua tautan `target="_blank"` memakai `rel="noopener noreferrer"`.
- Hex langsung hanya di `meta theme-color` (meta tidak bisa membaca variabel CSS).

### Interaksi
- [x] "Lewati ke konten" muncul pada Tab pertama.
- [x] Menu HP: tombol membuka (aria-expanded true), Escape menutup dan mengembalikan fokus.
- [x] Semua tautan internal (/, /aqiqah/, /tabungan-qurban/, /kunjungan/, /lotion/, /burger/, /#kontak) mengembalikan 200.
- [x] Pemilih paket di Aqiqah tetap berjalan (skrip halaman).
- [ ] Telusur Tab penuh dan buka dari HP asli — belum terverifikasi.

### Metadata
- [x] Judul, deskripsi, canonical, Open Graph per halaman; og-image.png (peternakan), og-aqiqah.png (aqiqah).
- [x] favicon, 404.html, robots.txt, sitemap.xml.
- [ ] Domain sendiri — belum ada (URL di canonical/sitemap memakai pages.dev; ganti bila domain dipasang).
- [ ] Analytics — belum ada.

## Cek setelah online (6 Nov 2026)
- [x] Semua halaman 200: /, /aqiqah/, /tabungan-qurban/, /kunjungan/, /lotion/, /burger/, /sitemap.xml, /fonts/fonts.css.
- [x] Alamat acak (/tes-404) mengembalikan 404.
- [x] URL produksi tanpa header `x-robots-tag` → audit SEO `is-crawlable` lolos di produksi.

## Pantau minggu pertama (setelah tayang resmi)
- Chat WA per hari, per halaman asal (pesan terisi berbeda tiap lini).
- Permintaan kunjungan sekolah/magang.
- Pertanyaan berulang → bahan FAQ.
