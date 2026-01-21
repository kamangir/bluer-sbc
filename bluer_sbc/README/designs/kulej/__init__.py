from bluer_objects import README

from bluer_sbc.README.designs.consts import assets2

description = {
    "short": {
        "fa": "کوله‌ج — شاهدانِ بی‌نام",
        "en": "kulej — silent witnesses",
    },
    "long": {
        "fa": """
کوله‌ج یک دستگاه کوچک مبتنی بر رزبری‌پای است که با باتری لیتیومی در کوله‌پشتی حمل می‌شود.
این دستگاه بدون نیاز به تماس انسانی، از طریق بلوتوث حضور کوله‌ج‌های دیگر را تشخیص می‌دهد و هنگام نزدیک شدن، عکس‌ها و ویدئوهای ذخیره‌شده را با آن‌ها همگام می‌کند.

کاربر با اتصال گوشی به وای‌فای کوله‌ج، عکس و ویدئو می‌گیرد؛ فایل‌ها فوراً به کوله‌ج منتقل و از گوشی حذف می‌شوند.
کوله‌ج‌ها به‌صورت ناشناس حافظه‌ی جمعی می‌سازند.

هر از گاهی، یک حامل کوله‌ج دستگاه را به اینترنت خارج از مرز متصل می‌کند تا داده‌ها به سرورهای امن ارسال شوند و برای حفاظت از حقوق بشر در اختیار رسانه‌ها و نهادهای بین‌المللی قرار گیرند.

کوله‌ج همان‌طور تلفظ می‌شود که «کوله» در فارسی.
""",
        "en": """
Kulej is a Raspberry-Pi-based device powered by a Li-Po battery and carried in a backpack.
It operates without human coordination: discovering nearby Kulej devices via BLE and synchronizing photos and videos directly over Wi-Fi when they meet.

A companion smartphone app connects to Kulej's hotspot, uploads newly captured media instantly, and deletes it from the phone.
Over time, Kulej carriers form an anonymous, shared archive through peer-to-peer syncing.

Occasionally, a carrier travels to a border or safe location and connects Kulej to the internet, allowing the data to be transmitted abroad to support international media and human-rights organizations.

Kulej is pronounced “kuleh,” like the Persian word for backpack.
""",
    },
}

image_template = assets2 + "kulej/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "kulej ⛰️",
            "marquee": image_template.format("20260118_142743.jpg"),
            "url": "./bluer_sbc/docs/kulej",
        }
    ]
)
