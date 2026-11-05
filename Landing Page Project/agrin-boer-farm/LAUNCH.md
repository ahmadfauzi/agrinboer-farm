# LAUNCH.md — Agrin Boer Farm (landing page aqiqah)

**Status: BELUM DEPLOY — ditahan.** QA Tahap 6 dijalankan 5 Nov 2026. Halaman lolos semua pemeriksaan teknis yang bisa dijalankan, tetapi masih punya penghalang deploy di bawah.

- URL: — (belum ada)
- Tanggal tayang: —
- Host: Cloudflare Pages (dibuat pengguna 5 Nov 2026), build command kosong, output directory `site`

## Penghalang deploy (wajib beres sebelum tayang)

- [ ] **16 penanda `[BUTUH DATA]`** masih tampil (alamat, jam kunjung, ongkir, pemesanan/DP, kebijakan kambing sakit, skema Tabungan Qurban, tanggal buka qurban, foto).
- [ ] **Nomor WhatsApp dummy** `62812000000000` → ganti `WA_NUMBER` dan cari-ganti di `site/index.html`.
- [ ] **Harga, bobot, porsi, umur, tanggal timbang dummy** (`data-dummy`, bergaris titik).
- [ ] **Foto**: slot `data-sementara` masih bingkai kosong. Pasang foto asli (atau gambar dari `image-prompts.md` sementara, lalu tetap ganti foto asli).
- [ ] **Materi hukum aqiqah** (section Ketentuan + FAQ hari ke-7) ditinjau ustaz.
- [ ] **[CEK] klaim proses**: Kartu Kambing sudah berjalan; skema tertulis Tabungan Qurban sudah ada.
- [ ] **Font self-host** (sekarang Google Fonts CDN; privasi pengunjung, UU PDP).

## Hasil pemeriksaan

### Pemeriksaan screenshot (arah-visual-web-id, Mode Periksa) — 2 putaran
| Lebar | FAIL | WARN |
|---|---|---|
| 360 | placeholder | 0 |
| 768 | placeholder | 0 |
| 1440 | placeholder | 0 |

Diperbaiki di putaran 1: kontras teks alur (warna color-mix diganti token), judul hero 3 baris di 768/1440 (`--fs-h1` maks 3.5rem, kolom 16ch), tombol hero melebar 32px di HP (reset box-sizing ditambah), Kartu Kambing hero dibatasi 30rem di tablet.

## Kritik putaran 2
- Layar pertama (5 detik): jelas: aqiqah, dari kandang sendiri, tombol "Tanya paket aqiqah" terlihat tanpa scroll di 360/768/1440.
- Ide terlihat: ya — Kartu Kambing di hero, kartu paket, dan section Kandang memakai bentuk baris berlabel yang sama.
- Tiga masalah teratas: 1. bingkai foto kosong melemahkan hero (menunggu foto asli); 2. label "Disembelih dengan tata cara syar'i," berakhir koma (copy); 3. tanpa foto, section Kandang terasa datar.
- FAIL/WARN tersisa: placeholder (penghalang deploy, disengaja).

### Sisa AI di kode (antislop-code-id, Audit)
| No | Temuan | Status |
|---|---|---|
| 1 | Placeholder `[BUTUH DATA]` ×16 | Penghalang deploy (disengaja) |
| 2 | Tailwind CDN dimuat tetapi tidak ada kelas Tailwind yang dipakai | Diperbaiki: dihapus atas persetujuan pengguna (5 Nov 2026) |
| 3 | Warna galat ditulis langsung | Diperbaiki → token `--galat` (6,6–8,1:1) |
| 4 | `rgb()` literal untuk tekstur jerami & bayangan sticky | Diterima: turunan transparan dari warna token |
| 5 | `meta theme-color` memakai hex | Diterima: meta tidak bisa membaca variabel CSS |
| 6 | Tautan WA tanpa `target`/`rel` | Diperbaiki: `target="_blank" rel="noopener noreferrer"` |
| — | `href="#"`, `alert()`, `console.log`, `!important`, statistik/testimoni karangan | Tidak ada |

### Audit teknis (web-quality-audit)
**Belum terverifikasi.** Lighthouse tidak tersedia di lingkungan ini dan CDN Tailwind diblokir jaringan, jadi angka performa/SEO tidak ditebak. Jalankan Lighthouse (Chrome DevTools) setelah keputusan Tailwind dan font self-host.

### QA checklist
**Isi & pesan**
- [x] Satu tujuan tindakan (WhatsApp)
- [x] Hero menjanjikan hasil ("Aqiqah tuntas…")
- [x] Teks sama dengan `copy.md` (kecuali teks UI pemilih paket — lihat Catatan lanjutan di project.md)
- [ ] Tidak ada placeholder — **gagal (penghalang)**
- [x] Tanpa superlatif/klaim tanpa bukti
- [x] Kata ulang bertanda hubung ("laki-laki")
- [x] Judul `text-wrap: balance`

**Kepatuhan**
- [ ] Harga & data paket asli — **gagal (dummy)**
- [x] Tidak ada testimoni/nama pelanggan
- n/a Layanan kesehatan
- [x] Tidak mengumpulkan data pribadi (pemilih paket tidak mengirim apa pun; semua lewat WhatsApp)

**Tautan & aksi**
- [x] Semua CTA → wa.me dengan pesan terisi sesuai section (diperiksa di kode)
- [x] Format 62…
- [x] Tautan eksternal tab baru
- [x] Tanpa `#`/tautan mati

**Interaksi & state**
- [x] "Lewati ke konten", fokus terlihat (outline emas), hover & active pada tombol/pilihan/FAQ
- [x] Pemilih paket: validasi angka + pesan galat inline (`aria-invalid`, tanpa `alert`)
- n/a Tombol kirim form (tidak ada pengiriman)
- [ ] Telusur Tab manual seluruh halaman — **belum terverifikasi** (perlu dicoba di browser)

**Tampilan**
- [x] 360 tanpa scroll horizontal; 1440 terkunci 72rem
- [x] Warna/radius/durasi dari `tokens.css` (pengecualian no. 4–5 di atas)
- [x] Kontras AA (dihitung + pemeriksa otomatis)
- [x] Target sentuh ≥44px
- [x] Landmark `header`, `main`, `section`, `footer`; satu `h1` (tidak ada `nav` karena navigasi minimal)

**Gerak**
- [x] Hanya transform/opacity; IntersectionObserver; prefers-reduced-motion mematikan gerak; tanpa animasi otomatis >5 detik

**Aset & kecepatan**
- n/a Kompres gambar (belum ada gambar) — jalankan `image-optimization` saat foto dipasang (WebP, ≤200KB hero, `loading="lazy"` di bawah lipatan, `alt` bermakna)
- [x] Font `display=swap`

**Metadata**
- [x] Judul tab berisi brand, `lang="id"`, deskripsi meta (141 karakter)
- [ ] Favicon — **belum ada** (menunggu logo)
- [ ] Gambar Open Graph — **belum ada** (menunggu foto/logo)
- [ ] `404.html` — **belum ada**

**Penutup**
- [ ] Analytics — **belum ada** [BUTUH DATA: pilih alat]
- [ ] Dibuka dari HP asli — **belum terverifikasi**

## Pantau minggu pertama (setelah tayang)
- Jumlah chat WhatsApp masuk per hari dan pesan terisi mana yang paling sering dipakai (paket, kunjungan, tabungan).
- Pertanyaan yang berulang di chat → bahan FAQ.
- Permintaan kunjungan kandang.
