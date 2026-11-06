# DESIGN.md — Website Peternakan Agrin Boer Farm
Pemilik: sendiri
Sumber arah: brand guideline (`../agrin-boer-farm/brand-strategy.md`) + usulan arah 1 "Tur kandang" dipilih pengguna (5 Nov 2026). Rujukan bangunan: preview `/tur/` di branch kerja dan `../agrin-boer-farm/DESIGN.md`.

## Identitas & mood
- Peternakan keluarga yang terbuka: hangat dan alami supaya terasa aman, rapi supaya terpercaya.
- Caregiver tenang, Sage pendukung. Tidak seperti startup agritech (tanpa angka klaim, tanpa lencana).

## Inventaris subjek
1. Kandang di Tajinan, Kabupaten Malang, bisa dikunjungi dengan janji.
2. Lima lini dari satu kandang: Aqiqah, Tabungan Qurban, Kunjungan & Magang, Lotion, Burger.
3. Kartu Kambing (foto, jenis, bobot, umur, tanggal timbang).
4. Ciri Boer: kepala cokelat kemerahan, telinga panjang terkulai.
5. Rombongan sekolah dan anak magang di kandang.
6. Musim Iduladha sebagai tujuan Tabungan Qurban.
7. Tagline "Dari kandang kami, untuk momen keluargamu."
8. Palet brand: Hijau Kandang, Krem Jerami, Cokelat Tanduk, Emas.

## Arah & ide
- Arah: **page-is-the-object / Tur kandang** — denah peternakan menjadi peta navigasi situs.
- Kalimat ide: Di halaman ini, **denah peternakan di Tajinan** menjadi **peta navigasi situs**: tiap pin adalah satu lini dan membuka halamannya.
- Uji kompetitor: nusaQu & peternakan lain → lulus; mereka memakai deretan kartu divisi, bukan denah kandang yang bisa didatangi.
- Elemen hidup: pin denah di beranda (hover/fokus membesar, klik membuka halaman lini) + pemilih paket yang sudah ada di Aqiqah. Halaman lain tanpa elemen hidup.

## Komposisi
- **Beranda, layar pertama:** kiri judul "Peternakan kambing yang bisa didatangi.", subjudul, tombol "Chat dengan peternakan", tautan "Lihat semua lini", trust line. Kanan denah besar dengan 5 pin bernomor berlabel **nama lini** (bukan nama ruangan), keterangan "Ilustrasi denah, bukan denah asli." HP: denah di bawah tombol.
- **Beranda, section berikutnya** (urutan `brief.md` §5, bertetangga beda bentuk):
  A3 Peta lini → daftar pos bernomor (nomor besar, nama lini, satu kalimat, tautan) bersambung garis jalan setapak; sama nomornya dengan pin.
  A4 Sorotan aqiqah → satu Kartu Kambing contoh + teks + tombol.
  A5 Kandang terbuka → bidang Hijau Kandang penuh, teks krem.
  A6 Hasil kandang → dua kartu krem berdampingan (lotion, burger) dengan slot foto.
  A7 Tabungan Qurban → bidang Krem Jerami, satu kolom teks.
  A8 Tentang Agrin → daftar empat nilai dua kolom di latar putih.
  A9 Kontak & lokasi → split: blok info kiri, slot peta `[BUTUH DATA]` kanan.
  A10 Footer → hijau gelap, gelombang emas, tautan semua lini.
- **Halaman lini** (`/tabungan-qurban/`, `/kunjungan/`, `/lotion/`, `/burger/`): kerangka landing aqiqah — header sama (menu 6 item), hero dua kolom (teks + kartu krem berisi data utama lini), section tabel dalam kartu krem berbaris putih, FAQ accordion, CTA akhir hijau bergelombang emas, footer sama. Hero diawali **penanda pos** (lingkaran nomor sesuai pin + nama lini) di samping judul, bukan label kecil di atas judul.
- **Aqiqah** (`/aqiqah/`): halaman yang sudah ada, dipindah apa adanya; header diganti header situs (menu 6 item).

