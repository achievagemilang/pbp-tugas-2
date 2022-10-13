# Assignment 3: Implement Data Delivery using Django

**Nama                 :** Achieva Futura Gemilang

**NPM                  :** 2106750452

**Kelas                :** PBP D

**Link Heroku          :** https://pbp-tugas-2-achievagemilang.herokuapp.com/todolist
<br>


### Describe the difference between asynchronous programming with synchronous programming.
  Synchronous programming memungkinkan kita untuk menjalankan perintah/request secara single thread, atau dengan kata lain tiap request akan dijalankan satu per satu secara linear. Dengan demikian, kita perlu menunggu respons dari server sebelum menjalankan request lainnya. Di lain sisi, asynchronous programming memungkinkan kita untuk menjalankan request secara multi thread, artinya kita dapat menjalankan request secara paralel. Dengan demikian, kita tidak perlu menunggu respons dari server untuk melakukan hal lainnya karena proses tersebut berjalan secara asinkronus.
<br>

### When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.
    Event-driven programming adalah paradigma pengeksekusian program yang ditentukan berdasarkan action (event) yang telah dilakukan user. Contoh dari event tersebut seperti click, drag, dan lain-lain. Salah satu contohnya pada tugas ini adalah pembuatan button `Add Task` pada popup modal. Ketika user telah mengisi form untuk menambahkan task lalu menekan tombol tersebut, maka akan menjalankan event untuk mengupdate penambahan task.
<br>

### Describe the implementation of asynchronous programming in AJAX.
  Pada awalnya, browser akan memanggil fungsi AJAX javascript untuk membuat objek XMLHttpRequest dan mengirimkan HTTPRequest. XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkronus apabila kita menyimpan data menggunakan XML. Sedangkan HTTPRequest akan diproses oleh server secara asinkronus dan menghasilkan respons yang kemudian akan diberikan pada client (browser). Browser yang menerima data tersebut akan menampilkannya di page website tanpa kita perlu melakukan refresh/reload pada page website.

### Explain how you would implement the checklist above.
  1. Pada `views.py`, lakukan pembuatan method `show_json` dan `add_task` untuk mereturn data task user dalam bentuk JSON dan menambahkan task. 
  2. Menambahkan routing pada `urls.py` untuk fungsi yang baru kita buat.
  3. Setelah mengimport script AJAX, saya menambahkan fungsi javascript `showTodolist()` pada `todolist.html` yang mengimplementasikan AJAX GET. Fungsi ini berfungsi untuk menampilkan card task yang telah dibuat.   
  4. Menambahkan kode html untuk menampilkan modal pada `todolist.html` yang akan diintegrasikan pada view `add_task` yang telah kita buat.
  5. Menambahkan fungsi javascript `update()` yang mengimplementasikan AJAX POST. Fungsi ini berfungsi untuk mengupdate task yang telah kita tambahkan.
  6. Melakukan pembuatan fungsi javascript `deleteTask()` untuk handle pengerjaan bonus yang mengimplementasikan AJAX DELETE. Fungsi ini berfungsi untuk menghapus task yang telah kita buat.
  7. Add, commit, dan push changes yang telah kita buat. Project otomatis terdeploy! :)
  
  <br>
  <br>
