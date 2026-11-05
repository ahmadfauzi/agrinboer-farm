# DESIGN.md — Agrin Boer Farm (landing page aqiqah)
Pemilik: sendiri
Sumber arah: brand guideline (`brand-strategy.md`, bagian Arah visual) + usulan arah 1 yang dipilih pengguna (4 Nov 2026)

## Identitas & mood
- Hangat dan alami supaya terasa aman; rapi dan berkelas supaya terasa terpercaya (brand-strategy).
- Kepribadian: Caregiver tenang, Sage pendukung. Tidak ceria-bulat, tidak mewah-dingin.
- Terasa seperti catatan kandang yang dirawat baik, bukan brosur jualan musiman.

## Inventaris subjek
1. Kandang nyata di Tajinan, Kabupaten Malang; kunjungan dengan janji lewat WhatsApp.
2. Kambing Boer: kepala cokelat kemerahan, badan putih, telinga panjang terkulai.
3. Kartu Kambing: foto, jenis, bobot, umur, tanggal timbang (format konten tetap brand).
4. Bobot dalam kg sebagai bukti, bukan taksiran.
5. Kalimat persona "Kamar sudah. Baju sudah. Nama sudah."
6. Hari ke-7, ke-14, ke-21 dalam pembahasan waktu aqiqah.
7. Pilihan 1 ekor atau 2 ekor per paket.
8. Jerami dan hijauan pakan (tekstur brand).
9. Garis gelombang emas di atas panel hijau (aset carousel brand).
10. Tagline "Dari kandang kami, untuk momen keluargamu."
11. Palet brand: Hijau Kandang, Krem Jerami, Cokelat Tanduk, Emas.

## Arah & ide
- Arah: **page-is-the-object** — halaman berbentuk Kartu Kambing / catatan kandang, karena Kartu Kambing adalah aset pembeda milik brand sendiri.
- Kalimat ide: Di halaman ini, **Kartu Kambing** menjadi **bentuk tiap section**: paket, ketentuan, dan kunjungan ditulis sebagai baris berlabel (label kiri, isi kanan) seperti catatan kandang.
- Uji kompetitor: This Is Farm / lapak Sukun → lulus, karena mereka menjual lewat live streaming dan harga, bukan lewat kartu data per ekor.
- Pengantar hero tetap kalimat persona (dari copy.md); gelombang emas hanya di panel hijau CTA akhir dan footer.
- Elemen hidup: **pemilih paket** di section Paket — pilih anak laki-laki/perempuan + perkiraan jumlah tamu → saran paket + tombol WA dengan pesan terisi. Data porsi dan harga masih dummy (ditandai). Tanpa JavaScript, tabel paket tetap terbaca lengkap. (Usulan diterima tanpa keberatan; bisa dibuang di Tahap 5 bila mengganggu.)

## Komposisi
- **Layar pertama (desktop):** dua kolom. Kiri: pengantar kecil "Kamar sudah. Baju sudah. Nama sudah." → H1 Fraunces besar (2 baris) → subjudul → tombol WA + microcopy → trust line. Kanan: satu Kartu Kambing contoh, besar, bidang krem lebih terang dengan tepi bidang (bukan garis tipis), label "Contoh".
- **Layar pertama (HP 360):** pengantar → H1 (≤3 baris) → subjudul → tombol WA lebar penuh; Kartu Kambing di bawah lipatan.
- **Per section** (urutan brief.md; bertetangga tidak berbentuk sama):
  1. Header → bilah polos krem: wordmark teks kiri, tombol WA kanan. Tanpa menu.
  2. Hero → dua kolom teks + Kartu Kambing (lihat atas).
  3. Ketentuan → satu kolom sempit, daftar baris berlabel bergaya kartu (label tebal kiri, isi kanan, pemisah bidang antar-baris). Bukan kartu berikon.
  4. Paket & harga → pemilih paket di atas, lalu tiga kartu paket bergaya Kartu Kambing (kepala kartu Hijau Kandang, baris data di bawah, harga besar, tombol). HP: bertumpuk.
  5. Alur 4 langkah → bidang Hijau Kandang penuh, teks krem; garis waktu horizontal bernomor 1–4 (urutan nyata). HP: vertikal.
  6. Kandang terbuka → split: kiri slot foto kandang lebar; kanan Kartu Kambing contoh + blok kunjungan (alamat, jam, tombol "Atur jadwal kunjungan").
  7. Qurban & Tabungan → bidang krem lebih tua, dua kolom teks berdampingan (Qurban | Tabungan Qurban), aksen Emas Tua, satu tombol.
  8. FAQ → accordion satu kolom sempit di krem.
  9. CTA akhir → panel Hijau Kandang dengan garis gelombang emas di tepi atas; tagline besar Fraunces terpusat; satu sapaan tulisan tangan emas di luar judul; tombol.
  10. Footer → Hijau Kandang lebih gelap, kolom info (nama, deskriptor, alamat, WA, jam kunjung).
