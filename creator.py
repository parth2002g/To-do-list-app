import sqlite3

database_path = './todo.db'
notstarted = 'Not Started'
inprogress = 'In Progress'
completed = 'completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('insert into items(item, status) values(?,?)', (item, notstarted))
        conn.commit()
        return {"item": item, "status": notstarted}
    except Exception as e:
        print('Error: ', e)
        return None

todo_list = {}

def get_all_items():
    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(item):
    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute("select status from items where item='%s'" % item)
        status = c.fetchone()[0]
        print(status)
        return status
    except Exception as e:
        print('Error: ', e)
        return None
    
def update_status(item, status):
    #Check if the passed status is a valid value
    if(status.lower().strip() == 'not started'):
        status = notstarted
    elif(status.lower().strip() == 'in progress'):
        status = inprogress
    elif(status.lower().strip() == 'completed'):
        status = completed
    else:
        print("Invalid Status - " + status)
        return None
    
    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('update items set status=? where item=?', (status, item))
        conn.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(item):
    try:
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('delete from items where item=?', (item,))
        conn.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None