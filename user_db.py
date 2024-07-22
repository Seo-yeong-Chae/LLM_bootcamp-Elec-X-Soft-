import sqlite3
# con = sqlite3.connect('user.db')

# 사용자 정보 추가
def add_user(id, pwd, email):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_information (
        "ID" TEXT PRIMARY KEY NOT NULL,
        "PWD" TEXT NOT NULL,
        "EMAIL" TEXT 
    ); ''')
   
    cur.execute("INSERT INTO user_information Values(?, ?, ?)", (id, pwd, email))
    con.commit()
    cur.close()
    con.close()


# 사용자 정보 수정 ( password, email )
def edit_information(id, new_pwd, new_email):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("UPDATE user_information SET PWD = ?, EMAIL = ? WHERE ID = ?", (new_pwd, new_email, id))

    con.commit()
    cur.close()
    con.close()


# 사용자 계정 삭제
def delete_user(id):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("DELETE FROM user_information WHERE ID = ?", (id, ))

    con.commit()
    cur.close()
    con.close()


# 냉장고에 재료 추가
def add_ingredient(id, ingredient):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS refrigerator (
            "ID" TEXT NOT NULL,
            "INGREDIENT" TEXT NOT NULL,
            PRIMARY KEY ("ID", "INGREDIENT")
        );
    ''')

    cur.execute("INSERT INTO refrigerator Values(?, ?)", (id, ingredient))
    con.commit()
    cur.close()
    con.close()


# 냉장고에 재료 삭제
def delete_ingredient(id, ingredient):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("DELETE FROM refrigerator WHERE ID = ? AND INGREDIENT = ?", (id, ingredient))

    con.commit()
    cur.close()
    con.close()


# 냉장고 재료 조회
def get_ingredient(id):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("SELECT INGREDIENT FROM refrigerator WHERE ID = ?", (id, ))
    result = cur.fetchall()
    lst = [row[0] for row in result] if result else []

    cur.close()
    con.close()
    return lst


# 좋아하는 음식 추가 
def add_likes(id, like):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS like_items (
        "ID" TEXT NOT NULL,
        "LIKE" TEXT NOT NULL,
        PRIMARY KEY ("ID", "LIKE")
    ); ''')

    cur.execute("INSERT INTO like_items Values(?, ?)", (id, like))

    con.commit()
    cur.close()
    con.close()


# 좋아하는 음식 삭제
def delete_likes(id, like):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("DELETE FROM like_items WHERE ID = ? AND LIKE = ?", (id, like))

    con.commit()
    cur.close()
    con.close()


# 좋아하는 음식 조회
def get_likes(id):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("SELECT LIKE FROM like_items WHERE ID = ?", (id, ))
    result = cur.fetchall()
    lst = [row[0] for row in result] if result else []
    
    cur.close()
    con.close()
    return lst


# 싫어하는 음식 추가
def add_dislikes(id, dislike):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS dislike_items (
        "ID" TEXT NOT NULL,
        "DISLIKE" TEXT NOT NULL,
        PRIMARY KEY ("ID", "DISLIKE")   
    ); ''')

    cur.execute("INSERT INTO dislike_items Values(?, ?)", (id, dislike))

    con.commit()
    cur.close()
    con.close()


# 싫어하는 음식 삭제
def delete_dislikes(id, dislike):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("DELETE FROM dislike_items WHERE ID = ? AND DISLIKE = ?", (id, dislike))
    
    con.commit()
    cur.close()
    con.close()


# 싫어하는 음식 조회
def get_dislikes(id):
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("SELECT DISLIKE FROM dislike_items WHERE ID = ?", (id, ))
    result = cur.fetchall()
    lst = [row[0] for row in result] if result else []

    cur.close()
    con.close()
    return lst

