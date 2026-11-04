# Brief — Landing Page Agrin Boer Farm

Versi 1 · 4 Nov 2026 · Sumber brand: `brand-strategy.md` (v1, 22 Okt 2026)

## 1. Klasifikasi keputusan (landing-page-blueprint, Langkah 1)

- **Siapa memutuskan:** B2C — Ayah/Bunda, sering bersama kakek-nenek.
- **Berat keputusan:** berisiko tinggi (ibadah, sekali seumur hidup anak, tidak boleh keliru) → 8–10 section, transparansi jadi section tersendiri.
- **Risiko terbesar di kepala pengunjung:** "Kambingnya sesuai ketentuan atau tidak, dan apakah semuanya beres tepat waktu tanpa saya repot?" → dijawab di hero dan section kedua, bukan di FAQ.
- **Kondisional:** berlokasi fisik (kandang di Tajinan, kunjungan dengan janji) → kunjungan kandang tampil sebagai bukti di badan halaman, tetapi konversinya tetap lewat WhatsApp, bukan tombol Rute terpisah. Bukan halaman bertenggat (aqiqah sepanjang tahun).

## 2. Audiens

Ayah & Bunda muda 25–35 tahun di Malang Raya; anak pertama baru lahir atau hamil trimester akhir. Datang dari Instagram, TikTok, WhatsApp. Sapaan: **Ayah & Bunda** (bagian qurban: Bapak/Ibu).

Persona kedua (bagian sekunder): keluarga yang berqurban dan penabung qurban bulanan.

## 3. Masalah yang dirasakan

- Kewalahan mengurus bayi; aqiqah urusan yang tidak boleh keliru tapi penuh mitos dan perbedaan pendapat.
- Takut kambing tidak sesuai ketentuan atau tertipu bobot.
- Harga paket tidak jelas di banyak penyedia.
- Repot memasak dan mengantar ke keluarga.

## 4. Penawaran inti

Aqiqah tuntas — kambing Boer, sembelih, masak, packaging — dari kandang sendiri di Tajinan, Kabupaten Malang, yang bisa dikunjungi dengan janji lewat WhatsApp.

## 5. Satu CTA utama

**Tanya paket aqiqah via WhatsApp** (pesan otomatis terisi). Section qurban memakai tujuan WhatsApp yang sama dengan pesan berbeda; tidak ada CTA dengan tujuan lain. Atur jadwal kunjungan kandang juga lewat WhatsApp yang sama.

## 6. Bukti yang tersedia

| Bukti | Status |
|---|---|
| Kandang nyata di Tajinan, bisa dikunjungi dengan janji | Ada (alamat lengkap: [BUTUH DATA: alamat kandang & link Google Maps]) |
| Jenis kambing Boer murni | Dinyatakan pemilik; bukti asal indukan belum dicatat → tampil sebagai "Boer", tanpa "murni", sampai bukti siap [PERLU DIVERIFIKASI] |
| Alur sembelih–masak–packaging | Ada sebagai layanan; dokumentasi foto belum ada |
| Kambing ditimbang | [PERLU DIVERIFIKASI: apakah ditimbang digital per ekor] |
| Bukti kesehatan (dokter hewan/dinas) | **Dilewati** atas keputusan pengguna — tidak diklaim di halaman |
| Testimoni | **Dilewati** atas keputusan pengguna — tidak ada section testimoni |
| Sertifikat halal / juru sembelih bersertifikat | [PERLU DIVERIFIKASI] — tidak diklaim sampai ada |

## 7. Aset gambar yang benar-benar ada

**Belum ada foto asli.** Atas permintaan pengguna, slot gambar sementara diisi gambar AI atau stock photo.

> ⚠️ Benturan dengan `brand-strategy.md` (Foto dan grafis): "Jangan menampilkan kandang atau kambing yang tampak seperti milik Agrin tetapi bukan." Penyelesaiannya diputuskan di Tahap 3 (sumber gambar per slot). Apa pun pilihannya, gambar sementara **wajib diganti foto asli sebelum deploy** (penghalang deploy).

## 8. Data dummy (atas permintaan pengguna)

- Nomor WhatsApp: dummy, diganti pengguna.
- Harga paket: dummy, diganti pengguna.

Semua nilai dummy ditandai di kode (`data-dummy`) dan tercatat di `project.md` sebagai penghalang deploy.

