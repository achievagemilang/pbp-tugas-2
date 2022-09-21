# Assignment 3: Implement Data Delivery using Django

**Nama                 :** Achieva Futura Gemilang

**NPM                  :** 2106750452

**Kelas                :** PBP D

**Link Heroku (HTML)   :** https://pbp-tugas-2-achievagemilang.herokuapp.com/mywatchlist/html

**Link Heroku (XML)    :** https://pbp-tugas-2-achievagemilang.herokuapp.com/mywatchlist/xml

**Link Heroku (JSON)   :** https://pbp-tugas-2-achievagemilang.herokuapp.com/mywatchlist/json


<br/>

### (1) Explain the difference between JSON, XML, and HTML!
HTML atau Hyper Text Markup Language merupakan sebuah markup language yang tersusun atas "tag". Biasanya cenderung statis karena hanya berfungsi untuk menampilkan data. Di lain sisi, XML atau eXtensible Markup Language juga merupakan sebuah markup language. Meskipun XML juga merupakan sebuah markup language, namun XML lebih bersifat ketat dibandingkan HTML. XML juga cenderung lebih aman dan dapat support berbagai tipe encoding. Biasanya digunakan untuk menyimpan dan mengirim data. Terakhir, JSON atau JavaScript Object Notation cenderung lebih cepat untuk diakses dan memiliki ukuran yang lebih kecil. Namun begitu, JSON hanya support encoding UTF-8 dan biasanya digunakan untuk merepresentasikan data objek. Penulisan sintaks JSON tidak menggunakan "tag", namun menggunakan pemetaan key: value.  

<br/>

Berikut adalah perbedaan penulisan sintaksnya:

<br/>

HTML
```
...
<h1>Blog Posts.</h1>
<div class="controls">
    <input type="number" id="first" placeholder="First" oninput="inputsChanged()">
    <input type="number" id="last" placeholder="Last" oninput="inputsChanged()">
</div>
<span class="total-word-count"><b>Total Word Count:</b> <span id="word-count">0000</span></span>
...
```

XML
```
<?xml version="1.0" encoding="UTF-8"?>
<message>
<to>Students</to>
<from>Teacher</from>
<subject>Regarding assignment submission</subject>
<text>All students will have to submit assignment by tomorrow.</text>
</message>

```

JSON
```
...
    {
      "model": "mywatchlist.MyWatchList",
      "pk": 4,
      "fields": {
        "watched": true,
        "title": "Joker",
        "rating": 5,
        "release_date": "2019-10-02",
        "review": "A film that is quite different because of a different point of view as well, which is to tell how a villain is born. Recommended."
      }
    },
...
```

Referensi: [Omar A @ Medium](https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb)

<br/>

### (2) Explain why we need the data delivery when implementing on a platform!
Sebelum menjawab pertanyaan ini, kita perlu menyadari bahwa fungsi data delivery adalah untuk mengirim data. Pengiriman data ini juga tidak hanya berlangsung pada satu komputer saja (secara local/internal), melainkan komputer satu dengan yang lainnya (dapat berupa host/server). Untuk itulah, agar platform dapat saling terhubung dibutuhkan sebuah sistem yang bernama data delivery agar pengiriman data dapat terfasilitasi.
<br/>
<br/>

### (3) Explain how do you complete the tasks in this assignment!

1. Inisiasi pembuatan app django baru dengan command `python manage.py startapp mywatchlist` lalu daftarkan `mywatchlist` ke list `INSTALLED_APPS` yang ada di `settings.py` pada folder `project_django`.


2. Lakukan pembuatan model `mywatchlist`, yang tersusun atas parameter `watched`, `title`, `rating`, `release_date`, dan `review`.


3. Lakukan migrasi model ke database dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate` pada terminal. 


4. Buat folder `fixtures` lalu buat juga file `initial_mywatchlist_data.json`. Ini berguna untuk menyimpan 10 entri data awal `mywatchlist` yang berisikan film yang pernah ditonton ataupun tidak pernah ditonton. Jangan lupa juga untuk assign parameter lainnya. Lalu, load data tersebut dengan menjalankan command `python manage.py loaddata initial_mywatchlist_data.json`.


5. Lakukan pembuatan fungsi `show_mywatchlist_json`, `show_mywatchlist_xml`, dan `show_mywatchlist_html` pada `views.py` yang melakukan querying models `MyWatchList` yang telah dibuat dan mereturn data berbentuk HTML, XML, dan JSON. Dalam tahap ini, penggunaan `all()` method akan sangat berguna untuk mengquery setiap model yang ada di `models.py`. Untuk implementasi bonus, tambahkan pemetaan `mywatchlist_watched` dan `mywatchlist_not_watched` yang menyimpan value dari banyaknya film yang telah/tidak ditonton.


6. Lakukan pembuatan variabel `app_name` dan implementasi list `urlpatterns` pada `urls.py` yang terletak pada folder `mywatchlist`. Proses routing yang ditambahkan disesuaikan dengan path format file yang akan dirender. Jangan lupa tambahkan juga line `path("mywatchlist/", include("mywatchlist.urls")),` pada `urls.py` yang terletak di `project_django`.  


7. Buat `mywatchlist.html` pada folder `templates` untuk menampilkan webpage dengan basis HTML. Webpage ini nantinya akan menampilkan tabel yang memuat informasi `mywatchlist` yang terkait.


8. Membuat test unit dengan `tests.py` untuk tiap path dengan format file yang berbeda. Hal ini dilakukan untuk menguji URL routers agar tidak ada masalah. Untuk menjalankan testnya lakukan command `python manage.py test`.


9. Lakukan uji pengaksesan URL `localhost:8000` untuk 3 path format file yang telah ditambahkan menggunakan Postman. 
    
    Berikut lampiran screenshotnya:
    
    -HTML
    ![diagram](/images/postman_html.png)
    <br/>
    <br/>
    
    -XML
    ![diagram](/images/postman_xml.png)
    <br/>
    <br/>
    
    -JSON
    ![diagram](/images/postman_json.png)
    <br/>

10. Edit `Procfile` dengan meng-concate string ` && python manage.py loaddata initial_mywatchlist_data.json` pada `release: `. Hal ini dilakukan agar aplikasi dapat me-load initial data mywatchlist saat di-deployed.


11. Lakukan proses deployment menggunakan Heroku dengan melakukan hal berikut:
 
      -Buka halaman website Heroku, lalu lakukan pembuatan aplikasi Heroku yang baru.
      
      -Salin API Key yang ada di halaman Account Settings.
      
      -Buka repositori Github, lalu tambahkan 2 repository secret, yaitu `HEROKU_API_KEY` dan `HEROKU_APP_NAME`
      
      -Run/Re-run deployment Actions, dan project ini berhasil ter-deploy di [Heroku](https://pbp-tugas-2-achievagemilang.herokuapp.com/). 