## Warna (untuk tahap token)
- Sama dengan `site/tokens.css` sekarang: latar putih, kartu Krem Jerami + baris putih, bidang Hijau Kandang, footer hijau gelap, aksen Emas Tua di putih/krem dan Emas Terang di hijau. Tanpa warna baru per lini (brand: satu sistem visual).

## Tipografi (untuk tahap token)
- Fraunces judul, Plus Jakarta Sans isi, Caveat satu kali per halaman (stempel "Contoh" di Kartu Kambing). Judul hero ±40 karakter, 2 baris desktop, ≤3 baris di 360.

## Motif
- Denah kandang (beranda), jalan setapak titik-titik Emas Tua, penanda pos bundar hijau berangka emas, gelombang emas di CTA akhir & footer, Kartu Kambing.

## Gambar per slot
- Denah: ilustrasi SVG kode, berketerangan "ilustrasi" — permanen sampai ada denah asli.
- Siluet kepala Boer: ikon kode.
- Foto kandang, kambing, kegiatan kunjungan, produk lotion & burger, peta: `[BUTUH DATA: foto …]` bingkai kosong; diganti foto asli oleh pengguna. Foto siswa hanya dengan izin tertulis.
- Logo: tidak dibuat; wordmark teks.

## Gerak
- Satu gerak khas: penanda pos menyala (cincin emas) saat pengunjung tiba di pos; baris Kartu Kambing terisi berurutan. Pin denah membesar saat hover/fokus. Hormati prefers-reduced-motion.

## Larangan
- Berlaku: daftar larangan arah-visual-web-id.
- Pengecualian: tipografi 3 keluarga (Caveat, keputusan brand, satu kali per halaman).
- Tidak memakai: angka klaim, lencana kepercayaan, emoji, login di beranda (pelajaran dari nusaqu.id).

## Revisi v2 · 6 Nov 2026 (permintaan pengguna: tidak monoton, mewah tapi elegan, lebih banyak copy, animasi)
- **Ritme beranda:** tiap section berbeda bentuk dan latar: hero putih + pita fakta → manifesto hijau (kutipan besar, dua kolom teks) → peta lini (kepala lengket kiri, pos kanan) → kalender keluarga krem (garis waktu 4 momen) → sorotan aqiqah putih (alur bernomor + Kartu Kambing berbingkai emas) → kandang terbuka hijau (+ 4 langkah berkunjung) → pita lini berjalan → hasil kandang (kartu produk) → Tabungan Qurban krem (tiga prinsip) → nilai 4 kolom bernomor → FAQ krem dua kolom → kontak (panel hijau + slot peta) → footer.
- **Penanda pos** kini juga dipakai di judul section beranda (1 Aqiqah, 2 Tabungan, 3 Kunjungan, 4–5 produk), menggantikan label kecil di atas judul (eyebrow tetap dilarang).
- **Huruf:** Fraunces Italic (variabel, di-host sendiri, `site/fonts/Fraunces-italic-*.woff2`) hanya untuk: kutipan manifesto, nomor alur/nilai, keterangan momen kalender, catatan Kartu Kambing, tagline footer, pita lini. Kata beraksen di judul (h1–h3) tetap dilarang.
- **Pengecualian baru:** satu frasa italic emas di kutipan manifesto ("Tinggal kambingnya."). Kutipan berupa `blockquote`, bukan judul, dengan h2 tersembunyi untuk pembaca layar.
- **Gerak (semua halaman, mati di prefers-reduced-motion):** hero masuk berurutan; blok denah muncul lalu pin "melompat" bergiliran; titik jalan setapak berjalan pelan; elemen muncul naik saat digulir (situs.js menandai otomatis, termasuk halaman lini); header lengket berlapis kaca setelah digulir; bilah progres baca emas 2px; tombol terangkat dengan panah bergeser; pos peta lini bercincin emas saat hover; kartu produk terangkat; FAQ terbuka dengan jawaban turun halus; pita lini berjalan 48 detik per putaran, berhenti saat hover.
- **Slot foto:** bingkai garis putus emas + label penanda berbentuk pil, supaya kosongnya terlihat disengaja sampai foto asli ada.
