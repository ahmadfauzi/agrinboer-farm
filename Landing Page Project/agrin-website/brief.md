# Brief & Sitemap — Website Peternakan Agrin Boer Farm

Versi 1 · 5 Nov 2026 · Pemilik: sendiri
Sumber: `../agrin-boer-farm/brand-strategy.md`, `PRODUCT.md`, landing aqiqah yang sudah tayang (`site/index.html`).

## 1. Tujuan

Website utama adalah **peternakan Agrin Boer Farm di Tajinan, Malang**. Setiap lini punya halaman sendiri. **Beranda menampilkan peternakan sebagai yang utama** (keputusan pengguna 5 Nov 2026); aqiqah menjadi lini pertama di peta lini, bukan hero beranda.

## 2. Keputusan dari pengguna (5 Nov 2026)

- Pemasukan terbesar: **aqiqah** → aqiqah lini pertama di semua daftar dan halaman lini paling lengkap.
- **Beranda: peternakan yang utama** (bukan aqiqah) — hero tentang kandang di Tajinan.
- Data lini selain aqiqah: **dummy** (`data-dummy`) + `[BUTUH DATA]`, diganti pengguna nanti.
- Tabungan: **Tabungan Qurban** (bukan tabungan aqiqah).
- Lini lain **sudah berjalan semua**: lotion kambing, burger kambing, kunjungan sekolah, magang.
- Struktur: halaman (path), bukan subdomain.

## 3. Arketipe (farm-website-assistant)

- **Primer: Layanan Ibadah** (aqiqah, Tabungan Qurban) — arus kas utama.
- **Pendukung: Produk Turunan** (lotion, burger) dan **Edukasi** (kunjungan sekolah, magang) — membuktikan bahwa ini peternakan sungguhan, bukan reseller kambing.
- Pelajaran dari nusaqu.id: beranda sebagai payung + satu halaman per lini. Tidak ditiru: menu >25 item, login di beranda, angka klaim tanpa sumber.

## 4. Sitemap

| URL | Halaman | Audiens & sapaan | CTA (WhatsApp, pesan terisi) | Status |
|---|---|---|---|---|
| `/` | Beranda peternakan | Semua pengunjung | Utama: chat WA umum ke peternakan · tiap lini lewat kartu/denah | Baru |
| `/aqiqah/` | Aqiqah | Ayah & Bunda | Tanya paket aqiqah | **Sudah ada** (dipindah dari `/`) |
| `/tabungan-qurban/` | Tabungan Qurban | Bapak/Ibu | Tanya Tabungan Qurban | Baru |
| `/kunjungan/` | Kunjungan & edukasi (sekolah, magang) | Bapak/Ibu Guru, kampus, mahasiswa | Atur jadwal kunjungan · Tanya program magang | Baru |
| `/lotion/` | Lotion susu kambing | kamu (nada ringan) | Pesan lotion | Baru |
| `/burger/` | Burger kambing | kamu (nada ringan) | Pesan burger | Baru |
| `/404.html` | Tidak ditemukan | — | Kembali ke beranda | Sudah ada |

Menu utama (6): Beranda · Aqiqah · Tabungan Qurban · Kunjungan · Produk (Lotion, Burger) · Kontak (ke footer beranda).
Setiap halaman: tombol WA di header, maksimal 1 klik ke WA, footer NAP (nama, alamat, nomor) yang sama di semua halaman.

## 5. Beranda — urutan section (usulan)

1. **Header** — wordmark, menu, tombol WA.
2. **Hero peternakan** — siapa Agrin + kandang di Tajinan yang bisa dikunjungi; CTA utama chat WA ke peternakan, tautan kedua ke peta lini.
3. **Peta lini** — denah kandang (konsep "Tur kandang") atau kartu: tiap pos/kartu = satu lini dengan satu kalimat + tautan halamannya.
4. **Sorotan aqiqah** — ringkasan paket + harga mulai dari + tautan ke `/aqiqah/`.
5. **Kandang terbuka** — kunjungan keluarga, sekolah, magang (ke `/kunjungan/`).
6. **Hasil kandang** — lotion & burger (ke halamannya).
7. **Tabungan Qurban** — ringkas, ke `/tabungan-qurban/`.
8. **Tentang Agrin** — nilai (amanah, terbuka, hangat, tuntas), cara merawat kambing.
9. **Kontak & lokasi** — alamat, peta, jam kunjung, WA.

## 6. Data yang dibutuhkan per lini

Tanpa data ini, halaman dibuat dengan dummy (`data-dummy`) dan `[BUTUH DATA]`, seperti landing aqiqah.

- **Lotion:** varian & ukuran, harga, nomor notifikasi BPOM, cara beli & ongkir, foto produk.
- **Burger:** menu & harga, cara pesan (ambil/antar/area), status halal & izin pangan (nomor), jam operasional, foto.
- **Kunjungan sekolah:** paket kunjungan, durasi, kapasitas, rentang usia, harga per anak/rombongan, apa yang dilakukan, aturan keselamatan, foto kegiatan.
- **Magang:** untuk siapa (SMK/kampus), durasi, syarat, kuota, cara daftar.
- **Tabungan Qurban:** skema setoran, jadwal, aturan penarikan/pengembalian (perjanjian tertulis).
- **Umum:** domain sendiri (disarankan, mis. `agrinboerfarm.com`), alamat lengkap, jam kunjung, nomor WA.

## 7. Kepatuhan (ringkas, bukan nasihat hukum)

- Lotion & burger: nomor izin/halal hanya tampil bila nomornya diberikan; tanpa klaim khasiat atau penyembuhan.
- Kunjungan sekolah/magang: foto anak hanya dengan izin tertulis orang tua/sekolah; formulir pendaftaran (bila ada) wajib persetujuan data (UU 27/2022 PDP).
- Tabungan Qurban: tanpa kata "investasi", "untung", "bagi hasil".
- Aqiqah: rambu yang sudah berlaku di `../agrin-boer-farm/`.

## 8. Yang ikut berubah

- `site/index.html` (aqiqah) pindah ke `site/aqiqah/index.html`; `/` diisi beranda peternakan.
- Preview alternatif "Tur kandang" (`/tur/`) disimpan di branch kerja sebagai rujukan desain beranda.
- `brand-strategy.md`: arsitektur brand perlu ditambah lini **Kunjungan & Edukasi**, dan beranda bergeser ke peternakan (aqiqah tetap terdepan).

## 9. Aset gambar yang benar-benar ada

Belum ada foto asli (sama dengan landing aqiqah). Slot foto memakai bingkai `[BUTUH DATA: foto …]` atau ilustrasi kode (denah); pengguna mengganti sendiri.