- Sticky WA di HP: bilah bawah kecil, tidak menutupi judul/tombol.

## Warna (untuk tahap token)
- **Perubahan 5 Nov 2026 (keputusan pengguna):** latar halaman jadi **putih #FFFFFF**; kartu (Kartu Kambing, kartu paket, 404) berbadan Krem Jerami dengan baris belang putih, tanpa bayangan; panel pemilih, kunjungan, dan section qurban Krem Jerami. Proporsi di bawah ditulis untuk latar krem lama, yang kini cadangan (`?tema=krem`).
- Dari brand-strategy, nilai tidak diubah: Hijau Kandang #24482E, Krem Jerami #F4ECDD, Cokelat Tanduk #3A2A1C, Emas Tua #8F5F1F, Emas Terang #D9A441, Hijau Daun #6B8E4E.
- Proporsi: latar Krem ±65%; bidang Hijau Kandang penuh ±25% (alur, CTA akhir, footer, kepala kartu paket); tinta Cokelat Tanduk; aksen emas ±5% (garis, label kecil di krem = Emas Tua; garis/ikon/teks di hijau = Emas Terang).
- Tombol aksi: Hijau Kandang di atas krem; Emas Terang dengan teks Cokelat Tanduk di atas hijau. Emas tidak dipakai sebagai teks kecil di atas krem kecuali Emas Tua.
- Hijau Daun: hanya hiasan besar (3,19:1), tidak untuk teks. Lini Hasil Kandang tidak tampil di versi ini.
- Asal warna dari subjek: hijau kandang/pakan, krem jerami, cokelat tanduk dan kepala Boer, emas gelombang carousel.

## Tipografi (untuk tahap token)
- Judul: Fraunces (serif hangat). Isi & UI: Plus Jakarta Sans. Fredoka tidak dipakai.
- Aksen tulisan tangan: satu per halaman, 1–3 kata, bukan informasi penting, tidak di dalam judul (pengecualian brand dari aturan maks 2 keluarga). Nama font dipilih di Tahap 4.
- Judul hero "Aqiqah tuntas, dari kandang kami sendiri." (41 karakter): 2 baris desktop, ≤3 baris di 360.
- Label baris kartu: Plus Jakarta Sans tebal, ukuran kecil tapi ≥14px; isi ≥16px di HP.

## Motif
- Kartu Kambing (bentuk utama, lihat Komposisi).
- Garis gelombang emas: hanya di tepi atas panel CTA akhir dan footer.
- Tekstur jerami: sangat halus, hanya di latar hero atau bidang krem tua section 7; tidak mengganggu kontras.

## Gambar per slot
Keputusan pengguna (4 Nov 2026): gambar sementara boleh tidak sesuai aturan foto brand, karena akan diganti sendiri dengan foto asli. Semua gambar sementara ditandai `data-sementara` di kode dan tercatat sebagai penghalang deploy.
- Hero, Kartu Kambing contoh (foto kambing): gambar AI kambing Boer (prompt via image-prompt-generator) — sementara.
- Kandang terbuka (foto kandang lebar): gambar AI atau stock kandang kambing — sementara.
- Kartu paket (foto olahan, opsional): gambar AI sate/gulai kambing — sementara; boleh dihilangkan bila mengganggu.
- Tekstur jerami/latar: gambar AI atau tekstur CSS — boleh permanen (diizinkan brand).
- Logo: tidak dibuat; wordmark teks sampai logo final ada.
- Foto asli yang dibutuhkan: [BUTUH DATA: foto kambing per ekor, foto kandang, proses masak & packaging].

## Gerak
- Satu gerak khas: baris-baris Kartu Kambing muncul berurutan (opacity + geser kecil) saat kartu masuk layar, seperti kartu sedang diisi. Hormati prefers-reduced-motion.
- Sisanya mengikuti aturan gerak orkestrator.

## Larangan
- Berlaku: daftar larangan arah-visual-web-id (default).
- Pengecualian:
  - *(manual)* foto stok/AI untuk usaha lokal — sementara atas keputusan pengguna; wajib diganti foto asli sebelum deploy.
  - Tipografi 3 keluarga (aksen tulisan tangan) — keputusan brand-strategy; maks satu pemakaian, di luar judul.
- Catatan: palet krem + emas bukan krem-terakota (emas brand, bukan terakota); tidak perlu pengecualian `palet-krem-terakota`.
