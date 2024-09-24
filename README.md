# کتابخانه نرمال سازی تاریخ در زبان فارسی

این کتابخانه بخشی از پروژه NLP است که متنی فارسی که به آن داده می‌شود را آنالیز می‌کند و تمامی تاریخ‌های شمسی و میلادی را استخراج کرده و تبدیل به یک فرمت استاندارد در تاریخ میلادی می‌کند.

## نصب

برای نصب این کتابخانه کافیه از دستور زیر استفاده کنید: 

```bash
pip install nlp-date-normalization-snd==0.1.1
```

## نحوه پیاده‌سازی

برای استفاده از کتابخانه، می‌توانید از کد نمونه زیر استفاده کنید:

```python
# -*- coding: utf-8 -*-
from date_normalization.datenormalization import DateNormalization

def checking():
    text = 'در تاریخ ۲۸ اسفند ۱۳۹۸، جلسه‌ای مهم برای بررسی پیشرفت‌های سالانه برگزار شد. سپس، در تاریخ ۵ فوریه ۲۰۲۰، گزارشی درباره پروژه‌های در حال انجام منتشر شد. در تاریخ ۱۵ مارس ۲۰۲۱، تیم تحقیقاتی نتایج جدیدی را اعلام کرد. همچنین، در تاریخ ۱۷ اردیبهشت ۱۴۰۰، سمیناری درباره فناوری‌های نوین برگزار شد که شامل سخنرانی‌های مفصلی بود. برای برنامه‌ریزی جلسات آینده، به تاریخ‌های زیر توجه کنید: ۳۰ مرداد ۱۴۰۱، ۲۰ سپتامبر ۲۰۲۲ و ۱۰ دسامبر ۲۰۲۲. در تاریخ ۱۲ ژانویه ۲۰۲۳، تحلیل‌های جدیدی درباره روندهای جاری ارائه شد. همچنین، در تاریخ ۲۵ تیر ۱۴۰۲، گزارشی نهایی در مورد پیشرفت پروژه‌ها منتشر شد که به طور مفصل به بررسی جزئیات پرداخت.'
    dn = DateNormalization()
    print(dn.normalization_text(text))
```