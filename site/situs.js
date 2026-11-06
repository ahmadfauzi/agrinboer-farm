// Skrip bersama semua halaman Agrin Boer Farm.

// DUMMY: ganti dengan nomor WhatsApp asli (format 62…). Satu tempat untuk seluruh situs.
const WA_NUMBER = '62812000000000';

document.querySelectorAll('[data-wa]').forEach(a => {
  a.href = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(a.dataset.wa)}`;
});

// Menu dilipat di layar kecil.
const tombolMenu = document.querySelector('.menu-tombol');
const menu = document.getElementById('menu');
if (tombolMenu && menu) {
  const tutup = () => { menu.classList.remove('buka'); tombolMenu.setAttribute('aria-expanded', 'false'); };
  tombolMenu.addEventListener('click', () => {
    const buka = !menu.classList.contains('buka');
    menu.classList.toggle('buka', buka);
    tombolMenu.setAttribute('aria-expanded', String(buka));
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && menu.classList.contains('buka')) { tutup(); tombolMenu.focus(); }
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', tutup));
}

// Submenu Produk tertutup saat klik di luar (desktop).
document.addEventListener('click', e => {
  document.querySelectorAll('.menu details[open]').forEach(dt => {
    if (!dt.contains(e.target) && matchMedia('(min-width: 1024px)').matches) dt.removeAttribute('open');
  });
});

const adaIO = 'IntersectionObserver' in window;
const gerak = adaIO && !matchMedia('(prefers-reduced-motion: reduce)').matches;

// Baris Kartu Kambing terisi saat kartu masuk layar.
if (gerak) {
  document.documentElement.classList.add('js-gerak');
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('terisi'); io.unobserve(e.target); }
  }), { threshold: 0.3 });
  document.querySelectorAll('.kartu[data-isi]').forEach(k => io.observe(k));
}

// Sticky WA (HP): muncul setelah tombol hero lewat, sembunyi lagi saat CTA akhir terlihat.
const sticky = document.getElementById('sticky-wa');
const heroBtn = document.querySelector('.hero .aksi .btn');
const ctaAkhir = document.querySelector('.cta-akhir, .cta-akhir-beranda');
if (sticky && heroBtn) {
  const link = sticky.querySelector('a');
  if (adaIO) {
    let lewatHero = false, diAkhir = false;
    const atur = () => {
      const tampil = lewatHero && !diAkhir;
      sticky.classList.toggle('tampil', tampil);
      link.tabIndex = tampil ? 0 : -1;
    };
    new IntersectionObserver(([e]) => { lewatHero = !e.isIntersecting && e.boundingClientRect.top < 0; atur(); }).observe(heroBtn);
    if (ctaAkhir) new IntersectionObserver(([e]) => { diAkhir = e.isIntersecting || e.boundingClientRect.top < 0; atur(); }).observe(ctaAkhir);
  } else {
    sticky.classList.add('tampil');
    link.tabIndex = 0;
  }
}

// Header berlapis kaca setelah halaman digulir.
const header = document.querySelector('.header');
if (header) {
  const aturHeader = () => header.classList.toggle('tergulir', scrollY > 8);
  aturHeader();
  addEventListener('scroll', aturHeader, { passive: true });
}

// Gerak muncul saat digulir. Elemen ditandai di sini supaya semua halaman ikut tanpa mengubah HTML-nya;
// tanpa JS atau dengan prefers-reduced-motion, semua tampil biasa.
if (gerak) {
  const kelompok = [
    ['main .section .wrap > h2, main .section .sempit > h2', null],
    ['.label-bagian, .judul-section, .pengantar:not(.hero .pengantar)', null],
    ['.kalender-kepala > *, .nilai-kepala > *, .kontak-kepala > *, .produk-kepala > *, .lini-kepala > *', null],
    ['.pita-fakta > li, .lini > li, .musim > li, .tahap > li, .alur > li, .prinsip > li, .nilai > div, .faq > details', 'urut'],
    ['.produk > .kartu, .paket > .kartu, .qurban-kolom > div, .ketentuan > div, .daftar-poin > li', 'urut'],
    ['.kutipan, .manifesto-isi, .tanda-tangan, .manifesto-boer', null],
    ['.kartu-bingkai, .kandang-tata > .slot-foto, .kontak > *, .tabel-kartu, .sub-judul-bidang, .kandang .foto-besar', 'skala'],
  ];
  const sudah = new Set();
  kelompok.forEach(([sel, mode]) => {
    document.querySelectorAll(sel).forEach(el => {
      if (sudah.has(el) || el.closest('.hero') || el.closest('[data-muncul]')) return;
      sudah.add(el);
      el.dataset.muncul = mode === 'skala' ? 'skala' : '';
      if (mode === 'urut') el.style.setProperty('--urut', [...el.parentElement.children].indexOf(el) % 6);
    });
  });
  const ioMuncul = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    el.classList.add('muncul');
    ioMuncul.unobserve(el);
    // Lepas penanda setelah selesai, supaya transisi hover elemen itu kembali normal.
    const urut = parseFloat(getComputedStyle(el).getPropertyValue('--urut')) || 0;
    setTimeout(() => { el.removeAttribute('data-muncul'); el.classList.remove('muncul'); el.style.removeProperty('--urut'); }, 900 + urut * 90);
  }), { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  document.querySelectorAll('[data-muncul]').forEach(el => ioMuncul.observe(el));
}
