# Anomali Tespiti Araştırması

## Anomali Nedir?

Anomali, normal davranıştan belirgin şekilde farklı olan olay veya veri olarak düşünülebilir. Güvenlik loglarında anormal davranışlar, şüpheli aktivitelerin tespit edilmesinde kullanılabilir.

## Projede Anomali Tespiti

Projede ilk aşamada kural tabanlı tespit yöntemleri kullanılacaktır. Örneğin aynı IP adresinden kısa bir süre içerisinde çok sayıda başarısız giriş yapılması belirlenen bir kural üzerinden tespit edilebilir.

Daha sonraki aşamada ise normal kullanıcı davranışının incelenmesi ve normalden sapmaların tespit edilmesi planlanmaktadır.

Örneğin belirli bir kullanıcı için normalde düşük olan başarısız giriş sayısının kısa bir zaman içerisinde önemli ölçüde artması anomali olarak değerlendirilebilir.

## Kullanılabilecek Yöntemler

Projede anomali tespiti için iki farklı yaklaşım üzerinde durulmaktadır:

- **Kural tabanlı tespit:** Önceden belirlenen koşullara göre şüpheli
  olayların tespit edilmesi.
- **İstatistiksel anomali tespiti:** Normal davranıştan olan sapmaların
  istatistiksel yöntemlerle belirlenmesi.

İlerleyen aşamalarda uygun olması durumunda makine öğrenmesi tabanlı yöntemlerin de kullanılması planlanmaktadır.

## Projede Kullanımı

Anomali tespiti sonucunda belirlenen şüpheli olaylar daha sonra risk değerlendirmesi ve dashboard kısmında kullanılabilir.

Bu yöntemlerin sonuçlarının karşılaştırılması ile proje için hangi yaklaşımın daha uygun olduğu değerlendirilecektir.
