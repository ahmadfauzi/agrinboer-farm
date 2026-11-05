# Landing Page: Agrin Boer Farm

Dibuat: 2026-11-04
Folder: `Landing Page Project/agrin-boer-farm/`
Pemilik: sendiri
Sumber brand: `brand-strategy.md` (Brand Strategy v1, 22 Okt 2026)

## Posisi

Tahap terakhir selesai: **5 (Rakit kode)**; Tahap 6 QA selesai, deploy ditahan
Tahap berikutnya: **6 — Deploy (setelah penghalang di LAUNCH.md beres)**

| # | Tahap | Artefak | Status |
|---|---|---|---|
| 1 | Brief | `brief.md`, `CLAUDE.md`, `PRODUCT.md` | selesai (`PRODUCT.md` ditunda ke Tahap 5 saat `impeccable` dimuat) |
| 2 | Copy | `copy.md` | selesai (v1.1, lolos audit antislop; sisa [CEK] tercatat) |
| 3 | Arah visual & ide | `DESIGN.md` | selesai |
| 4 | Token desain | `tokens.css`, `icons.md` | selesai |
| 5 | Rakit kode | `index.html`, `image-prompts.md` | selesai |
| 6 | QA & Deploy | `LAUNCH.md` | QA selesai (5 Nov 2026); deploy ditahan — penghalang di LAUNCH.md |

Status yang dipakai: `belum` · `selesai` · `menunggu klien` · `[dilewati] — alasan`

---

## Keputusan terkunci

> Setelah tercatat di sini, keputusan TIDAK boleh diubah oleh tahap berikutnya tanpa
> persetujuan eksplisit. Kalau ada perubahan, tulis ulang barisnya dan catat tanggal +
> alasannya di Riwayat perubahan. Project klien: tulis siapa yang menyetujui.

**Dari Tahap 1 — Brief**
- Audiens utama: Ayah & Bunda muda 25–35 th di Malang Raya yang menyiapkan aqiqah; qurban/tabungan sebagai lapisan kedua (Bapak/Ibu)
- Satu tujuan tindakan (CTA): Tanya paket aqiqah via WhatsApp (satu nomor; pesan terisi berbeda per section)
- Penawaran inti: Aqiqah tuntas (kambing Boer, sembelih, masak, packaging) dari kandang di Tajinan yang bisa dikunjungi dengan janji
- Daftar section: 1 Header · 2 Hero · 3 Sesuai ketentuan · 4 Paket & harga · 5 Alur 4 langkah · 6 Kandang terbuka · 7 Qurban & Tabungan · 8 FAQ · 9 CTA akhir · 10 Footer
- Aset gambar yang ada: tidak ada foto asli; sementara AI/stock atas permintaan pengguna (benturan dengan brand-strategy → diputuskan Tahap 3)
- Dilewati atas keputusan pengguna: bukti kesehatan, testimoni

**Dari Tahap 2 — Copy**
- Sudut utama: ketenangan, bukan sekadar kambing. Pengantar hero "Kamar sudah. Baju sudah. Nama sudah." + H1 "Aqiqah tuntas, dari kandang kami sendiri."
- Nada bicara: sesuai brand-strategy (hangat, jujur, tenang, edukatif tanpa menggurui); Ayah & Bunda, section qurban Bapak/Ibu; hukum ditulis netral
- Keberatan yang dijawab: (a) sesuai ketentuan atau tidak → section 3 + Kartu Kambing + kunjungan kandang; (b) repot & harga tidak jelas → paket berharga total + alur 4 langkah
- Pengecualian register: tagline "…momen keluargamu" tetap dipakai (keputusan brand)
- Teks tiap section: `copy.md` v1.1

**Dari Tahap 3 — Arah visual & ide** (rincian di `DESIGN.md`)
- Arah: page-is-the-object — halaman berbentuk Kartu Kambing / catatan kandang
- Kalimat ide: Di halaman ini, Kartu Kambing menjadi bentuk tiap section (baris berlabel seperti catatan kandang)
- Elemen hidup: pemilih paket (jenis kelamin anak + jumlah tamu → saran paket + WA terisi); data dummy
- Pengecualian larangan (id — alasan): (manual) foto stok/AI — sementara atas keputusan pengguna, diganti foto asli sebelum deploy; tipografi 3 keluarga — aksen tulisan tangan dari brand
- Disetujui klien (nama, tanggal): n/a (pemilik sendiri)

