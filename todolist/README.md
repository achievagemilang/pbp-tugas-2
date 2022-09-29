# Assignment 3: Implement Data Delivery using Django

**Nama                 :** Achieva Futura Gemilang

**NPM                  :** 2106750452

**Kelas                :** PBP D

**Link Heroku          :** https://pbp-tugas-2-achievagemilang.herokuapp.com/todolist
<br>

### What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?
  Cross-Site Request Forgery (CSRF) merupakan sebuah serangan yang membuat pengguna internet tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. Untuk menghindari serangan seperti ini maka digunakan tag `csrf_token`. `csrf_token` akan mengenerate token pada server setelah kita proses rendering pada webpage, hal ini juga berguna untuk memfilter request.
  
  Jika tag token ini tidak ada, maka Django tetap merender webpage untuk menampilkan form pengisian data. Akan tetapi, setelah melakukan submit form, maka akan ada masalah HTTP Request Forbidden yang memberitahu bahwa verifikasi CSRF gagal sehingga request akan dibatalkan.
<br>

### Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
  Bisa saja. Secara general, cara membuatnya adalah sebagai berikut:
  - Pada file template `.html` yang dituju, inisiasi form dengan method POST menggunakan tag `<form method="POST">`
  - Tambahkan `{% csrf_token %}` untuk menghindari serangan siber CSRF
  - Tambahkan button submit untuk mengirimkan data pada form.
  - Apabila diperlukan, kita juga bisa membuat fungsi pada views.py yang telah dlakukan routing pada tag form dan akan menghandle request form tersebut.

### Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
  Setelah user menginput data-datanya dan menekan button submit. Maka user telah mengirimkan request berbentuk POST yang akan dihandle oleh fungsi pada views.py.
  Pada fungsi-fungsi tersebut, akan dilakukan pembacaan data, penyimpanan database, dan pengaksesan database. Pengaksesan database akan dimasukkan ke `context` sehingga dapat dikirim ke template. `context` akan digunakan oleh template untuk mendapatkan informasi yang dibutuhkan, lalu akan dirender oleh fungsi pada views.py untuk ditampilkan ke user. 

### Explain how you implement the checklist above.
  1. Inisiasi aplikasi baru dengan perintah `python manage.py startapp todolist` dan tambahkan pada `INSTALLED_APPS` di `settings.py` pada `project_django`.
  2. Membuat model `Task` pada `models.py` yang berisikan user, date, title, description, dan is_finished.
  3. Melakukan migrasi dengan perintah `python manage.py makemigrations` dan `python manage.py migrate`.
  4. Pada `views.py`, buat fungsi-fungsi yang dibutuhkan seperti:
      - login_user -> untuk handle login user menggunakan username dan password
      - logout_user -> untuk handle logout akun user 
      - register -> mendaftarkan akun user yang baru dibuat
      - show_todolist -> merender webpage untuk menampilkan halaman utama todolist
      - create_task -> menambahkan task pada todolist
      - toggle_is_finished -> untuk handle pergantian task agar dapat ditandai selesai
      - delete_task -> untuk menghapus task
  5. Membuat routing fungsi-fungsi tersebut pada `todolist.urls` dan integrasikan pada `project_django.urls`.
  6. Membuat template .html untuk menampilkan data yang diinginkan. Berikut .html yang dibuat:
      - create-task -> untuk menampilkan webpage yang berguna untuk menambahkan task pada todolist.html
      - todolist -> menampilkan webpage halaman utama yang berisikan task-task user dan situasi task tersebut.
      - login -> menampilkan webpage untuk handle halaman login
      - register -> untuk menampilkan webpage yang berguna ketika user ingin mendaftarkan akunnya
  7. Karena sudah melakukan deployment sebelumnya, maka lakukan proses deployment menggunakan Heroku dengan melakukan hal berikut:
      - Pull, add, commit, dan push file lokal ke repositori github. 
      - Run/Re-run deployment Actions, dan project ini berhasil ter-deploy di [Heroku](https://pbp-tugas-2-achievagemilang.herokuapp.com/).
