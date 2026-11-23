Penjelasan Struktur:

1. app.py: File ini isinya logika utama backend Flask buat ngatur halaman web dan nerima data dari form.

- from flask import Flask, render_template, request: Perintah buat ngambil fitur Flask, nampilin file HTML, dan ngebaca data yang dikirim user.
- app = Flask(__name__): Buat bikin aplikasi Flask utamanya.
- @app.route("/", methods=["GET", "POST"]): Buat ngatur alamat halaman utama ("/") supaya bisa nampilin halaman (GET) sekaligus nerima kiriman data form (POST).
- if request.method == "POST": Pengecekan apakah user baru aja ngeklik tombol kirim data lewat metode POST.
- nama_input = request.form.get("nama_input", "").strip(): Buat ngambil teks dari inputan form bernama "nama_input" lalu bersihin spasi berlebih di awal/akhir.
- render_template("index.html", hasil=hasil): Buat nampilin halaman index.html sambil ngirim variabel hasil ke tampilan web.
- if __name__ == "__main__": app.run(debug=True): Buat ngejalanin server Flask secara lokal biar bisa dicek di browser.

2. templates/index.html: File ini tampilan halaman web yang dilihat sama user di browser.

- <form method="POST">: Wadah form biar data di dalamnya dikirim pakai metode POST ke Flask.
- <label for="nama_input">: Teks label buat ngasih tahu user harus ngisi apa di kolom input.
- <input type="text" id="nama_input" name="nama_input" required>: Kolom isian teks (TextField) tempat user ngetik input, dan wajib diisi (required).
- <button type="submit">Kirim</button>: Tombol buat ngirim data form ke server Flask.
- {{ hasil if hasil else "Belum ada input" }}: Buat nampilin teks hasil dari app.py, atau nampilin pesan default kalau belum ada input yang dikirim.

3. static/styles.css: File ini buat ngatur tampilan atau gaya desain halaman web (opsional tapi bikin lebih rapi).

- body & .container: Buat ngatur posisi tengah, warna latar, ukuran kotak, dan bayangan biar tampilannya bersih.
- label, input[type="text"], & button: Buat ngatur jarak, ukuran huruf, border, dan warna tombol (termasuk efek hover pas kursor diarahkan).
- .output-box: Buat ngasih kotak khusus di bagian bawah biar hasil inputan kelihatan jelas.