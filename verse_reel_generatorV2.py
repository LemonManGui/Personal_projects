import sqlite3 as SQL

path_to_db = '/Users/gui/Desktop/RTDE/Jezus/bible_verses.db'


def get_verse():
    global path_to_db
    db = SQL.connect(path_to_db)
    cur = db.cursor()

    random_verse_query = '''
        SELECT book, chapter, verse, text
        FROM Verses
        ORDER BY RANDOM()
        LIMIT 1
        '''
    
    cur.execute(random_verse_query)
    res = cur.fetchone()
    book, chapter, verse, text = res

    cur.close()
    db.close()

    print(f"\n{book} {chapter}:{verse} - {text}")

get_verse()

def get_video():
    global path_to_db
    db = SQL.connect(path_to_db)
    cur = db.cursor()

    random_video_query = '''
        SELECT File_name, File_path
        FROM background_videos
        ORDER BY RANDOM()
        LIMIT 1
        '''
    cur.execute(random_video_query)
    res = cur.fetchall()

    cur.close()
    db.close()

    print(res)

def insert_verse():
    global path_to_db

    db = SQL.connect(path_to_db)
    cur = db.cursor()

    book = str(input('Give book: '))
    chapter = str(input('Give chapter: '))
    verse = str(input('Give verse: '))
    text = str(input('Give text: '))

    while True:
        try:
            print(f"\n{book} {chapter}:{verse} - {text}\n")
            print(f"Save this verse in DataBase? (Yes/No)")
            cmd = (str(input("Awnser: ")))
        
            if cmd.lower() == 'yes':
                insert_verse_query = '''
                    INSERT INTO Verses (book, chapter, verse, text)
                    VALUES (?, ?, ?, ?);
                '''
                cur.execute(insert_verse_query, (book, chapter, verse, text))
                db.commit()

                print('Verse succesfully saved to DataBase!')
                break

            elif cmd.lower() == 'no':
                print('Verse NOT saved to DataBase')
                break

            else:
                print('!!! Invalid choice !!! (Please enter Yes or No)')

        except Exception as e:
            print(f'ERROR: {e}')

    cur.close()
    db.close()

insert_verse()
