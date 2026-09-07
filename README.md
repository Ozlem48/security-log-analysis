# Güvenlik Loglarının Analizi ve Şüpheli Davranışların Tespitine Yönelik Bir İzleme Sistemi

## Proje Hakkında

Bu projede güvenlik loglarının analiz edilmesi ve şüpheli kullanıcı davranışlarının tespit edilmesi amaçlanmaktadır.

İlk aşamada Windows Event Log içerisindeki Security Log kayıtları incelenecek ve özellikle kullanıcı girişleri ile başarısız giriş denemeleri üzerinde çalışılacaktır.

Loglar Python ile alınarak düzenlenecek ve analiz edilebilir bir yapıya dönüştürülecektir. İlk çalışan sürümde kural tabanlı yöntemlerle temel şüpheli davranışların tespit edilmesi hedeflenmektedir.

İlerleyen aşamalarda istatistiksel anomali tespiti, makine öğrenmesi ve sonuçların gösterileceği basit bir dashboard eklenmesi planlanmaktadır.

## Genel Akış

Windows Event Log
→ Logların Alınması
→ Logların Düzenlenmesi
→ Veri Analizi
→ Şüpheli Davranış Tespiti
→ Risk Değerlendirmesi
→ Dashboard

## Kullanılacak Teknolojiler

- Python
- Pandas
- scikit-learn
- SQLite
- Flask
- HTML/CSS
- Git / GitHub

## Proje Dokümantasyonu

Proje kapsamında yapılan araştırmalar ve alınan teknik notlar `/doc` klasörü altında tutulmaktadır.
- [Windows Event Log](doc/windows-event-log.md)
