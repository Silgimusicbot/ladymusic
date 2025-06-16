HELP_1 = """<b><u>Admin Komutları:</b></u>

Komutların başına <b>ç</b> ekleyin veya komutları kanalda kullanmak için komutların başına <b>ç</b> kullanın.

/pause - Şu anda oynatılan yayını duraklatın.

/resume - Duraklatılmış bir yayını devam ettirin.

/skip - Şu anda oynatılan yayını atlayın ve bir sonraki parçayı oynatmaya başlayın.

/end veya /stop - Eklenen tüm tekrarları kaldırın ve şu anda oynatılan yayını durdurun.

/player - Etkileşimli oynatıcı panelini alın.

/queue - Eklenen parçaların listesini gösterin.

"""

HELP_2 = """<b><u>Auth Kullanıcıları:</b></u>

Yetkili kullanıcılar, sohbette yönetici haklarına sahip olmadan botta yönetici hakları elde edebilir.

/auth [kullanıcı adı/kullanıcı_kimliği] - Botun yetki listesine bir kullanıcı ekle.

/unauth [kullanıcı adı/kullanıcı_kimliği] - Yetkili kullanıcıları yetki listesinden kaldır.

/authusers - Grup için yetkili kullanıcıların listesini göster.
"""

HELP_3 = """<u><b>Broadcast Özelliği:</b></u> [yalnızca sudo kullanıcıları için]

/broadcast [mesaj veya mesaja yanıt] - Mesajınızı botun sunucu gruplarına yayınlayın.

<u>Yayın modları:</u>
<b>-pin</b> - Yayınladığınız mesajı sunucu gruplarına sabitleyin.
<b>-pinloud</b> - Yayınladığınız mesajı sunucu gruplarına sabitleyin ve üyelere bildirim gönderin.
<b>-user</b> - Mesajınızı botunuzu başlatan kullanıcılara yayınlayın.
<b>-assistant</b> - Mesajınızı botun asistan hesabından yayınlayın.
<b>-nobot</b> - Botu mesajı yayınlamaya zorlamayın.

<b>Örnek:</b> <code>/broadcast -user -assistant -pin Merhaba.</code>
"""

HELP_4 = """<u><b>Sohbet Kara Listesi Özelliği:</b></u> [yalnızca sudo kullanıcıları için]

Değerli botumuzu kullanmadan önce botumuzu şüpheli sohbetlerle sınırlayın.

/blacklistchat [chat ID] - Botun bu sohbeti kullanmasını sınırlayın.
/whitelistchat [chat ID] - Kara listeye alınmış bir sohbeti beyaz listeye alın.
/blacklistedchat - Kara listeye alınmış sohbetlerin bir listesini gösterir.
"""

HELP_5 = """<u><b>Kullanıcıların Banlanması:</b></u> [yalnızca sudo kullanıcıları için]

Kara listeye alınmış kullanıcıları izleyin, böylece bot komutlarını kullanamazlar.

/block [kullanıcı adı veya kullanıcı kimliği] - Bir kullanıcıyı botumuzdan yasaklayın.

/unblock [kullanıcı adı veya kullanıcı kimliği] - Engellenen bir kullanıcının engellemesini kaldırın.

/blockedusers - Engellenen kullanıcıların listesini gösterir.
"""

HELP_6 = """"\<u>\<b>Komutların Listi:</b></u>

Ses/video oynatma kanalında oynatabilirsiniz.

/cplay - İstenen sesin ses oynatımını başlatır.

/cvplay - İstenen video çalışmalarının video oynatımını başlatır.

/cplayforce veya /cvplayforce - Devam eden bir ses/video oynatmayı durdurur ve istenen çalışmaların oynatımını başlatır.

/channelplay [Sohbet kullanıcı adı veya kimliği] veya [devre dışı] - Kanalı gruba ekler ve gönderilen komuta göre çalışmaların oynatımını başlatır.""""

HELP_7 = """<u><b>Qlobal Ban Özelliği:</b></u> [yalnızca sudo kullanıcıları için]

- `/gban` [kullanıcı adı veya kimlik] - Kullanıcıyı tüm sohbetlerden yasaklar ve botu kullanmasını engeller.
- `/ungban` [kullanıcı adı veya kimlik] - Küresel olarak yasaklanmış bir kullanıcının yasağını kaldırır.
- `/gbannedusers` - Küresel olarak yasaklanmış kullanıcıların bir listesini listeler.
"""

HELP_8 = """<b><u>Döngü Yayınla:</b></u>

<b>Mevcut akış aşağıdaki komutla döngüye alınacaktır:</b>

- `/loop [enable/disable]` - Mevcut akışın döngüye alınmasını etkinleştirir veya devre dışı bırakır.
- `/loop [1, 2, 3, ...]` - Belirtilen sayıda döngüye izin verir.
"""

HELP_9 = """<u><b>Bakım Modu:</b></u> [yalnızca sudo-lar için]

- `/logs` - Botun aktivitelerinin kurallarını alın.

- `/logger [enable/disable]` - Bot, botta gerçekleşen aktiviteleri günlüğe kaydeder.

- `/maintenance [enable/disable]` - Botunuzun bakım modunu etkinleştirin veya devre dışı bırakın.
"""

HELP_10 = """<b><u>Ping ve Status:</b></u>

- `/start` - Müzik botunu başlat.
- `/help` - Komutların açıklamalarının bulunduğu Yardım menüsünü al.

- `/ping` - Botun ping'ini ve sistem durumunu gösterir.

- `/stats` - Botun genel durumunu gösterir.
"""

HELP_11 = """<u><b>Play Komutları:</b></u>

- `v` - Video oynatmayı durdur.
- `force` - Zorla oynatmayı durdur.

- `/play` veya `/vplay` - İstenen parçayı videoya oynatır.

- `/playforce` veya `/vplayforce` - Şu anda oynatılan hızı durdurur ve istenen parçayı oynatır.
"""

HELP_12 = """<b><u>Karışık Oynatma:</b></u>

- `/shuffle` - Çalma listesini karıştırır.
- `/queue` - Karıştırılmış çalma listesini gösterir.
"""

HELP_13 = """<b><u>Streame Geçiş:</b></u>

- `/seek [saniye cinsinden süre]` - Akışı belirtilen süreye taşır.
- `/seekback [saniye cinsinden süre]` - Akışı geri taşır.
"""

HELP_14 = """<b><u>Mahnı indirme:</b></u>

- `/song [şarkı adı/yt URL]` - YouTube'dan herhangi bir parçayı MP3 veya MP4 formatında indirin.
"""

HELP_15 = """<b><u>Hız Komutları</b></u>

- `/speed` veya `/playback` - Gruptaki ses bozulmasının hızını ayarlamak için.
- `/cspeed` veya `/cplayback` - Kanaldaki ses bozulmasının hızını ayarlamak için.
"""

HELP_16 = """<b><u>Şarkı Sözleri Komutları</b></u>

`/lyrics [şarkı adı]` - İstenilen şarkının sözlerini ara ve sonuçları gönder.
"""
