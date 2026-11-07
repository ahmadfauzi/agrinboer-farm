# Landing Page: Website Peternakan Agrin Boer Farm

Dibuat: 2026-11-05
Folder: `Landing Page Project/agrin-website/`
Pemilik: sendiri

## Posisi

Tahap terakhir selesai: **5 (Rakit kode) halaman lini v1.3, 7 Nov 2026**
Tahap berikutnya: **6 — QA & Deploy** (QA penuh ulang: antislop-code-id, image-optimization, Mode Periksa, web-quality-audit; deploy tetap ditahan sampai penghalang di LAUNCH.md beres)

| # | Tahap | Artefak | Status |
|---|---|---|---|
| 1 | Brief | `brief.md`, `CLAUDE.md` (repo), `PRODUCT.md` (repo) | selesai (PRODUCT.md perlu diperluas ke semua lini di Tahap 5) |
| 2 | Copy | `copy.md` (beranda + 4 halaman lini baru) | selesai (v1.3, 6 Nov 2026: halaman lini diperkaya; cek_klise 0 temuan) |
| 3 | Arah visual & ide | `DESIGN.md` | selesai |
| 4 | Token desain | `site/tokens.css` | selesai (dipakai ulang + 5 token baru) |
| 5 | Rakit kode (beranda v2 + halaman lini v1.3 selesai 7 Nov 2026) | `site/index.html`, `site/{aqiqah,tabungan-qurban,kunjungan,lotion,burger}/index.html`, `site/situs.css`, `site/situs.js` | selesai |
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

**Dari Tahap 2 (dibuka ulang 6 Nov 2026)**
- Beranda v2 (12 section, copy v1.2) dikunci sebagai daftar section beranda yang baru (pilihan 2a pengguna)
- Halaman lini: section tambahan disetujui (pilihan 1b): Tabungan 5→8, Kunjungan 6→9, Lotion 4→7, Burger 4→7; Aqiqah tidak diubah isinya
- Sumber kalimat hanya brand-strategy, brief, copy yang ada; detail baru = [BUTUH DATA]/[CEK]

**Dari Tahap 5 (halaman lini v1.3, 7 Nov 2026)**
- Urutan section halaman lini = copy.md v1.3; bentuk section memakai ulang komponen beranda v2, tanpa token baru
- CTA tetap WhatsApp per halaman; pesan baru di Tabungan: kunjungan melihat kambing qurban
- Craft-floor impeccable: garis kiri emas 3px pada kartu prinsip diganti garis tipis atas-bawah; nomor 01–04 di nilai beranda dihapus

**Dari Tahap 3 — Arah visual & ide** (rincian di `DESIGN.md`)
- Arah: Tur kandang — denah peternakan sebagai peta navigasi situs
- Kalimat ide: Di halaman ini, denah peternakan di Tajinan menjadi peta navigasi situs
- Elemen hidup: pin denah → halaman lini; pemilih paket di Aqiqah
- Halaman lini: kerangka landing aqiqah (penanda pos dihapus 7 Nov 2026)
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
| 2026-11-06 | Daftar section halaman lini | copy.md v1.1 B–E → v1.3 (section baru bertanda "baru, v1.3") | Pengguna minta halaman lini tidak monoton dan lebih banyak copy | Pengguna |
| 2026-11-07 | Penanda pos | lingkaran bernomor di hero lini, judul section beranda, kartu produk → dihapus; pin denah, peta lini, nomor langkah tetap | Pengguna: section dan halaman tanpa nomor pos | Pengguna |

---

## Catatan lanjutan

- Data per lini (`brief.md` §6) dan domain sendiri belum ada.
- Nomor izin lotion (BPOM), burger (halal/izin pangan) hanya ditulis bila nomornya diberikan.
- `brand-strategy.md` perlu ditambah lini Kunjungan & Edukasi.
- WCAG 2.2.2 beres (7 Nov 2026): pita lini punya tombol "Jeda gerak"; titik jalan denah berhenti setelah 2 putaran (4,8 detik).
- Data untuk copy v1.3 halaman lini (semua [BUTUH DATA] di copy.md B–E): Lotion: kulit sasaran sesuai label, nomor BPOM (penghalang deploy, kosmetik hanya boleh dipromosikan bila sudah ternotifikasi), cara terima pesanan, area kirim; Burger: cara olah daging, status halal, cara bayar, pesanan besar; Kunjungan: barang bawaan siswa; Tabungan: bentuk catatan setoran.
- [CEK] baru (copy v1.3): Kartu Kambing dipakai juga untuk kambing qurban; isi kegiatan kunjungan; rincian kunjungan dikirim tertulis; lingkup magang; asal susu lotion dan daging burger dari kandang Agrin.
- [CEK] baru (copy v1.2): Kartu Kambing dikirim untuk tiap pesanan aqiqah sebelum hari-H; tim selalu menemani kunjungan.
- [CEK] dari copy: lotion dari susu kambing Agrin; daging burger dari kambing Agrin; aturan keselamatan kunjungan; skema tertulis Tabungan Qurban; fungsi lotion sesuai label.

---

## Catatan perbaikan alur

- 7 Nov 2026: launcher `impeccable context` gagal jalan karena skripnya berakhiran baris CRLF (Windows) dan tidak executable; konteks dibaca langsung dari PRODUCT.md dan DESIGN.md.
- 6 Nov 2026: beranda v2 sempat dirakit tanpa checkpoint copy; dikunci belakangan atas persetujuan pengguna (2a).
