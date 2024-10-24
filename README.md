# Asalsaja - Bot Discord dengan Python

**Asalsaja** adalah bot Discord yang dikembangkan menggunakan bahasa pemrograman Python. Bot ini dirancang untuk meningkatkan pengalaman interaksi di server Discord Anda dengan berbagai fitur menarik dan bermanfaat.

## Fitur Utama

- **Moderasi Server**: Alat moderasi otomatis seperti kick, ban, dan mute untuk menjaga komunitas tetap aman dan tertib.
- **Perintah Kustom**: Buat perintah khusus sesuai kebutuhan server Anda.
- **Integrasi API**: Mendapatkan informasi real-time seperti cuaca, berita, atau data lain melalui integrasi API eksternal.
- **Permainan dan Hiburan**: Menyediakan mini-game dan aktivitas seru untuk anggota server.

## Instalasi

1. **Klon Repository**
- git clone https://github.com/username/asalsaja.git
2. **Instal Dependensi**
- Navigasikan ke direktori proyek dan instal dependensi yang diperlukan:
- cd asalsaja pip install -r requirements.txt
3. **Konfigurasi Bot**
- Buat file `.env` di root direktori proyek.
- Tambahkan token bot Discord Anda ke dalam file `.env`:

  ```
  DISCORD_TOKEN=your_discord_bot_token_here
  ```

4. **Menjalankan Bot**
- python bot.py

## Penggunaan

- Gunakan prefix `!` untuk mengakses perintah bot.
- Ketik `!help` untuk melihat daftar perintah yang tersedia.

## Contoh Perintah

- `!halo` - Bot akan menyapa Anda.
- `!bersihkan [jumlah]` - Menghapus sejumlah pesan dari kanal.
- `!kick @user [alasan]` - Mengeluarkan anggota dari server.
- `!ban @user [alasan]` - Memblokir anggota dari server.
- `!unban nama#tag` - Membuka blokir anggota dari server.
- `!cuaca [kota]` - Menampilkan informasi cuaca terkini untuk kota yang ditentukan.
- `!tebak [angka]` - Bermain tebak angka dengan bot.

## Kontribusi

Kami menyambut kontribusi dari siapa pun. Silakan fork repository ini dan buat pull request untuk penambahan fitur atau perbaikan bug.

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](LICENSE).

## Kontak

Jika Anda memiliki pertanyaan atau saran, silakan buka *issues* atau buat *pull request* untuk kontribusi.
