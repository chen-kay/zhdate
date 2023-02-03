class ZhModel:
    zh_year: str
    zh_month: str
    zh_day: str
    year_tiandi: str
    shengxiao: str

    def __str__(self):
        return f"{self.zh_year}{self.zh_month}{self.zh_day} {self.year_tiandi} ({self.shengxiao}年)"
