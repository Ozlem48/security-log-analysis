# Windows Event Log Araştırması

## Windows Event Log Nedir?

Windows Event Log, Windows işletim sisteminde gerçekleşen olayların kayıt altına alındığı log yapısıdır. Sistem, uygulama ve güvenlik ile ilgili farklı olaylar burada tutulabilir.

Projede özellikle güvenlik olaylarının bulunduğu **Security Log** üzerinde çalışılması planlanmaktadır.

## Windows Event Log Yapısı

Windows Event Log içerisinde farklı log kategorileri bulunmaktadır. Bunlar arasında **Application**, **System** ve **Security** logları yer almaktadır.

Proje açısından özellikle **Security Log** önemlidir çünkü kullanıcı oturum açma gibi güvenlikle ilgili olaylar burada tutulmaktadır.

Event kayıtlarında olayın ne zaman gerçekleştiği, Event ID'si ve olayla ilgili çeşitli bilgiler bulunabilir. Projede ihtiyaç duyulan alanların bu kayıtlardan çıkarılması planlanmaktadır.

## Security Log

Security Log içerisinde kullanıcı girişleri, başarısız giriş denemeleri ve hesaplarla ilgili çeşitli güvenlik olayları tutulmaktadır.

Proje kapsamında özellikle kullanıcı girişleri ve başarısız giriş denemeleri incelenecektir.

## Login Olayları ve Event ID

Windows'ta login olayları farklı Event ID değerleri ile takip edilebilir.

Projede başlangıç olarak:

- **4624:** Başarılı oturum açma
- **4625:** Başarısız oturum açma

olayları incelenecektir.

Bu olaylar, kullanıcı girişlerinin incelenmesi ve şüpheli giriş davranışlarının tespit edilmesi için kullanılabilir.

## Loglardan Alınabilecek Bilgiler

Login olaylarının incelenmesi sırasında proje açısından kullanılabilecek bazı bilgiler:

- Zaman bilgisi
- Event ID
- Kullanıcı hesabı
- Kaynak IP adresi
- Logon Type
- Bilgisayar bilgisi

Bu bilgilerin Python ile alınarak daha düzenli ve analiz edilebilir bir veri yapısına dönüştürülmesi planlanmaktadır.

## Projede Kullanımı

İlk aşamada Windows Security Log içerisindeki login olaylarının okunması ve gerekli bilgilerin çıkarılması hedeflenmektedir.

Örneğin aynı IP adresinden kısa bir zaman içerisinde çok sayıda başarısız giriş yapılması şüpheli bir davranış olarak değerlendirilebilir.

İlerleyen aşamalarda elde edilen log verileri üzerinde istatistiksel anomali tespiti ve makine öğrenmesi yöntemlerinin uygulanması değerlendirilecektir.

## Sonraki Aşama

Bir sonraki aşamada Windows Event Log kayıtlarının Python üzerinden nasıl okunabileceği ve gerekli alanların nasıl çıkarılacağı araştırılacaktır.
