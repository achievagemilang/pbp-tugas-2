# Assignment 4: Implementing Forms and Authentication Using Django

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
  
  <br>
  <br>
  
# Assignment 5: Web Design Using HTML, CSS, and CSS Framework
  
**Nama                 :** Achieva Futura Gemilang

**NPM                  :** 2106750452

**Kelas                :** PBP D

**Link Heroku          :** https://pbp-tugas-2-achievagemilang.herokuapp.com/todolist
<br>
  
### What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?
Inline CSS adalah cara menulis kode CSS secara langsung pada elemen HTML. Kelebihan metode ini adalah sangat efektif apabila hanya ingin melakukan styling
untuk satu elemen saja. Sedangkan kekurangannya adalah tidak terlalu efektif digunakan apabila styling multiple pages. Hal ini karena kita perlu setting secara satu per satu tiap elemen yang ada sehingga cenderung boros waktu.

Internal CSS adalah cara menulis kode CSS pada tag `<style>` pada section `head`. Kelebihannya adalah meerupakan penggunaan efektif apabila ingin melakukan styling untuk 1 page saja. Sedangkan kekurangannya hampir sama dengan inline CSS, yakni tidak efektif karena cenderung boros akan waktu apabila kita ingin melakukan styling secara besar untuk multiple pages, apabila dengan penggunaan styling yang mirip.

External CSS adalah cara menulis kode CSS pada file `.css` yang berada luar program yang kemudian terhubung dengan page-page website kita. Kelebihan metode ini adalah merupakan cara yang efektif untuk melakukan styling secara besar-besaran terhadap multiple page. Hal ini karena stylingnya akan digunakan untuk setiap komponen yang diseleksi. Karena bersifat applicable untuk setiap komponen yang sesuai, ada kalanya kita tidak ingin mengubah komponen tersebut menjadi design yang telah ditulis sebelumnya pada .css. Hal inilah yang menjadi kekurangan metode ini. Kita perlu membuat design terpisah untuk beberapa kasus elemen yang mungkin kita inginkan berbeda.    
   
### Describe the HTML5 tags that you know.
Sumber rujukan: https://www.tutorialrepublic.com/html-reference/html5-tags.php

Beberapa yang saya ketahui adalah:
- `<a>` -> mendefinisikan hyperlink.
- `br` -> membuat single line break.
- `<form>` -> mendefinisikan HTML form untuk input user.
- `<table>` -> mendefiniskan data berbentuk table.
- `<h1>,<h2>, .. ,<h6>` -> membuat HTML heading. (indeks 1 paling besar).
- `<input>` -> mendefinisikan input field untuk user menginput data.
- dsb.
  
### Describe the types of CSS selectors you know.
Sumber rujukan: https://www.w3schools.com/cssref/css_selectors.asp

Beberapa yang saya ketahui adalah:
- `*` -> Menseleksi semua komponen elemen.
- `.[class_name]` -> Menseleksi semua elemen yang memiliki class="[class_name]". Contoh [class_name] = "card", maka seleksi class="card".
- `[elemen]` -> Menseleksi tipe elemen yang merupakan [elemen]. Contoh [elemen] -> p, table, h5, dsb.
- `[elemen].[class_name]` -> Menseleksi tipe elemen yang merupakan [elemen] dan mempunyai class [class_name].
- `[elemen],[elemen2] -> Menseleksi lebih dari satu elemen dapat menggunakan separator koma.
- `.[class_name]:hover -> Menseleksi semua elemen yang memiliki class=[class_name] ketika didatangi kursor mouse.
- dsb.
   
### Explain how you would implement the checklist above.
- Pertama, saya mencari inspirasi color pallete yang ingin saya gunakan pada https://flatuicolors.com/ dan https://colorhunt.co/palettes/white.
- Instalasi bootstrap dengan menambahkan `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">` dan `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>` pada `base.html`.
- Selanjutnya saya mulai melakukan styling untuk pages yang ada pada `templates` saya. Karena saya cukup newbie, kebanyakan styling saya menggunakan Inline CSS sehingga kurang efektif dan time-consuming. Akan tetapi, cukup menyenangkan dan saya mendapat pengalaman baru dari sini.
- Selanjutnya, saya memastikan web responsif dengan bantuan acuan https://getbootstrap.com/docs/4.1/layout/overview/
- Add, commit, and push. Setelah workflow, jalan maka akan terdeploy (link heroku masih sama dengan tugas 4 diatas). 
