# Landing Page: Website Peternakan Agrin Boer Farm

Dibuat: 2026-11-05
Folder: `Landing Page Project/agrin-website/`
Pemilik: sendiri

## Posisi

Tahap terakhir selesai: **5 (Rakit kode)**; Tahap 6 QA selesai, deploy resmi ditahan
Tahap berikutnya: **6 — Deploy (setelah penghalang di LAUNCH.md beres)**

| # | Tahap | Artefak | Status |
|---|---|---|---|
| 1 | Brief | `brief.md`, `CLAUDE.md` (repo), `PRODUCT.md` (repo) | selesai (PRODUCT.md perlu diperluas ke semua lini di Tahap 5) |
| 2 | Copy | `copy.md` (beranda + 4 halaman lini baru) | selesai (v1.1, lolos audit antislop) |
| 3 | Arah visual & ide | `DESIGN.md` | selesai |
| 4 | Token desain | `site/tokens.css` | selesai (dipakai ulang + 5 token baru) |
| 5 | Rakit kode | `site/index.html`, `site/{aqiqah,tabungan-qurban,kunjungan,lotion,burger}/index.html`, `site/situs.css`, `site/situs.js` | selesai |
| 6 | QA & Deploy | `LAUNCH.md` | QA selesai (5 Nov 2026); deploy resmi ditahan |

Status yang dipakai: `belum` · `selesai` · `menunggu klien` · `[dilewati] — alasan`

---

## Keputusan terkunci

**Dari Tahap 1 — Brief**
- Audiens utama: keluarga di Malang Raya (aqiqah, qurban), sekolah & kampus (kunjungan, magang), pembeli produk kandang (lotion, burger)
- Satu tujuan tindakan (CTA): chat WhatsApp; beranda = chat umum ke peternakan, tiap halaman lini = pesan terisi sesuai lini
- Penawaran inti: peternakan kambing keluarga di Tajinan yang bisa dikunjungi, dengan lini aqiqah, Tabungan Qurban, kunjungan & magang, lotion, burger
- Daftar section: lihat `brief.md` §4 (sitemap) dan §5 (beranda, 9 section)
- Aset gambar yang ada: tidak ada foto asli
- Beranda: peternakan yang utama; aqiqah lini pertama
- Tabungan = Tabungan Qurban; path, bukan subdomain; menu utama 6 item
- Data lini baru: dummy + `[BUTUH DATA]`
- Visual: palet, huruf, latar putih, kartu krem sama dengan landing aqiqah

**Dari Tahap 2 — Copy**
- Sudut utama beranda: "Peternakan kambing yang bisa didatangi." — kandang di Tajinan sebagai benang merah semua lini
- Nada bicara: brand-strategy; sapaan per halaman (beranda kami–keluarga, Tabungan Bapak/Ibu, Kunjungan Bapak/Ibu Guru & kamu, Lotion/Burger kamu)
- Keberatan yang dijawab: peternakan sungguhan atau reseller (kandang terbuka); aman untuk anak (aturan keselamatan); izin produk (jujur [BUTUH DATA]); uang tabungan (aturan tertulis, tanpa bahasa investasi)
- Teks tiap halaman: `copy.md` v1.1

**Dari Tahap 3 — Arah visual & ide** (rincian di `DESIGN.md`)
- Arah: Tur kandang — denah peternakan sebagai peta navigasi situs
- Kalimat ide: Di halaman ini, denah peternakan di Tajinan menjadi peta navigasi situs
- Elemen hidup: pin denah → halaman lini; pemilih paket di Aqiqah
- Halaman lini: kerangka landing aqiqah + penanda pos sesuai pin
- Pengecualian larangan: tipografi 3 keluarga (Caveat) — keputusan brand
- Disetujui klien: n/a (pemilik sendiri)

**Dari Tahap 4 — Token desain**
- Warna utama, pasangan font, radius & motion, ikon: dipakai ulang dari `site/tokens.css` (landing aqiqah); ikon SVG inline (`../agrin-boer-farm/icons.md`)
- Token baru: --tinggi-header, --pos-ukuran, --pos-ukuran-besar, --denah-maks, --garis-jalan

**Dari Tahap 5 — Rakit kode**
- Urutan section final: beranda sesuai brief §5; halaman lini sesuai copy.md B–E
- Tujuan tombol CTA: wa.me/62812000000000 (DUMMY), satu konstanta `WA_NUMBER` di `site/situs.js` untuk seluruh situs; pesan terisi per halaman
- Header & footer bersama; aqiqah dipindah ke `/aqiqah/` (og-aqiqah.png); og-image.png kini versi peternakan
- Preview `/tur/` dihapus (idenya masuk ke beranda)

---

## WARN yang diterima

| Lebar | id | Alasan satu kalimat |
|---|---|---|
| 360 (`/`) | wa-menutupi | Bilah WA tersembunyi di bawah layar saat diperiksa; pemeriksa membaca posisinya ketika halaman masih menggulir ke atas |

---

## Riwayat perubahan keputusan

| Tanggal | Yang diubah | Dari → Ke | Alasan | Disetujui |
|---|---|---|---|---|
| 2026-11-05 | Fokus beranda | aqiqah sebagai CTA utama beranda → peternakan yang utama, aqiqah lini pertama | Tujuan website adalah peternakan | Pengguna |
| 2026-11-06 | Beranda & gaya bersama (v2) | 9 section ringkas → 12 section beragam bentuk + copy v1.2; header lengket, gerak masuk, Fraunces Italic | Pengguna minta situs tidak monoton, mewah tapi elegan, lebih banyak copy dan animasi | Pengguna |

---

## Catatan lanjutan

- Data per lini (`brief.md` §6) dan domain sendiri belum ada.
- Nomor izin lotion (BPOM), burger (halal/izin pangan) hanya ditulis bila nomornya diberikan.
- `brand-strategy.md` perlu ditambah lini Kunjungan & Edukasi.
- [CEK] baru (copy v1.2): Kartu Kambing dikirim untuk tiap pesanan aqiqah sebelum hari-H; tim selalu menemani kunjungan.
- [CEK] dari copy: lotion dari susu kambing Agrin; daging burger dari kambing Agrin; aturan keselamatan kunjungan; skema tertulis Tabungan Qurban; fungsi lotion sesuai label.

---

## Catatan perbaikan alur

-
