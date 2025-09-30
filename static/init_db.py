import sqlite3

DB = "quran.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

# ----- Surahs Table -----
cursor.execute("""
CREATE TABLE IF NOT EXISTS surahs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER UNIQUE,
    name TEXT,
    meaning TEXT,
    audio TEXT,
    reference TEXT
)
""")

# ----- Tips Table -----
cursor.execute("""
CREATE TABLE IF NOT EXISTS tips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
""")

# ----- Sample Data -----
surahs = surahs = [
    {"number": 1, "name": "Al-Fatiha", "meaning": "The opening","audio": "static/01-Al-Fatiha1.mp3", "reference": ""},
    {"number": 2, "name": "Al-Baqarah", "meaning": "The Cow", "audio": "static/02-Al-Baqara1.mp3", "reference": ""},
    {"number": 3, "name": "Aal-E-Imran", "meaning": "The Family of Imran", "audio": "static/03-Aal-E-Imran1.mp3", "reference": ""},
    {"number":4, "name":"An-Nisa", "meaning":"The Women", "audio":"static/04-An-Nisa1.mp3", "reference": ""},
    {"number":5, "name":"Al-Maidah", "meaning":"The Table Spread", "audio":"static/05-Al-Maeda1.mp3", "reference": ""},
    {"number":6, "name":"Al-An'am", "meaning":"The Cattle", "audio":"static/06-Al-Anaam1.mp3", "reference": ""},
    {"number":7, "name":"Al-A'raf", "meaning":"The Heights", "audio":"static/07-Al-Araf1.mp3", "reference": ""},
    {"number":8, "name":"Al-Anfal", "meaning":"The Spoils of War", "audio":"static/08-Al-Anfal1 (1).mp3", "reference": ""},
    {"number":9, "name":"At-Tawbah", "meaning":"The Repentance", "audio":"static/09-At-Tawba1.mp3", "reference": ""},
    {"number":10, "name":"Yunus", "meaning":"Prophet Yunus", "audio":"static/10-Yunus1.mp3", "reference": ""},
    {"number":11, "name":"Hud", "meaning":"Prophet Hud", "audio":"static/11-Hud1.mp3", "reference": ""},
    {"number":12, "name":"Yusuf", "meaning":"Prophet Yusuf", "audio":"static/12-Yusuf1.mp3", "reference": ""},
    {"number":13, "name":"Ar-Ra'd", "meaning":"The Thunder", "audio":"static/13-Ar-Rad1.mp3", "reference": ""},
    {"number":14, "name":"Ibrahim", "meaning":"Prophet Ibrahim", "audio":"tatic/14-Ibrahim1.mp3", "reference": ""},
    {"number":15, "name":"Al-Hijr", "meaning":"The Rocky Tract", "audio":"static/15-Al-Hijr1.mp3", "reference": ""},
    {"number":16, "name":"An-Nahl", "meaning":"The Bee", "audio":"static/16-An-Nahl1.mp3", "reference": ""},
    {"number":17, "name":"Al-Isra", "meaning":"The Night Journey", "audio":"static/17-Al-Isra1.mp3", "reference": ""},
    {"number":18, "name":"Al-Kahf", "meaning":"The Cave", "audio":"static/18-Al-Kahf1.mp3", "reference": ""},
    {"number":19, "name":"Maryam", "meaning":"Prophet Maryam", "audio":"static/19-Maryam1.mp3", "reference": ""},
    {"number":20, "name":"Ta-Ha", "meaning":"Prophet Musa", "audio":"static/20-Ta-Ha1.mp3.mp3", "reference": ""},
    {"number": 21, "name": "Al-Anbiya", "meaning": "The Prophets", "audio": "static/21-Al-Anbiya1.mp3", "reference": ""},
    {"number": 22, "name": "Al-Hajj", "meaning": "The Pilgrimage", "audio": "static/22-Al-Hajj1.mp3", "reference": ""},
    {"number": 23, "name": "Al-Mu'minun", "meaning": "The Believers", "audio": "static/23-Al-Mumenoon1.mp3", "reference": ""},
    {"number": 24, "name": "An-Nur", "meaning": "The Light", "audio": "static/24-An-Noor1.mp3", "reference": ""},
    {"number": 25, "name": "Al-Furqan", "meaning": "The Criterion", "audio": "static/25-Al-Furqan1.mp3", "reference": ""},
    {"number": 26, "name": "Ash-Shu'ara", "meaning": "The Poets", "audio": "static/26-Ash-Shuara1.mp3", "reference": ""},
    {"number": 27, "name": "An-Naml", "meaning": "The Ant", "audio": "static/27-An-Namal.mp3", "reference": ""},
    {"number": 28, "name": "Al-Qasas", "meaning": "The Stories", "audio": "static/28-Al-Qasas1.mp3", "reference": ""},
    {"number": 29, "name": "Al-Ankabut", "meaning": "The Spider", "audio": "static/29-Al-Ankaboot1.mp3", "reference": ""},
    {"number": 30, "name": "Ar-Rum", "meaning": "The Romans", "audio": "static/30-Ar-Room1.mp3", "reference": ""},
    {"number": 31, "name": "Luqman", "meaning": "Luqman", "audio": "static/31-Luqman1.mp3.mp3", "reference": ""}, 
    {"number": 32, "name": "As-Sajda", "meaning": "The Prostration", "audio": "static/32-As-Sajda1.mp3", "reference": ""},
    {"number": 33, "name": "Al-Ahzab", "meaning": "The Combined Forces", "audio": "static/33-Al-Ahzab1.mp3", "reference": ""},
    {"number": 34, "name": "Saba", "meaning": "Sheba", "audio": "static/34-Saba1.mp3", "reference": ""},
    {"number": 35, "name": "Fatir", "meaning": "The Originator", "audio": "static/35-Fatir1.mp3", "reference": ""},
    {"number": 36, "name": "Ya-Sin", "meaning": "Ya-Sin", "audio": "static/36-Ya-Seen1.mp3", "reference": ""},
    {"number": 37, "name": "As-Saffat", "meaning": "Those Who Set The Ranks", "audio": "static/37-As-Saaffat1.mp3.mp3", "reference": ""},
    {"number": 38, "name": "Sad", "meaning": "Sad", "audio": "static/38-Sad1.mp3.", "reference": ""},
    {"number": 39, "name": "Az-Zumar", "meaning": "The Groups", "audio": "static/39-Az-Zumar1.mp3.", "reference": ""},
    {"number": 40, "name": "Ghafir", "meaning": "The Forgiver", "audio": "static/40-Al-Ghafir1.mp3.", "reference": ""},
    {"number": 41, "name": "Fussilat", "meaning": "Explained in Detail", "audio": "static/41-Fussilat1.mp3", "reference": ""},
    {"number": 42, "name": "Ash-Shura", "meaning": "The Consultation", "audio": "static/42-Ash-Shura1.mp3", "reference": ""},
    {"number": 43, "name": "Az-Zukhruf", "meaning": "Ornaments of Gold", "audio": "static/43-Az-Zukhruf1.mp3", "reference": ""},
    {"number": 44, "name": "Ad-Dukhan", "meaning": "The Smoke", "audio": "static/44-Ad-Dukhan1.mp3", "reference": ""},
    {"number": 45, "name": "Al-Jathiya", "meaning": "The Crouching", "audio": "static/45-Al-Jathiya1.mp3", "reference": ""},
    {"number": 46, "name": "Al-Ahqaf", "meaning": "The Wind-Curved Sandhills", "audio": "static/46-Al-Ahqaf1.mp3.mp3", "reference": ""},
    {"number": 47, "name": "Muhammad", "meaning": "Prophet Muhammad", "audio": "static/47-Muhammad1.mp3.", "reference": ""},
    {"number": 48, "name": "Al-Fath", "meaning": "The Victory", "audio": "48-Al-Fath1.mp3.mp3", "reference": ""},
    {"number": 49, "name": "Al-Hujurat", "meaning": "The Rooms", "audio": "static/49-Al-Hujraat1.mp3.", "reference": ""},
    {"number": 50, "name": "Qaf", "meaning": "Qaf", "audio": "static/50-Qaaf.mp3.", "reference": ""},
    {"number": 51, "name": "Adh-Dhariyat", "meaning": "The Winnowing Winds", "audio": "static/51-Adh-Dhariyat1.mp3.mp3", "reference": ""},
    {"number": 52, "name": "At-Tur", "meaning": "The Mount", "audio": "static/52-At-Tur1.mp3", "reference": ""},
    {"number": 53, "name": "An-Najm", "meaning": "The Star", "audio": "static/53-An-Najam.mp3", "reference": ""},
    {"number": 54, "name": "Al-Qamar", "meaning": "The Moon", "audio": "static/54-Al-Qamar1.mp3", "reference": ""},
    {"number": 55, "name": "Ar-Rahman", "meaning": "The Beneficent", "audio": "static/55-Ar-Rahman1.mp3", "reference": ""},
    {"number": 56, "name": "Al-Waqia", "meaning": "The Inevitable", "audio": "static/56-Al-Waqiya.mp3.mp3", "reference": ""},
    {"number": 57, "name": "Al-Hadid", "meaning": "The Iron", "audio": "static/57-Al-Hadeed.mp3.mp3", "reference": ""},
    {"number": 58, "name": "Al-Mujadila", "meaning": "The Pleading Woman", "audio": "static/58-Al-Mujadila1.mp3.mp3", "reference": ""}, 
    {"number": 59, "name": "Al-Hashr", "meaning": "The Exile", "audio": "static/59-Al-Hashr1.mp3.mp3", "reference": ""},
    {"number": 60, "name": "Al-Mumtahina", "meaning": "She that is to be examined", "60-Al-Mumtahina1.mp3 ": ""},
    {"number": 61, "name": "As-Saff", "meaning": "The Ranks", "audio": "static/61-As-Saff1.mp3", "reference": ""},
    {"number": 62, "name": "Al-Jumu'a", "meaning": "The Congregation", "audio": "static/62-Al-Jumua1.mp3", "reference": ""},
    {"number": 63, "name": "Al-Munafiqun", "meaning": "The Hypocrites", "audio": "static/63-Al-Munafiqoon1.mp3", "reference": ""},
    {"number": 64, "name": "At-Taghabun", "meaning": "The Mutual Disillusion", "audio": "static/64-At-Taghabun1.mp3.mp3", "reference": ""},
    {"number": 65, "name": "At-Talaq", "meaning": "The Divorce", "audio": "static/65-At-Talaq1.mp3/065.mp3", "reference": ""},
    {"number": 66, "name": "At-Tahrim", "meaning": "The Prohibition", "audio": "static/66-At-Tahrim1.mp3", "reference": ""},
    {"number": 67, "name": "Al-Mulk", "meaning": "The Sovereignty", "audio": "static/67-Al-Mulk1.mp3", "reference": ""},
    {"number": 68, "name": "Al-Qalam", "meaning": "The Pen", "audio": "static/68-Al-Qalam1.mp3", "reference": ""},
    {"number": 69, "name": "Al-Haqqah", "meaning": "The Reality", "audio": "static/69-Al-Haaqqa1.mp3", "reference": ""},
    {"number": 70, "name": "Al-Ma'arij", "meaning": "The Ascending Stairways", "audio": "static/70-Al-Maarij1.mp3.", "reference": ""},
    {"number": 71, "name": "Nuh", "meaning": "Prophet Nuh", "audio": "static/71-Nooh1.mp3.mp3", "reference": ""},
    {"number": 72, "name": "Al-Jinn", "meaning": "The Jinn", "audio": "static/72-Al-Jinn1.mp3", "reference": ""},
    {"number": 73, "name": "Al-Muzzammil", "meaning": "The Enshrouded One", "audio": "static/73-Al-Muzzammil1.mp3", "reference": ""},
    {"number": 74, "name": "Al-Muddathir", "meaning": "The Cloaked One", "audio": "static/74-Al-Muddaththir1.mp3", "reference": ""},
    {"number": 75, "name": "Al-Qiyama", "meaning": "The Resurrection", "audio": "static/75-Al-Qiyamah.mp3", "reference": ""},
   {"number": 76, "name": "Al-Insan", "meaning": "Man", "audio":"static/76-Al-Insan1.mp3","reference": ""},
    {"number": 77, "name": "Al-Mursalat", "meaning": "The Emissaries", "audio": "static/77-Al-Mursalat1.mp3", "reference": ""},
    {"number": 78, "name": "An-Naba", "meaning": "The Tidings", "audio": "static/78-An-Naba1.mp3", "reference": ""},
    {"number": 79, "name": "An-Nazi'at", "meaning": "Those who drag forth", "audio": "static/79-An-Naziat1.mp3", "reference": ""},
    {"number": 80, "name": "Abasa", "meaning": "He frowned", "audio": "static/80-Abasa1.mp3", "reference": ""},
    {"number": 81, "name": "At-Takwir", "meaning": "The Overthrowing", "audio": "static/81-At-Takwir1.mp3", "reference": ""},
    {"number": 82, "name": "Al-Infitar", "meaning": "The Cleaving", "audio": "static/82-Al-Infitar1.mp3", "reference": ""},
    {"number": 83, "name": "Al-Mutaffifin", "meaning": "Defrauding", "audio": "static/83-Al-Mutaffifin1.mp3", "reference": ""},
    {"number": 84, "name": "Al-Inshiqaq", "meaning": "The Splitting Open", "audio": "static/84-Al-Inshiqaq1.mp3", "reference": ""},
    {"number": 85, "name": "Al-Buruj", "meaning": "The Mansions of the Stars", "audio": "static/85-Al-Burooj1.mp3", "reference": ""},
    {"number": 86, "name": "At-Tariq", "meaning": "The Morning Star", "audio": "static/86-At-Tariq1.mp3", "reference": ""},
    {"number": 87, "name": "Al-A'la", "meaning": "The Most High", "audio": "static/87-Al-Ala1.mp3", "reference": ""},
    {"number": 88, "name": "Al-Ghashiya", "meaning": "The Overwhelming", "audio": "static/88-Al-Ghashiya1.mp3", "reference": ""},
    {"number": 89, "name": "Al-Fajr", "meaning": "The Dawn", "audio": "static/89-Al-Fajr1.mp3", "reference": ""},
    {"number": 90, "name": "Al-Balad", "meaning": "The City", "audio": "static/90-Al-Balad1.mp3", "reference": ""},
    {"number": 91, "name": "Ash-Shams", "meaning": "The Sun", "audio": "static/91-Ash-Shams1.mp3", "reference": ""},
    {"number": 92, "name": "Al-Lail", "meaning": "The Night", "audio": "static/92-Al-Lail1.mp3", "reference": ""},
    {"number": 93, "name": "Ad-Duha", "meaning": "The Morning Hours", "audio": "static/93-Ad-Dhuha1 (1).mp3", "reference": ""},
    {"number": 94, "name": "Ash-Sharh", "meaning": "The Relief", "audio": "static/94-Al-Inshirah1.mp3", "reference": ""},
    {"number": 95, "name": "At-Tin", "meaning": "The Fig", "audio": "static/95-At-Teen.mp3", "reference": ""},
    {"number": 96, "name": "Al-Alaq", "meaning": "The Clot", "audio": "static/96-Al-Alaq1.mp3","reference": ""},
    {"number": 97, "name": "Al-Qadr", "meaning": "The Power", "audio": "static/97-Al-Qadr1.mp3", "reference": ""},
    {"number": 98, "name": "Al-Bayyina", "meaning": "The Clear Proof", "audio": "static/98-Al-Bayyina1.mp3", "reference": ""},
    {"number": 99, "name": "Az-Zalzala", "meaning": "The Earthquake", "audio": "static/99-Az-Zalzala1.mp3", "reference": ""},
    {"number": 100, "name": "Al-Adiyat", "meaning": "The Courser", "audio": "static/100-Al-Adiyat1.mp3", "reference": ""},
    {"number": 101, "name": "Al-Qari'a", "meaning": "The Striking Hour", "audio": "static/101-Al-Qariyah.mp3", "reference": ""},
    {"number": 102, "name": "At-Takathur", "meaning": "The Rivalry in world increase", "audio": "static/102-At-Takathur1.mp3", "reference": ""},
    {"number": 103, "name": "Al-Asr", "meaning": "The Declining Day", "audio": "static/103-Al-Asr1.mp3", "reference": ""},
    {"number": 104, "name": "Al-Humaza", "meaning": "The Traducer", "audio": "static/104-Al-Humaza1.mp3", "reference": ""},
    {"number": 105, "name": "Al-Fil", "meaning": "The Elephant", "audio": "static/105-Al-Feel.mp3", "reference": ""},
    {"number": 106, "name": "Quraish", "meaning": "Quraish", "audio": "static/106-Quraish1.mp3", "reference": ""},
    {"number": 107, "name": "Al-Ma'un", "meaning": "The Small Kindnesses", "audio": "static/107-Al-Maun1.mp3", "reference": ""},
    {"number": 108, "name": "Al-Kawthar", "meaning": "The Abundance", "audio": "static/108-Al-Kauther1.mp3", "reference": ""},
    {"number": 109, "name": "Al-Kafirun", "meaning": "The Disbelievers", "audio": "static/109-Al-Kafiroon1.mp3", "reference": ""},
    {"number": 110, "name": "An-Nasr", "meaning": "The Divine Support", "audio": "static/110-An-Nasr1.mp3", "reference": ""},
    {"number": 111, "name": "Al-Masad", "meaning": "The Palm Fiber", "audio": "static/111-Al-Masadd1.mp3", "reference": ""},
    {"number": 112, "name": "Al-Ikhlas", "meaning": "The Sincerity", "audio": "static/112-Al-Ikhlas1.mp3", "reference": ""},
    {"number": 113, "name": "Al-Falaq", "meaning": "The Daybreak", "audio": "static/113-Al-Falaq1.mp3", "reference": ""},
    {"number": 114, "name": "An-Nas", "meaning": "Mankind", "audio": "static/114-An-Nas1 (1).mp3", "reference": ""}
]


tips = [
    "Set a clear intention — Read with the purpose of understanding and applying, not just finishing pages.",
    "Start with dua — Ask for guidance and understanding before you begin.",
    "Make a small daily routine — Even 10–15 minutes every day is better than long, irregular sessions.",
    "Read with translation & tafsir — Learn the meanings; context matters.",
    "Improve tajweed gradually — Focus on correct pronunciation; small improvements add up.",
    "Listen to good reciters — Repeat after them to improve rhythm and articulation.",
    "Memorize in small portions — Short daily memorization + frequent review is most effective.",
    "Keep a notes section — Write down verses that inspire you and practical lessons."
]

cursor.executemany("INSERT OR IGNORE INTO surahs (number, name, meaning, audio, reference) VALUES (?,?,?,?,?)", surahs)
cursor.executemany("INSERT INTO tips (content) VALUES (?)", [(t,) for t in tips])

conn.commit()
conn.close()
print("Database initialized successfully!")