## 9. Daftar section (urutan dari blueprint "berisiko tinggi")

| # | Section | Tujuan | Isi yang harus ada | CTA |
|---|---|---|---|---|
| 1 | Header | Identitas + jalan pintas | Wordmark teks "Agrin Boer Farm · Aqiqah" (logo belum final), tombol WhatsApp. Navigasi minimal | WA |
| 2 | Hero | Uji 5 detik: apa, untuk siapa, langkah berikutnya | Judul dari insight "Kamar sudah, baju sudah, nama sudah. Kambingnya?"; subjudul layanan tuntas dari kandang di Tajinan; satu trust line (kandang bisa dikunjungi) | WA |
| 3 | Sesuai ketentuan, tanpa menebak | Jawab risiko terbesar | Ketentuan dasar hewan aqiqah (umur, sehat, tidak cacat) dan jumlah kambing umum dipakai, disampaikan netral dengan catatan perbedaan pendapat ulama + ajakan bertanya ke ustaz bila ragu. Tanpa vonis "dijamin sah". Materi hukum ditinjau ustaz sebelum tayang [PERLU DIVERIFIKASI] | — |
| 4 | Paket & harga | Hapus ketidakpastian biaya | 2–3 paket (dummy) berisi: jumlah kambing, jenis, perkiraan bobot, jumlah porsi/box, menu, area antar & ongkir, cara bayar/DP. Tanpa "termurah" | WA per paket |
| 5 | Alur 4 langkah | Tunjukkan "tuntas" | Pilih kambing → sembelih → dimasak → dikemas & diantar. Siapa yang mengerjakan, kapan Ayah & Bunda dilibatkan (mis. kirim foto kambing sebelum disembelih [PERLU DIVERIFIKASI]) | — |
| 6 | Kandang terbuka (transparansi) | Section transparansi tersendiri | Contoh Kartu Kambing (foto, jenis, bobot, tanggal); ajakan kunjungan dengan janji WA; jam kunjung [BUTUH DATA]; peta/alamat [BUTUH DATA] | WA "atur kunjungan" |
| 7 | Qurban & Tabungan Qurban | Lapisan kedua, sapaan Bapak/Ibu | Ringkas: qurban musim Iduladha 2027 + Tabungan Qurban (setoran bertahap). Tanpa bahasa investasi/untung. Skema rinci [BUTUH DATA] | WA (pesan qurban) |
| 8 | FAQ | Keberatan nyata | Lewat hari ke-7 bagaimana (netral, sebut perbedaan pendapat); bisa lihat kambingnya dulu?; area & ongkir antar; berapa hari sebelumnya pesan; bagaimana kalau kambing sakit sebelum hari-H [PERLU DIVERIFIKASI kebijakan]; DP & pembayaran | — |
| 9 | CTA akhir | Tutup dengan tenang | Ulang janji inti + tagline "Dari kandang kami, untuk momen keluargamu." | WA |
| 10 | Footer | Konsistensi identitas | Nama brand, deskriptor "Peternakan Kambing untuk Keluarga — Malang", alamat, WhatsApp, jam kunjung | — |

**Sticky WhatsApp di mobile:** ya.

## 10. Prioritas (MoSCoW)

- **Must:** section 1–6, 8–10; sticky WA; teks netral soal hukum; tidak ada klaim kesehatan/halal/"murni"/superlatif tanpa bukti.
- **Should:** section 7 (qurban & tabungan).
- **Could:** kalkulator porsi sederhana (jumlah tamu → paket).
- **Won't (versi ini):** produk harian (susu, lotion, burger) — izin belum beres; testimoni; bukti pemeriksaan kesehatan; form lead (semua lewat WhatsApp, tidak ada data pribadi dikumpulkan di halaman).

## 11. Rambu compliance (sebelum copy)

- Tidak memakai "dijamin sah", "pasti sesuai syariat", "terbaik/termurah se-Malang", "premium", "100% sehat".
- Tidak ada urgensi palsu ("stok tinggal 2").
- Foto bayi/anak hanya dengan izin orang tua (tidak dipakai di versi ini).
- Tabungan Qurban: tanpa kata "investasi", "untung"; perjanjian tertulis dirujuk, bukan dijelaskan secara hukum.
