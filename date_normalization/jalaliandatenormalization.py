import re
from .datestandard import CNLPDateManager


class JalalianDateNormalization:

    # Patterns to find jalalian dates in which the names of the months are used
    _jalalian_words_dates_regs = [
        r'\b(\d{4})\s(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s(\d{1,2})\b',
        r'\b(\d{4})\s(\d{1,2})\s(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\b',
        r'\b(\d{1,2})\s(\d{4})\s(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\b',
        r'\b(\d{1,2})\s(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s(\d{4})\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s(\d{4})\s(\d{1,2})\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s(\d{1,2})\s(\d{4})\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s(\d{1,2})\b',
        r'\b(\d{1,2})\s(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s(\d{3,4})\b',
        r'\b(\d{3,4})\s(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s?ماه\s?(\d{3,4})\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s?سال\s?(\d{3,4})\b',
        r'\b(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)\s?ماه\s?سال\s?(\d{3,4})\b',
    ]

    # Patterns to find jalalian dates that refer to a date numerically inside them
    _jalalian_numeric_dates_regs = [
        r'\b(\d{4})[-/](1[0-2])[-/](3[0-1])\b',
        r'\b(\d{4})[-/](1[0-2])[-/]([1-2][0-9])\b',
        r'\b(\d{4})[-/](1[0-2])[-/](0[1-9])\b',
        r'\b(\d{4})[-/](1[0-2])[-/]([1-9])\b',
        r'\b(\d{4})[-/](0[1-9])[-/](3[0-1])\b',
        r'\b(\d{4})[-/](0[1-9])[-/]([1-2][0-9])\b',
        r'\b(\d{4})[-/](0[1-9])[-/](0[1-9])\b',
        r'\b(\d{4})[-/](0[1-9])[-/]([1-9])\b',
        r'\b(\d{4})[-/]([1-9])[-/](3[0-1])\b',
        r'\b(\d{4})[-/]([1-9])[-/]([1-2][0-9])\b',
        r'\b(\d{4})[-/]([1-9])[-/](0[1-9])\b',
        r'\b(\d{4})[-/]([1-9])[-/]([1-9])\b',
        r'\b(\d{4})[-/]([1-9])[-/](1[0-2])\b',
        r'\b(\d{4})[-/](0[1-9])[-/](1[0-9])\b',
        r'\b(\d{4})[-/]([12][0-9])[-/]([1-9])\b',
        r'\b(\d{4})[-/]([12][0-9])[-/](0[1-9])\b',
        r'\b(\d{4})[-/]([12][0-9])[-/](1[0-2])\b',
        r'\b(\d{4})[-/](3[0-9])[-/]([1-9])\b',
        r'\b(\d{4})[-/](3[0-9])[-/](0[1-9])\b',
        r'\b(\d{4})[-/](3[0-9])[-/](1[0-2])\b',
        r'\b(1[0-2])[-/](3[0-1])[-/](\d{4})\b',
        r'\b(1[0-2])[-/]([1-2][0-9])[-/](\d{4})\b',
        r'\b(1[0-2])[-/](0[1-9])[-/](\d{4})\b',
        r'\b(1[0-2])[-/]([1-9])[-/](\d{4})\b',
        r'\b(0[1-9])[-/](3[0-1])[-/](\d{4})\b',
        r'\b(0[1-9])[-/]([1-2][0-9])[-/](\d{4})\b',
        r'\b(0[1-9])[-/](0[1-9])[-/](\d{4})\b',
        r'\b(0[1-9])[-/]([1-9])[-/](\d{4})\b',
        r'\b([1-9])[-/](3[0-1])[-/](\d{4})\b',
        r'\b([1-9])[-/]([1-2][0-9])[-/](\d{4})\b',
        r'\b([1-9])[-/](0[1-9])[-/](\d{4})\b',
        r'\b([1-9])[-/]([1-9])[-/](\d{4})\b',
        r'\b([1-9])[-/](1[0-2])[-/](\d{4})\b',
        r'\b(0[1-9])[-/](1[0-9])[-/](\d{4})\b',
        r'\b([12][0-9])[-/]([1-9])[-/](\d{4})\b',
        r'\b([12][0-9])[-/](0[1-9])[-/](\d{4})\b',
        r'\b([12][0-9])[-/](1[0-2])[-/](\d{4})\b',
        r'\b(3[0-9])[-/]([1-9])[-/](\d{4})\b',
        r'\b(3[0-9])[-/](0[1-9])[-/](\d{4})\b',
        r'\b(3[0-9])[-/](1[0-2])[-/](\d{4})\b',
        r'\b(3[0-1])[-/](\d{4})[-/](1[0-2])\b',
        r'\b([1-9])[-/](\d{4})[-/]([1-9])\b',
        r'\b(0[1-9])[-/](\d{4})[-/]([1-9])\b',
        r'\b(1[0-2])[-/](\d{4})[-/]([1-9])\b',
        r'\b([1-9])[-/](\d{4})[-/](0[1-9])\b',
        r'\b(0[1-9])[-/](\d{4})[-/](0[1-9])\b',
        r'\b(1[0-2])[-/](\d{4})[-/](0[1-9])\b',
        r'\b([1-9])[-/](\d{4})[-/]([12][0-9])\b',
        r'\b(0[1-9])[-/](\d{4})[-/]([12][0-9])\b',
        r'\b(1[0-2])[-/](\d{4})[-/]([12][0-9])\b',
        r'\b([1-9])[-/](\d{4})[-/](3[0-1])\b',
        r'\b(0[1-9])[-/](\d{4})[-/](3[0-1])\b',
        r'\b(1[0-2])[-/](\d{4})[-/](3[0-1])\b',
        r'\b([1-9])[-/](\d{4})[-/]([1-9])\b',
        r'\b([1-9])[-/](\d{4})[-/](0[1-9])\b',
        r'\b([1-9])[-/](\d{4})[-/](1[0-2])\b',
        r'\b(0[1-9])[-/](\d{4})[-/]([1-9])\b',
        r'\b(0[1-9])[-/](\d{4})[-/](0[1-9])\b',
        r'\b(0[1-9])[-/](\d{4})[-/](1[0-2])\b',
        r'\b([12][0-9])[-/](\d{4})[-/]([1-9])\b',
        r'\b([12][0-9])[-/](\d{4})[-/](0[1-9])\b',
        r'\b([12][0-9])[-/](\d{4})[-/](1[0-2])\b',
        r'\b(3[0-1])[-/](\d{4})[-/]([1-9])\b',
        r'\b(3[0-1])[-/](\d{4})[-/](0[1-9])\b',
        r'\b\s([1-9])[-/]([1-9])\s\b',
        r'\b\s([1-9])[-/](0[1-9])\s\b',
        r'\b\s([1-9])[-/]([1-2][0-9])\s\b',
        r'\b\s([1-9])[-/](3[0-1])\s\b',
        r'\b\s(0[1-9])[-/]([1-9])\s\b',
        r'\b\s(0[1-9])[-/](0[1-9])\s\b',
        r'\b\s(0[1-9])[-/]([1-2][0-9])\s\b',
        r'\b\s(0[1-9])[-/](3[0-1])\s\b',
        r'\b\s(1[0-2])[-/]([1-9])\s\b',
        r'\b\s(1[0-2])[-/](0[1-9])\s\b',
        r'\b\s(1[0-2])[-/]([1-2][0-9])\s\b',
        r'\b\s(1[0-2])[-/](3[0-1])\s\b',
        r'\b\s([1-9])[-/]([1-9])\s\b',
        r'\b\s([1-9])[-/](0[1-9])\s\b',
        r'\b\s([1-9])[-/](1[0-2])\s\b',
        r'\b\s(0[1-9])[-/]([1-9])\s\b',
        r'\b\s(0[1-9])[-/](0[1-9])\s\b',
        r'\b\s(0[1-9])[-/](1[0-2])\s\b',
        r'\b\s([1-2][0-9])[-/]([1-9])\s\b',
        r'\b\s([1-2][0-9])[-/](0[1-9])\s\b',
        r'\b\s([1-2][0-9])[-/](1[0-2])\s\b',
        r'\b\s(3[0-1])[-/]([1-9])\s\b',
        r'\b\s(3[0-1])[-/](0[1-9])\s\b',
        r'\b\s(3[0-1])[-/](1[0-2])\s\b',
    ]

    # In this method, we search for jalalian dates by using the patterns of finding dates in which the name of the
    # month is mentioned, and after finding them, we convert them into standard Gregorian dates.
    def j_normalization_dates(self, text: str) -> str:
        date_manager = CNLPDateManager()
        for reg in self._jalalian_words_dates_regs:
            found_items = list(re.finditer(reg, text))
            for found_item in found_items:
                original = found_item.group(0)
                text = text.replace(original, date_manager.convert_str_jalali_to_standard_date(original))

        return self._normalization_numeric_dates(text=text)

    # In this method, we search for jalalian dates by using the patterns of finding dates that are only indicated by
    # numbers, and after finding them, we convert them into standard Gregorian dates.
    def _normalization_numeric_dates(self, text: str) -> str:
        date_manager = CNLPDateManager()
        for reg in self._jalalian_numeric_dates_regs:
            found_items = list(re.finditer(reg, text))
            for found_item in found_items:
                original = found_item.group(0)
                text = text.replace(original, date_manager.convert_fmt_jalali_to_standard_date(original))

        return text
