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