**Dari Tahap 4 — Token desain**
- Warna utama: palet brand apa adanya + turunan krem-kartu #FBF7EF, krem-tua #EADFC9, hijau-gelap #1A3521, cokelat-lembut #5E4A38 (semua pasangan teks lolos AA; Emas Tua di krem tua hanya ≥24px/hiasan)
- Pasangan font: Fraunces (judul) + Plus Jakarta Sans (isi) + Caveat (aksen tangan, sekali)
- Radius & motion (durasi, easing): kartu 12 · tombol 10 · isian 8; 200ms / 480ms, cubic-bezier(0.22, 0.61, 0.36, 1); reduced-motion → 0
- Library ikon: tanpa library; SVG inline (path Lucide ISC + siluet Boer gambar sendiri), lihat icons.md

**Dari Tahap 5 — Rakit kode**
- Urutan section final: sesuai brief (10 section) + sticky WA HP (muncul setelah hero, sembunyi di CTA akhir)
- Tujuan tombol CTA (URL/nomor): wa.me/62812000000000 (DUMMY) + pesan terisi per section; nomor di konstanta WA_NUMBER
- Gambar: host stock diblokir dari lingkungan kerja → slot foto berupa bingkai [BUTUH DATA] + siluet Boer; prompt GPT Image di image-prompts.md
- Font: Google Fonts CDN (sementara)

---

## WARN yang diterima

| Lebar | id | Alasan satu kalimat |
|---|---|---|
| — | — | Tidak ada WARN pada putaran 2 |

---

## Riwayat perubahan keputusan

| Tanggal | Yang diubah | Dari → Ke | Alasan | Disetujui |
|---|---|---|---|---|
| 2026-11-04 | Sumber gambar | Foto asli saja (brand-strategy) → gambar AI/stock sementara | Foto asli belum ada; pengguna akan mengganti sendiri | Pengguna |

---

## Catatan lanjutan

Temuan yang sengaja ditunda, bukan dilupakan:

- PENGHALANG DEPLOY: nomor WhatsApp dummy, harga paket dummy, gambar AI/stock sementara, alamat & jam kunjung, materi hukum aqiqah belum ditinjau ustaz.
- Font: masih Google Fonts CDN → pindah ke self-host sebelum deploy (privasi UU PDP).
- Teks UI baru yang tidak ada di copy.md (perlu persetujuan pengguna): label pemilih paket "Si Kecil", "Laki-laki", "Perempuan", "Perkiraan tamu", pesan galat "Isi dengan angka, misalnya 60.", teks saran "Saran: … (sekitar N porsi).", lencana "Cocok".
- Penyimpangan DESIGN.md: aksen tulisan tangan dipakai sebagai stempel "Contoh" di Kartu Kambing hero, bukan di CTA akhir (copy CTA akhir tidak punya sapaan untuk ditulis tangan).
- Penanda copy di label ketentuan "Disembelih dengan tata cara syar'i," berakhir koma karena kalimat copy terpotong label/isi; pertimbangkan sunting copy.
- [CEK] dari copy: Kartu Kambing berjalan sebelum tayang; skema tertulis Tabungan Qurban; materi hukum ditinjau ustaz.
- [PERLU DIVERIFIKASI] timbangan digital per ekor, kebijakan kambing sakit sebelum hari-H, sertifikat halal/juru sembelih, kirim foto kambing sebelum disembelih.
- Review Brand Strategy v1 (4 Nov 2026): izin susu (bukan PIRT; NKV/BPOM MD), izin burger (SLHS), cek batas wajib halal UMK 17 Okt 2026 untuk lini aqiqah, jadwal kampanye qurban (mulai ±Maret 2027), aksen warna per lini belum ditetapkan, font tulisan tangan belum dinamai.

---

## Catatan perbaikan alur

-
