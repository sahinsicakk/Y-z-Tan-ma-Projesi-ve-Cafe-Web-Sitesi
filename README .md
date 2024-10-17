
# Yüz Tanıma Yoklama Sistemi

Bu proje, Python, SQLite, OpenCV ve Tkinter kullanılarak geliştirilen bir yüz tanıma tabanlı yoklama sistemidir. Program, kaydedilmiş yüzlerden yüz tanıma yoluyla yoklama alır ve yoklama sonuçlarını Excel formatında bir dosyaya kaydeder. Programın kullanılabilmesi için kullanıcı adı ve şifre ile giriş yapılması gerekmektedir.

## Özellikler
- **Giriş**: Kullanıcı adı ve şifre ile güvenli giriş yapılır.
- **Yüz Tanıma ve Yoklama**: Yüz tanıma algoritması kullanılarak kaydedilmiş yüzlerin varlığı kontrol edilir, yoklama alınır ve sonuçlar Excel dosyasına kaydedilir.
- **Veritabanı Kullanımı**: SQLite veritabanında kullanıcı bilgileri saklanır.
- **Veri Çıktısı**: Yoklama sonuçları Excel dosyasına kaydedilir.

## Kullanılan Teknolojiler
- **Python**
- **Tkinter** - Arayüz oluşturma
- **OpenCV** - Yüz tanıma algoritması
- **SQLite** - Veritabanı yönetimi
- **Pandas** - Verilerin işlenmesi
- **Excel Çıktısı** - `xlwt` kütüphanesi ile Excel dosyasına yoklama kaydı

## Kurulum ve Kullanım
1. Bu projeyi GitHub üzerinden indirin veya klonlayın.
2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install pandas opencv-python-headless xlwt
   ```
3. `personeller.db` SQLite veritabanını oluşturun ve `personel_listesi.xlsx` Excel dosyasını hazırlayın.
4. `datasets` klasöründe yüz resimlerini kaydedin ve ardından yüzleri `egitim/egitim.yml` dosyasına eğitmek için scripti çalıştırın.
5. `Yüz Tanıma Yoklama Sistemi` dosyasını çalıştırarak giriş ve yoklama ekranlarına erişin.

## Kullanım Kılavuzu
1. **Giriş**: Kullanıcı adı ve şifre ile giriş yapın.
2. **Yoklama Alma**: Giriş sonrası `Yoklama Al` butonuna tıklayarak yüz tanıma işlemini başlatın. Tanımlanan yüzler, Excel dosyasına yoklama kaydı olarak kaydedilecektir.

---

*Bu proje bir ekip çalışması olup, öğrenme amaçlı geliştirilmiştir.*
