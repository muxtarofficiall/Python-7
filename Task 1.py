class NumberList:
    def __init__(self):
        self.mylist = []  # Boş bir siyahı yaradırıq

    def add_numbers(self, numbers):
        """Rəqəmləri siyahıya əlavə et."""
        self.mylist.extend(numbers)  # Verilən siyahını mövcud siyahıya əlavə edirik

    def find_target_sum(self, target):
        """Verilən hədəf üçün iki rəqəmin cəmini tap."""
        num_index = {}  # Rəqəmləri və indekslərini saxlamaq üçün bir lüğət

        # Siyahı üzərində keçərək cütləri tapırıq
        for index, num in enumerate(self.mylist):
            complement = target - num  # Hədəf üçün lazım olan tamamlayıcı rəqəm
            if complement in num_index:  # Əgər tamamlayıcı rəqəm artıq mövcuddursa
                return [num_index[complement], index]  # Tamamlayıcı və cari rəqəmin indekslərini qaytar
            num_index[num] = index  # Əks təqdirdə cari rəqəmi və indeksini lüğətə əlavə et

        return -1  # Əgər cüt tapılmazsa, -1 qaytar
