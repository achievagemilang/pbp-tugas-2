# Assignments 2: Introduction to Django dan Models View Template (MVT) in Django

**Nama                 :** Achieva Futura Gemilang

**NPM                  :** 2106750452

**Kelas                :** PBP D

**Link Aplikasi Heroku :** https://pbp-tugas-2-achievagemilang.herokuapp.com/



### (1) Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.


Pertama-tama, user yang berperan sebagai client-side akan melakukan request berupa URL path. Lalu, Django sebagai server-side akan mencari kecocokan request user dengan URL patterns yang ada di `urls.py` (dalam kasus ini adalah `katalog.urls`. Request yang bersesuaian tersebut kemudian diteruskan ke `views.py` (`katalog.views`) yang berfungsi sebagai controller untuk merender webpage dari data yang tersedia. Untuk melakukan hal ini, `views.py` akan berinteraksi dengan `models.py` untuk mendapatkan data dari database yang kemudian dirender menjadi file HTML menggunakan template terkait yang telah tersedia di folder `templates`. Terakhir, user akan menerima response hasil render file HTML tersebut.


### (2) Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?

Virtual environment berguna untuk mengisolasi satu project dengan project lainnya. Hal ini direkomendasikan agar dapat menghindari potensi terjadinya konflik antara project satu dengan lainnya. Contoh konflik yang memungkinkan untuk terjadi adalah penggunaan dependency dan library yang sama namun berbeda versi. Meski begitu, kita tidak wajib untuk mengimplementasikan virtual environment untuk mendevelop web aplikasi berbasis Django. Hal ini karena selama masih terinstall python dan django, maka project Django masih dapat tetap berjalan selama tidak mengalami konflik seperti yang telah disebutkan sebelumnya. Meskipun begitu, hal ini tidak disarankan karena rentan mengalami konflik dengan project lainnya. 


### (3) Explain how did you implement the steps on point 1 to point 4 above.

1. Lakukan proses kloning template dari repositori template Django PBP. Dari template ini, kita telah mendapatkan template aplikasi bernama 'katalog' yang telah didaftarkan `project_django`.

2. Lakukan pembuatan fungsi `show_katalog` pada `views.py` yang melakukan querying models dan mereturn data berbentuk HTML. Dalam tahap ini, penggunaan `all()` method akan sangat berguna untuk mengquery setiap model yang ada di `models.py`

3. Lakukan proses routing dengan menambahkan route pada urls.py yang terletak di folder `katalog` dan `project_django`. Pada `projext_django`, tambahkan`path('katalog/', include('katalog.urls')),` sedangkan pada `katalog` tambahkan `path("", show_katalog, name="show_katalog"),` diikuti dengan packages yang dibutuhkan. 

4. Edit file `katalog.html` yang sudah ada di folder `templates` dengan menambahkan sintaks HTML terkait untuk menampilkan nama, NPM, dan setiap list katalog yang ada.

5. Lakukan migrasi dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate` pada terminal. Ini akan menghasilkan file `0001_initial.py` pada folder `migrations`. Setelah itu, load data yang telah ada pada file `initial_catalog_data` yang terletak pada folder `fixtures` dengan menjalankan `python manage.py loaddata initial_catalog_data.json` pada terminal.

6. Lakukan proses deployment menggunakan Heroku dengan melakukan hal berikut:
 
      -Buka halaman website Heroku, lalu lakukan pembuatan aplikasi Heroku yang baru.
      
      -Salin API Key yang ada di halaman Account Settings.
      
      -Buka repositori Github, lalu tambahkan 2 repository secret, yaitu `HEROKU_API_KEY` dan `HEROKU_APP_NAME`
      
      -Run/Re-run deployment Actions, dan project ini berhasil terdeploy di [Heroku](https://pbp-tugas-2-achievagemilang.herokuapp.com/). 
